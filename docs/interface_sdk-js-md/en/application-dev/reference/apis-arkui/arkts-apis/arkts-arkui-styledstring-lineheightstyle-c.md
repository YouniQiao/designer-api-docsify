# LineHeightStyle

文本行高对象说明。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare class LineHeightStyle--><!--Device-unnamed-export declare class LineHeightStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(lineHeight: LengthMetrics)
```

文本行高的构造函数。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LineHeightStyle-constructor(lineHeight: LengthMetrics)--><!--Device-LineHeightStyle-constructor(lineHeight: LengthMetrics)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| lineHeight | [LengthMetrics](arkts-arkui-lengthmetrics-t.md) | Yes | 文本行高设置项。LengthMetrics的value值大于0时，文本行高设置生效，否则文本行高自适应字体大小。 |

## constructor

```TypeScript
constructor(lineHeight: LengthMetrics, lineHeightMultiple: double)
```

文本行高及倍数的构造函数。

> **说明：**
> 
> - lineHeightMultiple与lineHeight或
> [LineSpacingStyle](../../../reference/apis-arkui/arkui-ts/ts-universal-styled-string.md#linespacingstyle)同时设置
> 时，仅lineHeightMultiple生效，行高为该行最高字体高度与倍数的乘积。
> 
> - lineHeightMultiple小于0或undefined时不生效，使用lineHeight和
> [LineSpacingStyle](../../../reference/apis-arkui/arkui-ts/ts-universal-styled-string.md#linespacingstyle)设置行高和
> 行间距。
> 
> - lineHeightMultiple等于0时等效于设置为1。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LineHeightStyle-constructor(lineHeight: LengthMetrics, lineHeightMultiple: double)--><!--Device-LineHeightStyle-constructor(lineHeight: LengthMetrics, lineHeightMultiple: double)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| lineHeight | [LengthMetrics](arkts-arkui-lengthmetrics-t.md) | Yes | 文本行高设置项。LengthMetrics的value值大于0时，文本行高设置生效，否则文本行高自适应字体大小。 |
| lineHeightMultiple | double | Yes | 文本行高的倍数值。&lt;br/&gt;取值范围：[0, +∞)，支持小数。 |

## lineHeight

```TypeScript
readonly lineHeight: double
```

获取属性字符串的文本行高。

单位：[vp](../../../reference/apis-arkui/arkui-ts/ts-pixel-units.md#基本像素单位)

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LineHeightStyle-readonly lineHeight: double--><!--Device-LineHeightStyle-readonly lineHeight: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## lineHeightMultiple

```TypeScript
readonly lineHeightMultiple?: double
```

文本行高的倍数值。实际生效的行高为该行最高的字体高度与倍数的乘积。

**Type:** double

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LineHeightStyle-readonly lineHeightMultiple?: double--><!--Device-LineHeightStyle-readonly lineHeightMultiple?: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

