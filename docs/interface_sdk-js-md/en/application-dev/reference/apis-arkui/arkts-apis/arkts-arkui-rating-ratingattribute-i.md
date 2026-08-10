# RatingAttribute

**Inheritance/Implementation:** RatingAttribute extends [CommonMethod](arkts-arkui-common-commonmethod-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface RatingAttribute extends CommonMethod--><!--Device-unnamed-export declare interface RatingAttribute extends CommonMethod-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
default attributeModifier(modifier: AttributeModifier<RatingAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

设置Rating的属性修改器。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RatingAttribute-default attributeModifier(modifier: AttributeModifier<RatingAttribute> | AttributeModifier<CommonMethod> | undefined): this--><!--Device-RatingAttribute-default attributeModifier(modifier: AttributeModifier<RatingAttribute> | AttributeModifier<CommonMethod> | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;RatingAttribute&gt; \| AttributeModifier&lt;CommonMethod&gt; \| undefined | Yes | Rating组件的属 性修改器。&lt;br/&gt;当modifier的值为undefined时，不使用属性修改器。 |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## contentModifier

```TypeScript
default contentModifier(modifier: ContentModifier<RatingConfiguration> | undefined): this
```

定制Rating内容区的方法。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RatingAttribute-default contentModifier(modifier: ContentModifier<RatingConfiguration> | undefined): this--><!--Device-RatingAttribute-default contentModifier(modifier: ContentModifier<RatingConfiguration> | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| modifier | [ContentModifier](../arkts-components/arkts-arkui-contentmodifier-i.md)&lt;RatingConfiguration&gt; \| undefined | Yes | 在Rating组件上，定制内容区的方法。&lt;br/&gt;modifier：内容修改器，开发 者需要自定义class实现ContentModifier接口。&lt;br/&gt;当modifier的值为undefined时，不使用内容修改器。 |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onChange

```TypeScript
default onChange(callback: OnRatingChangeCallback | undefined): this
```

当评分条的评星变化时会触发该回调。与[onChange](arkts-arkui-rating-ratingattribute-i.md#onchange)相比，callback参数新增了对undefined类型的支持。使用callback异步回调。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RatingAttribute-default onChange(callback: OnRatingChangeCallback | undefined): this--><!--Device-RatingAttribute-default onChange(callback: OnRatingChangeCallback | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [OnRatingChangeCallback](../arkts-components/arkts-arkui-onratingchangecallback-t.md) \| undefined | Yes | 操作评分条的评星变化时触发该回调。&lt;br/&gt;当callback的值为undefined时，不使用回调函数。 |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## starStyle

```TypeScript
default starStyle(options: StarStyleOptions | undefined): this
```

设置评分的样式。该属性所支持的图片类型能力参考[Image](../../apis-image-kit/arkts-apis/arkts-multimedia-image.md/arkts-multimedia-image.md)组件。

支持加载本地图片和网络图片，暂不支持[PixelMap](../../apis-image-kit/arkts-apis/arkts-image-image-pixelmap-i.md/arkts-image-image-pixelmap-i.md)类型。

默认图片加载方式为异步，暂不支持同步加载。

与[starStyle](arkts-arkui-rating-ratingattribute-i.md#starstyle)相比，options参数新增了对undefined类型的支持。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RatingAttribute-default starStyle(options: StarStyleOptions | undefined): this--><!--Device-RatingAttribute-default starStyle(options: StarStyleOptions | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [StarStyleOptions](../arkts-components/arkts-arkui-starstyleoptions-i.md) \| undefined | Yes | 评分的样式。取值为undefined时，按各属性的默认值处理。&lt;br/&gt;**说明：** &lt;br/&gt;当backgroundUri 、foregroundUri或secondaryUri设置的图片路径错误时，图片将保持上次的图片显示结果。如果首次设置错误，则不显示图片。&lt;br/&gt;当backgroundUri或foregroundUri设置为 undefined或空字符串时，Rating组件将加载系统默认星型图源。&lt;br/&gt;当secondaryUri未设置或设置为undefined或空字符串时，将优先使用backgroundUri，效果等同于仅设置 foregroundUri和backgroundUri。 |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## stars

```TypeScript
default stars(value: int | undefined): this
```

设置评分总数。设置为小于等于0的值时，按默认值显示。与[stars](arkts-arkui-rating-ratingattribute-i.md#stars)相比，value参数新增了对undefined类型的支持。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RatingAttribute-default stars(value: int | undefined): this--><!--Device-RatingAttribute-default stars(value: int | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | int \| undefined | Yes | 设置评分总数。&lt;br/&gt;当value的值为undefined时，默认值：5 |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## stepSize

```TypeScript
default stepSize(value: double | undefined): this
```

设置操作评级的步长。设置为小于0.1的值时，按默认值显示。与[stepSize](arkts-arkui-rating-ratingattribute-i.md#stepsize)相比，value参数新增了对undefined类型的支持。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RatingAttribute-default stepSize(value: double | undefined): this--><!--Device-RatingAttribute-default stepSize(value: double | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | double \| undefined | Yes | 操作评级的步长。&lt;br/&gt;当value的值为undefined时，默认值：0.5&lt;br/&gt;取值范围：[0.1, stars] |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

