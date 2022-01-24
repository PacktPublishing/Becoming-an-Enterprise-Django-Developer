---

# **Generate Chapter 1 Diagram Commands**

---

| Description | Command |
| --- | --- |
| Graph All Project Models | `python manage.py graph_models -a -o diagrams/chapter_1/all_models.png ` |
| Graph Only the User, Team and Award Models | `python manage.py graph_models -a -I User,Team,Award -o diagrams/chapter_1/team_models.png` |
| Graph Only the User Model | `python manage.py graph_models -a -I User -o diagrams/chapter_1/user_model.png` |
| Graph Only the Team Model | `python manage.py graph_models -a -I Team -o diagrams/chapter_1/team_model.png` |
| Graph Only the Award Model | `python manage.py graph_models -a -I Award -o diagrams/chapter_1/award_model.png` |

