# Gauge

## Gauge

```TypeScript
export declare function Gauge(
    options: GaugeOptions, 
    content_?: CustomBuilder
): GaugeAttribute
```

Defines the Gauge component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function Gauge(    options: GaugeOptions,     content_?: CustomBuilder): GaugeAttribute--><!--Device-unnamed-export declare function Gauge(    options: GaugeOptions,     content_?: CustomBuilder): GaugeAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [GaugeOptions](arkts-arkui-gauge-gaugeoptions-i.md) | Yes | gauge options. |
| content_ | [CustomBuilder](arkts-arkui-custombuilder-t.md) | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| [GaugeAttribute](arkts-arkui-gauge-gaugeattribute-i.md) |  |


## Gauge

```TypeScript
export declare function Gauge(
    style: CustomBuilderT<GaugeAttribute>,
    content_?: CustomBuilder,
): GaugeAttribute
```

Defines Gauge Component.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function Gauge(    style: CustomBuilderT<GaugeAttribute>,    content_?: CustomBuilder,): GaugeAttribute--><!--Device-unnamed-export declare function Gauge(    style: CustomBuilderT<GaugeAttribute>,    content_?: CustomBuilder,): GaugeAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | [CustomBuilderT](arkts-arkui-custombuildert-t.md)&lt;[GaugeAttribute](arkts-arkui-gauge-gaugeattribute-i.md)&gt; | Yes | Gauge attribute instance |
| content_ | [CustomBuilder](arkts-arkui-custombuilder-t.md) | No | Child component |

**Return value:**

| Type | Description |
| --- | --- |
| [GaugeAttribute](arkts-arkui-gauge-gaugeattribute-i.md) |  |

