# ProgressAttribute

Defines the Progress component attributes.

**Inheritance/Implementation:** ProgressAttribute extends CommonMethod

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare interface ProgressAttribute--><!--Device-unnamed-export declare interface ProgressAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
attributeModifier(modifier: AttributeModifier<ProgressAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-ProgressAttribute-attributeModifier(modifier: AttributeModifier<ProgressAttribute> | AttributeModifier<CommonMethod> | undefined): this--><!--Device-ProgressAttribute-attributeModifier(modifier: AttributeModifier<ProgressAttribute> | AttributeModifier<CommonMethod> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| modifier | [AttributeModifier](../../apis-arkui/arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[ProgressAttribute](arkts-progress-attribute.md)&gt; \| [AttributeModifier](../../apis-arkui/arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../../apis-arkui/arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## color

```TypeScript
color(value: ResourceColor | LinearGradient | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-ProgressAttribute-color(value: ResourceColor | LinearGradient | undefined): this--><!--Device-ProgressAttribute-color(value: ResourceColor | LinearGradient | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ResourceColor](../../apis-arkui/arkts-apis/arkts-arkui-resourcecolor-t.md) \| [LinearGradient](arkts-datapanel-lineargradient-c.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## contentModifier

```TypeScript
contentModifier(modifier: ContentModifier<ProgressConfiguration> | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-ProgressAttribute-contentModifier(modifier: ContentModifier<ProgressConfiguration> | undefined): this--><!--Device-ProgressAttribute-contentModifier(modifier: ContentModifier<ProgressConfiguration> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| modifier | [ContentModifier](../../apis-arkui/arkts-components/arkts-arkui-contentmodifier-i.md)&lt;[ProgressConfiguration](arkts-progress-progressconfiguration-i.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## privacySensitive

```TypeScript
privacySensitive(isPrivacySensitiveMode: boolean | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-ProgressAttribute-privacySensitive(isPrivacySensitiveMode: boolean | undefined): this--><!--Device-ProgressAttribute-privacySensitive(isPrivacySensitiveMode: boolean | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| isPrivacySensitiveMode | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## setProgressOptions

```TypeScript
setProgressOptions(options: ProgressOptions): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-ProgressAttribute-setProgressOptions(options: ProgressOptions): this--><!--Device-ProgressAttribute-setProgressOptions(options: ProgressOptions): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [ProgressOptions](arkts-progress-progressoptions-i.md) | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## style

```TypeScript
style(value: LinearStyleOptions | RingStyleOptions | CapsuleStyleOptions | ProgressStyleOptions | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-ProgressAttribute-style(value: LinearStyleOptions | RingStyleOptions | CapsuleStyleOptions | ProgressStyleOptions | undefined): this--><!--Device-ProgressAttribute-style(value: LinearStyleOptions | RingStyleOptions | CapsuleStyleOptions | ProgressStyleOptions | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [LinearStyleOptions](arkts-progress-linearstyleoptions-i.md) \| [RingStyleOptions](arkts-progress-ringstyleoptions-i.md) \| [CapsuleStyleOptions](arkts-progress-capsulestyleoptions-i.md) \| [ProgressStyleOptions](arkts-progress-progressstyleoptions-i.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## value

```TypeScript
value(value: double | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-ProgressAttribute-value(value: double | undefined): this--><!--Device-ProgressAttribute-value(value: double | undefined): this-End-->

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

Set Progress options.

**Since:** 26.1.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ProgressAttribute-default--><!--Device-ProgressAttribute-default-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

