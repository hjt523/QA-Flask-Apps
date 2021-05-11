from Todo_List import db, todo

db.drop_all()
db.create_all()

testtask = todo(Task = "clean" ,Complete = False) # Extra: this section populates the table with an example entry
testtask = todo(Task = "cook", Complete = False)
testtask = todo(Task = "Get the QA Todo_list done", Complete = True)
db.session.add(testtask)
db.session.commit()