# Span

As a child of the Text and ContainerSpan components, the **Span** component is used to display inline text.
> **NOTE**>> This component is supported since API version 10. It can inherit attribute settings from its parent component> **Text**. This means that, if an attribute is not set in this component, it takes the value (if any) of the> attribute from its parent component. Only the following attributes can be inherited: **fontColor**, **fontSize**,> **fontStyle**, **fontWeight**, **decoration**, **letterSpacing**, **textCase**, **fontFamily**, and **textShadow**.>> The [universal attributes](../../../reference/apis-arkui/arkui-ts/ts-component-general-attributes.md) are not> supported. To set universal attributes, use Text for configuration or use> [CustomSpan](../arkts-apis/arkts-arkui-customspan-c.md) in the Styled String for custom drawing.>> Among [universal events](../../../reference/apis-arkui/arkui-ts/ts-component-general-events.md), only> onClick click events and> onHover hover events are supported.

## Child Components

Not supported

## Span

```TypeScript
Span(value: string | Resource)
```

Defines the constructor of Span.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | string \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) | Yes |

## Summary

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
