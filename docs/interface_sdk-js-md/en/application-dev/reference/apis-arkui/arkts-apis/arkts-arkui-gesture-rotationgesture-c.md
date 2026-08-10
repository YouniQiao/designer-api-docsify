# RotationGesture

用于触发旋转手势，最少需要2指，最多5指，最小改变度数为1度。该手势不支持通过触控板双指旋转操作触发。

> **说明：**
> 
> - 从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

**Inheritance/Implementation:** RotationGesture extends [Gesture](arkts-arkui-gesture-gesture-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare class RotationGesture extends Gesture--><!--Device-unnamed-export declare class RotationGesture extends Gesture-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## $_instantiate

```TypeScript
static $_instantiate(factory: () => RotationGesture, value?: RotationGestureHandlerOptions): RotationGesture
```

设置旋转手势事件。继承自[Gesture](arkts-arkui-gesture-gesture-c.md)。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RotationGesture-static $_instantiate(factory: () => RotationGesture, value?: RotationGestureHandlerOptions): RotationGesture--><!--Device-RotationGesture-static $_instantiate(factory: () => RotationGesture, value?: RotationGestureHandlerOptions): RotationGesture-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| factory | () =&gt; RotationGesture | Yes |  |
| value | [RotationGestureHandlerOptions](arkts-arkui-gesture-rotationgesturehandleroptions-i.md) | No | 旋转手势处理器配置参数。 |

**Return value:**

| Type | Description |
| --- | --- |
| [RotationGesture](arkts-arkui-gesture-rotationgesture-c.md) |  |

## onActionCancel

```TypeScript
onActionCancel(event: Callback<GestureEvent>): this
```

Rotation手势识别成功，接收到触摸取消事件触发的回调。与[onActionCancel](arkts-arkui-gesture-rotationgesture-c.md#onactioncancel)相比，该回调返回手势事件信息。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RotationGesture-onActionCancel(event: Callback<GestureEvent>): this--><!--Device-RotationGesture-onActionCancel(event: Callback<GestureEvent>): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;GestureEvent&gt; | Yes | 手势事件回调函数。 |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onActionEnd

```TypeScript
onActionEnd(event: Callback<GestureEvent>): this
```

Rotation手势识别成功，当抬起最后一根满足手势触发条件的手指后触发的回调。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RotationGesture-onActionEnd(event: Callback<GestureEvent>): this--><!--Device-RotationGesture-onActionEnd(event: Callback<GestureEvent>): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;GestureEvent&gt; | Yes | 手势事件回调函数。 |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onActionStart

```TypeScript
onActionStart(event: Callback<GestureEvent>): this
```

Rotation手势识别成功后触发的回调。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RotationGesture-onActionStart(event: Callback<GestureEvent>): this--><!--Device-RotationGesture-onActionStart(event: Callback<GestureEvent>): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;GestureEvent&gt; | Yes | 手势事件回调函数。 |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onActionUpdate

```TypeScript
onActionUpdate(event: Callback<GestureEvent>): this
```

Rotation手势移动过程中触发的回调。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RotationGesture-onActionUpdate(event: Callback<GestureEvent>): this--><!--Device-RotationGesture-onActionUpdate(event: Callback<GestureEvent>): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;GestureEvent&gt; | Yes | 手势事件回调函数。 |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

