# EventResult

Represents the event consumption result sent to the Web component. For details about the supported events, see TouchEvent/MouseEvent. If the application does not consume the event, set this parameter to false, and the event will be consumed by the Web component. If the application has consumed the event, set this parameter to true, and the event will not be consumed by the Web component.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

## constructor

```TypeScript
constructor()
```

Constructor.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

## setGestureEventResult

```TypeScript
setGestureEventResult(result: boolean): void
```

Sets the gesture event consumption result.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| result | boolean | 是 |

**示例**

触摸事件示例代码参考[onNativeEmbedGestureEvent](./arkts-basic-components-web-events.md#onnativeembedgestureevent11)。

触摸事件示例代码参考[onNativeEmbedGestureEvent](./arkts-basic-components-web-events.md#onnativeembedgestureevent11)。

## setGestureEventResult

```TypeScript
setGestureEventResult(result: boolean, stopPropagation: boolean): void
```

Sets the gesture event consumption result.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| result | boolean | 是 |
| stopPropagation | boolean | 是 |

**示例**

参见 [setGestureEventResult](#setgestureeventresult)

## setMouseEventResult

```TypeScript
setMouseEventResult(result: boolean, stopPropagation?: boolean): void
```

Sets the mouse event consumption result.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| result | boolean | 是 |
| stopPropagation | boolean | 否 |

**示例**

鼠标事件示例代码参考[onNativeEmbedMouseEvent](./arkts-basic-components-web-events.md#onnativeembedmouseevent20)。
