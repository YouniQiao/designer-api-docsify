# RadioStyle

单选框的颜色。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface RadioStyle--><!--Device-unnamed-export declare interface RadioStyle-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## checkedBackgroundColor

```TypeScript
checkedBackgroundColor?: ResourceColor
```

开启状态底板颜色。

默认值：`\$r('sys.color.ohos_id_color_text_primary_activated')`

**Type:** [ResourceColor](arkts-arkui-resourcecolor-t.md)

**Default:** #007DFF

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RadioStyle-checkedBackgroundColor?: ResourceColor--><!--Device-RadioStyle-checkedBackgroundColor?: ResourceColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## indicatorColor

```TypeScript
indicatorColor?: ResourceColor
```

开启状态内部圆饼颜色。从API version 12开始，indicatorType设置为RadioIndicatorType.TICK和RadioIndicatorType.DOT时，支持修改内部颜色。indicatorType设置为RadioIndicatorType.CUSTOM时，不支持修改内部颜色。

默认值：`\$r('sys.color.ohos_id_color_foreground_contrary')`

**Type:** [ResourceColor](arkts-arkui-resourcecolor-t.md)

**Default:** #FFFFFF

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RadioStyle-indicatorColor?: ResourceColor--><!--Device-RadioStyle-indicatorColor?: ResourceColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## uncheckedBorderColor

```TypeScript
uncheckedBorderColor?: ResourceColor
```

关闭状态描边颜色。

默认值：`\$r('sys.color.ohos_id_color_switch_outline_off')`

**Type:** [ResourceColor](arkts-arkui-resourcecolor-t.md)

**Default:** #182431

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RadioStyle-uncheckedBorderColor?: ResourceColor--><!--Device-RadioStyle-uncheckedBorderColor?: ResourceColor-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

