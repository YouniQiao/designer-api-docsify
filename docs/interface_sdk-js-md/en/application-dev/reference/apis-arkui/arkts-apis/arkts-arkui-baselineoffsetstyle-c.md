# BaselineOffsetStyle

文本基线偏移量对象说明。适用于需要微调文本垂直位置的场景，例如化学公式、数学表达式中的上下标文本与正常文本的对齐调整。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-unnamed-declare class BaselineOffsetStyle--><!--Device-unnamed-declare class BaselineOffsetStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(value: LengthMetrics)
```

文本基线偏移的构造函数。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-BaselineOffsetStyle-constructor(value: LengthMetrics)--><!--Device-BaselineOffsetStyle-constructor(value: LengthMetrics)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [LengthMetrics](arkts-arkui-lengthmetrics-t.md) | Yes | 文本基线偏移量设置项。如果LengthMetrics的unit值是PERCENT，该设置不生效。 |

## baselineOffset

```TypeScript
readonly baselineOffset: number
```

获取属性字符串的文本基线偏移量。

单位：[vp](../../../reference/apis-arkui/arkui-ts/ts-pixel-units.md#基本像素单位)

**Type:** number

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-BaselineOffsetStyle-readonly baselineOffset: number--><!--Device-BaselineOffsetStyle-readonly baselineOffset: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

