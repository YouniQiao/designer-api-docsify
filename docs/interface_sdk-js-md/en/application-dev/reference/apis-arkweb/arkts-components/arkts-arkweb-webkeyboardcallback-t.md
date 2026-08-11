# WebKeyboardCallback

```TypeScript
type WebKeyboardCallback = (keyboardCallbackInfo: WebKeyboardCallbackInfo) => WebKeyboardOptions
```

Defines a callback to intercept the soft keyboard initiated from editable elements on a web page. This event is typically called when the **\&lt;input&gt;** tag on the web page is clicked.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-unnamed-type WebKeyboardCallback = (keyboardCallbackInfo: WebKeyboardCallbackInfo) => WebKeyboardOptions--><!--Device-unnamed-type WebKeyboardCallback = (keyboardCallbackInfo: WebKeyboardCallbackInfo) => WebKeyboardOptions-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| keyboardCallbackInfo | [WebKeyboardCallbackInfo](arkts-arkweb-webkeyboardcallbackinfo-i.md) | Yes | Input parameter of the callback used to intercept the soft keyboard initiated from editable elements on a web page, including [WebKeyboardController](../arkts-apis/arkts-arkweb-web-web-f.md/arkts-arkweb-web-web-f.md#web) and editable element attributes. |

**Return value:**

| Type | Description |
| --- | --- |
| [WebKeyboardOptions](arkts-arkweb-webkeyboardoptions-i.md) | R[WebKeyboardOptions]{ |

