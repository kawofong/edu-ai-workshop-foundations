from temporalio import activity

@activity.defn
async def get_weather_alerts(weather_alerts_request: GetWeatherAlertsRequest) -> str:
    """Get weather alerts for a US state.

    Args:
        state: Two-letter US state code (e.g. CA, NY)
    """
    data = await _make_nws_request(_alerts_url(weather_alerts_request.state))
    return json.dumps(data)