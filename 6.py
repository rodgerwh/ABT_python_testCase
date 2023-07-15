import json
import os
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional


@dataclass
class ChainData:
    id: int
    prev_item_id: Optional[int]
    next_item_id: Optional[int]
    data: str


@dataclass
class Response:
    items: List[ChainData]
    total: int


def get_chain() -> Response:
    p = subprocess.Popen(["./chainTest"], stdout=subprocess.PIPE)
    r = json.loads(p.stdout.read())
    r["items"] = [ChainData(**c) for c in r["items"]]
    return Response(**r)


def check_chain(filepath: Path) -> bool:
    status_code = os.system(f"./chainTest {filepath}")
    return status_code == 0


def solution(response: Response) -> Path:
    restored_chain = []
    chain_map = {item.id: item for item in response.items}

    # Находим первый элемент (элемент без prev_item_id):
    current_item = next(
        (item for item in response.items if item.prev_item_id is None), None
    )

    while current_item:
        restored_chain.append(current_item)
        next_item_id = current_item.next_item_id
        current_item = chain_map.get(next_item_id, None)

    # Возвращаем полученную цепочку в Response:
    restored_response = Response(items=restored_chain, total=response.total)

    # Сохраняем в json:
    json_data = {
        "items": [item.__dict__ for item in restored_response.items],
        "total": restored_response.total,
    }
    filepath = Path("chainTest.json")
    with open(filepath, "w") as f:
        json.dump(json_data, f)

    return filepath


def main():
    response = get_chain()
    # Нужно восстановить цепочку элементов в порядке возрастания
    # например из get_chain пришли элементы (в items) [
    #                               ChainData(id=2, prev_item_id=None, next_item_id=3, data=''),
    #                               ChainData(id=1, prev_item_id=3, next_item_id=None, data=''),
    #                               ChainData(id=3, prev_item_id=2, next_item_id=1, data='')]
    # Из них получится цепочка [ChainData(id=2...), ChainData(id=3...), ChainData(id=1 ...)]
    # Получившуюся цепочку нужно вернуть в структуру Response и сохранить в json файл
    # путь до файла передать в check_chain

    filepath = solution(response)

    if check_chain(filepath):
        print("Success")
    else:
        print("Fail")


if __name__ == "__main__":
    main()
