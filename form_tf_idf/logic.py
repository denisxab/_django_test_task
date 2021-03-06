def tf_idf(arr: list) -> dict[str, list[int, int]]:
	"""
	Функция получения (частоты вхождения, и частоты не вхождения) слова в списке

	>>> a = tf_idf(["дом","дом","дом","машина","квартира","квартира",])
	>>> a["квартира"]
	[2, 4]
	>>> a["машина"]
	[1, 5]
	>>> a["дом"]
	[3, 3]
	"""

	return dict((x, [arr.count(x), len(arr) - arr.count(x)]) for x in set(arr))
