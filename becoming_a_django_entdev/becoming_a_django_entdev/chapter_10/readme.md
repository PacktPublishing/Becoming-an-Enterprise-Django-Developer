---

# **Fixture dumpdata Commands**

---

Run the following commands to produce the results specified in the Description column. Each command will produce a different output file for you to review the differences between each action and the resulting output.

| Description | Command |
| --- | --- |
| Dump Everything From Every Table and Every App | `python manage.py dumpdata -o becoming_a_django_entdev/chapter_10/fixtures/chapter_10.json` |
| Dump Everything From Every Table and Every App - As Natural Foreign | `python manage.py dumpdata --natural-foreign -o becoming_a_django_entdev/chapter_10/fixtures/chapter_10_natural_foreign.json` |
| Dump Everything From Every Table and Every App - As Natural Primary | `python manage.py dumpdata --natural-primary -o becoming_a_django_entdev/chapter_10/fixtures/chapter_10_natural_primary.json` |
| Dump Everything From Every Table and Every App - As Natural Foreign and Primary | `python manage.py dumpdata --natural-foreign --natural-primary -o becoming_a_django_entdev/chapter_10/fixtures/chapter_10_natural_both.json` |
| Dump Everything From Every Table and Every App - Exclude contenttypes, sessions, authtoken, auth and admin app tables | `python manage.py dumpdata -e contenttypes -e sessions -e authtoken -e auth -e admin -o becoming_a_django_entdev/chapter_10/fixtures/chapter_10_exclude.json` |
| Dump All of chapter_3 App Models | `python manage.py dumpdata chapter_3 -o becoming_a_django_entdev/chapter_10/fixtures/chapter_3_models.json` |
| Dump All of chapter_3 App Models - As Natural Foreign | `python manage.py dumpdata chapter_3 --natural-foreign -o becoming_a_django_entdev/chapter_10/fixtures/chapter_3_models_natural_foreign.json` |
| Dump All of chapter_3 App Models - As Natural Primary | `python manage.py dumpdata chapter_3 --natural-primary -o becoming_a_django_entdev/chapter_10/fixtures/chapter_3_models_natural_primary.json` |
| Dump All of chapter_3 App Models - As Natural Foreign and Primary | `python manage.py dumpdata chapter_3 --natural-foreign --natural-primary -o becoming_a_django_entdev/chapter_10/fixtures/chapter_3_models_natural_both.json` |
| Dump Only the chapter_3 Seller Model | `python manage.py dumpdata chapter_3.seller -o becoming_a_django_entdev/chapter_10/fixtures/chapter_3_sellers.json` |
| Dump Only the chapter_3 Seller Model - As Natural Foreign | `python manage.py dumpdata chapter_3.seller --natural-foreign -o becoming_a_django_entdev/chapter_10/fixtures/chapter_3_sellers_natural_foreign.json` |
| Dump Only the chapter_3 Seller Model - As Natural Primary | `python manage.py dumpdata chapter_3.seller --natural-primary -o becoming_a_django_entdev/chapter_10/fixtures/chapter_3_sellers_natural_primary.json` |
| Dump Only the chapter_3 Seller Model - As Natural Foreign and Primary | `python manage.py dumpdata chapter_3.seller --natural-foreign --natural-primary -o becoming_a_django_entdev/chapter_10/fixtures/chapter_3_sellers_natural_both.json` |
| Dump All of chapter_3 App Models - As XML | `python manage.py dumpdata chapter_3 --format xml -o becoming_a_django_entdev/chapter_10/fixtures/chapter_3_models.xml` |
| Dump Only the chapter_3 Seller Model - As XML | `python manage.py dumpdata chapter_3.seller --format xml -o becoming_a_django_entdev/chapter_10/fixtures/chapter_3_sellers.xml` |
| Dump Everything From Every Table and Every App - As JSONL | `python manage.py dumpdata --format jsonl -o becoming_a_django_entdev/chapter_10/fixtures/chapter_10.jsonl` |
| Dump All of chapter_3 App Models - As JSONL | `python manage.py dumpdata chapter_3 --format jsonl -o becoming_a_django_entdev/chapter_10/fixtures/chapter_3_models.jsonl` |
| Dump Only the chapter_3 Seller Model - As JSONL | `python manage.py dumpdata chapter_3.seller --format jsonl -o becoming_a_django_entdev/chapter_10/fixtures/chapter_3_sellers.jsonl` |
| Dump Everything From Every Table and Every App - As YAML | `python manage.py dumpdata --format yaml -o becoming_a_django_entdev/chapter_10/fixtures/chapter_10.yaml` |
| Dump All of chapter_3 App Models - As YAML | `python manage.py dumpdata chapter_3 --format yaml -o becoming_a_django_entdev/chapter_10/fixtures/chapter_3_models.yaml` |
| Dump Only the chapter_3 Seller Model - As YAML | `python manage.py dumpdata chapter_3.seller --format yaml -o becoming_a_django_entdev/chapter_10/fixtures/chapter_3_sellers.yaml` |
|  | `` |
|  | `` |
|  | `` |
|  | `` |
|  | `` |
|  | `` |
|  | `` |
|  | `` |
|  | `` |
|  | `` |

---

# **Commands That Should Produce An Error**

---

| Description | Command |
| --- | --- |
| Dump Everything From Every Table and Every App - As XML | `python manage.py dumpdata --format xml -o becoming_a_django_entdev/chapter_10/fixtures/chapter_10.xml` |
