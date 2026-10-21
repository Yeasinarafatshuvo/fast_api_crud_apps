from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.models import Employee
from app.schemas import EmployeeCreate, EmployeeUpdate


class EmployeeService:

    @staticmethod
    def create(db: Session, data: EmployeeCreate) -> Employee:
        employee = Employee(
            name=data.name,
            email=str(data.email),
            salary=data.salary,
        )

        db.add(employee)

        try:
            db.commit()
            db.refresh(employee)
        except IntegrityError:
            db.rollback()
            raise HTTPException(
                status_code=409,
                detail="Employee email already exists",
            )

        return employee

    @staticmethod
    def get_all(db: Session) -> list[Employee]:
        statement = select(Employee).order_by(Employee.id)
        return list(db.scalars(statement).all())

    @staticmethod
    def get_by_id(db: Session, employee_id: int) -> Employee:
        employee = db.get(Employee, employee_id)

        if employee is None:
            raise HTTPException(
                status_code=404,
                detail="Employee not found",
            )

        return employee

    @staticmethod
    def update(
        db: Session,
        employee_id: int,
        data: EmployeeUpdate,
    ) -> Employee:
        employee = EmployeeService.get_by_id(db, employee_id)

        employee.name = data.name
        employee.email = str(data.email)
        employee.salary = data.salary

        try:
            db.commit()
            db.refresh(employee)
        except IntegrityError:
            db.rollback()
            raise HTTPException(
                status_code=409,
                detail="Employee email already exists",
            )

        return employee

    @staticmethod
    def delete(db: Session, employee_id: int) -> None:
        employee = EmployeeService.get_by_id(db, employee_id)

        db.delete(employee)
        db.commit()