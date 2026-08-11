# WebKeyboardCallback

```TypeScript
type WebKeyboardCallback = (keyboardCallbackInfo: WebKeyboardCallbackInfo) => WebKeyboardOptions
```

Defines a callback to intercept the soft keyboard initiated from editable elements on a web page. This event is typically called when the **\&lt;input&gt;** tag on the web page is clicked.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-unnamed-type WebKeyboardCallback = (keyboardCallbackInfo: WebKeyboardCallbackInfo) => WebKeyboardOptions--><!--Device-unnamed-type WebKeyboardCallback = (keyboardCallbackInfo: WebKeyboardCallbackInfo) => WebKeyboardOptions-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| keyboardCallbackInfo | [WebKeyboardCallbackInfo](arkts-arkweb-webkeyboardcallbackinfo-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [WebKeyboardOptions](arkts-arkweb-webkeyboardoptions-i.md) |
