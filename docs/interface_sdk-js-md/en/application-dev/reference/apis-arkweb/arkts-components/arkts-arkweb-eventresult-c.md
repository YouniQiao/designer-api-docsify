# EventResult

EventResult is a class in ArkWeb Kit used to notify the **Web** component of the same-layer event consumption result. In same-layer embedding scenarios, the app and the **Web** component are both exposed in the event response chain. EventResult allows the app to declare to the **Web** component whether it has consumed a touch or mouse event, thereby determining whether the **Web** component continues to process the event. When the app sets the consumption result to **true**, it indicates that the app has consumed the event and the **Web** component will no longer consume it. When set to **false**, it indicates that the app does not consume the event, and the event will be consumed by the **Web** component. EventResult is used to set the consumption result of touch events (TouchType) and mouse events (MouseAction, limited to left, middle, and right buttons), with the mouse button type defined by MouseButton. It is applicable to event coordination scenarios where the app and the **Web** component interact at the same layer.For details about the sample code of the touch event, see [onNativeEmbedGestureEvent](arkts-arkweb-web-attribute.md#onnativeembedgestureevent).For details about the sample code of the mouse event, see [onNativeEmbedMouseEvent](arkts-arkweb-web-attribute.md#onnativeembedmouseevent).

**Since:** 12

**ArkTS mode:** Supports only ArkTS-Dyn, since version 12.

**System capability:** SystemCapability.Web.Webview.Core

## Modules to Import

```TypeScript
```

## constructor

```TypeScript
constructor()
```

Constructs a **EventResult** object.

**Since:** 12

**ArkTS mode:** Supports only ArkTS-Dyn, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Web.Webview.Core

## setGestureEventResult

```TypeScript
setGestureEventResult(result: boolean): void
```

Sets the gesture event consumption result.

**Since:** 12

**ArkTS mode:** Supports only ArkTS-Dyn, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| result | boolean | Yes |

**Examples**

For details, see [onNativeEmbedGestureEvent](./arkts-basic-components-web-events.md#onnativeembedgestureevent11).

For details, see [onNativeEmbedGestureEvent](./arkts-basic-components-web-events.md#onnativeembedgestureevent11).

## setGestureEventResult

```TypeScript
setGestureEventResult(result: boolean, stopPropagation: boolean): void
```

Sets the gesture event consumption result and bubbling control.

**Since:** 14

**ArkTS mode:** Supports only ArkTS-Dyn, since version 14.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| result | boolean | Yes |
| stopPropagation | boolean | Yes |

**Examples**

See [setGestureEventResult](#setgestureeventresult)

## setMouseEventResult

```TypeScript
setMouseEventResult(result: boolean, stopPropagation?: boolean): void
```

Sets the mouse event consumption result and bubbling control.

**Since:** 20

**ArkTS mode:** Supports only ArkTS-Dyn, since version 20.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| result | boolean | Yes |
| stopPropagation | boolean | No |

**Examples**

For details, see [onNativeEmbedMouseEvent](./arkts-basic-components-web-events.md#onnativeembedmouseevent20).
