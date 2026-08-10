# ButtonLabelStyle

按钮中文本的显示样式。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface ButtonLabelStyle--><!--Device-unnamed-export declare interface ButtonLabelStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## font

```TypeScript
font?: Font
```

设置label文本字体样式。

默认值：默认值参考[Font](arkts-arkui-arkui-uicontext-font-c.md)。

**Type:** [Font](arkts-arkui-font-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ButtonLabelStyle-font?: Font--><!--Device-ButtonLabelStyle-font?: Font-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## heightAdaptivePolicy

```TypeScript
heightAdaptivePolicy?: TextHeightAdaptivePolicy
```

设置label文本自适应高度的方式。

默认值：TextHeightAdaptivePolicy.MAX_LINES_FIRST

**Type:** [TextHeightAdaptivePolicy](arkts-arkui-textheightadaptivepolicy-e.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ButtonLabelStyle-heightAdaptivePolicy?: TextHeightAdaptivePolicy--><!--Device-ButtonLabelStyle-heightAdaptivePolicy?: TextHeightAdaptivePolicy-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## maxFontSize

```TypeScript
maxFontSize?: double | ResourceStr
```

设置label文本最大显示字号。需配合minFontSize以及maxLines或布局大小限制使用。

**Type:** double \| ResourceStr

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ButtonLabelStyle-maxFontSize?: double | ResourceStr--><!--Device-ButtonLabelStyle-maxFontSize?: double | ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## maxLines

```TypeScript
maxLines?: int
```

设置label文本的最大行数。如果指定此参数，则文本最多不会超过指定的行。如果有多余的文本，可以通过overflow来指定截断方式。

默认值：1

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ButtonLabelStyle-maxLines?: int--><!--Device-ButtonLabelStyle-maxLines?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## minFontSize

```TypeScript
minFontSize?: double | ResourceStr
```

设置label文本最小显示字号。需配合maxFontSize以及maxLines或布局大小限制使用。

**说明：**

minFontSize小于或等于0时，自适应字号不生效。

**Type:** double \| ResourceStr

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ButtonLabelStyle-minFontSize?: double | ResourceStr--><!--Device-ButtonLabelStyle-minFontSize?: double | ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## overflow

```TypeScript
overflow?: TextOverflow
```

设置label文本超长时的显示方式。文本截断是按字截断。例如，英文以单词为最小单位进行截断，若需要以字母为单位进行截断，可在字母间添加零宽空格。

默认值：TextOverflow.Ellipsis

**Type:** [TextOverflow](arkts-arkui-textoverflow-e.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ButtonLabelStyle-overflow?: TextOverflow--><!--Device-ButtonLabelStyle-overflow?: TextOverflow-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## textAlign

```TypeScript
textAlign?: TextAlign
```

设置内容的水平对齐模式。

默认值：TextAlign.Start

**设备差异：** 

默认值是TextAlign.Start。在穿戴设备上，默认值为TextAlign.Center。

**Type:** [TextAlign](arkts-arkui-textalign-e.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ButtonLabelStyle-textAlign?: TextAlign--><!--Device-ButtonLabelStyle-textAlign?: TextAlign-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

