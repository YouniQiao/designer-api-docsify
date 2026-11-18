# OnQueryWebSiteConfigCallback

```TypeScript
type OnQueryWebSiteConfigCallback =
      (params: WebSiteConfigParams) => WebSiteConfigResult
```

由[setWebSiteConfigCallback](arkts-arkweb-webview-webviewcontroller-c.md#setwebsiteconfigcallback)或[setGlobalWebSiteConfigCallback](arkts-arkweb-webview-webviewcontroller-c.md#setglobalwebsiteconfigcallback)触发、用于获取网站配置的回调。实例级回调触发时，[WebSiteConfigParams](arkts-arkweb-webview-websiteconfigparams-i.md)的所有可选字段均会填充；静态全局回调触发时，仅填充`url`和`source`。

**起始版本：** 26.1.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-webview-type OnQueryWebSiteConfigCallback =      (params: WebSiteConfigParams) => WebSiteConfigResult--><!--Device-webview-type OnQueryWebSiteConfigCallback =      (params: WebSiteConfigParams) => WebSiteConfigResult-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| params | [WebSiteConfigParams](arkts-arkweb-webview-websiteconfigparams-i.md) | 是 | 网站配置参数，包含请求 URL 和触发来源。可选字段仅在实例级回调触发时填充。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [WebSiteConfigResult](arkts-arkweb-webview-websiteconfigresult-i.md) | 网站配置结果。 |
