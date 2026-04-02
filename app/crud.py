from sqlalchemy.orm import Session
from . import models, schemas


# Create user
def create_user(db: Session, user: schemas.UserCreate):
    # Check if email already exists
    existing_user = (
        db.query(models.User).filter(models.User.email == user.email).first()
    )
    if existing_user:
        return None

    db_user = models.User(
        full_name=user.full_name, email=user.email, age=user.age, city=user.city
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# Get all users
def get_all_users(db: Session):
    return db.query(models.User).all()


# Get single user by ID
def get_user_by_id(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


# Update user
def update_user(db: Session, user_id: int, user_update: schemas.UserUpdate):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()

    if not db_user:
        return None

    # If email is being updated, check uniqueness
    if user_update.email and user_update.email != db_user.email:
        existing_email = (
            db.query(models.User).filter(models.User.email == user_update.email).first()
        )
        if existing_email:
            return "email_exists"

    # Update only provided fields
    update_data = user_update.dict(exclude_unset=True)

    for key, value in update_data.items():
        setattr(db_user, key, value)

    db.commit()
    db.refresh(db_user)
    return db_user


# Delete user
def delete_user(db: Session, user_id: int):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()

    if not db_user:
        return None

    db.delete(db_user)
    db.commit()
    return db_user
