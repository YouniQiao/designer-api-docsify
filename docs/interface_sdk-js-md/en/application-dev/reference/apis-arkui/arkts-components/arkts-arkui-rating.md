# Rating

The **Rating** component provides a rating bar. > **NOTE** > - If the parent node of the **Rating** component has fixed dimensions, you must also specify the width and height > for the **Rating** component, or set its parent node's clip > attribute to **true**.

## Child Components Not supported ###### Sequential Keyboard Navigation Specifications | Key        | Description                       | |------------|-----------------------------| | Tab        | Switch the focus between components.                   | | Left and right arrow keys  | Increase or decrease the rating on preview at the specified step, without changing the actual rating.| | Home       | Move the focus to the first star, without changing the actual rating.         | | End        | Move the focus to the last star, without changing the actual rating.        | | Space/Enter | Submit the rating result based on the current rating.              |

## Rating

```TypeScript
Rating(options?: RatingOptions)
```

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-RatingInterface-(options?: RatingOptions): RatingAttribute--><!--Device-RatingInterface-(options?: RatingOptions): RatingAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [RatingOptions](arkts-arkui-ratingoptions-i.md) | No | Rating bar options.<br> The default values of the parameters in **RatingOptions** apply if this parameter is not set. |

## Summary

### Interfaces

| Name | Description |
| --- | --- |
| [RatingConfiguration](arkts-arkui-ratingconfiguration-i.md) | You need a custom class to implement the **ContentModifier** API. Inherits from CommonConfiguration. |
| [RatingOptions](arkts-arkui-ratingoptions-i.md) | Provides configuration options for the **Rating** component. > **NOTE：**> > To standardize anonymous object definitions, the element definitions here have been revised in API version 18. > While historical version information is preserved for anonymous objects, there may be cases where the outer element > 's @since version number is higher than inner elements'. This does not affect interface usability. |
| [StarStyleOptions](arkts-arkui-starstyleoptions-i.md) | Provides style settings for the selected, unselected, and partially selected stars in the **Rating** component. > **NOTE：**> > To standardize anonymous object definitions, the element definitions here have been revised in API version 18. > While historical version information is preserved for anonymous objects, there may be cases where the outer element > 's @since version number is higher than inner elements'. This does not affect interface usability. > **NOTE：**> > The string type can be used to load network images and local images. When a relative path is used to reference a > local image, for example, **Image("common/test.jpg")**, the **common** directory must be placed at the same level > as the **pages** directory. Base64-encoded strings are also supported. |

### Types

| Name | Description |
| --- | --- |
| [OnRatingChangeCallback](arkts-arkui-onratingchangecallback-t.md) | Defines the callback triggered when the rating value changes. |

