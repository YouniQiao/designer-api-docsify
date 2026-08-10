# SearchButtonOptions

定义搜索按钮选项。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-unnamed-interface SearchButtonOptions--><!--Device-unnamed-interface SearchButtonOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## autoDisable

```TypeScript
autoDisable?: Boolean
```

Search无文本内容时按钮置灰且不可点击。

默认值：false 

true表示开启按钮置灰功能，false表示不开启。

**Type:** Boolean

**Default:** false

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

<!--Device-SearchButtonOptions-autoDisable?: Boolean--><!--Device-SearchButtonOptions-autoDisable?: Boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fontColor

```TypeScript
fontColor?: ResourceColor
```

文本按钮字体颜色。

**Type:** [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-SearchButtonOptions-fontColor?: ResourceColor--><!--Device-SearchButtonOptions-fontColor?: ResourceColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fontSize

```TypeScript
fontSize?: Length
```

文本按钮字体大小，不传入单位时默认单位为vp，不支持百分比。传入百分比时，不生效。

默认值：跟随主题。

**Type:** [Length](../arkts-apis/arkts-arkui-length-t.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-SearchButtonOptions-fontSize?: Length--><!--Device-SearchButtonOptions-fontSize?: Length-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

