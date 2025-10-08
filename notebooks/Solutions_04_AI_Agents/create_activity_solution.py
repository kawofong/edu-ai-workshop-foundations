from temporalio import activity
from openai import AsyncOpenAI
from openai.types.responses import Response

@activity.defn
async def create(request: OpenAIResponsesRequest) -> Response:
    # Temporal best practice: Disable retry logic in OpenAI API client library.
    client = AsyncOpenAI(max_retries=0)

    resp = await client.responses.create(
        model=request.model,
        instructions=request.instructions,
        input=request.input,
        tools=request.tools,
        timeout=30,
    )

    return resp