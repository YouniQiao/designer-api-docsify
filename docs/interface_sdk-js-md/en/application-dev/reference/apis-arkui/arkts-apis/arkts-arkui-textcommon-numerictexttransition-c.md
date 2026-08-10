# NumericTextTransition

数字翻牌动效。仅限正整数，不支持小数和负数。不支持渐变色和Text跑马灯模式。不支持选中，  
[copyOption](../../../reference/apis-arkui/arkui-ts/ts-basic-components-text.md#copyoption9)属性无效。当文本存在子组件时或通过属性字符串设置时，数字翻牌失效。

NumericTextTransition继承自[ContentTransition](arkts-arkui-textcommon-contenttransition-c.md)。

**Inheritance/Implementation:** NumericTextTransition extends [ContentTransition](arkts-arkui-textcommon-contenttransition-c.md)

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

<!--Device-unnamed-export declare class NumericTextTransition extends ContentTransition--><!--Device-unnamed-export declare class NumericTextTransition extends ContentTransition-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(options?: NumericTextTransitionOptions)
```

用于创建NumericTextTransition对象的构造函数。

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NumericTextTransition-constructor(options?: NumericTextTransitionOptions)--><!--Device-NumericTextTransition-constructor(options?: NumericTextTransitionOptions)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [NumericTextTransitionOptions](arkts-arkui-numerictexttransitionoptions-i.md) | No | 设置数字翻牌动效。 默认值继承 [NumericTextTransitionOptions](arkts-arkui-textcommon-numerictexttransitionoptions-i.md)。 |

## enableBlur

```TypeScript
enableBlur?: boolean
```

是否开启翻牌模糊效果。

默认值：false

true：开启翻牌模糊效果。

false：不开启翻牌模糊效果。

**Type:** boolean

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NumericTextTransition-enableBlur?: boolean--><!--Device-NumericTextTransition-enableBlur?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## flipDirection

```TypeScript
flipDirection?: FlipDirection
```

翻牌方向。

默认值：FlipDirection.DOWN

**Type:** [FlipDirection](arkts-arkui-textcommon-flipdirection-e.md)

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-NumericTextTransition-flipDirection?: FlipDirection--><!--Device-NumericTextTransition-flipDirection?: FlipDirection-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

