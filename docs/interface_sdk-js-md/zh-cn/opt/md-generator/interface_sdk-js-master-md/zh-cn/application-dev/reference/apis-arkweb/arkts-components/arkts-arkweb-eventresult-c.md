# EventResult

通知Web组件同层事件消费结果，支持的事件：[触摸事件的类型](../../apis-arkui/arkts-apis/arkts-arkui-touchtype-e.md#TouchType)和[鼠标事件的类型](../../apis-arkui/arkts-apis/arkts-arkui-mouseaction-e.md#MouseAction)，鼠标仅支持 [左中右按键](../../apis-arkui/arkts-apis/arkts-arkui-mousebutton-e.md#MouseButton)。 如果应用不消费该事件，则应设置消费结果为false，事件将会被Web组件消费；反之如果应用消费了该事件，则应将消费结果设置为true，Web组件将不消费该事件。若应用设置消费结果不符合以上使用规格，将产生与开发者预期不匹配的现象。 触摸事件示例代码参考onNativeEmbedGestureEvent事件。 鼠标事件示例代码参考onNativeEmbedMouseEvent事件。

**起始版本：** 12

**废弃版本：** -1

<!--Device-unnamed-declare class EventResult--><!--Device-unnamed-declare class EventResult-End-->

**系统能力：** SystemCapability.Web.Webview.Core

## constructor

```TypeScript
constructor()
```

EventResult的构造函数。

**起始版本：** 12

**废弃版本：** -1

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-EventResult-constructor()--><!--Device-EventResult-constructor()-End-->

**系统能力：** SystemCapability.Web.Webview.Core

## setGestureEventResult

```TypeScript
setGestureEventResult(result: boolean): void
```

设置手势事件消费结果。

**起始版本：** 12

**废弃版本：** -1

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-EventResult-setGestureEventResult(result: boolean): void--><!--Device-EventResult-setGestureEventResult(result: boolean): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| result | boolean | 是 |

## setGestureEventResult

```TypeScript
setGestureEventResult(result: boolean, stopPropagation: boolean): void
```

设置手势事件消费结果。

**起始版本：** 14

**废弃版本：** -1

<!--Device-EventResult-setGestureEventResult(result: boolean, stopPropagation: boolean): void--><!--Device-EventResult-setGestureEventResult(result: boolean, stopPropagation: boolean): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| result | boolean | 是 |
| stopPropagation | boolean | 是 |

## setMouseEventResult

```TypeScript
setMouseEventResult(result: boolean, stopPropagation?: boolean): void
```

设置鼠标事件消费结果。

**起始版本：** 20

**废弃版本：** -1

<!--Device-EventResult-setMouseEventResult(result: boolean, stopPropagation?: boolean): void--><!--Device-EventResult-setMouseEventResult(result: boolean, stopPropagation?: boolean): void-End-->

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| result | boolean | 是 |
| stopPropagation | boolean | 否 |
