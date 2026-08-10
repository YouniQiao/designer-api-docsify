# LineHeightStyle

文本行高对象说明。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-unnamed-declare class LineHeightStyle--><!--Device-unnamed-declare class LineHeightStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(lineHeight: LengthMetrics)
```

文本行高的构造函数。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-LineHeightStyle-constructor(lineHeight: LengthMetrics)--><!--Device-LineHeightStyle-constructor(lineHeight: LengthMetrics)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| lineHeight | [LengthMetrics](arkts-arkui-lengthmetrics-t.md) | Yes | 文本行高设置项。如果LengthMetrics的unit值是PERCENT，当前设置不生效。LengthMetrics的value值大于0时，文本行高设置 生效，否则文本行高自适应字体大小。 |

## constructor

```TypeScript
constructor(lineHeight: LengthMetrics, lineHeightMultiple?: number)
```

文本行高及倍数的构造函数。

> **说明：**
> 
> - lineHeightMultiple与lineHeight或[LineSpacingStyle](arkts-arkui-linespacingstyle-c.md)同时设置时，仅lineHeightMultiple生效，行高为该行最高字体高度
> 与倍数的乘积。
> 
> - lineHeightMultiple小于0或undefined时不生效，使用lineHeight和[LineSpacingStyle](arkts-arkui-linespacingstyle-c.md)设置行高和行间距。
> 
> - lineHeightMultiple等于0时等效于设置为1。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-LineHeightStyle-constructor(lineHeight: LengthMetrics, lineHeightMultiple?: number)--><!--Device-LineHeightStyle-constructor(lineHeight: LengthMetrics, lineHeightMultiple?: number)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| lineHeight | [LengthMetrics](arkts-arkui-lengthmetrics-t.md) | Yes | 文本行高设置项。LengthMetrics的value值大于0时，文本行高设置生效，否则文本行高自适应字体大小。 |
| lineHeightMultiple | number | No | 文本行高的倍数值。 &lt;br&gt;取值范围：[0, +∞)，支持小数。 &lt;br&gt;**说明：** &lt;br&gt;与lineHeight或[LineSpacingStyle](arkts-arkui-linespacingstyle-c.md)同时设置时，仅lineHeightMultiple生效，行高为该行最高字体高度与倍数的乘积； &lt;br&gt;小于0或undefined时不生效； &lt;br&gt;等于0时等效于设置为1。 |

## lineHeight

```TypeScript
readonly lineHeight: number
```

获取属性字符串的文本行高。

单位：[vp](../../../reference/apis-arkui/arkui-ts/ts-pixel-units.md#基本像素单位)

**Type:** number

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-LineHeightStyle-readonly lineHeight: number--><!--Device-LineHeightStyle-readonly lineHeight: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## lineHeightMultiple

```TypeScript
readonly lineHeightMultiple?: number
```

文本行高的倍数值。实际生效的行高为该行最高的字体高度与倍数的乘积。

**说明：** lineHeightMultiple与lineHeight或[LineSpacingStyle](arkts-arkui-linespacingstyle-c.md)同时设置时，仅lineHeightMultiple生效。lineHeightMultiple小于0或undefined时不生效。lineHeightMultiple等于0时等效于设置为1。

**Type:** number

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-LineHeightStyle-readonly lineHeightMultiple?: number--><!--Device-LineHeightStyle-readonly lineHeightMultiple?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

