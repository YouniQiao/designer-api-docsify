# PanGestureHandler

滑动手势处理器对象类型。

**Inheritance/Implementation:** PanGestureHandler extends [GestureHandler<PanGestureHandler>](GestureHandler<PanGestureHandler>)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-unnamed-declare class PanGestureHandler extends GestureHandler<PanGestureHandler>--><!--Device-unnamed-declare class PanGestureHandler extends GestureHandler<PanGestureHandler>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(options?: PanGestureHandlerOptions)
```

滑动手势处理器的构造函数。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-PanGestureHandler-constructor(options?: PanGestureHandlerOptions)--><!--Device-PanGestureHandler-constructor(options?: PanGestureHandlerOptions)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [PanGestureHandlerOptions](arkts-arkui-pangesturehandleroptions-i.md) | No | 滑动手势处理器配置参数。 |

## onActionCancel

```TypeScript
onActionCancel(event: Callback<void>): PanGestureHandler
```

设置滑动手势处理器取消回调。滑动手势处理器识别成功后，接收到触摸取消事件时触发回调。不返回手势事件信息。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-PanGestureHandler-onActionCancel(event: Callback<void>): PanGestureHandler--><!--Device-PanGestureHandler-onActionCancel(event: Callback<void>): PanGestureHandler-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;void&gt; | Yes | 滑动手势处理器取消回调。 |

**Return value:**

| Type | Description |
| --- | --- |
| [PanGestureHandler](arkts-arkui-gesture-pangesturehandler-c.md) | 返回当前滑动手势处理器对象。 |

## onActionCancel

```TypeScript
onActionCancel(event: Callback<GestureEvent>): PanGestureHandler
```

设置滑动手势处理器取消回调。滑动手势处理器识别成功后，接收到触摸取消事件时触发回调。与  
[onActionCancel](arkts-arkui-pangesturehandler-c.md#onactioncancel)接口相比，此接口返回手势事件信息。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-PanGestureHandler-onActionCancel(event: Callback<GestureEvent>): PanGestureHandler--><!--Device-PanGestureHandler-onActionCancel(event: Callback<GestureEvent>): PanGestureHandler-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;GestureEvent&gt; | Yes | 滑动手势处理器取消回调。返回手势事件信息。 |

**Return value:**

| Type | Description |
| --- | --- |
| [PanGestureHandler](arkts-arkui-gesture-pangesturehandler-c.md) | 返回当前滑动手势处理器对象。 |

## onActionEnd

```TypeScript
onActionEnd(event: Callback<GestureEvent>): PanGestureHandler
```

设置滑动手势处理器结束回调。滑动手势处理器识别成功后，手指抬起时触发回调。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-PanGestureHandler-onActionEnd(event: Callback<GestureEvent>): PanGestureHandler--><!--Device-PanGestureHandler-onActionEnd(event: Callback<GestureEvent>): PanGestureHandler-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;GestureEvent&gt; | Yes | 滑动手势处理器结束回调。 |

**Return value:**

| Type | Description |
| --- | --- |
| [PanGestureHandler](arkts-arkui-gesture-pangesturehandler-c.md) | 返回当前滑动手势处理器对象。 |

## onActionStart

```TypeScript
onActionStart(event: Callback<GestureEvent>): PanGestureHandler
```

设置滑动手势处理器识别成功回调。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-PanGestureHandler-onActionStart(event: Callback<GestureEvent>): PanGestureHandler--><!--Device-PanGestureHandler-onActionStart(event: Callback<GestureEvent>): PanGestureHandler-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;GestureEvent&gt; | Yes | 滑动手势处理器识别成功回调。 |

**Return value:**

| Type | Description |
| --- | --- |
| [PanGestureHandler](arkts-arkui-gesture-pangesturehandler-c.md) | 返回当前滑动手势处理器对象。 |

## onActionUpdate

```TypeScript
onActionUpdate(event: Callback<GestureEvent>): PanGestureHandler
```

设置滑动手势处理器更新回调。滑动手势处理器移动过程中触发回调。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-PanGestureHandler-onActionUpdate(event: Callback<GestureEvent>): PanGestureHandler--><!--Device-PanGestureHandler-onActionUpdate(event: Callback<GestureEvent>): PanGestureHandler-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;GestureEvent&gt; | Yes | 滑动手势处理器更新回调。&lt;br/&gt;fingerList为多根手指时，该回调监听每次只会更新一根手指的位置信息。 |

**Return value:**

| Type | Description |
| --- | --- |
| [PanGestureHandler](arkts-arkui-gesture-pangesturehandler-c.md) | 返回当前滑动手势处理器对象。 |

