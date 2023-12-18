import openai

def read_file():
    with open('changes.txt', 'r') as f:
        data = f.read()
        commits = data.split('commit')
        commits.reverse() # reversing so the first commit is first in the list
        for commit in commits:
            # prompt openai to summarize the commit message, no clue if this works or not this is just boilerplate
            response = openai.Completion.create(
                engine="davinci",
                prompt=commit,
                temperature=0.7,
                max_tokens=60,
                top_p=1,
                frequency_penalty=0.5,
                presence_penalty=0.5,
                stop=["\n", "commit"]
            )
            # write resposne to file
            with open('commits.txt', 'a') as f:
                f.write(response)

        return commits

read_file()