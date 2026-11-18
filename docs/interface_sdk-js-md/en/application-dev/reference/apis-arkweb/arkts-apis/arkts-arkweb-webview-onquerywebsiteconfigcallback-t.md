# OnQueryWebSiteConfigCallback

```TypeScript
type OnQueryWebSiteConfigCallback =
      (params: WebSiteConfigParams) => WebSiteConfigResult
```

Represents the callback triggered by [setWebSiteConfigCallback](arkts-arkweb-webview-webviewcontroller-c.md#setwebsiteconfigcallback) or [setGlobalWebSiteConfigCallback](arkts-arkweb-webview-webviewcontroller-c.md#setglobalwebsiteconfigcallback) to obtain the website configuration. When invoked by the instance-level callback, all optional fields of [WebSiteConfigParams](arkts-arkweb-webview-websiteconfigparams-i.md) are populated; when invoked by the static global callback, only `url` and `source` are populated.

**Since:** 26.1.0

**Model restriction:** This API can be used only in the stage model.

<!--Device-webview-type OnQueryWebSiteConfigCallback =      (params: WebSiteConfigParams) => WebSiteConfigResult--><!--Device-webview-type OnQueryWebSiteConfigCallback =      (params: WebSiteConfigParams) => WebSiteConfigResult-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| params | [WebSiteConfigParams](arkts-arkweb-webview-websiteconfigparams-i.md) | Yes | Website configuration parameters, including the request URL and the source that triggers the query. Optional fields are populated only when the instance-level callback is invoked. |

**Return value:**

| Type | Description |
| --- | --- |
| [WebSiteConfigResult](arkts-arkweb-webview-websiteconfigresult-i.md) | Website configuration result. |
