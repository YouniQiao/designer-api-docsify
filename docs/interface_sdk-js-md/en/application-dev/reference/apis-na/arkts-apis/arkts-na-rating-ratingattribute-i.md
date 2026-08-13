# RatingAttribute

Defines the Rating component attributes.

**Inheritance/Implementation:** RatingAttribute extends CommonMethod

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-export declare interface RatingAttribute--><!--Device-unnamed-export declare interface RatingAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
attributeModifier(modifier: AttributeModifier<RatingAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta only, since version -1.

**Deprecated since:** -1

<!--Device-RatingAttribute-attributeModifier(modifier: AttributeModifier<RatingAttribute> | AttributeModifier<CommonMethod> | undefined): this--><!--Device-RatingAttribute-attributeModifier(modifier: AttributeModifier<RatingAttribute> | AttributeModifier<CommonMethod> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| modifier | [AttributeModifier](../../apis-arkui/arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[RatingAttribute](arkts-na-rating-ratingattribute-i.md)&gt; \| [AttributeModifier](../../apis-arkui/arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../../apis-arkui/arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## contentModifier

```TypeScript
contentModifier(modifier: ContentModifier<RatingConfiguration> | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta only, since version -1.

**Deprecated since:** -1

<!--Device-RatingAttribute-contentModifier(modifier: ContentModifier<RatingConfiguration> | undefined): this--><!--Device-RatingAttribute-contentModifier(modifier: ContentModifier<RatingConfiguration> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| modifier | [ContentModifier](../../apis-arkui/arkts-components/arkts-arkui-contentmodifier-i.md)&lt;[RatingConfiguration](arkts-na-rating-ratingconfiguration-i.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onChange

```TypeScript
onChange(callback: OnRatingChangeCallback | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta only, since version -1.

**Deprecated since:** -1

<!--Device-RatingAttribute-onChange(callback: OnRatingChangeCallback | undefined): this--><!--Device-RatingAttribute-onChange(callback: OnRatingChangeCallback | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [OnRatingChangeCallback](arkts-na-onratingchangecallback-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## setRatingOptions

```TypeScript
setRatingOptions(options?: RatingOptions): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta only, since version -1.

**Deprecated since:** -1

<!--Device-RatingAttribute-setRatingOptions(options?: RatingOptions): this--><!--Device-RatingAttribute-setRatingOptions(options?: RatingOptions): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [RatingOptions](arkts-na-rating-ratingoptions-i.md) | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## starStyle

```TypeScript
starStyle(options: StarStyleOptions | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta only, since version -1.

**Deprecated since:** -1

<!--Device-RatingAttribute-starStyle(options: StarStyleOptions | undefined): this--><!--Device-RatingAttribute-starStyle(options: StarStyleOptions | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [StarStyleOptions](arkts-na-rating-starstyleoptions-i.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## stars

```TypeScript
stars(value: int | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta only, since version -1.

**Deprecated since:** -1

<!--Device-RatingAttribute-stars(value: int | undefined): this--><!--Device-RatingAttribute-stars(value: int | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | int \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## stepSize

```TypeScript
stepSize(value: double | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta only, since version -1.

**Deprecated since:** -1

<!--Device-RatingAttribute-stepSize(value: double | undefined): this--><!--Device-RatingAttribute-stepSize(value: double | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | double \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## default

```TypeScript
default
```

Set rating options.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-RatingAttribute-default--><!--Device-RatingAttribute-default-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

