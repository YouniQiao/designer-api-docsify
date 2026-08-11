# DividerOptions

Defines the struct of DividerOptions.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface DividerOptions--><!--Device-unnamed-export declare interface DividerOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## color

```TypeScript
color?: ResourceColor
```

Color of the divider.

**Type:** [ResourceColor](arkts-arkui-resourcecolor-t.md)

**Default:** "#33000000"

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DividerOptions-color?: ResourceColor--><!--Device-DividerOptions-color?: ResourceColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## endMargin

```TypeScript
endMargin?: Dimension
```

Distance between the divider and the end edge of the picker.The unit is vp by default. You can also specify it as px. The percentage type is not supported.

&lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;:&lt;br&gt;Values less than 0 are invalid. The maximum value allowed is the width of the column.&lt;/p&gt;

**Type:** [Dimension](arkts-arkui-dimension-t.md)

**Default:** 0

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DividerOptions-endMargin?: Dimension--><!--Device-DividerOptions-endMargin?: Dimension-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## startMargin

```TypeScript
startMargin?: Dimension
```

Distance between the divider and the start edge of the picker.The unit is vp by default. You can also specify it as px. The percentage type is not supported.

&lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;:Values less than 0 are invalid. The maximum value allowed is the width of the column.&lt;/p&gt;

**Type:** [Dimension](arkts-arkui-dimension-t.md)

**Default:** 0

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DividerOptions-startMargin?: Dimension--><!--Device-DividerOptions-startMargin?: Dimension-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## strokeWidth

```TypeScript
strokeWidth?: Dimension
```

Stroke width of the divider.The unit is vp by default. You can also specify it as px. The percentage type is not supported.

&lt;p&gt;&lt;strong&gt;NOTE&lt;/strong&gt;:&lt;br&gt;If the value is less than 0, the default value is used.&lt;br&gt;The maximum value allowed is half the height of the column.&lt;/p&gt;

**Type:** [Dimension](arkts-arkui-dimension-t.md)

**Default:** 2.0px

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-DividerOptions-strokeWidth?: Dimension--><!--Device-DividerOptions-strokeWidth?: Dimension-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

