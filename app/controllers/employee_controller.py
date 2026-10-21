from fastapi import Depends, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas import EmployeeCreate, EmployeeUpdate, EmployeeResponse
from app.services.employee_service import EmployeeService


class EmployeeController:

    @staticmethod
    def create(
        data: EmployeeCreate,
        db: Session = Depends(get_db),
    ) -> EmployeeResponse:
        return EmployeeService.create(db, data)

    @staticmethod
    def get_all(
        db: Session = Depends(get_db),
    ) -> list[EmployeeResponse]:
        return EmployeeService.get_all(db)

    @staticmethod
    def get_one(
        employee_id: int,
        db: Session = Depends(get_db),
    ) -> EmployeeResponse:
        return EmployeeService.get_by_id(db, employee_id)

    @staticmethod
    def update(
        employee_id: int,
        data: EmployeeUpdate,
        db: Session = Depends(get_db),
    ) -> EmployeeResponse:
        return EmployeeService.update(db, employee_id, data)

    @staticmethod
    def delete(
        employee_id: int,
        db: Session = Depends(get_db),
    ) -> dict:
        EmployeeService.delete(db, employee_id)

        return {
            "message": "Employee deleted successfully",
            "employee_id": employee_id,
        }