import math
from scipy.stats import norm
import numpy as np

normalizer = norm()

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

def black_scholes_model(spot_price: float, strike_price: float, risk_free_rate: float, time_to_maturity: float, volatility: float) -> float:
    """
    Docstring for black_scholes_model
    
    :param spot_price: Description
    :type spot_price: float
    :param strike_price: Description
    :type strike_price: float
    :param risk_free_rate: Description
    :type risk_free_rate: float
    :param time_to_maturity: Description
    :type time_to_maturity: float
    :param volatility: Description
    :type volatility: float
    :return: Description
    :rtype: float
    """
    d1: float = (math.log(spot_price / strike_price) + (risk_free_rate + volatility**2 / 2) * time_to_maturity) / (volatility * math.sqrt(time_to_maturity))
    d2: float = d1 - volatility * math.sqrt(time_to_maturity)

    call_option_price: float = spot_price * (norm.cdf(d1)) - strike_price * math.e**-(risk_free_rate * time_to_maturity) * norm.cdf(d2)

    return call_option_price

def monte_carlo_simulation(initial_price: float, risk_free_rate: float, volatility: float, simulated_period: float) -> float:
    """
    Docstring for monte_carlo_simulation
    
    :param initial_price: Description
    :type initial_price: float
    :param risk_free_rate: Description
    :type risk_free_rate: float
    :param volatility: Description
    :type volatility: float
    :param simulated_period: Description
    :type simulated_period: float
    :return: Description
    :rtype: float
    """
    num_simulations: int = 10000
    num_steps: int = 252

    # time increment
    dt = simulated_period / num_steps

    # simulating price paths
    np.random.seed(42)
    price_paths = np.zeros((num_steps, num_simulations))
    price_paths[0] = initial_price

    for t in range(1, num_steps):
        z = np.random.standard_normal(num_simulations)
        price_paths[t] = price_paths[t-1] * np.exp((risk_free_rate - 0.5 * volatility ** 2) * dt + volatility * np.sqrt(dt) * z)

    avg_simulated_price = np.mean(price_paths[-1])
    return avg_simulated_price

print(cost_of_carry_model(1.20, 0.02, 0.01, 0.5))
print(black_scholes_model(1.20, 1.25, 0.02, 0.5, 0.25))
print(monte_carlo_simulation(1.20, 0.02, 0.25, 0.5))