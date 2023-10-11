# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator (autorest: 3.8.0, generator: @autorest/python@5.12.2)
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import TYPE_CHECKING

from azure.core.configuration import Configuration
from azure.core.pipeline import policies

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Optional

VERSION = "unknown"

class AzureMachineLearningDesignerServiceClientConfiguration(Configuration):
    """Configuration for AzureMachineLearningDesignerServiceClient.

    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param api_version: Api Version. The default value is "1.0.0".
    :type api_version: str
    """

    def __init__(
        self,
        api_version="1.0.0",  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        super(AzureMachineLearningDesignerServiceClientConfiguration, self).__init__(**kwargs)

        self.api_version = api_version
        kwargs.setdefault(
            'sdk_moniker', f'azuremachinelearningdesignerserviceclient/{VERSION}'
        )
        self._configure(**kwargs)

    def _configure(
        self,
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        self.user_agent_policy = kwargs.get('user_agent_policy') or policies.UserAgentPolicy(**kwargs)
        self.headers_policy = kwargs.get('headers_policy') or policies.HeadersPolicy(**kwargs)
        self.proxy_policy = kwargs.get('proxy_policy') or policies.ProxyPolicy(**kwargs)
        self.logging_policy = kwargs.get('logging_policy') or policies.NetworkTraceLoggingPolicy(**kwargs)
        self.http_logging_policy = kwargs.get('http_logging_policy') or policies.HttpLoggingPolicy(**kwargs)
        self.retry_policy = kwargs.get('retry_policy') or policies.RetryPolicy(**kwargs)
        self.custom_hook_policy = kwargs.get('custom_hook_policy') or policies.CustomHookPolicy(**kwargs)
        self.redirect_policy = kwargs.get('redirect_policy') or policies.RedirectPolicy(**kwargs)
        self.authentication_policy = kwargs.get('authentication_policy')
