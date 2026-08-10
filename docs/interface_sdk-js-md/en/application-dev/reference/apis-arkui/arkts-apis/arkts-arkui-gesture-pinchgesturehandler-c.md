# PinchGestureHandler

捏合手势处理器对象类型。

**Inheritance/Implementation:** PinchGestureHandler extends [GestureHandler](arkts-arkui-gesturehandler-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare class PinchGestureHandler extends GestureHandler--><!--Device-unnamed-export declare class PinchGestureHandler extends GestureHandler-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(options?: PinchGestureHandlerOptions)
```

捏合手势处理器的构造函数。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PinchGestureHandler-constructor(options?: PinchGestureHandlerOptions)--><!--Device-PinchGestureHandler-constructor(options?: PinchGestureHandlerOptions)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [PinchGestureHandlerOptions](arkts-arkui-gesture-pinchgesturehandleroptions-i.md) | No | 捏合手势处理器配置参数。 |

## onActionCancel

```TypeScript
onActionCancel(event: Callback<GestureEvent>): this
```

设置捏合手势处理器取消回调。捏合手势处理器识别成功后，接收到触摸取消事件时触发回调。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PinchGestureHandler-onActionCancel(event: Callback<GestureEvent>): this--><!--Device-PinchGestureHandler-onActionCancel(event: Callback<GestureEvent>): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;GestureEvent&gt; | Yes | 捏合手势处理器取消回调。返回手势事件信息。 |

**Return value:**

| Type | Description |
| --- | --- |
| this | 返回当前捏合手势处理器对象。 |

## onActionEnd

```TypeScript
onActionEnd(event: Callback<GestureEvent>): this
```

设置捏合手势处理器结束回调。捏合手势处理器识别成功后，手指抬起时触发回调。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PinchGestureHandler-onActionEnd(event: Callback<GestureEvent>): this--><!--Device-PinchGestureHandler-onActionEnd(event: Callback<GestureEvent>): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;GestureEvent&gt; | Yes | 捏合手势处理器结束回调。 |

**Return value:**

| Type | Description |
| --- | --- |
| this | 返回当前捏合手势处理器对象。 |

## onActionStart

```TypeScript
onActionStart(event: Callback<GestureEvent>): this
```

设置捏合手势处理器识别成功回调。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PinchGestureHandler-onActionStart(event: Callback<GestureEvent>): this--><!--Device-PinchGestureHandler-onActionStart(event: Callback<GestureEvent>): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;GestureEvent&gt; | Yes | 捏合手势处理器识别成功回调。 |

**Return value:**

| Type | Description |
| --- | --- |
| this | 返回当前捏合手势处理器对象。 |

## onActionUpdate

```TypeScript
onActionUpdate(event: Callback<GestureEvent>): this
```

设置捏合手势处理器更新回调。捏合手势处理器移动过程中触发回调。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PinchGestureHandler-onActionUpdate(event: Callback<GestureEvent>): this--><!--Device-PinchGestureHandler-onActionUpdate(event: Callback<GestureEvent>): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;GestureEvent&gt; | Yes | 捏合手势处理器更新回调。 |

**Return value:**

| Type | Description |
| --- | --- |
| this | 返回当前捏合手势处理器对象。 |

