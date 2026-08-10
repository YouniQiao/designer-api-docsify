# RotationGestureHandler

旋转手势处理器对象类型。

**Inheritance/Implementation:** RotationGestureHandler extends [GestureHandler<RotationGestureHandler>](GestureHandler<RotationGestureHandler>)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-unnamed-declare class RotationGestureHandler extends GestureHandler<RotationGestureHandler>--><!--Device-unnamed-declare class RotationGestureHandler extends GestureHandler<RotationGestureHandler>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(options?: RotationGestureHandlerOptions)
```

旋转手势处理器的构造函数。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RotationGestureHandler-constructor(options?: RotationGestureHandlerOptions)--><!--Device-RotationGestureHandler-constructor(options?: RotationGestureHandlerOptions)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [RotationGestureHandlerOptions](arkts-arkui-gesture-rotationgesturehandleroptions-i.md) | No | 旋转手势处理器配置参数。 |

## onActionCancel

```TypeScript
onActionCancel(event: Callback<void>): RotationGestureHandler
```

设置旋转手势处理器取消回调。旋转手势处理器识别成功后，接收到触摸取消事件时触发回调。不返回手势事件信息。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RotationGestureHandler-onActionCancel(event: Callback<void>): RotationGestureHandler--><!--Device-RotationGestureHandler-onActionCancel(event: Callback<void>): RotationGestureHandler-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;void&gt; | Yes | 旋转手势处理器取消回调。不返回手势事件信息。 |

**Return value:**

| Type | Description |
| --- | --- |
| [RotationGestureHandler](arkts-arkui-rotationgesturehandler-c.md) | 返回当前旋转手势处理器对象。 |

## onActionCancel

```TypeScript
onActionCancel(event: Callback<GestureEvent>): RotationGestureHandler
```

设置旋转手势处理器取消回调。旋转手势处理器识别成功后，接收到触摸取消事件时触发回调。与  
[onActionCancel](arkts-arkui-rotationgesturehandler-c.md#onactioncancel)相比，此接口返回手势事件信息。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-RotationGestureHandler-onActionCancel(event: Callback<GestureEvent>): RotationGestureHandler--><!--Device-RotationGestureHandler-onActionCancel(event: Callback<GestureEvent>): RotationGestureHandler-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;GestureEvent&gt; | Yes | 旋转手势处理器取消回调。返回手势事件信息。 |

**Return value:**

| Type | Description |
| --- | --- |
| [RotationGestureHandler](arkts-arkui-rotationgesturehandler-c.md) | 返回当前旋转手势处理器对象。 |

## onActionEnd

```TypeScript
onActionEnd(event: Callback<GestureEvent>): RotationGestureHandler
```

设置旋转手势处理器结束回调。旋转手势处理器识别成功后，手指抬起时触发回调。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RotationGestureHandler-onActionEnd(event: Callback<GestureEvent>): RotationGestureHandler--><!--Device-RotationGestureHandler-onActionEnd(event: Callback<GestureEvent>): RotationGestureHandler-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;GestureEvent&gt; | Yes | 旋转手势处理器结束回调。 |

**Return value:**

| Type | Description |
| --- | --- |
| [RotationGestureHandler](arkts-arkui-rotationgesturehandler-c.md) | 返回当前旋转手势处理器对象。 |

## onActionStart

```TypeScript
onActionStart(event: Callback<GestureEvent>): RotationGestureHandler
```

设置旋转手势处理器识别成功回调。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RotationGestureHandler-onActionStart(event: Callback<GestureEvent>): RotationGestureHandler--><!--Device-RotationGestureHandler-onActionStart(event: Callback<GestureEvent>): RotationGestureHandler-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;GestureEvent&gt; | Yes | 旋转手势处理器识别成功回调。 |

**Return value:**

| Type | Description |
| --- | --- |
| [RotationGestureHandler](arkts-arkui-rotationgesturehandler-c.md) | 返回当前旋转手势处理器对象。 |

## onActionUpdate

```TypeScript
onActionUpdate(event: Callback<GestureEvent>): RotationGestureHandler
```

设置旋转手势处理器更新回调。旋转手势处理器移动过程中触发回调。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RotationGestureHandler-onActionUpdate(event: Callback<GestureEvent>): RotationGestureHandler--><!--Device-RotationGestureHandler-onActionUpdate(event: Callback<GestureEvent>): RotationGestureHandler-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;GestureEvent&gt; | Yes | 旋转手势处理器更新回调。 |

**Return value:**

| Type | Description |
| --- | --- |
| [RotationGestureHandler](arkts-arkui-rotationgesturehandler-c.md) | 返回当前旋转手势处理器对象。 |

