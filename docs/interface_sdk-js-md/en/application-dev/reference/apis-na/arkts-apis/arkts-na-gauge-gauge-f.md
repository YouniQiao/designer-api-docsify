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

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@ComponentBuilderexport declare function Gauge(    options: GaugeOptions,     content_?: CustomBuilder): GaugeAttribute--><!--Device-unnamed-@ComponentBuilderexport declare function Gauge(    options: GaugeOptions,     content_?: CustomBuilder): GaugeAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [GaugeOptions](arkts-na-gauge-gaugeoptions-i.md) | Yes | gauge options. |
| content_ | CustomBuilder | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| GaugeAttribute |  |


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

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@Builderexport declare function Gauge(    style: CustomBuilderT<GaugeAttribute>,    content_?: CustomBuilder,): GaugeAttribute--><!--Device-unnamed-@Builderexport declare function Gauge(    style: CustomBuilderT<GaugeAttribute>,    content_?: CustomBuilder,): GaugeAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | CustomBuilderT&lt;GaugeAttribute&gt; | Yes | Gauge attribute instance |
| content_ | CustomBuilder | No | Child component |

**Return value:**

| Type | Description |
| --- | --- |
| GaugeAttribute |  |

