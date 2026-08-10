# PinchGestureHandler

捏合手势处理器对象类型。

**Inheritance/Implementation:** PinchGestureHandler extends [GestureHandler<PinchGestureHandler>](GestureHandler<PinchGestureHandler>)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-unnamed-declare class PinchGestureHandler extends GestureHandler<PinchGestureHandler>--><!--Device-unnamed-declare class PinchGestureHandler extends GestureHandler<PinchGestureHandler>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(options?: PinchGestureHandlerOptions)
```

捏合手势处理器的构造函数。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-PinchGestureHandler-constructor(options?: PinchGestureHandlerOptions)--><!--Device-PinchGestureHandler-constructor(options?: PinchGestureHandlerOptions)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [PinchGestureHandlerOptions](arkts-arkui-gesture-pinchgesturehandleroptions-i.md) | No | 捏合手势处理器配置参数。 |

## onActionCancel

```TypeScript
onActionCancel(event: Callback<void>): PinchGestureHandler
```

设置捏合手势处理器取消回调。捏合手势处理器识别成功后，接收到触摸取消事件时触发回调。不返回手势事件信息。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-PinchGestureHandler-onActionCancel(event: Callback<void>): PinchGestureHandler--><!--Device-PinchGestureHandler-onActionCancel(event: Callback<void>): PinchGestureHandler-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;void&gt; | Yes | 捏合手势处理器取消回调。不返回手势事件信息。 |

**Return value:**

| Type | Description |
| --- | --- |
| [PinchGestureHandler](arkts-arkui-pinchgesturehandler-c.md) | 返回当前捏合手势处理器对象。 |

## onActionCancel

```TypeScript
onActionCancel(event: Callback<GestureEvent>): PinchGestureHandler
```

设置捏合手势处理器取消回调。捏合手势处理器识别成功后，接收到触摸取消事件时触发回调。与  
[onActionCancel](arkts-arkui-pinchgesturehandler-c.md#onactioncancel)接口相比，此接口返回手势事件信息。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-PinchGestureHandler-onActionCancel(event: Callback<GestureEvent>): PinchGestureHandler--><!--Device-PinchGestureHandler-onActionCancel(event: Callback<GestureEvent>): PinchGestureHandler-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;GestureEvent&gt; | Yes | 捏合手势处理器取消回调。返回手势事件信息。 |

**Return value:**

| Type | Description |
| --- | --- |
| [PinchGestureHandler](arkts-arkui-pinchgesturehandler-c.md) | 返回当前捏合手势处理器对象。 |

## onActionEnd

```TypeScript
onActionEnd(event: Callback<GestureEvent>): PinchGestureHandler
```

设置捏合手势处理器结束回调。捏合手势处理器识别成功后，手指抬起时触发回调。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-PinchGestureHandler-onActionEnd(event: Callback<GestureEvent>): PinchGestureHandler--><!--Device-PinchGestureHandler-onActionEnd(event: Callback<GestureEvent>): PinchGestureHandler-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;GestureEvent&gt; | Yes | 捏合手势处理器结束回调。 |

**Return value:**

| Type | Description |
| --- | --- |
| [PinchGestureHandler](arkts-arkui-pinchgesturehandler-c.md) | 返回当前捏合手势处理器对象。 |

## onActionStart

```TypeScript
onActionStart(event: Callback<GestureEvent>): PinchGestureHandler
```

设置捏合手势处理器识别成功回调。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-PinchGestureHandler-onActionStart(event: Callback<GestureEvent>): PinchGestureHandler--><!--Device-PinchGestureHandler-onActionStart(event: Callback<GestureEvent>): PinchGestureHandler-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;GestureEvent&gt; | Yes | 捏合手势处理器识别成功回调。 |

**Return value:**

| Type | Description |
| --- | --- |
| [PinchGestureHandler](arkts-arkui-pinchgesturehandler-c.md) | 返回当前捏合手势处理器对象。 |

## onActionUpdate

```TypeScript
onActionUpdate(event: Callback<GestureEvent>): PinchGestureHandler
```

设置捏合手势处理器更新回调。捏合手势处理器移动过程中触发回调。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-PinchGestureHandler-onActionUpdate(event: Callback<GestureEvent>): PinchGestureHandler--><!--Device-PinchGestureHandler-onActionUpdate(event: Callback<GestureEvent>): PinchGestureHandler-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;GestureEvent&gt; | Yes | 捏合手势处理器更新回调。 |

**Return value:**

| Type | Description |
| --- | --- |
| [PinchGestureHandler](arkts-arkui-pinchgesturehandler-c.md) | 返回当前捏合手势处理器对象。 |

