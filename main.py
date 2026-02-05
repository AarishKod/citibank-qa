import math

def cost_of_carry_model(spot_price: float, risk_free_rate: float, storage_costs: float, time_to_maturity: float) -> float:
    """
    Docstring for cost_of_carry_model
    
    :param spot_price: Description
    :type spot_price: float
    :param risk_free_rate: Description
    :type risk_free_rate: float
    :param storage_costs: Description
    :type storage_costs: float
    :param time_to_maturity: Description
    :type time_to_maturity: float
    :return: Description
    :rtype: float
    """
    futures_price: float = spot_price * math.e**((risk_free_rate + storage_costs)* time_to_maturity)
    return futures_price