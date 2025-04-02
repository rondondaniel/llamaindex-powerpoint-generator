from structure_builder_tool import StructureBuilderTool
from prompt_builder_tool import PromptBuilderTool
from pptx import Presentation
from pprint import pprint

if __name__ == "__main__":
    template_path: str = "templates/prez_template.pptx"
    query: str = "Create an example of pitch for a new product named \"Nose\", a platform that helps investors to find the best investment opportunities."
    prs = Presentation(template_path)  
    structure_builder: StructureBuilderTool = StructureBuilderTool(prs)
    prompt_builder: PromptBuilderTool = PromptBuilderTool(query)
    structure: str = structure_builder.build_structure()
    content_prompt: str = prompt_builder.build(structure)
    pprint(structure)
    pprint(content_prompt)
    