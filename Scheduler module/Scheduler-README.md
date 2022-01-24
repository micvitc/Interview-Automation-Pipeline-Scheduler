# SCHEDULER - MIC Interview Automation
The overall project is to automate the interviewing procedure of candidates applying to join Microsoft Innovations Club.

## SCHEDULER
This repo works on the scheduling part only.
Given the details of the candidates who are to be interviewed, this project (this repo) will create an interview schedule (timeline) and provide it to the interviewers and to the fresh candidates as well.

This is just the basic idea, working on more features and plans

## Points to Consider (Discuss TECH HEAD)
1. Basic Scheduler - DONE
2. Pre/Postpone 1 interview from the edge - ADMIN WILL ALTER INDIVIDUALLY AND I HAVE TO CREATE SEPARATE FUNC TO ACCOMODATE THAT
3. Pre/Postpone 1 interview from the middle creating a void - DRAG & DROP IN FRON END AND SCHEDULE AGAIN
4. Pre/Postpone all the interviews - ADMIN CAN JUST SCHEDULE AGAIN WITH NEW DATE & TIME
5. Handling of Leap year, February, months with 30 or 31 days - WILL BE DONE LATER IN CODE QUALITY ASSESSMENT
6. Verifying if start date & time is not already behind current date & time - VALIDATION DONE BY FRONT END
7. Add single/multiple new entries after all interviews are scheduled - ADMIN CAN JUST SCHEDULE AGAIN
Note: Try creating a diff dict storing interviews' info with keys as date if necessary - NOT NECESSARY IG, ALSO THE CURRENT DICT STRUCTURE IS EASY TO MANIPULATE
Note: Try making it as modular as possible - DONE
Note: Better to include sorting in front end itself
Note: Candidates dict also I should take from web request through API and schedule
