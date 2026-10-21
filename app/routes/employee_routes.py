from fastapi import APIRouter, status

from app.controllers.employee_controller import EmployeeController
from app.schemas import EmployeeCreate, EmployeeUpdate, EmployeeResponse

router = APIRouter(
    prefix="/employees",
    tags=["Employees"],
)

router.add_api_route(
    "/",
    EmployeeController.create,
    methods=["POST"],
    response_model=EmployeeResponse,
    status_code=status.HTTP_201_CREATED,
)

router.add_api_route(
    "/",
    EmployeeController.get_all,
    methods=["GET"],
    response_model=list[EmployeeResponse],
)

router.add_api_route(
    "/{employee_id}",
    EmployeeController.get_one,
    methods=["GET"],
    response_model=EmployeeResponse,
)

router.add_api_route(
    "/{employee_id}",
    EmployeeController.update,
    methods=["PUT"],
    response_model=EmployeeResponse,
)

router.add_api_route(
    "/{employee_id}",
    EmployeeController.delete,
    methods=["DELETE"],
)