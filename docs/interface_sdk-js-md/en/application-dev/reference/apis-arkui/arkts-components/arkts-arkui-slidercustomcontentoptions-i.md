# SliderCustomContentOptions

Slider前后缀组件无障碍信息参数。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

<!--Device-unnamed-interface SliderCustomContentOptions--><!--Device-unnamed-interface SliderCustomContentOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## accessibilityDescription

```TypeScript
accessibilityDescription?: ResourceStr
```

无障碍功能详细描述，描述滑块前缀或后缀的功能或用途，供屏幕阅读器等工具使用。 

默认值为“单指双击即可执行”。

**Type:** [ResourceStr](../arkts-apis/arkts-arkui-resourcestr-t.md)

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-SliderCustomContentOptions-accessibilityDescription?: ResourceStr--><!--Device-SliderCustomContentOptions-accessibilityDescription?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## accessibilityGroup

```TypeScript
accessibilityGroup?: boolean
```

标识元素是否属于无障碍组，帮助屏幕阅读器等工具分组相关元素。

true：该组件及其所有子组件为一整个可以选中的组件，无障碍服务将不再关注其子组件内容；false：不启用无障碍分组。

默认值：false

**Type:** boolean

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-SliderCustomContentOptions-accessibilityGroup?: boolean--><!--Device-SliderCustomContentOptions-accessibilityGroup?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## accessibilityLevel

```TypeScript
accessibilityLevel?: string
```

控制组件是否可被无障碍辅助服务识别。

支持的值为:

"auto"：当前组件会转换为“yes”。

"yes"：当前组件可被无障碍辅助服务所识别。

"no"：当前组件不可被无障碍辅助服务所识别。

"no-hide-descendants"：当前组件及其所有子组件不可被无障碍辅助服务所识别。

默认值："auto"。

**Type:** string

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-SliderCustomContentOptions-accessibilityLevel?: string--><!--Device-SliderCustomContentOptions-accessibilityLevel?: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## accessibilityText

```TypeScript
accessibilityText?: ResourceStr
```

无障碍文本，供屏幕阅读器等工具读取，增强无障碍功能。 

默认值：""

**Type:** [ResourceStr](../arkts-apis/arkts-arkui-resourcestr-t.md)

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-SliderCustomContentOptions-accessibilityText?: ResourceStr--><!--Device-SliderCustomContentOptions-accessibilityText?: ResourceStr-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

