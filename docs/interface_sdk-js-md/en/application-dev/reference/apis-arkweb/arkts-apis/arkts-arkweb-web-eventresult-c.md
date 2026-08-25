# EventResult

Represents the event consumption result sent to the Web component. For details about the supported events, see TouchEvent/MouseEvent. If the application does not consume the event, set this parameter to false, and the event will be consumed by the Web component. If the application has consumed the event, set this parameter to true, and the event will not be consumed by the Web component.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.Web.Webview.Core

## constructor

```TypeScript
constructor()
```

Constructor.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.Web.Webview.Core

## setGestureEventResult

```TypeScript
setGestureEventResult(result: boolean): void
```

Sets the gesture event consumption result.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

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

Sets the gesture event consumption result.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

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

Sets the mouse event consumption result.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| result | boolean | Yes |
| stopPropagation | boolean | No |

**Examples**

For details, see [onNativeEmbedMouseEvent](./arkts-basic-components-web-events.md#onnativeembedmouseevent20).
