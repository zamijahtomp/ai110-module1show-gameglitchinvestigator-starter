# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
  - It looked like a pretty simple online brain game. There was a simple sidebar which allowed the user to change the difficulty and enter a number. There wasn't much congestion or anything popping on the site just guessing a number.
- List at least two concrete bugs you noticed at the start  
  - The attempts left display the wrong value at the start but they decrement correctly
  - Normal and Hard difficulties look to be reversed
  - Highest guess isn't updating after updating difficulties

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
  - Claude
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  - Claude suggested to change the hardcoded lowest and highest number a user could choose, so that for each mode it properly displays the highest number the user can guess. The text is first displayed when the user enters the site, so I was able to check each mode and made sure their numbers matched.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
  - None, all suggestions were correct

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  - I went into a scenario with an expectation and if my expectations were met it's safe for me to assume that part of the program is functioning correctly
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  - When I first started the investigation, I knew something was wrong with the message from the check_guess function, and it would say to go higher when I should guess lower. Claude pointed the error out, and by following the corrected instructions I was able to guess the correct number.
- Did AI help you design or understand any tests? How?
  - Claude definitely helped me design the tests as I don't test my code often, and when my tests were failing it explained the specific error I received as well as how to correct that error if I ever see it again.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
