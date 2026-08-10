# Gauge

## Gauge

```TypeScript
export declare function Gauge(
    options: GaugeOptions, 
    content_?: CustomBuilder
): GaugeAttribute
```

创建数据量规图表组件。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function Gauge(    options: GaugeOptions,     content_?: CustomBuilder): GaugeAttribute--><!--Device-unnamed-export declare function Gauge(    options: GaugeOptions,     content_?: CustomBuilder): GaugeAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [GaugeOptions](arkts-arkui-gauge-gaugeoptions-i.md) | Yes | 数据量规图表组件参数。 |
| content_ | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | No |  |

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

定义Gauge组件。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function Gauge(    style: CustomBuilderT<GaugeAttribute>,    content_?: CustomBuilder,): GaugeAttribute--><!--Device-unnamed-export declare function Gauge(    style: CustomBuilderT<GaugeAttribute>,    content_?: CustomBuilder,): GaugeAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | [CustomBuilderT](../arkts-components/arkts-arkui-custombuildert-t.md)&lt;GaugeAttribute&gt; | Yes | Gauge属性的实例。 |
| content_ | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | No | 子组件。 |

**Return value:**

| Type | Description |
| --- | --- |
| [GaugeAttribute](arkts-arkui-gauge-gaugeattribute-i.md) |  |

