GET_STORE_ALL_QUERY = """SELECT stock_id, package_model, weight_in_karat, cost_per_sell, clearance, color
                         FROM stock
                         WHERE status='בחנות'
                         """
