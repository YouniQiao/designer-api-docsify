# GaugeAttribute

除支持通用属性外，还支持以下属性。支持通用事件。

**继承/实现关系：** GaugeAttribute extends CommonMethod

**起始版本：** 23

**ArkTS模式：** ArkTS-Sta起始版本为23。

<!--Device-unnamed-export declare interface GaugeAttribute--><!--Device-unnamed-export declare interface GaugeAttribute-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
attributeModifier(modifier: AttributeModifier<GaugeAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-GaugeAttribute-attributeModifier(modifier: AttributeModifier<GaugeAttribute> | AttributeModifier<CommonMethod> | undefined): this--><!--Device-GaugeAttribute-attributeModifier(modifier: AttributeModifier<GaugeAttribute> | AttributeModifier<CommonMethod> | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| modifier | [AttributeModifier](../../apis-arkui/arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[GaugeAttribute](arkts-gauge-attribute.md)&gt; \| [AttributeModifier](../../apis-arkui/arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../../apis-arkui/arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## colors

```TypeScript
colors(colors: ResourceColor | LinearGradient | Array<[ResourceColor | LinearGradient, double]> | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-GaugeAttribute-colors(colors: ResourceColor | LinearGradient | Array<[ResourceColor | LinearGradient, double]> | undefined): this--><!--Device-GaugeAttribute-colors(colors: ResourceColor | LinearGradient | Array<[ResourceColor | LinearGradient, double]> | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| colors | [ResourceColor](../../apis-arkui/arkts-apis/arkts-arkui-resourcecolor-t.md) \| [LinearGradient](arkts-datapanel-lineargradient-c.md) \| Array&lt;[ResourceColor \| [LinearGradient](arkts-datapanel-lineargradient-c.md), double]&gt; \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## contentModifier

```TypeScript
contentModifier(modifier: ContentModifier<GaugeConfiguration> | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-GaugeAttribute-contentModifier(modifier: ContentModifier<GaugeConfiguration> | undefined): this--><!--Device-GaugeAttribute-contentModifier(modifier: ContentModifier<GaugeConfiguration> | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| modifier | [ContentModifier](../../apis-arkui/arkts-components/arkts-arkui-contentmodifier-i.md)&lt;[GaugeConfiguration](arkts-gauge-gaugeconfiguration-i.md)&gt; \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## description

```TypeScript
description(value: CustomBuilder | undefined | null): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-GaugeAttribute-description(value: CustomBuilder | undefined | null): this--><!--Device-GaugeAttribute-description(value: CustomBuilder | undefined | null): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [CustomBuilder](../arkts-apis/arkts-custombuilder-t.md) \| undefined \| null | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## endAngle

```TypeScript
endAngle(angle: double | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-GaugeAttribute-endAngle(angle: double | undefined): this--><!--Device-GaugeAttribute-endAngle(angle: double | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| angle | double \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## indicator

```TypeScript
indicator(value: GaugeIndicatorOptions | undefined | null): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-GaugeAttribute-indicator(value: GaugeIndicatorOptions | undefined | null): this--><!--Device-GaugeAttribute-indicator(value: GaugeIndicatorOptions | undefined | null): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [GaugeIndicatorOptions](arkts-gauge-gaugeindicatoroptions-i.md) \| undefined \| null | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## privacySensitive

```TypeScript
privacySensitive(isPrivacySensitiveMode: boolean | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-GaugeAttribute-privacySensitive(isPrivacySensitiveMode: boolean | undefined): this--><!--Device-GaugeAttribute-privacySensitive(isPrivacySensitiveMode: boolean | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isPrivacySensitiveMode | boolean \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## setGaugeOptions

```TypeScript
setGaugeOptions(options: GaugeOptions): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-GaugeAttribute-setGaugeOptions(options: GaugeOptions): this--><!--Device-GaugeAttribute-setGaugeOptions(options: GaugeOptions): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [GaugeOptions](arkts-gauge-gaugeoptions-i.md) | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## startAngle

```TypeScript
startAngle(angle: double | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-GaugeAttribute-startAngle(angle: double | undefined): this--><!--Device-GaugeAttribute-startAngle(angle: double | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| angle | double \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## strokeWidth

```TypeScript
strokeWidth(length: Length | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-GaugeAttribute-strokeWidth(length: Length | undefined): this--><!--Device-GaugeAttribute-strokeWidth(length: Length | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| length | [Length](../../apis-arkui/arkts-apis/arkts-arkui-length-t.md) \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## trackShadow

```TypeScript
trackShadow(value: GaugeShadowOptions | undefined | null): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-GaugeAttribute-trackShadow(value: GaugeShadowOptions | undefined | null): this--><!--Device-GaugeAttribute-trackShadow(value: GaugeShadowOptions | undefined | null): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [GaugeShadowOptions](arkts-gauge-gaugeshadowoptions-i.md) \| undefined \| null | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## value

```TypeScript
value(value: double | undefined): this
```

**起始版本：** -1

**ArkTS模式：** ArkTS-Sta起始版本为-1。

<!--Device-GaugeAttribute-value(value: double | undefined): this--><!--Device-GaugeAttribute-value(value: double | undefined): this-End-->

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | double \| undefined | 是 |  |

**返回值：**

| 类型 | 说明 |
| --- | --- |
## default

```TypeScript
default
```

设置Gauge选项。

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-GaugeAttribute-default--><!--Device-GaugeAttribute-default-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

