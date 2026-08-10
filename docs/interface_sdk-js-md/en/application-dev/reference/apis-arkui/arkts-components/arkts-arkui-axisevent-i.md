# AxisEvent

轴事件的对象说明，继承于[BaseEvent](arkts-arkui-baseevent-i.md)。

**Inheritance/Implementation:** AxisEvent extends [BaseEvent](arkts-arkui-baseevent-i.md)

**Since:** 17

**ArkTS mode:** ArkTS-Dyn only, since version 17.

<!--Device-unnamed-declare interface AxisEvent extends BaseEvent--><!--Device-unnamed-declare interface AxisEvent extends BaseEvent-End-->

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

<!--Device-AxisEvent-getCurrentLocalPosition?(): Coordinate2D--><!--Device-AxisEvent-getCurrentLocalPosition?(): Coordinate2D-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [Coordinate2D](../arkts-apis/arkts-arkui-coordinate2d-i.md) | 点击位置相对于当前组件实时位置的左上角坐标。 |

## getHorizontalAxisValue

```TypeScript
getHorizontalAxisValue(): number
```

获取此次轴事件的水平轴值。

**Since:** 17

**ArkTS mode:** ArkTS-Dyn only, since version 17.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 17.

<!--Device-AxisEvent-getHorizontalAxisValue(): number--><!--Device-AxisEvent-getHorizontalAxisValue(): number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| number | 水平轴值。 &lt;br&gt;单位：vp |

## getPinchAxisScaleValue

```TypeScript
getPinchAxisScaleValue(): number
```

返回此次轴事件双指缩放的比例。

**Since:** 21

**ArkTS mode:** ArkTS-Dyn only, since version 21.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 21.

<!--Device-AxisEvent-getPinchAxisScaleValue(): number--><!--Device-AxisEvent-getPinchAxisScaleValue(): number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| number | 双指缩放比例。&lt;br/&gt; **说明：** 缩放比例指的是触控板双指缩放事件触发过程中双指当前的距离与双指最初按下时的距离的比值。&lt;br/&gt;默认值：0 &lt;br/&gt;取值范围：[0, +∞)&lt;br/&gt; |

## getVerticalAxisValue

```TypeScript
getVerticalAxisValue(): number
```

获取此次轴事件的垂直轴值。

**Since:** 17

**ArkTS mode:** ArkTS-Dyn only, since version 17.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 17.

<!--Device-AxisEvent-getVerticalAxisValue(): number--><!--Device-AxisEvent-getVerticalAxisValue(): number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| number | 垂直轴值。 &lt;br&gt;单位：vp |

## hasAxis

```TypeScript
hasAxis(axisType: AxisType): boolean
```

检测此轴事件是否包含指定的轴类型。

**Since:** 22

**ArkTS mode:** ArkTS-Dyn only, since version 22.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-AxisEvent-hasAxis(axisType: AxisType): boolean--><!--Device-AxisEvent-hasAxis(axisType: AxisType): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| axisType | [AxisType](../arkts-apis/arkts-arkui-axistype-e.md) | Yes | 轴事件的轴类型。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 此轴事件是否包含指定的轴类型。 &lt;br&gt;true：包含指定的轴类型；false：不包含指定的轴类型。 |

## action

```TypeScript
action: AxisAction
```

轴事件的动作类型。

**Type:** [AxisAction](../arkts-apis/arkts-arkui-axisaction-e.md)

**Since:** 17

**ArkTS mode:** ArkTS-Dyn only, since version 17.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 17.

<!--Device-AxisEvent-action: AxisAction--><!--Device-AxisEvent-action: AxisAction-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## displayX

```TypeScript
displayX: number
```

鼠标光标在当前应用屏幕坐标系中的X坐标。

单位：vp

**Type:** number

**Since:** 17

**ArkTS mode:** ArkTS-Dyn only, since version 17.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 17.

<!--Device-AxisEvent-displayX: number--><!--Device-AxisEvent-displayX: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## displayY

```TypeScript
displayY: number
```

鼠标光标在当前应用屏幕坐标系中的Y坐标。

单位：vp

**Type:** number

**Since:** 17

**ArkTS mode:** ArkTS-Dyn only, since version 17.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 17.

<!--Device-AxisEvent-displayY: number--><!--Device-AxisEvent-displayY: number-End-->

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

<!--Device-AxisEvent-eventHandleId?: number--><!--Device-AxisEvent-eventHandleId?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## globalDisplayX

```TypeScript
globalDisplayX?: number
```

鼠标光标在[全局坐标系](../../../windowmanager/window-terminology.md#全局坐标系)中的X坐标。

单位：vp

取值范围：[0, +∞)

**Type:** number

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-AxisEvent-globalDisplayX?: number--><!--Device-AxisEvent-globalDisplayX?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## globalDisplayY

```TypeScript
globalDisplayY?: number
```

鼠标光标或手写笔位置在[全局坐标系](../../../windowmanager/window-terminology.md#全局坐标系)中的Y坐标。

单位：vp

取值范围：[0, +∞)

**Type:** number

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-AxisEvent-globalDisplayY?: number--><!--Device-AxisEvent-globalDisplayY?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## propagation

```TypeScript
propagation: Callback<void>
```

激活[事件冒泡](../../../ui/arkts-interaction-basic-principles.md#事件冒泡)。

**Type:** [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;void&gt;

**Since:** 17

**ArkTS mode:** ArkTS-Dyn only, since version 17.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 17.

<!--Device-AxisEvent-propagation: Callback<void>--><!--Device-AxisEvent-propagation: Callback<void>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## scrollStep

```TypeScript
scrollStep?: number
```

鼠标轴滚动步长配置。

**说明：** 仅支持鼠标滚轮，取值范围：[0~65535]

**Type:** number

**Since:** 17

**ArkTS mode:** ArkTS-Dyn only, since version 17.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 17.

<!--Device-AxisEvent-scrollStep?: number--><!--Device-AxisEvent-scrollStep?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## windowX

```TypeScript
windowX: number
```

鼠标光标在当前应用窗口坐标系中的X坐标。

单位：vp

**Type:** number

**Since:** 17

**ArkTS mode:** ArkTS-Dyn only, since version 17.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 17.

<!--Device-AxisEvent-windowX: number--><!--Device-AxisEvent-windowX: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## windowY

```TypeScript
windowY: number
```

鼠标光标在当前应用窗口坐标系中的Y坐标。

单位：vp

**Type:** number

**Since:** 17

**ArkTS mode:** ArkTS-Dyn only, since version 17.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 17.

<!--Device-AxisEvent-windowY: number--><!--Device-AxisEvent-windowY: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## x

```TypeScript
x: number
```

鼠标光标在被点击元素为基准的[组件坐标系](../../../ui/arkui-glossary.md#组件坐标系)中的X坐标。

单位：vp

**Type:** number

**Since:** 17

**ArkTS mode:** ArkTS-Dyn only, since version 17.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 17.

<!--Device-AxisEvent-x: number--><!--Device-AxisEvent-x: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## y

```TypeScript
y: number
```

鼠标光标在被点击元素为基准的[组件坐标系](../../../ui/arkui-glossary.md#组件坐标系)中的Y坐标。

单位：vp

**Type:** number

**Since:** 17

**ArkTS mode:** ArkTS-Dyn only, since version 17.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 17.

<!--Device-AxisEvent-y: number--><!--Device-AxisEvent-y: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

