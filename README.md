# translate-pptx
[![PyPI](https://img.shields.io/pypi/v/translate-pptx.svg?color=green)](https://pypi.org/project/translate-pptx)
[![License](https://img.shields.io/pypi/l/translate-pptx.svg?color=green)](https://github.com/haesleinhuepf/translate-pptx/raw/main/LICENSE)

translate-pptx is a command line tool that translates PowerPoint PPTX files from one language to another.

![banner](https://github.com/haesleinhuepf/translate-pptx/raw/main/docs/images/banner.png)

## Usage

```
translate-pptx my_slides.pptx chinese
```

Advanced usage: you can also add a target filename and an LLM name. At the moment, only ~~OpenAI's~~ Deepseek's LLMs are supported. 

```
translate-pptx my_slides.pptx chinese my_translated_slides.pptx deepseek-chat
```

Under the hood it uses ~~[OpenAI's GPT-4o](https://openai.com/blog/openai-api)~~ [Deepseek's v3](https://api-docs.deepseek.com/zh-cn/) to translate the text in the slides and [python-pptx](https://github.com/scanny/python-pptx) to handle the file-format.

## Disclaimer

`translate-pptx` is a research project aiming at streamlining generation of multi-lingual training materials. Under the hood it uses
artificial intelligence / large language models to generate translations. 
Users are responsible to verify the generated content according to good scientific practice.

> [!CAUTION]
> When using OpenAI's LLMs via translate-pptx, you are bound to the terms of service 
> of the respective companies or organizations.
> The slides you specify are transferred to their servers and may be processed and stored there. 
> Make sure to not submit any sensitive, confidential or personal data. Also using these services may cost money.

## Installation

translate-pptx can be installed using pip:

```
pip install translate-pptx
```

Please note that you must set an `OPENAI_API_KEY` environment variable to use this tool.

## Contributing

Feedback and contributions are welcome! Just open an issue and let's discuss before you send a pull request.

## Acknowledgements

We acknowledge the financial support by the Federal Ministry of Education and Research of Germany and by Sächsische Staatsministerium für Wissenschaft, Kultur und Tourismus in the programme Center of Excellence for AI-research „Center for Scalable Data Analytics and Artificial Intelligence Dresden/Leipzig", project identification number: ScaDS.AI
