# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
From the start, the game looked like a pretty simple online brain game. There was a simple sidebar which allowed the user to change the difficulty and enter a number. There wasn't much congestion or anything popping on the site just guessing a number. The attempts left display the wrong value at the start but they decrement correctly. The Normal and Hard difficulties look to be reversed, and the highest guess weren't updating after updating difficulties

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

|         Input         |                               Expected Behavior                                |                                      Actual Behavior                                 | Console Output / Error |
|-----------------------|--------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|------------------------|
| change the difficulty | attempts left displays the correct number of attempts allowed at start of game | attempts left displays one less than the number of attempts allowed at start of game |          none          |
| change the difficulty | normal mode should be 1 to 50 and hard 1 to 100                                | normal mode is 1 to 100 and hard is 1 to 50                                          |          none          |
| change the difficulty | highest guess updates after changing difficulty (e.g. 50 to 100)               | highest guess does not change after difficulty switch                                |          none          |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
I used Claude as my AI tool. Claude suggested to change the hardcoded lowest and highest number a user could choose, so that for each mode it properly displays the highest number the user can guess. The text is first displayed when the user enters the site, so I was able to check each mode and made sure their numbers matched. As far as incorrect suggestions, Claude incorrectly suggested changing the number of attempts the user starts with to get the correct number of attempts when the user first plays, but that change ended up changing the score.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?
To decide whether a bug was actually fixed, I went into a scenario with an expectation and if my expectations were met it's safe for me to assume that part of the program is functioning correctly. When I first started the investigation, I knew something was wrong with the message from the check_guess function, and it would say to go higher when I should guess lower. Claude pointed the error out, and by following the corrected instructions I was able to guess the correct number. Claude definitely helped me design the tests as I don't test my code often, and when my tests were failing it explained the specific error I received as well as how to correct that error if I ever see it again.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
So basically, "reruns" are what they sound like, like a show rerun. Every time you change something in the show's script, we have to take it from the top. Streamlit starts the code from the beginning whenever you update the code, hence it reruns.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
I want to commit more often, preferably after every step, so I can better seperate each step. Next time I work with Claude I want to ensure I have a better way of organizing the chats and responses. The project didn't change much in how I think about AI generated code in that I just see it as suggestions or templates, which I'm ultimately going to change because my code never stays the same. I was impressed with how good Claude caught and changed the errors and do trust Claude more over other agents when it comes to code.