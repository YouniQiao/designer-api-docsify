# Gauge

## Gauge

```TypeScript
@ComponentBuilder
export declare function Gauge(
    options: GaugeOptions, 
    content_?: CustomBuilder
): GaugeAttribute
```

Defines the Gauge component.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@ComponentBuilderexport declare function Gauge(    options: GaugeOptions,     content_?: CustomBuilder): GaugeAttribute--><!--Device-unnamed-@ComponentBuilderexport declare function Gauge(    options: GaugeOptions,     content_?: CustomBuilder): GaugeAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [GaugeOptions](arkts-gauge-gaugeoptions-i.md) | Yes | gauge options. |
| content_ | [CustomBuilder](../arkts-apis/arkts-custombuilder-t.md) | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| [GaugeAttribute](arkts-gauge-attribute.md) |  |


## Gauge

```TypeScript
@Builder
export declare function Gauge(
    style: CustomBuilderT<GaugeAttribute>,
    content_?: CustomBuilder,
): GaugeAttribute
```

Defines Gauge Component.

**Since:** 26.1.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@Builderexport declare function Gauge(    style: CustomBuilderT<GaugeAttribute>,    content_?: CustomBuilder,): GaugeAttribute--><!--Device-unnamed-@Builderexport declare function Gauge(    style: CustomBuilderT<GaugeAttribute>,    content_?: CustomBuilder,): GaugeAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | [CustomBuilderT](../arkts-apis/arkts-custombuildert-t.md)&lt;[GaugeAttribute](arkts-gauge-attribute.md)&gt; | Yes | Gauge attribute instance |
| content_ | [CustomBuilder](../arkts-apis/arkts-custombuilder-t.md) | No | Child component |

**Return value:**

| Type | Description |
| --- | --- |
| [GaugeAttribute](arkts-gauge-attribute.md) |  |

