from structure_builder_tool import StructureBuilderTool
from powerpoint_generator import PowerpointGenerator
from prompt_builder_tool import PromptBuilderTool
from llama_index.llms.openai import OpenAI
from pptx import Presentation
import dotenv
import os

dotenv.load_dotenv()
prompt_builder: PromptBuilderTool = PromptBuilderTool()
structure_builder: StructureBuilderTool = StructureBuilderTool()
powerpoint_generator: PowerpointGenerator = PowerpointGenerator()

if __name__ == "__main__":
    template_path: str = "templates/prez_template.pptx"
    query: str = """
        Programmation appliquée à l'analyse de données dont l'objectif de fournir aux apprenants les compétences nécessaires pour appliquer des techniques de programmation à l'analyse de données.
        En utilisant principalement le langage Python et ses bibliothèques spécialisées, les apprenants apprendront à manipuler, analyser et visualiser des données pour extraire des informations pertinentes.
    """
    model_name: str = "gpt-4o-mini"
    output_path: str = "output/prez.pptx"
    prs: Presentation = Presentation(template_path)
    llm: OpenAI = OpenAI(model=model_name,api_key=os.getenv("OPENAI_API_KEY"))
    
    structure: str = structure_builder.build_structure(prs)
    with open("output/structure.tmp", "w") as f:
        f.write(structure)
    
    content_prompt: str = prompt_builder.build(query, structure)
    powerpoint_generator.generate(prs, content_prompt, llm, output_path)
    
    