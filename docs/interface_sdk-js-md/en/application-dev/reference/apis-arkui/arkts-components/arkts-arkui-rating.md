# Rating

The **Rating** component provides a rating bar.
> **NOTE**
> - If the parent node of the **Rating** component has fixed dimensions, you must also specify the width and height> for the **Rating** component, or set its parent node's clip> attribute to **true**.

## Child Components

Not supported

## Sequential Keyboard Navigation Specifications

| [Key](../../apis-input-kit/arkts-apis/arkts-input-multimodalinput-keyevent-key-i.md) | Description | |------------|-----------------------------| | Tab | Switch the focus between components. | | Left and right arrow keys | Increase or decrease the rating on preview at the specified step, without changing the actual rating.| | Home | Move the focus to the first star, without changing the actual rating. | | End | Move the focus to the last star, without changing the actual rating. | | Space/Enter |

## Rating

```TypeScript
Rating(options?: RatingOptions)
```

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [RatingOptions](arkts-arkui-ratingoptions-i.md) | No |

## Summary

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |

### Types

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [OnRatingChangeCallback](arkts-arkui-onratingchangecallback-t.md) |
