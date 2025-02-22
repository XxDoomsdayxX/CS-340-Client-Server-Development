# CS-340-Client-Server-Development

Q&A: Reflection on the Grazioso Salvare Project

How do you write programs that are easy to maintain, read, and adapt?

To make programs maintainable, readable, and adaptable, I focus on writing clear and organized code. In my CRUD Python module, I used:
  Modular functions for Create, Read, Update, and Delete (CRUD) so each function had a specific job.
  Clear variable names and comments to make it easy to understand what the code does.
  Error handling with try-except blocks to catch and fix problems without crashing the program.
  Flexible query options so the module could be adjusted for different database needs.
This approach made it easy to connect my CRUD module to the dashboard in Project Two. The advantage was that the database logic stayed separate from the user interface, making it easier to update or improve one part without breaking the other. In the future, I could reuse this module for other projects, such as automated database updates, mobile apps, or new dashboard features.



How do you approach a problem as a computer scientist?

As a computer scientist, I break problems into smaller parts and solve them step by step. For Grazioso Salvare’s dashboard, I followed this process:

  Understand the requirements – I analyzed what the rescue organization needed, like filtering dogs by breed and rescue type.
  Build one piece at a time – I first developed the CRUD module to handle database queries, then worked on the dashboard separately.
  Test and refine – I tested my code often, fixing errors and making improvements along the way.
  Optimize performance – I made sure the database only sent filtered data to the dashboard, reducing load times.
Compared to previous school assignments, this project was more real-world focused because I had to think about how users would interact with the system. In future projects, I would use database indexing for faster searches, create APIs for better flexibility, and apply caching to speed up loading times.



What do computer scientists do, and why does it matter?

Computer scientists solve real-world problems using technology. In this project, my work helped Grazioso Salvare by:
  Making rescue data easy to access – The dashboard allows quick filtering of animals based on needs.
  Helping teams make better decisions – Charts and maps provide visual insights into rescue trends.
  Saving time – Automating the database connection reduced the need for manual data entry.

This type of technology is important in many fields. Hospitals use similar dashboards to track patients, delivery companies use them to monitor shipments, and law enforcement uses them to analyze crime data.

By thinking like a computer scientist, I can build solutions that make work faster, smarter, and more efficient!
