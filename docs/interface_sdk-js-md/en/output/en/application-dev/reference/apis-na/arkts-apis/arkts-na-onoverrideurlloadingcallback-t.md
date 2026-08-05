# OnOverrideUrlLoadingCallback

```TypeScript
export type OnOverrideUrlLoadingCallback = (webResourceRequest: WebResourceRequest) => boolean
```

The callback of onOverrideUrlLoading. Should not call WebviewController.loadUrl with the request's URL and then return true.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export type OnOverrideUrlLoadingCallback = (webResourceRequest: WebResourceRequest) => boolean--><!--Device-unnamed-export type OnOverrideUrlLoadingCallback = (webResourceRequest: WebResourceRequest) => boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| webResourceRequest | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | callback information of onOverrideUrlLoading.  |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | - Returning true causes the current Web to abort loading the URL, |

