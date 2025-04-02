from llama_index.llms.openai import OpenAI
from pptx import Presentation
import re
import json


class PowerpointGenerator:
    def init(self) -> None:
        self._init_message()

    def _init_message(self) -> None:
        print("Initializing Powerpoint Generator...")

    def extract_json(self, slides_response: str) -> dict:
        print("Extracting JSON...")
        # Searching for JSON in the response
        json_match = re.search(r'```json\s*(.*?)\s*```', slides_response, re.DOTALL)

        # Verification and parsing of JSON
        if json_match:
            json_content = json_match.group(1)
            try:
                slides = json.loads(json_content)
            except json.JSONDecodeError as e:
                raise ValueError(f"JSON parsing error: {str(e)}")
        else:
            raise ValueError("The JSON was not found in the model response.")
        
        return slides
    
    def generate(self, content_prompt: str, llm: OpenAI) -> None:
        print("Generating slides...")
        slides_response = llm.complete(content_prompt, True).text

        return slides_response
        