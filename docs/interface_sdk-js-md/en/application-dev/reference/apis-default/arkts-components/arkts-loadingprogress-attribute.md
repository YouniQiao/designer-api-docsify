# LoadingProgressAttribute

Defines the LoadingProgress component attributes.

**Inheritance/Implementation:** LoadingProgressAttribute extends CommonMethod

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-unnamed-export declare interface LoadingProgressAttribute--><!--Device-unnamed-export declare interface LoadingProgressAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
attributeModifier(modifier: AttributeModifier<LoadingProgressAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-LoadingProgressAttribute-attributeModifier(modifier: AttributeModifier<LoadingProgressAttribute> | AttributeModifier<CommonMethod> | undefined): this--><!--Device-LoadingProgressAttribute-attributeModifier(modifier: AttributeModifier<LoadingProgressAttribute> | AttributeModifier<CommonMethod> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| modifier | [AttributeModifier](../../apis-arkui/arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[LoadingProgressAttribute](arkts-loadingprogress-attribute.md)&gt; \| [AttributeModifier](../../apis-arkui/arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../../apis-arkui/arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## color

```TypeScript
color(value: ResourceColor | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-LoadingProgressAttribute-color(value: ResourceColor | undefined): this--><!--Device-LoadingProgressAttribute-color(value: ResourceColor | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ResourceColor](../../apis-arkui/arkts-apis/arkts-arkui-resourcecolor-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## contentModifier

```TypeScript
contentModifier(modifier: ContentModifier<LoadingProgressConfiguration> | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-LoadingProgressAttribute-contentModifier(modifier: ContentModifier<LoadingProgressConfiguration> | undefined): this--><!--Device-LoadingProgressAttribute-contentModifier(modifier: ContentModifier<LoadingProgressConfiguration> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| modifier | [ContentModifier](../../apis-arkui/arkts-components/arkts-arkui-contentmodifier-i.md)&lt;[LoadingProgressConfiguration](arkts-loadingprogress-loadingprogressconfiguration-i.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## enableLoading

```TypeScript
enableLoading(value: boolean | undefined): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-LoadingProgressAttribute-enableLoading(value: boolean | undefined): this--><!--Device-LoadingProgressAttribute-enableLoading(value: boolean | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## setLoadingProgressOptions

```TypeScript
setLoadingProgressOptions(): this
```

**Since:** -1

**ArkTS mode:** ArkTS-Sta since version -1.

<!--Device-LoadingProgressAttribute-setLoadingProgressOptions(): this--><!--Device-LoadingProgressAttribute-setLoadingProgressOptions(): this-End-->

**Return value:**

| Type | Description |
| --- | --- |
## default

```TypeScript
default
```

Sets the default LoadingProgress options. The default options include the default loading progress style and color settings.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LoadingProgressAttribute-default--><!--Device-LoadingProgressAttribute-default-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

