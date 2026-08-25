# Gauge

The **Gauge** component represents a gauge that displays data in a circular format.
> **NOTE**>> - This component supports WithTheme since API version 26.0.0.

## Child Components

This component can contain only one child component.

> **NOTE：**&gt;
> - Supported child component types: built-in and custom components, including
> [if/else](../../../ui/rendering-control/arkts-rendering-control-ifelse.md) but excluding
> ForEach and LazyForEach.&gt;
> - You are advised to use the **Text** component to build the current value and auxiliary text.&gt;
> - If the width and height of the child component are in percentage, the reference range is the rectangle that has
> the outer ring as its inscribed circle.

## Gauge

```TypeScript
Gauge(options: GaugeOptions)
```

Creates a gauge.

**Since:** 8

**ArkTS mode:** Supports only ArkTS-Dyn, since version 8.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [GaugeOptions](arkts-arkui-gaugeoptions-i.md) | Yes |

## Summary

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
