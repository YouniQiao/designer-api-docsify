# RatingAttribute

Defines the Rating component attributes.

**Inheritance/Implementation:** RatingAttribute extends CommonMethod

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare interface RatingAttribute--><!--Device-unnamed-export declare interface RatingAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
attributeModifier(modifier: AttributeModifier<RatingAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-RatingAttribute-attributeModifier(modifier: AttributeModifier<RatingAttribute> | AttributeModifier<CommonMethod> | undefined): this--><!--Device-RatingAttribute-attributeModifier(modifier: AttributeModifier<RatingAttribute> | AttributeModifier<CommonMethod> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| modifier | [AttributeModifier](../../apis-arkui/arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[RatingAttribute](arkts-na-rating-ratingattribute-i.md)&gt; \| [AttributeModifier](../../apis-arkui/arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../../apis-arkui/arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## contentModifier

```TypeScript
contentModifier(modifier: ContentModifier<RatingConfiguration> | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-RatingAttribute-contentModifier(modifier: ContentModifier<RatingConfiguration> | undefined): this--><!--Device-RatingAttribute-contentModifier(modifier: ContentModifier<RatingConfiguration> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| modifier | [ContentModifier](../../apis-arkui/arkts-components/arkts-arkui-contentmodifier-i.md)&lt;[RatingConfiguration](arkts-na-rating-ratingconfiguration-i.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onChange

```TypeScript
onChange(callback: OnRatingChangeCallback | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-RatingAttribute-onChange(callback: OnRatingChangeCallback | undefined): this--><!--Device-RatingAttribute-onChange(callback: OnRatingChangeCallback | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [OnRatingChangeCallback](arkts-na-onratingchangecallback-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## setRatingOptions

```TypeScript
setRatingOptions(options?: RatingOptions): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-RatingAttribute-setRatingOptions(options?: RatingOptions): this--><!--Device-RatingAttribute-setRatingOptions(options?: RatingOptions): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [RatingOptions](arkts-na-rating-ratingoptions-i.md) | No |  |

**Return value:**

| Type | Description |
| --- | --- |
## starStyle

```TypeScript
starStyle(options: StarStyleOptions | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-RatingAttribute-starStyle(options: StarStyleOptions | undefined): this--><!--Device-RatingAttribute-starStyle(options: StarStyleOptions | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [StarStyleOptions](arkts-na-rating-starstyleoptions-i.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## stars

```TypeScript
stars(value: int | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-RatingAttribute-stars(value: int | undefined): this--><!--Device-RatingAttribute-stars(value: int | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | int \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## stepSize

```TypeScript
stepSize(value: double | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-RatingAttribute-stepSize(value: double | undefined): this--><!--Device-RatingAttribute-stepSize(value: double | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | double \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## default

```TypeScript
default
```

Set rating options.

**Since:** 26.1.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RatingAttribute-default--><!--Device-RatingAttribute-default-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

