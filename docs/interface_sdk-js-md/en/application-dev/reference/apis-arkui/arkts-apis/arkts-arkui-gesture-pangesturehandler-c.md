# PanGestureHandler

滑动手势处理器对象类型。

**Inheritance/Implementation:** PanGestureHandler extends [GestureHandler](arkts-arkui-gesturehandler-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare class PanGestureHandler extends GestureHandler--><!--Device-unnamed-export declare class PanGestureHandler extends GestureHandler-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(options?: PanGestureHandlerOptions)
```

滑动手势处理器的构造函数。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PanGestureHandler-constructor(options?: PanGestureHandlerOptions)--><!--Device-PanGestureHandler-constructor(options?: PanGestureHandlerOptions)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [PanGestureHandlerOptions](arkts-arkui-pangesturehandleroptions-i.md) | No | 滑动手势处理器配置参数。 |

## onActionCancel

```TypeScript
onActionCancel(event: Callback<GestureEvent>): this
```

设置滑动手势处理器取消回调。滑动手势处理器识别成功后，接收到触摸取消事件时触发回调。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PanGestureHandler-onActionCancel(event: Callback<GestureEvent>): this--><!--Device-PanGestureHandler-onActionCancel(event: Callback<GestureEvent>): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;GestureEvent&gt; | Yes | 滑动手势处理器取消回调。返回手势事件信息。 |

**Return value:**

| Type | Description |
| --- | --- |
| this | 返回当前滑动手势处理器对象。 |

## onActionEnd

```TypeScript
onActionEnd(event: Callback<GestureEvent>): this
```

设置滑动手势处理器结束回调。滑动手势处理器识别成功后，手指抬起时触发回调。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PanGestureHandler-onActionEnd(event: Callback<GestureEvent>): this--><!--Device-PanGestureHandler-onActionEnd(event: Callback<GestureEvent>): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;GestureEvent&gt; | Yes | 滑动手势处理器结束回调。 |

**Return value:**

| Type | Description |
| --- | --- |
| this | 返回当前滑动手势处理器对象。 |

## onActionStart

```TypeScript
onActionStart(event: Callback<GestureEvent>): this
```

设置滑动手势处理器识别成功回调。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PanGestureHandler-onActionStart(event: Callback<GestureEvent>): this--><!--Device-PanGestureHandler-onActionStart(event: Callback<GestureEvent>): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;GestureEvent&gt; | Yes | 滑动手势处理器识别成功回调。 |

**Return value:**

| Type | Description |
| --- | --- |
| this | 返回当前滑动手势处理器对象。 |

## onActionUpdate

```TypeScript
onActionUpdate(event: Callback<GestureEvent>): this
```

设置滑动手势处理器更新回调。滑动手势处理器移动过程中触发回调。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PanGestureHandler-onActionUpdate(event: Callback<GestureEvent>): this--><!--Device-PanGestureHandler-onActionUpdate(event: Callback<GestureEvent>): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;GestureEvent&gt; | Yes | 滑动手势处理器更新回调。&lt;br/&gt;fingerList为多根手指时，该回调监听每次只会更新一根手指的位置信息。 |

**Return value:**

| Type | Description |
| --- | --- |
| this | 返回当前滑动手势处理器对象。 |

