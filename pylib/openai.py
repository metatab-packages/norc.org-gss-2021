def openai_one_completion(prompt, system=None, **kwargs):
    """Call the OpenAI completions interface to re-write the extra path for a census variable
    into an English statement that can be used to describe the variable."""

    import os
    import openai
    import tiktoken

    encoding = tiktoken.get_encoding("cl100k_base")

    openai.api_key = os.getenv("OPENAI_API_KEY")

    encoding = tiktoken.encoding_for_model("gpt-3.5-turbo") # Eh, close enough

    n_prompt_tokens = len(encoding.encode(prompt))

    args = {
        'model': 'text-davinci-003',
        'temperature': 0.7,
        'max_tokens': 3900-n_prompt_tokens,
        'top_p': 1,
        'frequency_penalty': 0.2,
        'presence_penalty': 0.2,

    }

    args.update(kwargs)

    chat_models = ('3.5','4','4.0')

    if any([e in args['model'] for e in chat_models]):

        if isinstance(prompt, str):

            if system:
                messages = [{"role": "system", "content": system},
                            {"role": "user", "content": prompt}]
            else:
                messages = [{"role": "user", "content": prompt}]
        else:
            messages = prompt

        response = openai.ChatCompletion.create(
            messages=messages,
            **args
        )

        return response['choices'][0]['message']['content'].strip()

    else:

        response = openai.Completion.create(**args,prompt=prompt)

        return response["choices"][0]["text"].strip()
