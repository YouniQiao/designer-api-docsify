# OnOverrideUrlLoadingCallback

```TypeScript
type OnOverrideUrlLoadingCallback = (webResourceRequest: WebResourceRequest) => boolean
```

The callback of onOverrideUrlLoading. Should not call WebviewController.loadUrl with the request's URL and then return true.

**Since:** 12

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-unnamed-type OnOverrideUrlLoadingCallback = (webResourceRequest: WebResourceRequest) => boolean--><!--Device-unnamed-type OnOverrideUrlLoadingCallback = (webResourceRequest: WebResourceRequest) => boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| webResourceRequest | [WebResourceRequest](arkts-arkweb-webresourcerequest-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |
