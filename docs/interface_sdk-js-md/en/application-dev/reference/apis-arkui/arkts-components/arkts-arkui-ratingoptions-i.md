# RatingOptions

评分组件的信息。

> **说明：**
> 
> 为规范匿名对象的定义，API 18版本修改了此处的元素定义。其中，保留了历史匿名对象的起始版本信息，会出现外层元素@since版本号高于内层元素版本号的情况，但这不影响接口的使用。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

<!--Device-unnamed-declare interface RatingOptions--><!--Device-unnamed-declare interface RatingOptions-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## indicator

```TypeScript
indicator?: boolean
```

设置评分组件作为指示器使用。值为true时，作为指示器使用，不可改变评分；值为false时，可进行评分。

默认值：false，可进行评分

**说明：**

indicator=true时，默认组件高度height=12.0vp，组件width=height * stars。 

indicator=false时，默认组件高度height=28.0vp，组件width=height * stars。

**Type:** boolean

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-RatingOptions-indicator?: boolean--><!--Device-RatingOptions-indicator?: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## rating

```TypeScript
rating: number
```

设置并接收评分值。

默认值：0

取值范围： [0, stars]

小于0取0，大于[stars](RatingAttribute#stars(value: number))取最大值stars。

该参数支持[\$\$](../../../ui/state-management/arkts-two-way-sync.md)双向绑定变量。

**Type:** number

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-RatingOptions-rating: number--><!--Device-RatingOptions-rating: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

