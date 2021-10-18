# 규격 선택 정보
from enum import Enum


# 인쇄 방식
class PrintMethod(Enum):
    Digital = 1     # 디지털
    OffSet = 2      # 옵셋


# 인쇄물 종류
class PrintKind(Enum):
    Book = 1            # 책자
    Leaflet = 2         # 리플렛
    Flyer = 3           # 전단
    Poster = 4          # 포스터
    ShoppingBack = 5    # 쇼핑백


## 규격 선택 정보
