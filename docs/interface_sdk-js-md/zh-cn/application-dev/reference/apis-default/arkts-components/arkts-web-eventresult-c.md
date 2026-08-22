# EventResult

Represents the event consumption result sent to the Web component. For details about the supported events, see TouchEvent/MouseEvent. If the application does not consume the event, set this parameter to false, and the event will be consumed by the Web component. If the application has consumed the event, set this parameter to true, and the event will not be consumed by the Web component.

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-unnamed-export declare class EventResult--><!--Device-unnamed-export declare class EventResult-End-->

**系统能力：** SystemCapability.Web.Webview.Core

## constructor

```TypeScript
constructor()
```

Constructor.

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-EventResult-constructor()--><!--Device-EventResult-constructor()-End-->

**系统能力：** SystemCapability.Web.Webview.Core

## setGestureEventResult

```TypeScript
setGestureEventResult(result: boolean): void
```

Sets the gesture event consumption result.

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-EventResult-setGestureEventResult(result: boolean): void--><!--Device-EventResult-setGestureEventResult(result: boolean): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| result | boolean | 是 | Whether to consume the gesture event. {@code true} Indicates the consumption of the gesture event. {@code false} Indicates the non-consumption of the gesture event. Default value: true. |

**示例**

触摸事件示例代码参考[onNativeEmbedGestureEvent](./arkts-basic-components-web-events.md#onnativeembedgestureevent11)。

触摸事件示例代码参考[onNativeEmbedGestureEvent](./arkts-basic-components-web-events.md#onnativeembedgestureevent11)。

## setGestureEventResult

```TypeScript
setGestureEventResult(result: boolean, stopPropagation: boolean): void
```

Sets the gesture event consumption result.

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-EventResult-setGestureEventResult(result: boolean, stopPropagation: boolean): void--><!--Device-EventResult-setGestureEventResult(result: boolean, stopPropagation: boolean): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| result | boolean | 是 | Whether to consume the gesture event. {@code true} Indicates the consumption of the gesture event. {@code false} Indicates the non-consumption of the gesture event. Default value: true. |
| stopPropagation | boolean | 是 | Whether to stop propagation. This parameter is valid only when result is set to true. {@code true} Indicates stops the propagation of events farther along. {@code false} Indicates the propagation of events farther along. Default value: true. |

**示例**

参见 [setGestureEventResult](#setgestureeventresult)

## setMouseEventResult

```TypeScript
setMouseEventResult(result: boolean, stopPropagation?: boolean): void
```

Sets the mouse event consumption result.

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-EventResult-setMouseEventResult(result: boolean, stopPropagation?: boolean): void--><!--Device-EventResult-setMouseEventResult(result: boolean, stopPropagation?: boolean): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| result | boolean | 是 | Whether to consume the mouse event. {@code true} Indicates the consumption of the mouse event. {@code false} Indicates the non-consumption of the mouse event. Default value: true. |
| stopPropagation | boolean | 否 | Whether to stop propagation. This parameter is valid only when result is set to true. {@code true} Indicates stops the propagation of events farther along. {@code false} Indicates the propagation of events farther along. Default value: true. |

**示例**

鼠标事件示例代码参考[onNativeEmbedMouseEvent](./arkts-basic-components-web-events.md#onnativeembedmouseevent20)。

