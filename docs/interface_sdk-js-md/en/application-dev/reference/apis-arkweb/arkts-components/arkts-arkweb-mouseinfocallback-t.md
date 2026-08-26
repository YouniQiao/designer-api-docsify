# MouseInfoCallback

```TypeScript
type MouseInfoCallback = (event: NativeEmbedMouseInfo) => void
```

This callback is triggered when a same-layer tag is clicked using the mouse or touchpad.

**Since:** 20

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [NativeEmbedMouseInfo](arkts-arkweb-nativeembedmouseinfo-i.md) | Yes | Detailed information about the mouse or touchpad click or long press on the same-layer tag. |

**Examples**

For details about the sample code, see [onNativeEmbedMouseEvent](./arkts-basic-components-web-events.md#onnativeembedmouseevent).
