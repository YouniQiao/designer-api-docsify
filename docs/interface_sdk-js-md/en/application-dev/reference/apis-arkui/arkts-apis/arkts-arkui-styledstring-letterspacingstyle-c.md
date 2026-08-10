# LetterSpacingStyle

文本字符间距对象说明。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare class LetterSpacingStyle--><!--Device-unnamed-export declare class LetterSpacingStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(value: LengthMetrics)
```

文本字符间距的构造函数。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LetterSpacingStyle-constructor(value: LengthMetrics)--><!--Device-LetterSpacingStyle-constructor(value: LengthMetrics)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [LengthMetrics](arkts-arkui-lengthmetrics-t.md) | Yes | 文本字符间距设置项。如果LengthMetrics的unit值是PERCENT，该设置不生效。 |

## letterSpacing

```TypeScript
readonly letterSpacing: double
```

获取属性字符串的文本字符间距。

单位：[vp](../../../reference/apis-arkui/arkui-ts/ts-pixel-units.md#基本像素单位)

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LetterSpacingStyle-readonly letterSpacing: double--><!--Device-LetterSpacingStyle-readonly letterSpacing: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

