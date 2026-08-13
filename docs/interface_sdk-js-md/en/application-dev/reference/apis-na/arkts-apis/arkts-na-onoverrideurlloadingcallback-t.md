# OnOverrideUrlLoadingCallback

```TypeScript
export type OnOverrideUrlLoadingCallback = (webResourceRequest: WebResourceRequest) => boolean
```

The callback of onOverrideUrlLoading. Should not call WebviewController.loadUrl with the request's URL and then return true.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-export type OnOverrideUrlLoadingCallback = (webResourceRequest: WebResourceRequest) => boolean--><!--Device-unnamed-export type OnOverrideUrlLoadingCallback = (webResourceRequest: WebResourceRequest) => boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| webResourceRequest | [WebResourceRequest](arkts-na-web-webresourcerequest-c.md) | Yes | callback information of onOverrideUrlLoading. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Returning true causes the current Web to abort loading the URL, false causes the Web to continue loading the url as usual. |

