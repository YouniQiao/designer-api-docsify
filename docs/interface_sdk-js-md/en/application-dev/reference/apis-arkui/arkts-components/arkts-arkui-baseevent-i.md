# BaseEvent

基础事件类型。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

<!--Device-unnamed-declare interface BaseEvent--><!--Device-unnamed-declare interface BaseEvent-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## getModifierKeyState

```TypeScript
getModifierKeyState?(keys: Array<string>): boolean
```

获取功能键按压状态。报错信息请参考以下错误码。支持功能键'Ctrl'\|'Alt'\|'Shift'。

> **说明：**
> 
> 此接口不支持在手写笔场景下使用。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-BaseEvent-getModifierKeyState?(keys: Array<string>): boolean--><!--Device-BaseEvent-getModifierKeyState?(keys: Array<string>): boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| keys | Array&lt;string&gt; | Yes | 功能键列表。 |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | 返回功能键按压状态。当功能键均处于按压状态时返回true，否则返回false。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types. 2. Parameter verification failed. |

## axisHorizontal

```TypeScript
axisHorizontal ?: number
```

水平轴值。

默认值：0

**说明：**

当前仅在鼠标滚轮或触控板双指滑动触发的Pan手势，或使用Ctrl+鼠标滚轮触发的Pinch手势中可以获取。

对于Shift+鼠标滚轮触发的横向滚动场景，axisHorizontal为0，滚动值体现在axisVertical中。

**Type:** number

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-BaseEvent-axisHorizontal ?: number--><!--Device-BaseEvent-axisHorizontal ?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## axisPinch

```TypeScript
axisPinch?: number
```

双指缩放比例。

默认值：0

**说明：**

仅在触控板上通过双指缩放操作触发的Pinch手势，或在轴事件中，可以获取该值；在其他场景下，获取到的将是默认值。

缩放比例是指在双指缩放事件触发过程中，双指当前距离与最初按下时距离的比值。

取值范围：[0, +∞)

**Type:** number

**Since:** 21

**ArkTS mode:** ArkTS-Dyn only, since version 21.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 21.

**Widget capability:** This API can be used in ArkTS widgets since API version 21.

<!--Device-BaseEvent-axisPinch?: number--><!--Device-BaseEvent-axisPinch?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## axisVertical

```TypeScript
axisVertical ?: number
```

垂直轴值。

默认值：0

**说明：**

当前仅在鼠标滚轮或触控板双指滑动触发的Pan手势，或使用Ctrl+鼠标滚轮触发的Pinch手势中可以获取。

对于Shift+鼠标滚轮触发的横向滚动场景，滚动值体现在axisVertical中。

**Type:** number

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

<!--Device-BaseEvent-axisVertical ?: number--><!--Device-BaseEvent-axisVertical ?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## deviceId

```TypeScript
deviceId?: number
```

触发当前事件的输入设备ID。

默认值：0

取值范围：[0, +∞)

**Type:** number

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-BaseEvent-deviceId?: number--><!--Device-BaseEvent-deviceId?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## pressure

```TypeScript
pressure: number
```

按压的压力大小。

默认值：0

取值范围：[0,1]，典型值0.913168，压感大小与数值正相关。在部分设备中，由于设备的硬件参数配置不同，可能会返回大于1的值。

**Type:** number

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-BaseEvent-pressure: number--><!--Device-BaseEvent-pressure: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## rollAngle

```TypeScript
rollAngle?: number
```

手写笔与设备平面的夹角。

单位：deg

**Type:** number

**Since:** 17

**ArkTS mode:** ArkTS-Dyn only, since version 17.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 17.

**Widget capability:** This API can be used in ArkTS widgets since API version 17.

<!--Device-BaseEvent-rollAngle?: number--><!--Device-BaseEvent-rollAngle?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## source

```TypeScript
source: SourceType
```

事件输入设备的类型。

**Type:** [SourceType](../../apis-arkweb/arkts-apis/arkts-arkweb-webview-sourcetype-e.md)

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-BaseEvent-source: SourceType--><!--Device-BaseEvent-source: SourceType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## sourceTool

```TypeScript
sourceTool: SourceTool
```

事件输入源的类型。

**Type:** [SourceTool](../arkts-apis/arkts-arkui-common-sourcetool-e.md)

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-BaseEvent-sourceTool: SourceTool--><!--Device-BaseEvent-sourceTool: SourceTool-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## target

```TypeScript
target: EventTarget
```

触发手势事件的元素对象。

**Type:** [EventTarget](../../apis-arkts/arkts-apis/arkts-arkts-worker-eventtarget-i.md)

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-BaseEvent-target: EventTarget--><!--Device-BaseEvent-target: EventTarget-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## targetDisplayId

```TypeScript
targetDisplayId?: number
```

事件发生的屏幕ID。 

默认值：0

取值范围：[0, +∞)

**Type:** number

**Since:** 15

**ArkTS mode:** ArkTS-Dyn only, since version 15.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-BaseEvent-targetDisplayId?: number--><!--Device-BaseEvent-targetDisplayId?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## tiltX

```TypeScript
tiltX: number
```

手写笔在设备平面上的投影与设备平面X轴的夹角。

单位：deg

默认值：0

**Type:** number

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-BaseEvent-tiltX: number--><!--Device-BaseEvent-tiltX: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## tiltY

```TypeScript
tiltY: number
```

手写笔在设备平面上的投影与设备平面Y轴的夹角。

单位：deg

默认值：0

**Type:** number

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-BaseEvent-tiltY: number--><!--Device-BaseEvent-tiltY: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## timestamp

```TypeScript
timestamp: number
```

事件时间戳，触发事件时距离系统启动的时间间隔。

单位：ns

**Type:** number

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-BaseEvent-timestamp: number--><!--Device-BaseEvent-timestamp: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

