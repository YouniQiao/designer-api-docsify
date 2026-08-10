# RatingConfiguration

开发者需要自定义class实现ContentModifier接口。继承自[CommonConfiguration](../arkts-apis/arkts-arkui-common-commonconfiguration-i.md/arkts-arkui-common-commonconfiguration-i.md)。

**Inheritance/Implementation:** RatingConfiguration extends [CommonConfiguration<RatingConfiguration>](CommonConfiguration<RatingConfiguration>)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-unnamed-declare interface RatingConfiguration extends CommonConfiguration<RatingConfiguration>--><!--Device-unnamed-declare interface RatingConfiguration extends CommonConfiguration<RatingConfiguration>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## indicator

```TypeScript
indicator: boolean
```

评分条是否作为指示器使用。当值为true时，表示作为指示器；当值为false时，表示不作为指示器。

默认值：false

**Type:** boolean

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RatingConfiguration-indicator: boolean--><!--Device-RatingConfiguration-indicator: boolean-End-->

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

该参数支持[!!](../../../ui/state-management/arkts-new-binding.md#系统组件参数双向绑定)双向绑定变量。

**Type:** number

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RatingConfiguration-rating: number--><!--Device-RatingConfiguration-rating: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## stars

```TypeScript
stars: number
```

评分条的星级总数。

默认值：5

**Type:** number

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RatingConfiguration-stars: number--><!--Device-RatingConfiguration-stars: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## stepSize

```TypeScript
stepSize: number
```

评分条的评分步长。

默认值：0.5

**Type:** number

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RatingConfiguration-stepSize: number--><!--Device-RatingConfiguration-stepSize: number-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## triggerChange

```TypeScript
triggerChange: Callback<number>
```

触发评分变化的回调，参数为新的评分值。

**Type:** [Callback](arkts-arkui-callback-i.md)&lt;number&gt;

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-RatingConfiguration-triggerChange: Callback<number>--><!--Device-RatingConfiguration-triggerChange: Callback<number>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

