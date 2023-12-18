import openai

def read_file():
    with open('changes.txt', 'r') as f:
        data = f.read()
        commits = data.split('commit')
        commits.reverse() # reversing so the first commit is first in the list
        for commit in commits:
            # use openai to summarize the commit, idk if this code works yet tbh
            response = openai.Completion.create(
                engine="davinci",
                prompt=commit,
                temperature=0.3,
                max_tokens=60,
                top_p=1,
                frequency_penalty=0.5,
                presence_penalty=0.5,
                stop=["\n", "commit"]
            )
        return commits

read_file()