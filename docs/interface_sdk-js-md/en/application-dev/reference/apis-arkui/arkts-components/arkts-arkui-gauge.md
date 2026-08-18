# Gauge

The **Gauge** component represents a gauge that displays data in a circular format. > **NOTE** > > - This component supports WithTheme since API version 26.0.0.

## Child Components This component can contain only one child component. > **NOTE** > > - Supported child component types: built-in and custom components, including > [if/else](../../../ui/rendering-control/arkts-rendering-control-ifelse.md) but excluding > ForEach and LazyForEach. > > - You are advised to use the **Text** component to build the current value and auxiliary text. > > - If the width and height of the child component are in percentage, the reference range is the rectangle that has > the outer ring as its inscribed circle.

## Gauge

```TypeScript
Gauge(options: GaugeOptions)
```

Creates a gauge.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-GaugeInterface-(options: GaugeOptions): GaugeAttribute--><!--Device-GaugeInterface-(options: GaugeOptions): GaugeAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [GaugeOptions](arkts-arkui-gaugeoptions-i.md) | Yes | Settings of the gauge. |

## Summary

### Interfaces

| Name | Description |
| --- | --- |
| [GaugeConfiguration](arkts-arkui-gaugeconfiguration-i.md) | You need a custom class to implement the **ContentModifier** API. Inherits from CommonConfiguration. |
| [GaugeIndicatorOptions](arkts-arkui-gaugeindicatoroptions-i.md) | Provides gauge indicator options. |
| [GaugeOptions](arkts-arkui-gaugeoptions-i.md) | Provides gauge options. |
| [GaugeShadowOptions](arkts-arkui-gaugeshadowoptions-i.md) | Inherits from MultiShadowOptions and has all attributes of **MultiShadowOptions**. |

