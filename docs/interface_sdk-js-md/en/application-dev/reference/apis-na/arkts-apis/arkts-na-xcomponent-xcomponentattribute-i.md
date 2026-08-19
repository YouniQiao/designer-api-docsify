# XComponentAttribute

Defines the XComponent attribute.

**Inheritance/Implementation:** XComponentAttribute extends CommonMethod

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-unnamed-export declare interface XComponentAttribute--><!--Device-unnamed-export declare interface XComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
attributeModifier(modifier: AttributeModifier<XComponentAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-XComponentAttribute-attributeModifier(modifier: AttributeModifier<XComponentAttribute> | AttributeModifier<CommonMethod> | undefined): this--><!--Device-XComponentAttribute-attributeModifier(modifier: AttributeModifier<XComponentAttribute> | AttributeModifier<CommonMethod> | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| modifier | [AttributeModifier](../../apis-arkui/arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[XComponentAttribute](arkts-na-xcomponent-xcomponentattribute-i.md)&gt; \| [AttributeModifier](../../apis-arkui/arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../../apis-arkui/arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## enableAnalyzer

```TypeScript
enableAnalyzer(enable: boolean | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-XComponentAttribute-enableAnalyzer(enable: boolean | undefined): this--><!--Device-XComponentAttribute-enableAnalyzer(enable: boolean | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enable | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## enableSecure

```TypeScript
enableSecure(isSecure: boolean | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-XComponentAttribute-enableSecure(isSecure: boolean | undefined): this--><!--Device-XComponentAttribute-enableSecure(isSecure: boolean | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| isSecure | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## enableTransparentLayer

```TypeScript
enableTransparentLayer(enabled: boolean | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-XComponentAttribute-enableTransparentLayer(enabled: boolean | undefined): this--><!--Device-XComponentAttribute-enableTransparentLayer(enabled: boolean | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enabled | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## hdrBrightness

```TypeScript
hdrBrightness(brightness: double | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-XComponentAttribute-hdrBrightness(brightness: double | undefined): this--><!--Device-XComponentAttribute-hdrBrightness(brightness: double | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| brightness | double \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## hdrBrightness

```TypeScript
hdrBrightness(brightness: double | undefined, type?: HdrType): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-XComponentAttribute-hdrBrightness(brightness: double | undefined, type?: HdrType): this--><!--Device-XComponentAttribute-hdrBrightness(brightness: double | undefined, type?: HdrType): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| brightness | double \| undefined | Yes |  |
| type | [HdrType](arkts-na-xcomponent-hdrtype-e.md) | No |  |

**Return value:**

| Type | Description |
| --- | --- |
## onDestroy

```TypeScript
onDestroy(event: VoidCallback | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-XComponentAttribute-onDestroy(event: VoidCallback | undefined): this--><!--Device-XComponentAttribute-onDestroy(event: VoidCallback | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [VoidCallback](../../apis-arkui/arkts-apis/arkts-arkui-voidcallback-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## onLoad

```TypeScript
onLoad(callback: VoidCallback | undefined): this
```

**Since:** -1

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version -1.

<!--Device-XComponentAttribute-onLoad(callback: VoidCallback | undefined): this--><!--Device-XComponentAttribute-onLoad(callback: VoidCallback | undefined): this-End-->

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [VoidCallback](../../apis-arkui/arkts-apis/arkts-arkui-voidcallback-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
## setXComponentOptions

```TypeScript
setXComponentOptions(params: XComponentParameters | XComponentOptions | NativeXComponentParameters): this
```

Sets xcomponent options.

**Since:** 26.1.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-XComponentAttribute-setXComponentOptions(params: XComponentParameters | XComponentOptions | NativeXComponentParameters): this--><!--Device-XComponentAttribute-setXComponentOptions(params: XComponentParameters | XComponentOptions | NativeXComponentParameters): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| params | [XComponentParameters](arkts-na-xcomponent-xcomponentparameters-i.md) \| [XComponentOptions](arkts-na-xcomponent-xcomponentoptions-i.md) \| [NativeXComponentParameters](arkts-na-xcomponent-nativexcomponentparameters-i.md) | Yes | The options to create an XComponent |

**Return value:**

| Type | Description |
| --- | --- |
| this | XComponentAttribute instance |

## default

```TypeScript
default
```

Call attributeModifier.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-XComponentAttribute-default--><!--Device-XComponentAttribute-default-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

