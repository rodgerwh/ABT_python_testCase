import os


def black_book(page: int) -> bool:
    status_code = os.system(f"./black-book -n {page}")
    return status_code == 0


def main():
    """
    Вам дали книгу, конкретное количество страниц вам не сообщили,
    но оно точно не превышает 10 000 000.
    Вам необходимо вычислить номер последней страницы.
    Книгу открывать нельзя - вместо этого вам выдали черный ящик, чтобы слегка усложнить задачу.
    Черному ящику (функция black_book) можно сообщить предполагаемый номер последней страницы,
    а в ответ узнать, есть ли эта страница в книге.

    Уточнение:
        black_book возвращает True, если страница последняя
                  возвращает False, если страница не последняя.


    Важно: написать наиболее эффективный алгоритм (по числу итераций)
    """
    # Используем бинарный поиск: задаём start и end (10000000 по условию).
    # Ошибка в уточнении: black_book возвращает True если страница есть в книге, False если нет.
    start = 1
    end = 10000000
    last_page = None
    iterations = 1

    while start <= end:
        mid = (start + end) // 2
        # Если black_book() возвращает True - страница есть в книге, сохраняем её в last_page
        # Продолжаем искать в "правой" половине массива
        if black_book(mid):
            last_page = mid
            start = mid + 1
        # Если black_book() возвращает False - страницы нет в книге, обновляем значение end
        # Ищем по "левой" половине массива
        else:
            end = mid - 1
        iterations += 1

    print(f"The last page number is: {last_page}, iterations: {iterations}")
    # The last page number is: 7922400, iterations: 24


if __name__ == "__main__":
    main()
