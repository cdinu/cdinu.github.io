from mcp.server.fastmcp import FastMCP
import datetime
import requests

mcp = FastMCP("CarbonIntensityMCP")

@mcp.tool()
def get_fizzbuzz(n: int) -> str:
    """Given an integer n,
        return 'Fizz' if divisible by 3,
        'Buzz' if divisible by 5,
        'FizzBuzz' if divisible by both,
        or the number itself as a string otherwise.
    This tool helps determine the correct FizzBuzz value for a given integer."""
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return str(n)

@mcp.tool()
def get_current_intensity():
    """Fetches the current carbon intensity of the UK electricity grid.
    Returns a JSON with the current carbon intensity in gCO2eq/kWh."""
    url = "https://api.carbonintensity.org.uk/intensity"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data['data']
    
    except Exception as e:
        return f"Failed to retrieve current carbon intensity: {str(e)}"

@mcp.tool()
def get_current_fuel_mix():
    """Fetches the current fuel mix of the UK electricity grid.
    Returns a JSON with the current fuel mix percentages."""
    url = "https://api.carbonintensity.org.uk/generation"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data['data']['generationmix']
    
    except Exception as e:
        return f"Failed to retrieve current fuel mix: {str(e)}"

@mcp.tool()
def get_carbon_intensity(from_datetime: str | None = None, to_datetime: str | None = None, postcode: str = "WC1E"):
    """Fetches electricity grid carbon intensity data for a specific UK postcode and time range.
    The `from_datetime` and `to_datetime` should be in ISO 8601 format (e.g. 2018-05-15T12:00Z).
    The `postcode` needs only the first part e.g. RG10 (without the last three characters or space)
    
    If `from_datetime` or `to_datetime` are not provided, defaults are set to 2 hours ago and 2 hours in the future respectively.
    If postcode is not provided, defaults to "WC1E" -- UCL London.
    Returns a summary including average forecast and generation mix.
    """
    if from_datetime is None: # default to 12 hours ago
        from_datetime = datetime.datetime.utcnow() - datetime.timedelta(hours=2)
        from_datetime = from_datetime.isoformat() + "Z"

    if to_datetime is None: # default to 12 hours in the future
        to_datetime = datetime.datetime.utcnow() + datetime.timedelta(hours=2)
        to_datetime = to_datetime.isoformat() + "Z"
    

    url = f"https://api.carbonintensity.org.uk/regional/intensity/{from_datetime}/{to_datetime}/postcode/{postcode}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()["data"]
    
    except Exception as e:
        return f"Failed to retrieve carbon intensity data: {str(e)}"

if __name__ == "__main__":
    mcp.run()
