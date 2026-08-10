# SearchButtonOptions

搜索按钮样式对象。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export interface SearchButtonOptions--><!--Device-unnamed-export interface SearchButtonOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## autoDisable

```TypeScript
autoDisable?: boolean
```

Search无文本内容时按钮置灰且不可点击。

默认值：false

true表示开启按钮置灰功能，false表示不开启。

**Type:** boolean

**Default:** false

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SearchButtonOptions-autoDisable?: boolean--><!--Device-SearchButtonOptions-autoDisable?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fontColor

```TypeScript
fontColor?: ResourceColor
```

文本按钮字体颜色。

默认值：Wearable设备是'#007dff'，TV设备是'#5291ff'，其他设备是'#5ea1ff'，均是蓝色。

**Type:** [ResourceColor](arkts-arkui-resourcecolor-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SearchButtonOptions-fontColor?: ResourceColor--><!--Device-SearchButtonOptions-fontColor?: ResourceColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## fontSize

```TypeScript
fontSize?: Length
```

文本按钮字体大小，不支持百分比。

默认值：Wearable设备15fp，其他设备14fp。

**Type:** [Length](arkts-arkui-length-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SearchButtonOptions-fontSize?: Length--><!--Device-SearchButtonOptions-fontSize?: Length-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

