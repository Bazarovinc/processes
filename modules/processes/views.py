from typing import Optional, Union

from fastapi import Response, status

from app.router import router
from modules.database import exports
from modules.processes.schemas.request import (CurrentLoadingRequestSchema,
                                               DeleteRecordingsRequestSchema)
from modules.processes.schemas.response import (CurrenLoadingResponseSchema,
                                                MessageResponsetSchema)
from modules.utils import get_current_cpu, get_current_ram, get_current_time


@router.get('')
def get_current_loading() -> CurrenLoadingResponseSchema:
    current_time = get_current_time()
    loading = CurrenLoadingResponseSchema(
        cpu=get_current_cpu(),
        ram=get_current_ram()
    )
    exports.set_new_data(current_time, loading, 'GET')
    return loading


@router.post('')
def get_some_current_loading(data: CurrentLoadingRequestSchema) -> CurrenLoadingResponseSchema:
    current_time = get_current_time()
    ram = None
    cpu = None
    if data.cpu:
        cpu = get_current_cpu()
    if data.ram:
        ram = get_current_ram()
    loading = CurrenLoadingResponseSchema(
        cpu=cpu,
        ram=ram
    )
    exports.set_new_data(current_time, loading, 'POST')
    return loading


@router.get('/recordings')
def get_all_recordings_from_db() -> Union[dict, Response]:
    if result := exports.get_all_data():
        return {'result': result}
    return Response(status_code=status.HTTP_204_NO_CONTENT, content='Redis database is empty!')


@router.post('/delete')
def delete_recordings_from_db(data: Optional[DeleteRecordingsRequestSchema] = None) -> MessageResponsetSchema:
    message = ''
    if data:
        exports.filter_deleting_data(data)
        message = 'Data in your gap was successefully deleted.'
    else:
        exports.delete_data()
        message = 'All data was successefully deleted.'
    return MessageResponsetSchema(message=message)
