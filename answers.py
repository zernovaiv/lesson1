dialog={"привет": "И тебе привет!","как дела":"Лучше всех","пока":"Увидимся"}
def get_answer(key,dicti):
	key=str(key).lower()
	dicti=dialog
	return dicti.get(key)
call_function=get_answer("каК дЕЛа",dialog)
print(call_function)