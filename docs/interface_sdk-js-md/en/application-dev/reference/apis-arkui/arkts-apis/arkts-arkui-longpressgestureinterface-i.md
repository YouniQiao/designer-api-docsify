# LongPressGestureInterface

用于触发长按手势事件，触发长按手势的最少手指数为1，默认最短长按时间为500毫秒。可配置duration参数控制最短长按时长。

> **说明：**
> 
> 从API version 18开始，部分设备会优先响应系统的双指长按手势，导致应用的双指长按手势不生效。

**Inheritance/Implementation:** LongPressGestureInterface extends [GestureInterface<LongPressGestureInterface>](GestureInterface<LongPressGestureInterface>)

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

<!--Device-unnamed-interface LongPressGestureInterface extends GestureInterface<LongPressGestureInterface>--><!--Device-unnamed-interface LongPressGestureInterface extends GestureInterface<LongPressGestureInterface>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## [[Call]]

```TypeScript
(value?: { fingers?: number; repeat?: boolean; duration?: number }): LongPressGestureInterface
```

创建长按手势对象。继承自[GestureInterface&lt;T&gt;](arkts-arkui-gestureinterface-i.md)。

当组件默认支持可拖拽时，如Text、TextInput、TextArea、HyperLink、Image和RichEditor等组件。长按手势与拖拽会出现冲突，事件优先级如下：

当长按触发时间小于500毫秒时，系统优先响应长按事件而非拖拽事件。

当长按触发时间达到或超过500毫秒时，系统优先响应拖拽事件而非长按事件。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-LongPressGestureInterface-(value?: { fingers?: number; repeat?: boolean; duration?: number }): LongPressGestureInterface--><!--Device-LongPressGestureInterface-(value?: { fingers?: number; repeat?: boolean; duration?: number }): LongPressGestureInterface-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | { fingers?: number; repeat?: boolean; duration?: number } | No | 设置长按手势参数。&lt;br&gt; - fingers：触发长按的最少手指数，最小值为1，&nbsp;最大值为10。&lt;br/&gt;默认值：1 &lt;br&gt; - repeat：是否连续触发事件回调。true表示连续触发事件回调，false表示不连续触发事件回调。&lt;br/&gt;默认值：false &lt;br&gt; - duration：触发长按的最短时间，单位为毫秒（ms）。&lt;br/&gt;默认值：500 |

**Return value:**

| Type | Description |
| --- | --- |
| [LongPressGestureInterface](arkts-arkui-longpressgestureinterface-i.md) |  |

## [[Call]]

```TypeScript
(options?: LongPressGestureHandlerOptions): LongPressGestureInterface
```

创建长按手势对象。与[LongPressGesture](arkts-arkui-longpressgestureinterface-i.md))}相比，options参数新增了对isFingerCountLimited参数，表示是否检查触摸屏幕的手指数量。

当组件默认支持可拖拽时，如Text、TextInput、TextArea、HyperLink、Image和RichEditor等组件。长按手势与拖拽会出现冲突，事件优先级如下：

当长按触发时间小于500毫秒时，系统优先响应长按事件而非拖拽事件。

当长按触发时间达到或超过500毫秒时，系统优先响应拖拽事件而非长按事件。

**Since:** 15

**ArkTS mode:** ArkTS-Dyn only, since version 15.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-LongPressGestureInterface-(options?: LongPressGestureHandlerOptions): LongPressGestureInterface--><!--Device-LongPressGestureInterface-(options?: LongPressGestureHandlerOptions): LongPressGestureInterface-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [LongPressGestureHandlerOptions](arkts-arkui-gesture-longpressgesturehandleroptions-i.md) | No | 长按手势处理器配置参数。 |

**Return value:**

| Type | Description |
| --- | --- |
| [LongPressGestureInterface](arkts-arkui-longpressgestureinterface-i.md) |  |

## onAction

```TypeScript
onAction(event: (event: GestureEvent) => void): LongPressGestureInterface
```

设置长按手势识别成功回调。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-LongPressGestureInterface-onAction(event: (event: GestureEvent) => void): LongPressGestureInterface--><!--Device-LongPressGestureInterface-onAction(event: (event: GestureEvent) => void): LongPressGestureInterface-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | (event: GestureEvent) =&gt; void | Yes | 长按手势识别成功回调函数。 |

**Return value:**

| Type | Description |
| --- | --- |
| [LongPressGestureInterface](arkts-arkui-longpressgestureinterface-i.md) |  |

## onActionCancel

```TypeScript
onActionCancel(event: () => void): LongPressGestureInterface
```

设置长按手势取消回调。长按手势识别成功后，接收到触摸取消事件时触发回调。不返回手势事件信息。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-LongPressGestureInterface-onActionCancel(event: () => void): LongPressGestureInterface--><!--Device-LongPressGestureInterface-onActionCancel(event: () => void): LongPressGestureInterface-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | () =&gt; void | Yes | 长按手势取消回调函数。 |

**Return value:**

| Type | Description |
| --- | --- |
| [LongPressGestureInterface](arkts-arkui-longpressgestureinterface-i.md) |  |

## onActionCancel

```TypeScript
onActionCancel(event: Callback<GestureEvent>): LongPressGestureInterface
```

设置长按手势取消回调。长按手势识别成功后，接收到触摸取消事件时触发回调。返回手势事件信息。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-LongPressGestureInterface-onActionCancel(event: Callback<GestureEvent>): LongPressGestureInterface--><!--Device-LongPressGestureInterface-onActionCancel(event: Callback<GestureEvent>): LongPressGestureInterface-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;GestureEvent&gt; | Yes | 长按手势取消回调函数。 |

**Return value:**

| Type | Description |
| --- | --- |
| [LongPressGestureInterface](arkts-arkui-longpressgestureinterface-i.md) |  |

## onActionEnd

```TypeScript
onActionEnd(event: (event: GestureEvent) => void): LongPressGestureInterface
```

设置长按手势结束回调。长按手势识别成功后，最后一根手指抬起时触发回调。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-LongPressGestureInterface-onActionEnd(event: (event: GestureEvent) => void): LongPressGestureInterface--><!--Device-LongPressGestureInterface-onActionEnd(event: (event: GestureEvent) => void): LongPressGestureInterface-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | (event: GestureEvent) =&gt; void | Yes | 长按手势结束回调函数。 |

**Return value:**

| Type | Description |
| --- | --- |
| [LongPressGestureInterface](arkts-arkui-longpressgestureinterface-i.md) |  |

