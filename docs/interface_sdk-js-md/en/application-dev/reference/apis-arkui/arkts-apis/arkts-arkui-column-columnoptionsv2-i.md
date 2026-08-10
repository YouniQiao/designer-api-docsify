# ColumnOptionsV2

设置Column组件的子组件间距属性。间距类型SpaceType支持number、string或Resource类型。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export interface ColumnOptionsV2--><!--Device-unnamed-export interface ColumnOptionsV2-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## space

```TypeScript
space?: SpaceType
```

纵向布局元素垂直方向间距。&lt;br&gt;space为负数或者justifyContent设置为FlexAlign.SpaceBetween、FlexAlign.SpaceAround、FlexAlign.SpaceEvenly时，space不生效。&lt;br&gt;默认值：0&lt;br&gt;单位：vp&lt;br&gt;非法值：按默认值处理。&lt;br&gt;  
**说明：**&lt;br&gt;space取值是大于等于0的数字，或者可以转换为数字的字符串，或者可以转换为数字的Resource类型数据。

**Type:** [SpaceType](arkts-arkui-spacetype-t.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ColumnOptionsV2-space?: SpaceType--><!--Device-ColumnOptionsV2-space?: SpaceType-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

