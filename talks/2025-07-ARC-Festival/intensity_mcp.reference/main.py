from mcp.server.fastmcp import FastMCP
import datetime
import requests

mcp = FastMCP("CarbonIntensityMCP")

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

if __name__ == "__main__":
    mcp.run()
