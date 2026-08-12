# WebKeyboardCallback

```TypeScript
export type WebKeyboardCallback = (keyboardCallbackInfo: WebKeyboardCallbackInfo) => WebKeyboardOptions
```

The callback of onInterceptKeyboardAttach event.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export type WebKeyboardCallback = (keyboardCallbackInfo: WebKeyboardCallbackInfo) => WebKeyboardOptions--><!--Device-unnamed-export type WebKeyboardCallback = (keyboardCallbackInfo: WebKeyboardCallbackInfo) => WebKeyboardOptions-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| keyboardCallbackInfo | [WebKeyboardCallbackInfo](arkts-arkweb-web-webkeyboardcallbackinfo-i.md) | Yes | callback information of onInterceptKeyboardAttach. |

**Return value:**

| Type | Description |
| --- | --- |
| [WebKeyboardOptions](arkts-arkweb-web-webkeyboardoptions-i.md) | Return the web keyboard options of this web component. |

