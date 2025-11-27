from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func

from core.session import get_db
from core.security import get_current_user
from models.user import User
from models.coin import Coin, OriginalityEnum

router = APIRouter(prefix="/dashboard", tags=["dashboard"])


@router.get("/summary")
def get_summary(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    total_coins = db.query(func.count(Coin.id)).scalar() or 0
    total_countries = db.query(func.count(func.distinct(Coin.country))).scalar() or 0
    total_originals = (
        db.query(func.count(Coin.id))
        .filter(Coin.originality == OriginalityEnum.original)
        .scalar()
        or 0
    )
    total_replicas = (
        db.query(func.count(Coin.id))
        .filter(Coin.originality == OriginalityEnum.replica)
        .scalar()
        or 0
    )
    total_estimated_value = db.query(func.sum(Coin.estimated_value)).scalar() or 0.0

    by_country = (
        db.query(Coin.country, func.count(Coin.id))
        .group_by(Coin.country)
        .order_by(func.count(Coin.id).desc())
        .all()
    )
    by_year = (
        db.query(Coin.year, func.count(Coin.id))
        .group_by(Coin.year)
        .order_by(Coin.year)
        .all()
    )

    return {
        "total_coins": total_coins,
        "total_countries": total_countries,
        "total_originals": total_originals,
        "total_replicas": total_replicas,
        "total_estimated_value": total_estimated_value,
        "by_country": [{"country": c, "count": cnt} for c, cnt in by_country],
        "by_year": [{"year": y, "count": cnt} for y, cnt in by_year],
    }
