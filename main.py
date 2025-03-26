from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse

app = FastAPI()

# 예시용 가짜 주문 데이터
fake_orders = {
    "customer1@example.com": {
        "order_number": "A12345",
        "status": "배송 중",
        "tracking_url": "https://tracking.example.com/A12345"
    },
    "customer2@example.com": {
        "order_number": "B67890",
        "status": "배송 완료",
        "tracking_url": "https://tracking.example.com/B67890"
    }
}

@app.get("/")
def root():
    return {"message": "FastAPI 주문 조회 API입니다."}

@app.get("/orders")
def get_order(email: str = Query(..., description="주문자의 이메일 주소")):
    order = fake_orders.get(email)
    if order:
        return order
    return JSONResponse(status_code=404, content={"message": "주문 정보를 찾을 수 없습니다."})
