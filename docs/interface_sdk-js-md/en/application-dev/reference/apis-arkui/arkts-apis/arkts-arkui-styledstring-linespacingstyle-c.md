# LineSpacingStyle

文本行间距对象说明。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

<!--Device-unnamed-export declare class LineSpacingStyle--><!--Device-unnamed-export declare class LineSpacingStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(lineSpacing: LengthMetrics, options?: LineSpacingOptions)
```

文本行间距的构造函数。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LineSpacingStyle-constructor(lineSpacing: LengthMetrics, options?: LineSpacingOptions)--><!--Device-LineSpacingStyle-constructor(lineSpacing: LengthMetrics, options?: LineSpacingOptions)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| lineSpacing | [LengthMetrics](arkts-arkui-lengthmetrics-t.md) | Yes | 文本的行间距。&lt;br/&gt;默认值：0.0&lt;br/&gt;取值范围： [0, +∞)&lt;br/&gt;**说明：** LengthMetrics的value值小于0时，取默认值0.0。 |
| options | [LineSpacingOptions](arkts-arkui-linespacingoptions-i.md) | No | 行间距的配置项。&lt;br/&gt;默认值：{ onlyBetweenLines: false } |

## lineSpacing

```TypeScript
readonly lineSpacing: double
```

文本行间距。

取值范围：[0, +∞)

单位：[vp](../../../reference/apis-arkui/arkui-ts/ts-pixel-units.md#基本像素单位)

**Type:** double

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LineSpacingStyle-readonly lineSpacing: double--><!--Device-LineSpacingStyle-readonly lineSpacing: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## options

```TypeScript
readonly options?: LineSpacingOptions
```

行间距配置项。

**Type:** [LineSpacingOptions](arkts-arkui-linespacingoptions-i.md)

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LineSpacingStyle-readonly options?: LineSpacingOptions--><!--Device-LineSpacingStyle-readonly options?: LineSpacingOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

