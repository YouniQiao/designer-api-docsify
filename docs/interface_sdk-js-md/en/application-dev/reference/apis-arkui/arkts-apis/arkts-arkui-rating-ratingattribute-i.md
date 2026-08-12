# RatingAttribute

Defines the Rating component attributes.

**Inheritance/Implementation:** RatingAttribute extends [CommonMethod](CommonMethod)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface RatingAttribute extends CommonMethod--><!--Device-unnamed-export declare interface RatingAttribute extends CommonMethod-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
default attributeModifier(modifier: AttributeModifier<RatingAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

Set the attribute modifier of rating.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RatingAttribute-default attributeModifier(modifier: AttributeModifier<RatingAttribute> | AttributeModifier<CommonMethod> | undefined): this--><!--Device-RatingAttribute-default attributeModifier(modifier: AttributeModifier<RatingAttribute> | AttributeModifier<CommonMethod> | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[RatingAttribute](arkts-arkui-rating-ratingattribute-i.md)&gt; \| [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | Yes | The attribute modifier of rating. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## contentModifier

```TypeScript
default contentModifier(modifier: ContentModifier<RatingConfiguration> | undefined): this
```

Set the content modifier of rating.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RatingAttribute-default contentModifier(modifier: ContentModifier<RatingConfiguration> | undefined): this--><!--Device-RatingAttribute-default contentModifier(modifier: ContentModifier<RatingConfiguration> | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| modifier | [ContentModifier](../arkts-components/arkts-arkui-contentmodifier-i.md)&lt;[RatingConfiguration](arkts-arkui-rating-ratingconfiguration-i.md)&gt; \| undefined | Yes | The content modifier of rating. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onChange

```TypeScript
default onChange(callback: OnRatingChangeCallback | undefined): this
```

Called when the star rating of the operation scoring bar changes.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RatingAttribute-default onChange(callback: OnRatingChangeCallback | undefined): this--><!--Device-RatingAttribute-default onChange(callback: OnRatingChangeCallback | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [OnRatingChangeCallback](arkts-arkui-onratingchangecallback-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## setRatingOptions

```TypeScript
default setRatingOptions(options?: RatingOptions): this
```

Set rating options.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RatingAttribute-default setRatingOptions(options?: RatingOptions): this--><!--Device-RatingAttribute-default setRatingOptions(options?: RatingOptions): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [RatingOptions](arkts-arkui-rating-ratingoptions-i.md) | No | rating constructor options |

**Return value:**

| Type | Description |
| --- | --- |
| this | Returns the instance of the RatingAttribute. |

## starStyle

```TypeScript
default starStyle(options: StarStyleOptions | undefined): this
```

Called when a picture is set.Anonymous Object Rectification.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RatingAttribute-default starStyle(options: StarStyleOptions | undefined): this--><!--Device-RatingAttribute-default starStyle(options: StarStyleOptions | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [StarStyleOptions](arkts-arkui-rating-starstyleoptions-i.md) \| undefined | Yes | star style options |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## stars

```TypeScript
default stars(value: int | undefined): this
```

Called when the total number of stars is set.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RatingAttribute-default stars(value: int | undefined): this--><!--Device-RatingAttribute-default stars(value: int | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

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
default stepSize(value: double | undefined): this
```

Called when the step size of the operation rating.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RatingAttribute-default stepSize(value: double | undefined): this--><!--Device-RatingAttribute-default stepSize(value: double | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | double \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

