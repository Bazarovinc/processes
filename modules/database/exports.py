import ast
from typing import TYPE_CHECKING

from app.redis import database
from modules.database.scheams import InfoSchema

if TYPE_CHECKING:
    from modules.processes.schemas.request import DeleteRecordingsRequestSchema
    from modules.processes.schemas.response import CurrenLoadingResponseSchema


def filter_deleting_data(data: 'DeleteRecordingsRequestSchema') -> None:
    keys = sorted([key.decode('utf-8') for key in database.scan_iter()])
    database.delete(*keys[keys.index(data.start):keys.index(data.end) + 1])


def delete_data() -> None:
    database.delete(*database.scan_iter())


def get_all_data():
    return [{
        key: InfoSchema(**ast.literal_eval(database.get(key).decode('utf-8').replace("'", '"')))
    }
        for key in database.scan_iter()
    ]


def set_new_data(current_time: str, loading: 'CurrenLoadingResponseSchema', method: str) -> None:
    database.set(current_time, str(InfoSchema(method=method, loading=loading).dict()))
