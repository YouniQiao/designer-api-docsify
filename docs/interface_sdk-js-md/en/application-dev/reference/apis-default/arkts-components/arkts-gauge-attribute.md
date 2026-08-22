# GaugeAttribute

Defines the Gauge component attributes.

**Inheritance/Implementation:** GaugeAttribute extends CommonMethod

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-unnamed-export declare interface GaugeAttribute--><!--Device-unnamed-export declare interface GaugeAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
attributeModifier(modifier: AttributeModifier<GaugeAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-GaugeAttribute-attributeModifier(modifier: AttributeModifier<GaugeAttribute> | AttributeModifier<CommonMethod> | undefined): this--><!--Device-GaugeAttribute-attributeModifier(modifier: AttributeModifier<GaugeAttribute> | AttributeModifier<CommonMethod> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| modifier | [AttributeModifier](../../apis-arkui/arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[GaugeAttribute](arkts-gauge-attribute.md)&gt; \| [AttributeModifier](../../apis-arkui/arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../../apis-arkui/arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## colors

```TypeScript
colors(colors: ResourceColor | LinearGradient | Array<[ResourceColor | LinearGradient, double]> | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-GaugeAttribute-colors(colors: ResourceColor | LinearGradient | Array<[ResourceColor | LinearGradient, double]> | undefined): this--><!--Device-GaugeAttribute-colors(colors: ResourceColor | LinearGradient | Array<[ResourceColor | LinearGradient, double]> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| colors | [ResourceColor](../../apis-arkui/arkts-apis/arkts-arkui-resourcecolor-t.md) \| [LinearGradient](arkts-datapanel-lineargradient-c.md) \| Array&lt;[ResourceColor \| [LinearGradient](arkts-datapanel-lineargradient-c.md), double]&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## contentModifier

```TypeScript
contentModifier(modifier: ContentModifier<GaugeConfiguration> | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-GaugeAttribute-contentModifier(modifier: ContentModifier<GaugeConfiguration> | undefined): this--><!--Device-GaugeAttribute-contentModifier(modifier: ContentModifier<GaugeConfiguration> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| modifier | [ContentModifier](../../apis-arkui/arkts-components/arkts-arkui-contentmodifier-i.md)&lt;[GaugeConfiguration](arkts-gauge-gaugeconfiguration-i.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## description

```TypeScript
description(value: CustomBuilder | undefined | null): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-GaugeAttribute-description(value: CustomBuilder | undefined | null): this--><!--Device-GaugeAttribute-description(value: CustomBuilder | undefined | null): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [CustomBuilder](../arkts-apis/arkts-custombuilder-t.md) \| undefined \| null | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## endAngle

```TypeScript
endAngle(angle: double | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-GaugeAttribute-endAngle(angle: double | undefined): this--><!--Device-GaugeAttribute-endAngle(angle: double | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| angle | double \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## indicator

```TypeScript
indicator(value: GaugeIndicatorOptions | undefined | null): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-GaugeAttribute-indicator(value: GaugeIndicatorOptions | undefined | null): this--><!--Device-GaugeAttribute-indicator(value: GaugeIndicatorOptions | undefined | null): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [GaugeIndicatorOptions](arkts-gauge-gaugeindicatoroptions-i.md) \| undefined \| null | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## privacySensitive

```TypeScript
privacySensitive(isPrivacySensitiveMode: boolean | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-GaugeAttribute-privacySensitive(isPrivacySensitiveMode: boolean | undefined): this--><!--Device-GaugeAttribute-privacySensitive(isPrivacySensitiveMode: boolean | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| isPrivacySensitiveMode | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## setGaugeOptions

```TypeScript
setGaugeOptions(options: GaugeOptions): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-GaugeAttribute-setGaugeOptions(options: GaugeOptions): this--><!--Device-GaugeAttribute-setGaugeOptions(options: GaugeOptions): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [GaugeOptions](arkts-gauge-gaugeoptions-i.md) | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## startAngle

```TypeScript
startAngle(angle: double | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-GaugeAttribute-startAngle(angle: double | undefined): this--><!--Device-GaugeAttribute-startAngle(angle: double | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| angle | double \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## strokeWidth

```TypeScript
strokeWidth(length: Length | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-GaugeAttribute-strokeWidth(length: Length | undefined): this--><!--Device-GaugeAttribute-strokeWidth(length: Length | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| length | [Length](../../apis-arkui/arkts-apis/arkts-arkui-length-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## trackShadow

```TypeScript
trackShadow(value: GaugeShadowOptions | undefined | null): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-GaugeAttribute-trackShadow(value: GaugeShadowOptions | undefined | null): this--><!--Device-GaugeAttribute-trackShadow(value: GaugeShadowOptions | undefined | null): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [GaugeShadowOptions](arkts-gauge-gaugeshadowoptions-i.md) \| undefined \| null | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## value

```TypeScript
value(value: double | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-GaugeAttribute-value(value: double | undefined): this--><!--Device-GaugeAttribute-value(value: double | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | double \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## default

```TypeScript
default
```

Set Gauge options.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-GaugeAttribute-default--><!--Device-GaugeAttribute-default-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

