# ColumnOptions

设置Column组件的子组件间距属性。

> **说明：**
> 
> 为规范匿名对象的定义，API 18版本修改了此处的元素定义。其中，保留了历史匿名对象的起始版本信息，会出现外层元素@since版本号高于内层元素版本号的情况，但这不影响接口的使用。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

<!--Device-unnamed-interface ColumnOptions--><!--Device-unnamed-interface ColumnOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## space

```TypeScript
space?: string | number
```

纵向布局元素垂直方向间距。

space为负数或者[justifyContent](ColumnAttribute#justifyContent)设置为FlexAlign.SpaceBetween、FlexAlign.SpaceAround、FlexAlign.SpaceEvenly时，space不生效。

取值范围：[0, +∞)

默认值：0

非法值：按默认值处理。

单位：vp

**说明：**

space取值是大于等于0的数字，或者可以转换为非负数字的字符串。

**Type:** string \| number

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-ColumnOptions-space?: string | number--><!--Device-ColumnOptions-space?: string | number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

