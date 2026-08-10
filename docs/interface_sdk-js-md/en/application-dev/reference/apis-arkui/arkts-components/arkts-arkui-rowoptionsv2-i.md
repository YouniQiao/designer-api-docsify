# RowOptionsV2

设置Row组件的子组件间距属性。间距类型SpaceType支持number、string或Resource类型。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

<!--Device-unnamed-interface RowOptionsV2--><!--Device-unnamed-interface RowOptionsV2-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## space

```TypeScript
space?: SpaceType
```

横向布局元素间距。

取值范围：大于等于0。

从API version 9开始，justifyContent设置为FlexAlign.SpaceBetween、FlexAlign.SpaceAround、FlexAlign.SpaceEvenly时space参数不生效。

默认值：0

单位：vp

非法值：按默认值处理。

**说明：**

space取值是大于等于0的数字，或者可以转换为非负数字的字符串，或者可以转换为数字的Resource类型数据。负数作为非法值将被当作默认值0处理。

**Type:** [SpaceType](arkts-arkui-spacetype-t.md)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

**Widget capability:** This API can be used in ArkTS widgets since API version 18.

<!--Device-RowOptionsV2-space?: SpaceType--><!--Device-RowOptionsV2-space?: SpaceType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

