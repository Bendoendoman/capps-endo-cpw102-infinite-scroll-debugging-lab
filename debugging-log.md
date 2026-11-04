# Incident Note — INC-204

**Responders:**

## Investigation log

The program should:

---Works
- Show the first three posts when the program starts, without asking the user to scroll first.

---Buggy
- When the user enters `y`, add the next three posts in order. If fewer than three remain, add those remaining posts.

---Works(technically)
- After loading posts, show all posts loaded so far and a count of how many there are. 

- After displaying the last posts, the next `y` should print `No more posts.` and end the session. 

- If there are no posts when the program starts, print that message and end without asking the user to scroll.

- When the user enters `n`, end the session without loading any more posts.

- Accept uppercase and lowercase answers, including answers with spaces before or after them. For example, `Y` and ` y ` should both work like `y`.

- For any other answer other than case-insensitive `y` or `n`, print `Please enter y or n.` and ask again. 

- Whenever the session ends through quitting or reaching the end of the feed, print `Session ended.` exactly once.

## User bug report

Users submitted the following tickets with reports of buggy behavior! 

> “Every time I scroll, I see the same three posts added again instead of new ones.”
#fixed 2nd commit

> “I keep scrolling, but I never reach the end. The app never tells me there are no more posts.”
fixed 3rd commit

> “I typed ‘maybe’ instead of ‘y’ or ‘n’, and it loaded more posts anyway.”



Record **every debugging step in chronological order as you work**, including unsuccessful attempts and changes you undo. Commit your work as you go. 

For each step, briefly note what you tried and why, what you observed, and what you concluded or decided to try next.

Include relevant inputs, code changes, or output so someone else can follow your investigation. 

Use numbered entries or timestamps. Use Markdown formatting to make it easy to read.

## Resolution

Explain the causes, your repairs, and the evidence that verifies them. Identify
anything still uncertain or unresolved. Make code changes in `feed.py`.


1. fixed not loading more pages by swapping if else to match case and adding in a case for if the user inputs y 
2. fixed infinite scroll by adding in an if statement checking if the list length is shorter than the pagesize*pagenumber
3. fixed/added case for if there are no posts in the post list by adding an equals sign to the if statement detailed in bullet point 2
4. added code to format the input correctly no matter the case/empty spaces
5. tried to fix the issue of incorrect input when scrolling(i.e. not y or n) ran into problem where the scroll still continues despite having a catch case for all other inputs. Added if statement to check if the input is correct. If it is, it runs the code, if not, it doesnt run code and it asks for input again.