# RatingConfiguration

开发者需要自定义class实现ContentModifier接口。继承自[CommonConfiguration](arkts-arkui-common-commonconfiguration-i.md)。

**Inheritance/Implementation:** RatingConfiguration extends [CommonConfiguration<RatingConfiguration>](CommonConfiguration<RatingConfiguration>)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface RatingConfiguration extends CommonConfiguration<RatingConfiguration>--><!--Device-unnamed-export declare interface RatingConfiguration extends CommonConfiguration<RatingConfiguration>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## indicator

```TypeScript
indicator: boolean
```

评分条是否作为指示器使用。当值为true时，表示作为指示器；当值为false时，表示不作为指示器。

默认值：false

**Type:** boolean

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RatingConfiguration-indicator: boolean--><!--Device-RatingConfiguration-indicator: boolean-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## rating

```TypeScript
rating: double
```

设置并接收评分值。

默认值：0

取值范围： [0, stars]

小于0取0，大于[stars](arkts-arkui-rating-ratingconfiguration-i.md#stars)取最大值stars。

该参数支持[\$\$](../../../ui/state-management/arkts-two-way-sync.md)双向绑定变量。

该参数支持[!!](../../../ui/state-management/arkts-new-binding.md#系统组件参数双向绑定)双向绑定变量。

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RatingConfiguration-rating: double--><!--Device-RatingConfiguration-rating: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## stars

```TypeScript
stars: int
```

评分条的星级总数。

默认值：5

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RatingConfiguration-stars: int--><!--Device-RatingConfiguration-stars: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## stepSize

```TypeScript
stepSize: double
```

评分条的评分步长。

默认值：0.5

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RatingConfiguration-stepSize: double--><!--Device-RatingConfiguration-stepSize: double-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## triggerChange

```TypeScript
triggerChange: Callback<double>
```

触发评分数量变化。

**Type:** [Callback](../arkts-components/arkts-arkui-callback-i.md)&lt;double&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RatingConfiguration-triggerChange: Callback<double>--><!--Device-RatingConfiguration-triggerChange: Callback<double>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

