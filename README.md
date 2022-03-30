# Django Student Planner

For Project 4 I will be creating a student planner or task planner application. The application is inspired by a simple to-do list, the app Asana, Google Calendar, and a project management system or kanban. 

Users will be able to create events or projects and add them to a calendar style project management system. Within this calendar each event/project will open up to a separate event/project management area, where users will be able to edit or delete each project, add a separate to-do list for each task, add reminders, take notes, upload documents and more. I would also like to be able to have users share projects/events and assign one another to different portions of it - but this may be iceboxed for later on. 

# Usage
While its called a student planner by the repo, and this will likely be the iniital scope of the application, I would like this to be used for more than just projects and assignments, but for events and personal planning and daily reminders as well. Whether you are planning a bachelor party for a friend, planning a group trip, or just using it for your daily reminders - this app should work fine. 

## Models/Relationships
1:M - Each user will be able to create many events/projects to their calendar. 
M:M - Each event/project has many steps or attributes such as a to-do list, notes, reminders, and more. (I would pick one of these models to stick with for MVP, everything else would be additional or iceboxed)



