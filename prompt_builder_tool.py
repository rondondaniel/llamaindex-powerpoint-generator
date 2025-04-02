from llama_index.core import PromptTemplate

class PromptBuilderTool:
    def __init__(self, query: str) -> None:
        self.query = query
    
    def _get_prompt_template(self) -> str:
        prompt = """
            You are a PowerPoint presentation content generator. You are asked to create content for a presentation about {topic}.
            The PowerPoint template has the following structure:
            
            {structure}
            
            You need to generate content that fits into this structure, ensuring that all placeholders are filled appropriately.
            
            For each slide:
            1. Provide the title for the slide.
            2. Provide the text content for each text placeholder.
            3. If a slide contains a table, generate appropriate data to fill it based on the provided context.
            4. If a slide contains an image placeholder, describe the type of image that should be included.
            
            Return the structured information *only* as a JSON. Do not include any introductory text or explanations.
            """
        return prompt

    def build(self, structure: str) -> str:
        prompt_template = PromptTemplate(template=self._get_prompt_template())
        content_prompt = (
            prompt_template.format(
                topic=self.query,
                structure=structure
            )
        )
        return content_prompt