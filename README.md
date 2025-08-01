# claude_demo

## Quick overview of what your demo does and why it's compelling

This Jupyter notebook shows how a user can connect to Claude and generate docstrings for a given python file,  AST generated analysis, and a readme documenting the code. 

## Setup and running instructions

The Jupyter notebook should be self-explainatory. An API key will be needed in an .env file, instructions are linked if needed. There is also a code block to install dependancies. As long as the API key is in the .env file, the notebook should run, top-to-bottom. A python file is also needed to document, one is included as main.py for simplicity. 

## Technical approach and key architectural decisions

This is relatively simple, using complex, sequential prompting, to build artifacts and files that are used in the final step. While it should be easy to understand, it is also incredibly useful. The only aspect of the Claude api it's using is prompting via messages. It also relies a lot on AST, which was recommended by a friend and I have seen it used a few times but combined with Claude makes it awesome.

## Why you chose this particular demonstration

As someone who has been doing devrel for almost 10 years, documentation continues to be something that I need to encourage from both the people I teach and the teams making the tooling I work with. I've seen some LLM powered documentation tools but they're relatively huge and complex. This is a simplified version. It should show a novel integration by using AST, Domain-Specific Application, in that Claude is good at understanding code, and Developer Worflow Enhancement, as documenting is necesairy but also takes time to do correctly. 

## How this helps developers understand Claude's potential

I think there is a large focus on LLMs for code generation now, which is only somewhat of a boon. Lego Coding is a solid approach, but I think the major potential is augmenting the potentially boring and mundane parts of coding, like documentation, git pipelines, creating docker images... There's a lot that is necesairy when building code that isn't just the code itself. 

It's also helpful for understanding code, in general. For example, I use Claude all the time to summarize white papers or help explain things to me. This shows it can do the same with complex code and become an interactive tool.

## What would make other builders want to learn more

It shows how Claude can be used at various stages during code-creation, or assist in understanding new-to-you code. Claude is a tool that has high potential at many stages in code creation, not just generation. This also can be used to create a miriad of artifacts related to code that can be useful to various langauges or approaches. This example just shows documentation, but Claude could also generate Docker containers or augment existing code to add new functionality. There's also unit testing or code review.

## How you used Claude in creating this demo (prompts, iterations, insights)

For this demo, I used claude for some ideation, a bit of help with some of the code -specifically for AST, the prompts used to generate the various features (analyze code, generate docstrings, and generate readme), and finally the example, undocumented code was completely from Claude.
      

## What you would add or improve given more time


I would have played more with the file upload API as well as some tooling, even the text edit tool. With that, it could be expanded to document a whole library (multiple files) and API. Those are also going to be more important aspects to show as time moves on. Or expanding it to handle more languages and different docstring styles, on demand. More interactive, is what I should say. I also had a thought that it could integrate with Gitlab and generate Pages based on the documentation it generates. It could also review documentation to grade it.




