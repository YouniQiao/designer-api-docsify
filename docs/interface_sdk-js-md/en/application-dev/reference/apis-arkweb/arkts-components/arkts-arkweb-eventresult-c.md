# EventResult

通知Web组件同层事件消费结果，支持的事件：[触摸事件的类型](../../apis-arkui/arkts-apis/arkts-arkui-enums-touchtype-e.md/arkts-arkui-enums-touchtype-e.md)和[鼠标事件的类型](../../apis-arkui/arkts-apis/arkts-arkui-enums-mouseaction-e.md/arkts-arkui-enums-mouseaction-e.md)，鼠标仅支持  
[左中右按键](../../apis-test-kit/arkts-apis/arkts-test-uitest-mousebutton-e.md/arkts-test-uitest-mousebutton-e.md)。

如果应用不消费该事件，则应设置消费结果为false，事件将会被Web组件消费；反之如果应用消费了该事件，则应将消费结果设置为true，Web组件将不消费该事件。若应用设置消费结果不符合以上使用规格，将产生与开发者预期不匹配的现象。

触摸事件示例代码参考[onNativeEmbedGestureEvent事件](web:WebAttribute.onNativeEmbedGestureEvent)。

鼠标事件示例代码参考[onNativeEmbedMouseEvent事件](web:WebAttribute.onNativeEmbedMouseEvent)。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-unnamed-declare class EventResult--><!--Device-unnamed-declare class EventResult-End-->

**System capability:** SystemCapability.Web.Webview.Core

## constructor

```TypeScript
constructor()
```

EventResult的构造函数。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-EventResult-constructor()--><!--Device-EventResult-constructor()-End-->

**System capability:** SystemCapability.Web.Webview.Core

## setGestureEventResult

```TypeScript
setGestureEventResult(result: boolean): void
```

设置手势事件消费结果。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-EventResult-setGestureEventResult(result: boolean): void--><!--Device-EventResult-setGestureEventResult(result: boolean): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| result | boolean | Yes | 是否消费该手势事件。&lt;br&gt;true表示消费该手势事件，false表示不消费该手势事件。&lt;br&gt;传入null或undefined时为true。 |

## setGestureEventResult

```TypeScript
setGestureEventResult(result: boolean, stopPropagation: boolean): void
```

设置手势事件消费结果。

**Since:** 14

**ArkTS mode:** ArkTS-Dyn only, since version 14.

<!--Device-EventResult-setGestureEventResult(result: boolean, stopPropagation: boolean): void--><!--Device-EventResult-setGestureEventResult(result: boolean, stopPropagation: boolean): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| result | boolean | Yes | 是否消费该手势事件。&lt;br&gt;true表示消费该手势事件，false表示不消费该手势事件。&lt;br&gt;传入null或undefined时为true。 |
| stopPropagation | boolean | Yes | 是否阻止冒泡，在result为true时生效。&lt;br&gt;true表示阻止冒泡，false表示不阻止冒泡。&lt;br&gt;传入null或undefined时为true。 |

## setMouseEventResult

```TypeScript
setMouseEventResult(result: boolean, stopPropagation?: boolean): void
```

设置鼠标事件消费结果。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

<!--Device-EventResult-setMouseEventResult(result: boolean, stopPropagation?: boolean): void--><!--Device-EventResult-setMouseEventResult(result: boolean, stopPropagation?: boolean): void-End-->

**System capability:** SystemCapability.Web.Webview.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| result | boolean | Yes | 是否消费该鼠标事件。&lt;br&gt;true表示消费该鼠标事件，false表示不消费该鼠标事件。&lt;br&gt;传入null或undefined时为true。 |
| stopPropagation | boolean | No | 是否阻止冒泡，在result为true时生效。&lt;br&gt;true表示阻止冒泡，false表示不阻止冒泡。&lt;br&gt;传入null或undefined时为 true。&lt;br&gt;默认值：true。 |

