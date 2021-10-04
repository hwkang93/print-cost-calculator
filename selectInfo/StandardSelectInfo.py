# 규격 선택 정보
from enum import Enum


# 인쇄 방식
class PrintMethod(Enum):
    Digital = 1     # 디지털
    OffSet = 2     # 옵셋


# 인쇄물 종류
class PrintKind(Enum):
    Book = 1
    Leaflet = 2
    Flyer = 3
    Poster = 4
    ShoppingBack = 5


## 규격 선택 정보
