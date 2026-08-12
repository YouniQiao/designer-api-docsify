# XComponentAttribute

Defines the XComponent attribute.

**Inheritance/Implementation:** XComponentAttribute extends [CommonMethod](CommonMethod)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface XComponentAttribute extends CommonMethod--><!--Device-unnamed-export declare interface XComponentAttribute extends CommonMethod-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
default attributeModifier(modifier: AttributeModifier<XComponentAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

Call attributeModifier.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-XComponentAttribute-default attributeModifier(modifier: AttributeModifier<XComponentAttribute> | AttributeModifier<CommonMethod> | undefined): this--><!--Device-XComponentAttribute-default attributeModifier(modifier: AttributeModifier<XComponentAttribute> | AttributeModifier<CommonMethod> | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[XComponentAttribute](arkts-arkui-xcomponent-xcomponentattribute-i.md)&gt; \| [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## enableAnalyzer

```TypeScript
default enableAnalyzer(enable: boolean | undefined): this
```

Enable image analyzer for XComponent.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-XComponentAttribute-default enableAnalyzer(enable: boolean | undefined): this--><!--Device-XComponentAttribute-default enableAnalyzer(enable: boolean | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enable | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## enableSecure

```TypeScript
default enableSecure(isSecure: boolean | undefined): this
```

Enable privacy protection for XComponent.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-XComponentAttribute-default enableSecure(isSecure: boolean | undefined): this--><!--Device-XComponentAttribute-default enableSecure(isSecure: boolean | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| isSecure | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## hdrBrightness

```TypeScript
default hdrBrightness(brightness: double | undefined): this
```

Set hdrBrightness for XComponent.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-XComponentAttribute-default hdrBrightness(brightness: double | undefined): this--><!--Device-XComponentAttribute-default hdrBrightness(brightness: double | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| brightness | double \| undefined | Yes | control the brightness of HDR video |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## hdrBrightness

```TypeScript
default hdrBrightness(brightness: double | undefined, type?: HdrType): this
```

Set hdrBrightness for XComponent.

**Since:** 24

**ArkTS mode:** ArkTS-Sta only, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-XComponentAttribute-default hdrBrightness(brightness: double | undefined, type?: HdrType): this--><!--Device-XComponentAttribute-default hdrBrightness(brightness: double | undefined, type?: HdrType): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| brightness | double \| undefined | Yes | control the brightness of HDR video |
| type | [HdrType](arkts-arkui-xcomponent-hdrtype-e.md) | No | the HDR type of the XComponent |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onDestroy

```TypeScript
default onDestroy(event: VoidCallback | undefined): this
```

Called when judging whether the xcomponent is destroyed.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-XComponentAttribute-default onDestroy(event: VoidCallback | undefined): this--><!--Device-XComponentAttribute-default onDestroy(event: VoidCallback | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| event | [VoidCallback](arkts-arkui-voidcallback-t.md) \| undefined | Yes | Called when judging whether the xcomponent is destroyed. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## onLoad

```TypeScript
default onLoad(callback: VoidCallback | undefined): this
```

Called when judging whether the xcomponent surface is created.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-XComponentAttribute-default onLoad(callback: VoidCallback | undefined): this--><!--Device-XComponentAttribute-default onLoad(callback: VoidCallback | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [VoidCallback](arkts-arkui-voidcallback-t.md) \| undefined | Yes | Called when judging whether the xcomponent surface is created. |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## setXComponentOptions

```TypeScript
setXComponentOptions(params: XComponentParameters | XComponentOptions | NativeXComponentParameters): this
```

Sets xcomponent options.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-XComponentAttribute-setXComponentOptions(params: XComponentParameters | XComponentOptions | NativeXComponentParameters): this--><!--Device-XComponentAttribute-setXComponentOptions(params: XComponentParameters | XComponentOptions | NativeXComponentParameters): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| params | [XComponentParameters](arkts-arkui-xcomponent-xcomponentparameters-i.md) \| [XComponentOptions](arkts-arkui-xcomponent-xcomponentoptions-i.md) \| [NativeXComponentParameters](arkts-arkui-xcomponent-nativexcomponentparameters-i.md) | Yes | The options to create an XComponent |

**Return value:**

| Type | Description |
| --- | --- |
| this | XComponentAttribute instance |

