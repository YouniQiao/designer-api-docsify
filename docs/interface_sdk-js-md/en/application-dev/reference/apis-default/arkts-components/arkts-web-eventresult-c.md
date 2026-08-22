# EventResult

Represents the event consumption result sent to the Web component. For details about the supported events, see TouchEvent/MouseEvent. If the application does not consume the event, set this parameter to false, and the event will be consumed by the Web component. If the application has consumed the event, set this parameter to true, and the event will not be consumed by the Web component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-unnamed-export declare class EventResult--><!--Device-unnamed-export declare class EventResult-End-->

**System capability:** SystemCapability.Web.Webview.Core

## constructor

```TypeScript
constructor()
```

Constructor.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-EventResult-constructor()--><!--Device-EventResult-constructor()-End-->

**System capability:** SystemCapability.Web.Webview.Core

## setGestureEventResult

```TypeScript
setGestureEventResult(result: boolean): void
```

Sets the gesture event consumption result.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-EventResult-setGestureEventResult(result: boolean): void--><!--Device-EventResult-setGestureEventResult(result: boolean): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| result | boolean | Yes | Whether to consume the gesture event. {@code true} Indicates the consumption of the gesture event. {@code false} Indicates the non-consumption of the gesture event. Default value: true. |

## setGestureEventResult

```TypeScript
setGestureEventResult(result: boolean, stopPropagation: boolean): void
```

Sets the gesture event consumption result.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-EventResult-setGestureEventResult(result: boolean, stopPropagation: boolean): void--><!--Device-EventResult-setGestureEventResult(result: boolean, stopPropagation: boolean): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| result | boolean | Yes | Whether to consume the gesture event. {@code true} Indicates the consumption of the gesture event. {@code false} Indicates the non-consumption of the gesture event. Default value: true. |
| stopPropagation | boolean | Yes | Whether to stop propagation. This parameter is valid only when result is set to true. {@code true} Indicates stops the propagation of events farther along. {@code false} Indicates the propagation of events farther along. Default value: true. |

## setMouseEventResult

```TypeScript
setMouseEventResult(result: boolean, stopPropagation?: boolean): void
```

Sets the mouse event consumption result.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-EventResult-setMouseEventResult(result: boolean, stopPropagation?: boolean): void--><!--Device-EventResult-setMouseEventResult(result: boolean, stopPropagation?: boolean): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| result | boolean | Yes | Whether to consume the mouse event. {@code true} Indicates the consumption of the mouse event. {@code false} Indicates the non-consumption of the mouse event. Default value: true. |
| stopPropagation | boolean | No | Whether to stop propagation. This parameter is valid only when result is set to true. {@code true} Indicates stops the propagation of events farther along. {@code false} Indicates the propagation of events farther along. Default value: true. |

