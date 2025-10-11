async def query_research_result(client: Client, workflow_id: str) -> None:
    handle = client.get_workflow_handle(workflow_id)

    try:
        research_result = await handle.query(GenerateReportWorkflow.get_research_result)
        if research_result:
            print(f"Research Result: {research_result}")
        else:
            print("Research Result: Not yet available")

    except Exception as e:
        print(f"Query failed: {e}")


async def send_user_decision_signal(client: Client, workflow_id: str) -> None:
    handle = client.get_workflow_handle(workflow_id)

    while True:
        print("\n" + "=" * 50)
        print("Research is complete!")
        print("1. Type 'keep' to approve the research and create PDF")
        print("2. Type 'edit' to modify the research")
        print(
            "3. Type 'query' to query for research result. If querying, wait for `Reserch Complete` to appear in terminal window with Worker running first."
        )
        print("=" * 50)

        decision = input("Your decision (keep/edit/query): ").strip().lower()

        if decision in {"keep", "1"}:
            signal_data = UserDecisionSignal(decision=UserDecision.KEEP)
            await handle.signal("user_decision_signal", signal_data)
            print("Signal sent to keep research and create PDF")
            break
        elif decision in {"edit", "2"}:
            additional_prompt_input = input("Enter additional instructions for the research (optional): ").strip()
            additional_prompt = additional_prompt_input if additional_prompt_input else ""

            signal_data = UserDecisionSignal(decision=UserDecision.EDIT, additional_prompt=additional_prompt)
            await handle.signal("user_decision_signal", signal_data)
            print("Signal sent to regenerate research")
        elif decision in {"query", "3"}:
            await query_research_result(client, workflow_id)
        else:
            print("Please enter either 'keep', 'edit', or 'query'")