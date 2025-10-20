from temporalio import workflow

@workflow.defn(sandboxed=False)
class GenerateReportWorkflow:
    def __init__(self) -> None:
        self._current_prompt: str = ""
        # Instance variable to store the Signal in
        self._user_decision: UserDecisionSignal = UserDecisionSignal(decision=UserDecision.WAIT)
        self._research_result: str = ""

    # Method to handle the Signal
    @workflow.signal
    async def user_decision_signal(self, decision_data: UserDecisionSignal) -> None:
        # Update the instance variable with the received Signal data
        self._user_decision = decision_data

    @workflow.query # Query to get the current research result
    def get_research_result(self) -> str | None:
        return self._research_result

    @workflow.run
    async def run(self, input: GenerateReportInput) -> GenerateReportOutput:
      self._current_prompt = input.prompt

      llm_call_input = LLMCallInput(prompt=self._current_prompt)
      # rest of code here