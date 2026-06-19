
def calculate_restock_order(current_stock, reorder_point, max_capacity, supplier_batch_size, high_velocity):
   
    if current_stock < 0:
        raise ValueError("current_stock can't be negative")

    if reorder_point < 0:
        raise ValueError("reorder_point can't be negative")

    if max_capacity < 0:
        raise ValueError("max_capacity can't be negative")

    if supplier_batch_size <= 0:
        raise ValueError("supplier_batch_size has to be more than 0")

    if max_capacity <= reorder_point:
        raise ValueError("max_capacity has to be bigger than reorder_point")

    
    if current_stock >= reorder_point:
        return 0

   
    order_amount = max_capacity - current_stock
   
    if high_velocity:
        extra = order_amount * 0.15

        if extra > int(extra):
            extra = int(extra) + 1
        else:
            extra = int(extra)
        order_amount = order_amount + extra

   
    leftover = order_amount % supplier_batch_size
    if leftover != 0:
        order_amount = order_amount + (supplier_batch_size - leftover)

    return order_amount