# Badge

The **Badge** component is a container that can be attached to another component for notification and reminder purposes.

## Child Components

This component supports only one child component.

> **NOTE：**&gt;
> - Allowed child component types: built-in and custom components, including rendering control types (
> [if/else](../../../ui/rendering-control/arkts-rendering-control-ifelse.md), ForEach, and
> LazyForEach).&gt;
> - A custom component defaults to a width and height of 0. You must explicitly set its width and height; otherwise,
> the **Badge** component will not be displayed.&gt;
> - When there are multiple child components, only the last child component is displayed on the UI. However, the
> status update of other child components will still cause the badge and its child components to be re-rendered.&gt;
> - Child component layout is independent and does not automatically adjust to avoid overlapping with the badge.

## Badge

```TypeScript
Badge(value: BadgeParamWithNumber)
```

Creates a badge with the given numerical value.

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [BadgeParamWithNumber](arkts-arkui-badgeparamwithnumber-i.md) | Yes |

## Badge

```TypeScript
Badge(value: BadgeParamWithString)
```

Creates a badge with the given string.

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [BadgeParamWithString](arkts-arkui-badgeparamwithstring-i.md) | Yes |

## Summary

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
