import httpx
import pytest

from relevanceai import RelevanceAI, AsyncRelevanceAI


BASE_URLS = [
    None,
    "https://gateway.example/proxy",
    "https://gateway.example/proxy/",
    httpx.URL("https://gateway.example/proxy"),
]


def check_request(request, base_url):
    assert request.url.host == (
        "api-us.stack.tryrelevance.com" if base_url is None else "gateway.example"
    )
    assert request.url.path == (
        "/latest/studios/list" if base_url is None else "/proxy/studios/list"
    )
    assert request.url.params["page_size"] == "3"
    assert request.headers["Authorization"] == "project:test-key"


@pytest.mark.parametrize("base_url", BASE_URLS)
def test_sync_resource_uses_configured_base_url(base_url, monkeypatch):
    requests = []

    def send(self, request, **kwargs):
        requests.append(request)
        return httpx.Response(200, request=request, json={"results": []})

    monkeypatch.setattr(httpx.Client, "send", send)
    client = RelevanceAI(
        api_key="test-key", project="project", region="us", base_url=base_url
    )
    try:
        assert client.tools.list_tools(max_results=3) == []
    finally:
        client.close()
    assert len(requests) == 1
    check_request(requests[0], base_url)


@pytest.mark.asyncio
@pytest.mark.parametrize("base_url", BASE_URLS)
async def test_async_resource_uses_configured_base_url(base_url, monkeypatch):
    requests = []

    async def send(self, request, **kwargs):
        requests.append(request)
        return httpx.Response(200, request=request, json={"results": []})

    monkeypatch.setattr(httpx.AsyncClient, "send", send)
    async with AsyncRelevanceAI(
        api_key="test-key", project="project", region="us", base_url=base_url
    ) as client:
        assert await client.tools.list_tools(max_results=3) == []
    assert len(requests) == 1
    check_request(requests[0], base_url)
