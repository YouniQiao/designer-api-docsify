# FingerInfo

手指信息类型。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface FingerInfo--><!--Device-unnamed-export declare interface FingerInfo-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## getCurrentLocalPosition

```TypeScript
default getCurrentLocalPosition(): Coordinate2D
```

获取手指位置相对于当前组件实时位置的左上角坐标。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FingerInfo-default getCurrentLocalPosition(): Coordinate2D--><!--Device-FingerInfo-default getCurrentLocalPosition(): Coordinate2D-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [Coordinate2D](arkts-arkui-coordinate2d-i.md) | 获取手指位置相对于当前组件实时位置的左上角坐标。 |

## displayX

```TypeScript
displayX: double
```

相对于屏幕左上角的x轴坐标，单位为vp。

取值范围：[0, +∞)

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FingerInfo-displayX: double--><!--Device-FingerInfo-displayX: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## displayY

```TypeScript
displayY: double
```

相对于屏幕左上角的y轴坐标，单位为vp。

取值范围：[0, +∞)

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FingerInfo-displayY: double--><!--Device-FingerInfo-displayY: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## globalDisplayX

```TypeScript
globalDisplayX?: double
```

相对于全局屏幕的左上角的X坐标，单位为vp。

取值范围：[0, +∞)

**Type:** double

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FingerInfo-globalDisplayX?: double--><!--Device-FingerInfo-globalDisplayX?: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## globalDisplayY

```TypeScript
globalDisplayY?: double
```

相对于全局屏幕的左上角的Y坐标，单位为vp。

取值范围：[0, +∞)

**Type:** double

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FingerInfo-globalDisplayY?: double--><!--Device-FingerInfo-globalDisplayY?: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## globalX

```TypeScript
globalX: double
```

相对于应用窗口左上角的x轴坐标，单位为vp。

取值范围：[0, +∞)

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FingerInfo-globalX: double--><!--Device-FingerInfo-globalX: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## globalY

```TypeScript
globalY: double
```

相对于应用窗口左上角的y轴坐标，单位为vp。

取值范围：[0, +∞)

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FingerInfo-globalY: double--><!--Device-FingerInfo-globalY: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## hand

```TypeScript
hand?: InteractionHand
```

表示事件是由左手点击还是右手点击触发。

**Type:** [InteractionHand](arkts-arkui-interactionhand-e.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FingerInfo-hand?: InteractionHand--><!--Device-FingerInfo-hand?: InteractionHand-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## id

```TypeScript
id: int
```

手指的索引编号，由按下手指的数量决定，按下一根手指为0，之后每按下1根手指索引编号加一。

**说明：**

鼠标（索引编号为1001）、手写笔（索引编号为102）、鼠标滚轮（索引编号为0）、触摸板双指滑动（索引编号为0）的索引编号也会被转化为手指的索引编号。

取值范围：[0, 9)

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FingerInfo-id: int--><!--Device-FingerInfo-id: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## localX

```TypeScript
localX: double
```

相对于当前组件元素原始区域左上角的x轴坐标，单位为vp。

取值范围：[0, +∞)

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FingerInfo-localX: double--><!--Device-FingerInfo-localX: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## localY

```TypeScript
localY: double
```

相对于当前组件元素原始区域左上角的y轴坐标，单位为vp。

取值范围：[0, +∞)

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FingerInfo-localY: double--><!--Device-FingerInfo-localY: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

