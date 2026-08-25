# OnOverrideUrlLoadingCallback

```TypeScript
export type OnOverrideUrlLoadingCallback = (webResourceRequest: WebResourceRequest) => boolean
```

The callback of onOverrideUrlLoading. Should not call WebviewController.loadUrl with the request's URL and then return true.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| webResourceRequest | [WebResourceRequest](arkts-arkweb-web-webresourcerequest-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |
