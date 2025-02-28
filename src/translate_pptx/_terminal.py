def command_line_interface(argv=None):
    """Command-line interface for the translate_pptx package."""
    import sys
    import os
    import json

    from ._pptx import extract_text_from_slides, replace_text_in_slides
    from ._translation import translate_data_structure_of_texts_recursive
    from ._endpoints import Prompt

    # Read config from terminal arguments
    if argv is None:
        argv = sys.argv

    input_pptx = argv[1]
    target_language = argv[2]

    if len(argv) > 3:
        llm_name = argv[3]

    if not len(argv) > 3 or llm_name in ["default", "_"]:
        llm_name = "deepseek-chat"

    if len(argv) > 4:
        output_pptx = argv[4]
    else:
        counter = 0
        suffix = ""
        while True:
            output_pptx = input_pptx.replace(".pptx", f"_{target_language}{suffix}.pptx")
            if os.path.exists(output_pptx) and llm_name != "json":
                counter += 1
                suffix = f"_{counter}"
            else:
                break

    if llm_name == "nop":
        prompt_function = Prompt(model=None)
    elif "deepseek" in llm_name:
        prompt_function = Prompt(model=llm_name)
    elif llm_name == "json":
        prompt_function = Prompt(model="json", pptx=output_pptx)
    else:
        raise ValueError(f"Unknown model: {llm_name}")

    # Extract text
    texts = extract_text_from_slides(input_pptx)

    # Translate text
    translated_texts, raw_new_texts = translate_data_structure_of_texts_recursive(texts, prompt_function, target_language)
    if llm_name == "json":
        with open(output_pptx.replace('.pptx', '.json'), 'r', encoding='utf-8') as f:
            translated_texts = json.load(f)

    # Replace text
    replace_text_in_slides(input_pptx, translated_texts, output_pptx)

    # Save json
    if llm_name != "json":
        json_output = output_pptx.replace('.pptx', '.json')
        with open(json_output, 'w', encoding='utf-8') as f:
            json.dump(translated_texts, f, ensure_ascii=False, indent=2)
            print(f"Translation data saved to {json_output}")

    print(f"Translated presentation saved to {output_pptx}")
