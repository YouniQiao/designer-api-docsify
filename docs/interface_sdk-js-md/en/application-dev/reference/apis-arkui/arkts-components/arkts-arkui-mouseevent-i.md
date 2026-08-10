# MouseEvent

继承于[BaseEvent](arkts-arkui-baseevent-i.md)。

**Inheritance/Implementation:** MouseEvent extends [BaseEvent](arkts-arkui-baseevent-i.md)

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

<!--Device-unnamed-declare interface MouseEvent extends BaseEvent--><!--Device-unnamed-declare interface MouseEvent extends BaseEvent-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## getCurrentLocalPosition

```TypeScript
getCurrentLocalPosition?(): Coordinate2D
```

获取点击位置相对于当前组件实时位置的左上角坐标。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-MouseEvent-getCurrentLocalPosition?(): Coordinate2D--><!--Device-MouseEvent-getCurrentLocalPosition?(): Coordinate2D-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [Coordinate2D](../arkts-apis/arkts-arkui-coordinate2d-i.md) | 点击位置相对于当前组件实时位置的左上角坐标。 |

## getHistoricalPoints

```TypeScript
getHistoricalPoints?(): Array<MouseHistoricalPoint>
```

获取当前帧的所有历史点信息。历史点可用于实现更平滑的绘制效果。

该接口仅能在[MouseEvent](arkts-arkui-mouseevent-i.md)中调用，用于获取触发[onMouse](arkts-arkui-commonmethod-c.md#onmouse)时当前帧历史点的相关信息，不同设备每帧的鼠标事件上报频率不同，一帧通常只会上报一个鼠标事件，如果当前帧收到的[MouseEvent](arkts-arkui-mouseevent-i.md)数目大于1，会将该帧最后一个点通过[onMouse](arkts-arkui-commonmethod-c.md#onmouse)返回，其余点作为历史点。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-MouseEvent-getHistoricalPoints?(): Array<MouseHistoricalPoint>--><!--Device-MouseEvent-getHistoricalPoints?(): Array<MouseHistoricalPoint>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;MouseHistoricalPoint&gt; | 当前帧的所有历史点信息组成的数组。 |

## stopPropagation

```TypeScript
stopPropagation: () => void
```

阻塞[事件冒泡](../../../ui/arkts-interaction-basic-principles.md#事件冒泡)。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-MouseEvent-stopPropagation: () => void--><!--Device-MouseEvent-stopPropagation: () => void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## action

```TypeScript
action: MouseAction
```

鼠标动作。

**Type:** [MouseAction](../arkts-apis/arkts-arkui-mouseaction-e.md)

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-MouseEvent-action: MouseAction--><!--Device-MouseEvent-action: MouseAction-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## button

```TypeScript
button: MouseButton
```

鼠标按键。

**Type:** [MouseButton](../arkts-apis/arkts-arkui-mousebutton-e.md)

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-MouseEvent-button: MouseButton--><!--Device-MouseEvent-button: MouseButton-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## displayX

```TypeScript
displayX: number
```

鼠标位置在当前应用屏幕坐标系中的X坐标。

单位：vp

**Type:** number

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-MouseEvent-displayX: number--><!--Device-MouseEvent-displayX: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## displayY

```TypeScript
displayY: number
```

鼠标位置在当前应用屏幕坐标系中的Y坐标。

单位：vp

**Type:** number

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-MouseEvent-displayY: number--><!--Device-MouseEvent-displayY: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## eventHandleId

```TypeScript
eventHandleId?: number
```

用于事件处理的唯一标识。

取值范围：[0, +∞)

**说明：** 在使用[postInputEventWithStrategy](../arkts-apis/arkts-arkui-buildernode-c.md/arkts-arkui-buildernode-c.md#postinputeventwithstrategy)接口分发事件时会使用该字段，事件每分发一次字段会增加100000。

多次使用相同的eventHandleId进行事件分发将导致事件响应异常。仅在构造事件的时候需要对此字段赋值，其余情况开发者无需处理。

**Type:** number

**Since:** 24

**ArkTS mode:** ArkTS-Dyn only, since version 24.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 24.

<!--Device-MouseEvent-eventHandleId?: number--><!--Device-MouseEvent-eventHandleId?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## globalDisplayX

```TypeScript
globalDisplayX?: number
```

鼠标位置在[全局坐标系](../../../windowmanager/window-terminology.md#全局坐标系)中的X坐标。

单位：vp

取值范围：[0, +∞)

**Type:** number

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-MouseEvent-globalDisplayX?: number--><!--Device-MouseEvent-globalDisplayX?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## globalDisplayY

```TypeScript
globalDisplayY?: number
```

鼠标光标在[全局坐标系](../../../windowmanager/window-terminology.md#全局坐标系)中的Y坐标。

单位：vp

取值范围：[0, +∞)

**Type:** number

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-MouseEvent-globalDisplayY?: number--><!--Device-MouseEvent-globalDisplayY?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## pressedButtons

```TypeScript
pressedButtons?: MouseButton[]
```

当前按下的鼠标按键集合。

**Type:** [MouseButton](../arkts-apis/arkts-arkui-mousebutton-e.md)[]

**Since:** 15

**ArkTS mode:** ArkTS-Dyn only, since version 15.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-MouseEvent-pressedButtons?: MouseButton[]--><!--Device-MouseEvent-pressedButtons?: MouseButton[]-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## rawDeltaX

```TypeScript
rawDeltaX?: number
```

鼠标设备在二维平面X轴的移动增量。其数值为鼠标硬件的原始移动数据，使用物理世界中鼠标移动的距离单位进行表示。上报数值由硬件本身决定，并非屏幕的物理/逻辑像素。

**说明：** API版本26.0.0之前，rawDeltaX的返回值并非鼠标硬件的原始移动数据，而是原始数据缩小了X倍，X为系统的显示大小比例。API版本26.0.0开始，rawDeltaX的返回值为鼠标硬件的原始移动数据。

**Type:** number

**Since:** 15

**ArkTS mode:** ArkTS-Dyn only, since version 15.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-MouseEvent-rawDeltaX?: number--><!--Device-MouseEvent-rawDeltaX?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## rawDeltaY

```TypeScript
rawDeltaY?: number
```

鼠标设备在二维平面Y轴的移动增量。其数值为鼠标硬件的原始移动数据，使用物理世界中鼠标移动的距离单位进行表示。上报数值由硬件本身决定，并非屏幕的物理/逻辑像素。

**说明：** API版本26.0.0之前，rawDeltaY的返回值并非鼠标硬件的原始移动数据，而是原始数据缩小了X倍，X为系统的显示大小比例。API版本26.0.0开始，rawDeltaY的返回值为鼠标硬件的原始移动数据。

**Type:** number

**Since:** 15

**ArkTS mode:** ArkTS-Dyn only, since version 15.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-MouseEvent-rawDeltaY?: number--><!--Device-MouseEvent-rawDeltaY?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## screenX

```TypeScript
screenX: number
```

鼠标位置在当前应用窗口坐标系中的X坐标。

单位：vp

**Type:** number

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 10

**Substitutes:** [MouseEvent#windowX](arkts-arkui-mouseevent-i.md#windowx)

<!--Device-MouseEvent-screenX: number--><!--Device-MouseEvent-screenX: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## screenY

```TypeScript
screenY: number
```

鼠标位置在当前应用窗口坐标系中的Y坐标。

单位：vp

**Type:** number

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 10

**Substitutes:** [MouseEvent#windowY](arkts-arkui-mouseevent-i.md#windowy)

<!--Device-MouseEvent-screenY: number--><!--Device-MouseEvent-screenY: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## windowX

```TypeScript
windowX: number
```

鼠标位置在当前应用窗口坐标系中的X坐标。

单位：vp

**Type:** number

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-MouseEvent-windowX: number--><!--Device-MouseEvent-windowX: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## windowY

```TypeScript
windowY: number
```

鼠标位置在当前应用窗口坐标系中的Y坐标。

单位：vp

**Type:** number

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-MouseEvent-windowY: number--><!--Device-MouseEvent-windowY: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## x

```TypeScript
x: number
```

鼠标位置在事件响应组件为基准的[组件坐标系](../../../ui/arkui-glossary.md#组件坐标系)中的X坐标。

单位：vp

**Type:** number

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-MouseEvent-x: number--><!--Device-MouseEvent-x: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## y

```TypeScript
y: number
```

鼠标位置在事件响应组件为基准的[组件坐标系](../../../ui/arkui-glossary.md#组件坐标系)中的Y坐标。

单位：vp

**Type:** number

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-MouseEvent-y: number--><!--Device-MouseEvent-y: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

