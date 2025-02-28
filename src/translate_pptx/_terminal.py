def command_line_interface(argv=None):
    """Command-line interface for the translate_pptx package."""
    import sys
    import os

    from ._pptx import extract_text_from_slides, replace_text_in_slides
    from ._translation import translate_data_structure_of_texts_recursive
    from ._endpoints import prompt_openai, prompt_nop

    # Read config from terminal arguments
    if argv is None:
        argv = sys.argv

    input_pptx = argv[1]
    target_language = argv[2]
    if len(argv) > 3:
        output_pptx = argv[3]
    else:
        counter = 0
        suffix = ""
        while True:
            output_pptx = input_pptx.replace(".pptx", f"_{target_language}{suffix}.pptx")
            if os.path.exists(output_pptx):
                counter += 1
                suffix = f"_{counter}"
            else:
                break
    if len(argv) > 4:
        llm_name = argv[4]
    else:
        llm_name = "deepseek-chat"

    if llm_name == "nop":
        prompt_function = prompt_nop
    elif "deepseek" in llm_name:
        prompt_function = prompt_openai
    else:
        raise ValueError(f"Unknown model: {llm_name}")

    # Extract text
    texts = extract_text_from_slides(input_pptx)

    # Translate text
    translated_texts = translate_data_structure_of_texts_recursive(texts, prompt_function, target_language)

    # Replace text
    replace_text_in_slides(input_pptx, translated_texts, output_pptx)

    print(f"Translated presentation saved to {output_pptx}")
