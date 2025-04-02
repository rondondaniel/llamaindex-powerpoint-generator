from pptx import Presentation
import json

class StructureBuilderTool:
    def __init__(self) -> None:
        self.slide_structure = []
        self._init_message()
    
    def _init_message(self) -> None:
        print("Initializing Structure Builder...")

    def build_structure(self, prs: Presentation) -> str:
        print("Building structure...")
        for slide in prs.slides:
            structure = {"placeholders": []}
            
            # Iterate through each shape in the slide
            for shape in slide.shapes:
                if shape.is_placeholder:
                    # Create a dictionary to store placeholder details
                    placeholder = {
                        "type": shape.placeholder_format.type,
                        "idx": shape.placeholder_format.idx,
                        "has_text_frame": shape.has_text_frame,
                        "name": shape.name,
                    }
                    # Check if the placeholder contains a table
                    if shape.has_table:
                        placeholder["has_table"] = True
                        # Extract the table structure as a list of rows with cell texts
                        placeholder["table_structure"] = [
                            [cell.text for cell in row.cells] for row in shape.table.rows
                        ]
                    else:
                        placeholder["has_table"] = False

                    # Check if the placeholder is an image placeholder
                    if shape.placeholder_format.type == 18:
                        placeholder["has_image"] = True
                        placeholder["image_description"] = ""
                    else:
                        placeholder["has_image"] = False

                    # Append the placeholder information to the structure
                    structure["placeholders"].append(placeholder)

                    # Append the slide structure to the list of all slide structures
                    self.slide_structure.append(structure)
    
        # Convert the structure list to a JSON string for better readability
        slide_structures_str = json.dumps(self.slide_structure, indent=4)
        return slide_structures_str