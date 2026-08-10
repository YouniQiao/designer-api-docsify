# PanRecognizer

手势识别器对象。

**Inheritance/Implementation:** PanRecognizer extends [GestureRecognizer](arkts-arkui-gesturerecognizer-c.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-unnamed-declare class PanRecognizer extends GestureRecognizer--><!--Device-unnamed-declare class PanRecognizer extends GestureRecognizer-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## getDirection

```TypeScript
getDirection(): PanDirection
```

返回当前滑动手势识别器的识别方向。

**Since:** 19

**ArkTS mode:** ArkTS-Dyn only, since version 19.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-PanRecognizer-getDirection(): PanDirection--><!--Device-PanRecognizer-getDirection(): PanDirection-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [PanDirection](arkts-arkui-gesture-pandirection-e.md) | 当前滑动手势识别器的识别方向。 |

## getDistance

```TypeScript
getDistance(): number
```

返回当前滑动手势识别器触发的最小滑动距离。

**Since:** 19

**ArkTS mode:** ArkTS-Dyn only, since version 19.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-PanRecognizer-getDistance(): number--><!--Device-PanRecognizer-getDistance(): number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| number | 当前滑动手势识别器触发的最小滑动距离。单位：vp |

## getDistanceMap

```TypeScript
getDistanceMap(): Map<SourceTool, number>
```

返回滑动手势识别器在不同输入源的情况下触发的最小滑动距离。

> **说明：**
> 
> 仅支持对通过Pan手势初始化配置修改的设备类型进行阈值查询。对于默认滑动阈值，可通过查询[SourceTool](arkts-arkui-common-sourcetool-e.md).Unknown类型获取。其他未主动设置的类型则无法获取。

**Since:** 19

**ArkTS mode:** ArkTS-Dyn only, since version 19.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 19.

<!--Device-PanRecognizer-getDistanceMap(): Map<SourceTool, number>--><!--Device-PanRecognizer-getDistanceMap(): Map<SourceTool, number>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| Map&lt;[SourceTool](../arkts-components/arkts-arkui-sourcetool-e.md), number&gt; | 不同输入源的滑动手势识别器触发的最小滑动距离。滑动距离的单位：vp |

## getPanGestureOptions

```TypeScript
getPanGestureOptions(): PanGestureOptions
```

返回当前滑动手势识别器的属性。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-PanRecognizer-getPanGestureOptions(): PanGestureOptions--><!--Device-PanRecognizer-getPanGestureOptions(): PanGestureOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [PanGestureOptions](arkts-arkui-pangestureoptions-c.md) | 当前滑动手势识别器的属性。 |

