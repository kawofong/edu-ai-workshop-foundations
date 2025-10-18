from dataclasses import dataclass
from enum import StrEnum


class UserDecision(StrEnum):
    KEEP = "KEEP"
    EDIT = "EDIT"
    WAIT = "WAIT"


@dataclass
class LLMCallInput:
    prompt: str


@dataclass
class PDFGenerationInput:
    content: str
    filename: str = "research_pdf.pdf"


@dataclass
class GenerateReportInput:
    prompt: str
    llm_image_model: str = "dall-e-3"


@dataclass
class GenerateReportOutput:
    result: str


@dataclass
class UserDecisionSignal:
    decision: UserDecision
    additional_prompt: str = ""
