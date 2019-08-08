"""
Common Pluggable Django App settings
"""


def plugin_settings(settings):
    """
    Injects local settings into django settings
    """
    env_tokens = getattr(settings, 'ENV_TOKENS', {})
    if env_tokens.get('ANALYTICS_API_CLIENT'):
        settings.ANALYTICS_API_CLIENT = env_tokens['ANALYTICS_API_CLIENT']