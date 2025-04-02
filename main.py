from structure_builder_tool import StructureBuilderTool
from powerpoint_generator import PowerpointGenerator
from prompt_builder_tool import PromptBuilderTool
from llama_index.llms.openai import OpenAI
from pptx import Presentation
from pprint import pprint
import dotenv
import os

dotenv.load_dotenv()
prompt_builder: PromptBuilderTool = PromptBuilderTool()
structure_builder: StructureBuilderTool = StructureBuilderTool()
powerpoint_generator: PowerpointGenerator = PowerpointGenerator()

if __name__ == "__main__":
    template_path: str = "templates/pitch.pptx" #/prez_template.pptx"
    query: str = "Create an example of pitch for a new product named \"Nose\", a platform that helps investors to find the best investment opportunities."
    model_name: str = "gpt-4o-mini"
    output_path: str = "output/pitch.pptx" #prez.pptx"
    prs: Presentation = Presentation(template_path)
    llm: OpenAI = OpenAI(model=model_name,api_key=os.getenv("OPENAI_API_KEY"))
    
    structure: str = structure_builder.build_structure(prs)
    with open("output/structure.tmp", "w") as f:
        f.write(structure)
    
    content_prompt: str = prompt_builder.build(query, structure)
    powerpoint_generator.generate(prs, content_prompt, llm, output_path)
    
    