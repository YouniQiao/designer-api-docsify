# TabBarLabelStyle

label文本和字体的样式对象。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface TabBarLabelStyle--><!--Device-unnamed-export declare interface TabBarLabelStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## font

```TypeScript
font?: Font
```

设置Label文本字体样式。

当页签为子页签时，默认值是字体大小16.0fp、字体类型'HarmonyOS Sans'，字体风格正常，选中时字重中等，未选中时字重正常。

当页签为底部页签时，默认值是字体大小10.0fp、字体类型'HarmonyOS Sans'，字体风格正常，字重中等。

从API version 12开始，底部页签内容左右排布时默认字体大小为12.0fp。

**Type:** [Font](arkts-arkui-font-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TabBarLabelStyle-font?: Font--><!--Device-TabBarLabelStyle-font?: Font-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## heightAdaptivePolicy

```TypeScript
heightAdaptivePolicy?: TextHeightAdaptivePolicy
```

设置Label文本自适应高度的方式。默认值是最大行数优先。

**Type:** [TextHeightAdaptivePolicy](arkts-arkui-textheightadaptivepolicy-e.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TabBarLabelStyle-heightAdaptivePolicy?: TextHeightAdaptivePolicy--><!--Device-TabBarLabelStyle-heightAdaptivePolicy?: TextHeightAdaptivePolicy-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## maxFontSize

```TypeScript
maxFontSize?: double | ResourceStr
```

设置Label文本最大显示字号（不支持百分比设置）。需配合minFontSize以及maxLines或布局大小限制使用。自适应文本大小生效后，font.size不生效。默认值是0.0fp，即默认自适应文本大小不生效。

取值范围：[minFontSize, +∞)。

**Type:** double \| ResourceStr

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TabBarLabelStyle-maxFontSize?: double | ResourceStr--><!--Device-TabBarLabelStyle-maxFontSize?: double | ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## maxLines

```TypeScript
maxLines?: int
```

设置Label文本的最大行数。如果指定此参数，则文本最多不会超过指定的行。如果有多余的文本，可以通过textOverflow来指定截断方式。默认值是1。

取值范围：[1, +∞)。

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TabBarLabelStyle-maxLines?: int--><!--Device-TabBarLabelStyle-maxLines?: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## minFontSize

```TypeScript
minFontSize?: double | ResourceStr
```

设置Label文本最小显示字号（不支持百分比设置）。需配合maxFontSize以及maxLines或布局大小限制使用。自适应文本大小生效后，font.size不生效。默认值是0.0fp，即默认自适应文本大小不生效。

取值范围：(0, +∞)。

**Type:** double \| ResourceStr

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TabBarLabelStyle-minFontSize?: double | ResourceStr--><!--Device-TabBarLabelStyle-minFontSize?: double | ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## overflow

```TypeScript
overflow?: TextOverflow
```

设置Label文本超长时的显示方式。默认值是省略号截断。

**Type:** [TextOverflow](arkts-arkui-textoverflow-e.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TabBarLabelStyle-overflow?: TextOverflow--><!--Device-TabBarLabelStyle-overflow?: TextOverflow-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## selectedColor

```TypeScript
selectedColor?: ResourceColor
```

设置Label文本字体选中时的颜色。

默认值：#FF007DFF

**Type:** [ResourceColor](arkts-arkui-resourcecolor-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TabBarLabelStyle-selectedColor?: ResourceColor--><!--Device-TabBarLabelStyle-selectedColor?: ResourceColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## unselectedColor

```TypeScript
unselectedColor?: ResourceColor
```

设置Label文本字体未选中时的颜色。

默认值：#99182431

**Type:** [ResourceColor](arkts-arkui-resourcecolor-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-TabBarLabelStyle-unselectedColor?: ResourceColor--><!--Device-TabBarLabelStyle-unselectedColor?: ResourceColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

