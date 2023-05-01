from .openai import openai_one_completion
from pathlib import Path
prompt_templ = Path(__file__).parent.joinpath('rewrite_descriptions.txt').read_text()


