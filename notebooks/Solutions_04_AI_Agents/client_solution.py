import asyncio
import sys

from temporalio.client import Client
from temporalio.contrib.pydantic import pydantic_data_converter

async def main():
    client = await Client.connect(
        "localhost:7233",
        data_converter=pydantic_data_converter,
    )

    query = sys.argv[1] if len(sys.argv) > 1 else "Hello, how are you?"

    # Submit the Hello World workflow for execution
    result = await client.execute_workflow(
        ToolCallingWorkflow.run,
        query,
        id="my-workflow-id",
        task_queue="tool-calling-python-task-queue", # TODO: Set the task queue of the client to match the task queue the worker is polling
    )
    print(f"Result: {result}")