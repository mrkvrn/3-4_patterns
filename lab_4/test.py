# 1. Adapter Pattern
print("1. Adapter Pattern:")
from adapter import LegacyPaymentService, PaymentAdapter

legacy_service = LegacyPaymentService()
adapter = PaymentAdapter(legacy_service)
print("Legacy result:", legacy_service.process_legacy_payment())
print("Adapter result:", adapter.process_payment())
print()

# 2. Bridge Pattern
print("2. Bridge Pattern:")
from bridge import VectorRenderer, RasterRenderer, Shape

vector_renderer = VectorRenderer()
raster_renderer = RasterRenderer()

vector_shape = Shape(vector_renderer)
raster_shape = Shape(raster_renderer)

print("Vector shape:")
print(vector_shape.draw())
print("\nRaster shape:")
print(raster_shape.draw())
print()

# 3. Iterator Pattern
print("3. Iterator Pattern:")
from iterator import ItemCollection

collection = ItemCollection()
collection.add_item("Apple")
collection.add_item("Banana")
collection.add_item("Cherry")

print("Iterating through items:")
for item in collection:
    print(f" - {item}")
print()

# 4. Proxy Pattern
print("4. Proxy Pattern:")
from proxy import RealSubject, Proxy

real_subject = RealSubject()
proxy = Proxy(real_subject)

print("Direct call to RealSubject:")
print(real_subject.request())
print("\nCall through Proxy:")
print(proxy.request())
print()

# 5. Responsibility Chain Pattern
print("5. Responsibility Chain Pattern:")
from responsibility_chain import ConcreteHandler_A, ConcreteHandler_B

handler_a = ConcreteHandler_A()
handler_b = ConcreteHandler_B()
handler_a.set_next(handler_b)

requests = ["A", "B", "C"]
for req in requests:
    result = handler_a.handle(req)
    print(f"Request '{req}': {result if result else 'No handler could process'}")
print()

# 6. Strategy Pattern
print("6. Strategy Pattern:")
from strategy import Sorter, BubbleSort, QuickSort

numbers = [5, 3, 8, 4, 2]
sorter = Sorter()

print("Original list:", numbers)

sorter.set_strategy(BubbleSort())
bubble_result = sorter.sort_data(numbers.copy())
print("After BubbleSort:", bubble_result)

sorter.set_strategy(QuickSort())
quick_result = sorter.sort_data(numbers.copy())
print("After QuickSort:", quick_result)

print("\nAll patterns demonstrated successfully")
