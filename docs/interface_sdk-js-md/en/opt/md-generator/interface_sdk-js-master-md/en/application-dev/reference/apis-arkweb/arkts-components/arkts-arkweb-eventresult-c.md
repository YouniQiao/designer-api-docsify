# EventResult

Represents the event consumption result sent to the **Web** component. For details about the supported events, see  
[TouchType](../../apis-arkui/arkts-apis/arkts-arkui-touchtype-e.md#TouchType), [MouseAction](../../apis-arkui/arkts-apis/arkts-arkui-mouseaction-e.md#MouseAction), and left, middle, and right buttons in  
[MouseButton](../../apis-arkui/arkts-apis/arkts-arkui-mousebutton-e.md#MouseButton).

If the application does not consume the event, set the consumption result to **false**, and the event will be consumed by the **Web** component. If the application consumes the event, set the consumption result to **true**, and the **Web** component will not consume the event. If the consumption result is not set according to the preceding specifications, exceptions may occur.

For details about the sample code of the touch event, see  
[onNativeEmbedGestureEvent](web:WebAttribute.onNativeEmbedGestureEvent).

For details about the sample code of the mouse event, see  
[onNativeEmbedMouseEvent](web:WebAttribute.onNativeEmbedMouseEvent).

**Since:** 12

<!--Device-unnamed-declare class EventResult--><!--Device-unnamed-declare class EventResult-End-->

**System capability:** SystemCapability.Web.Webview.Core

## constructor

```TypeScript
constructor()
```

Constructs a **EventResult** object.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-EventResult-constructor()--><!--Device-EventResult-constructor()-End-->

**System capability:** SystemCapability.Web.Webview.Core

## setGestureEventResult

```TypeScript
setGestureEventResult(result: boolean): void
```

Sets the gesture event consumption result.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-EventResult-setGestureEventResult(result: boolean): void--><!--Device-EventResult-setGestureEventResult(result: boolean): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| result | boolean | Yes |

## setGestureEventResult

```TypeScript
setGestureEventResult(result: boolean, stopPropagation: boolean): void
```

Sets the gesture event consumption result.

**Since:** 14

<!--Device-EventResult-setGestureEventResult(result: boolean, stopPropagation: boolean): void--><!--Device-EventResult-setGestureEventResult(result: boolean, stopPropagation: boolean): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| result | boolean | Yes |
| stopPropagation | boolean | Yes |

## setMouseEventResult

```TypeScript
setMouseEventResult(result: boolean, stopPropagation?: boolean): void
```

Sets the mouse event consumption result.

**Since:** 20

<!--Device-EventResult-setMouseEventResult(result: boolean, stopPropagation?: boolean): void--><!--Device-EventResult-setMouseEventResult(result: boolean, stopPropagation?: boolean): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| result | boolean | Yes |
| stopPropagation | boolean | No |
