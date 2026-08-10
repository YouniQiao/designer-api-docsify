# LabelStyle

label文本和字体的样式对象。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-unnamed-declare interface LabelStyle--><!--Device-unnamed-declare interface LabelStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## font

```TypeScript
font?: Font
```

设置label文本字体样式。

当页签为子页签时，默认值是字体大小16.0fp、字体类型'HarmonyOS Sans'，字体风格正常，选中时字重中等，未选中时字重正常。

当页签为底部页签时，默认值是字体大小10.0fp、字体类型'HarmonyOS Sans'，字体风格正常，字重中等。

从API version 12开始，底部页签内容左右排布时默认字体大小为12.0fp。

**Type:** [Font](../arkts-apis/arkts-arkui-arkui-uicontext-font-c.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-LabelStyle-font?: Font--><!--Device-LabelStyle-font?: Font-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## heightAdaptivePolicy

```TypeScript
heightAdaptivePolicy?: TextHeightAdaptivePolicy
```

设置Label文本自适应高度的方式。默认值是最大行数优先。

**Type:** [TextHeightAdaptivePolicy](../arkts-apis/arkts-arkui-enums-textheightadaptivepolicy-e.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-LabelStyle-heightAdaptivePolicy?: TextHeightAdaptivePolicy--><!--Device-LabelStyle-heightAdaptivePolicy?: TextHeightAdaptivePolicy-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## maxFontSize

```TypeScript
maxFontSize?: number | ResourceStr
```

设置label文本最大显示字号（不支持百分比设置）。需配合minFontSize以及maxLines或布局大小限制使用。自适应文本大小生效后，font.size不生效。默认值是0.0fp，即默认自适应文本大小不生效。

取值范围：[minFontSize, +∞)。异常值时取默认值。

**Type:** number \| ResourceStr

**Default:** 0.0fp [since 11]

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-LabelStyle-maxFontSize?: number | ResourceStr--><!--Device-LabelStyle-maxFontSize?: number | ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## maxLines

```TypeScript
maxLines?: number
```

设置label文本的最大行数。如果指定此参数，则文本最多不会超过指定的行。如果有多余的文本，可以通过textOverflow来指定截断方式。默认值是1。

取值范围：[1, +∞)。异常值时取默认值。

**Type:** number

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-LabelStyle-maxLines?: number--><!--Device-LabelStyle-maxLines?: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## minFontSize

```TypeScript
minFontSize?: number | ResourceStr
```

设置label文本最小显示字号（不支持百分比设置）。需配合maxFontSize以及maxLines或布局大小限制使用。自适应文本大小生效后，font.size不生效。默认值是0.0fp，即默认自适应文本大小不生效。

取值范围：(0, +∞)。异常值时取默认值。

**Type:** number \| ResourceStr

**Default:** 0.0fp [since 11]

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-LabelStyle-minFontSize?: number | ResourceStr--><!--Device-LabelStyle-minFontSize?: number | ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## overflow

```TypeScript
overflow?: TextOverflow
```

设置label文本超长时的显示方式。默认值是省略号截断。

**Type:** [TextOverflow](../arkts-apis/arkts-arkui-enums-textoverflow-e.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-LabelStyle-overflow?: TextOverflow--><!--Device-LabelStyle-overflow?: TextOverflow-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## selectedColor

```TypeScript
selectedColor?: ResourceColor
```

设置label文本字体选中时的颜色。

默认值：#FF007DFF

**Type:** [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md)

**Default:** #FF007DFF

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-LabelStyle-selectedColor?: ResourceColor--><!--Device-LabelStyle-selectedColor?: ResourceColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## unselectedColor

```TypeScript
unselectedColor?: ResourceColor
```

设置label文本字体未选中时的颜色。

默认值：#99182431

**Type:** [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md)

**Default:** #99182431

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-LabelStyle-unselectedColor?: ResourceColor--><!--Device-LabelStyle-unselectedColor?: ResourceColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

