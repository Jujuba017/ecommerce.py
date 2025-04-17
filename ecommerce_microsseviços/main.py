from user_service import UserService 
from product_service import ProductService 
from order_service import OrderService

# Exemplo de uso com microsserviços 
user_service = UserService() 
product_service = ProductService() 
order_service = OrderService()

user_service.add_user("julia ap")
product_service.add_product("Laptop") 
print(order_service.place_order("julia ap", "Laptop", product_service))