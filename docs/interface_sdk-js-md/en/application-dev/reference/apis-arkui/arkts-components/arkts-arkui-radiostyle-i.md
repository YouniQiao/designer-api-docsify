# RadioStyle

单选框的样式。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-unnamed-declare interface RadioStyle--><!--Device-unnamed-declare interface RadioStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## checkedBackgroundColor

```TypeScript
checkedBackgroundColor?: ResourceColor
```

开启状态底板颜色。

默认值：`\$r('sys.color.ohos_id_color_text_primary_activated')`

**Type:** [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md)

**Default:** #007DFF

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-RadioStyle-checkedBackgroundColor?: ResourceColor--><!--Device-RadioStyle-checkedBackgroundColor?: ResourceColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## indicatorColor

```TypeScript
indicatorColor?: ResourceColor
```

开启状态内部圆饼颜色。从API version 12开始，indicatorType设置为RadioIndicatorType.TICK和RadioIndicatorType.DOT时，支持修改内部颜色。indicatorType设置为RadioIndicatorType.CUSTOM时，不支持修改内部颜色。

默认值：`\$r('sys.color.ohos_id_color_foreground_contrary')`

**Type:** [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md)

**Default:** #FFFFFF

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-RadioStyle-indicatorColor?: ResourceColor--><!--Device-RadioStyle-indicatorColor?: ResourceColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## uncheckedBorderColor

```TypeScript
uncheckedBorderColor?: ResourceColor
```

关闭状态描边颜色。

默认值：`\$r('sys.color.ohos_id_color_switch_outline_off')`

**Type:** [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md)

**Default:** #182431

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-RadioStyle-uncheckedBorderColor?: ResourceColor--><!--Device-RadioStyle-uncheckedBorderColor?: ResourceColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

