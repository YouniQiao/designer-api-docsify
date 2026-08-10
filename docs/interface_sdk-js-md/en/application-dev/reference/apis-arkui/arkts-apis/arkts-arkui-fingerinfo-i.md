# FingerInfo

手指信息类型。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

<!--Device-unnamed-interface FingerInfo--><!--Device-unnamed-interface FingerInfo-End-->

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

<!--Device-FingerInfo-getCurrentLocalPosition?(): Coordinate2D--><!--Device-FingerInfo-getCurrentLocalPosition?(): Coordinate2D-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [Coordinate2D](arkts-arkui-coordinate2d-i.md) | 点击位置相对于当前组件实时位置的左上角坐标。 |

## displayX

```TypeScript
displayX: number
```

相对于屏幕左上角的x轴坐标，单位为vp。

取值范围：[0, +∞)

**Type:** number

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-FingerInfo-displayX: number--><!--Device-FingerInfo-displayX: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## displayY

```TypeScript
displayY: number
```

相对于屏幕左上角的y轴坐标，单位为vp。

取值范围：[0, +∞)

**Type:** number

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-FingerInfo-displayY: number--><!--Device-FingerInfo-displayY: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## globalDisplayX

```TypeScript
globalDisplayX?: number
```

相对于全局屏幕的左上角的X坐标，单位为vp。

取值范围：[0, +∞)

**Type:** number

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-FingerInfo-globalDisplayX?: number--><!--Device-FingerInfo-globalDisplayX?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## globalDisplayY

```TypeScript
globalDisplayY?: number
```

相对于全局屏幕的左上角的Y坐标，单位为vp。

取值范围：[0, +∞)

**Type:** number

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-FingerInfo-globalDisplayY?: number--><!--Device-FingerInfo-globalDisplayY?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## globalX

```TypeScript
globalX: number
```

相对于应用窗口左上角的x轴坐标，单位为vp。

取值范围：[0, +∞)

**Type:** number

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-FingerInfo-globalX: number--><!--Device-FingerInfo-globalX: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## globalY

```TypeScript
globalY: number
```

相对于应用窗口左上角的y轴坐标，单位为vp。

取值范围：[0, +∞)

**Type:** number

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-FingerInfo-globalY: number--><!--Device-FingerInfo-globalY: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## hand

```TypeScript
hand?: InteractionHand
```

表示事件是由左手点击还是右手点击触发。

**Type:** [InteractionHand](arkts-arkui-interactionhand-e.md)

**Since:** 15

**ArkTS mode:** ArkTS-Dyn only, since version 15.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-FingerInfo-hand?: InteractionHand--><!--Device-FingerInfo-hand?: InteractionHand-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## id

```TypeScript
id: number
```

手指的索引编号，由按下手指的数量决定，按下一根手指为0，之后每按下1根手指索引编号加一。

**说明：**

鼠标（索引编号为1001）、手写笔（索引编号为102）、鼠标滚轮（索引编号为0）、触摸板双指滑动（索引编号为0）的索引编号也会被转化为手指的索引编号。

取值范围：[0, 9)

**Type:** number

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-FingerInfo-id: number--><!--Device-FingerInfo-id: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## localX

```TypeScript
localX: number
```

相对于当前组件元素原始区域左上角的x轴坐标，单位为vp。

取值范围：[0, +∞)

**Type:** number

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-FingerInfo-localX: number--><!--Device-FingerInfo-localX: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## localY

```TypeScript
localY: number
```

相对于当前组件元素原始区域左上角的y轴坐标，单位为vp。

取值范围：[0, +∞)

**Type:** number

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-FingerInfo-localY: number--><!--Device-FingerInfo-localY: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

