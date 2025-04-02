from llama_index.core import PromptTemplate

class PromptBuilderTool:
    def __init__(self) -> None:
        self._init_message()
    
    def _init_message(self) -> None:
        print("Initializing Prompt Builder...")
    
    def _get_prompt_template(self) -> str:
        prompt = """
            You are a PowerPoint presentation content generator. You are asked to create content for a presentation about {topic}.
            The PowerPoint template has the following structure:
            
            {structure}
            
            You need to generate content that fits into this structure, ensuring that all placeholders are filled appropriately.
            
            For each slide:
            1. Provide the title for the slide.
            2. Provide the text content for each text placeholder or text_box.
            3. If a slide contains a table, generate appropriate data to fill it based on the provided context.
            4. If a slide contains an image placeholder, describe the type of image that should be included.
            
            Return the structured information *only* as a JSON. Do not include any introductory text or explanations.
            """
        return prompt

    def build(self, query: str, structure: str) -> str:
        print("Building prompt...")
        prompt_template = PromptTemplate(template=self._get_prompt_template())
        content_prompt = (
            prompt_template.format(
                topic=query,
                structure=structure
            )
        )
        return content_prompt