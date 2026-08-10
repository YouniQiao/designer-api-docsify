# ColumnOptionsV2

设置Column组件的子组件间距属性。间距类型SpaceType支持number、string或Resource类型。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

<!--Device-unnamed-interface ColumnOptionsV2--><!--Device-unnamed-interface ColumnOptionsV2-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## space

```TypeScript
space?: SpaceType
```

设置纵向布局元素垂直方向间距。

space为负数或者[justifyContent](ColumnAttribute#justifyContent)设置为FlexAlign.SpaceBetween、FlexAlign.SpaceAround、FlexAlign.SpaceEvenly时，space不生效。

取值范围：[0, +∞)

默认值：0

单位：vp

非法值：按默认值处理。

**说明：**

space取值是大于等于0的数字，或者可以转换为非负数字的字符串，或者可以转换为数字的Resource类型数据。

**Type:** [SpaceType](../arkts-apis/arkts-arkui-spacetype-t.md)

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 18.

**Widget capability:** This API can be used in ArkTS widgets since API version 18.

<!--Device-ColumnOptionsV2-space?: SpaceType--><!--Device-ColumnOptionsV2-space?: SpaceType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

