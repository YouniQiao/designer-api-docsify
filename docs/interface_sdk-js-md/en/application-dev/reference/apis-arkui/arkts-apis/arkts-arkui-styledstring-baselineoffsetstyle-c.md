# BaselineOffsetStyle

文本基线偏移量对象说明。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare class BaselineOffsetStyle--><!--Device-unnamed-export declare class BaselineOffsetStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(value: LengthMetrics)
```

文本基线偏移的构造函数。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BaselineOffsetStyle-constructor(value: LengthMetrics)--><!--Device-BaselineOffsetStyle-constructor(value: LengthMetrics)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [LengthMetrics](arkts-arkui-lengthmetrics-t.md) | Yes | 文本基线偏移量设置项。如果LengthMetrics的unit值是PERCENT，该设置不生效。 |

## baselineOffset

```TypeScript
readonly baselineOffset: double
```

获取属性字符串的文本基线偏移量。

单位：[vp](../../../reference/apis-arkui/arkui-ts/ts-pixel-units.md#基本像素单位)

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BaselineOffsetStyle-readonly baselineOffset: double--><!--Device-BaselineOffsetStyle-readonly baselineOffset: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

