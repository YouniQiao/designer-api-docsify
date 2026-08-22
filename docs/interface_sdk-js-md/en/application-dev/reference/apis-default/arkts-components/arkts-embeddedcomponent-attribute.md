# EmbeddedComponentAttribute

Define the attribute functions of EmbeddedComponent.

**Inheritance/Implementation:** EmbeddedComponentAttribute extends CommonMethod

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-unnamed-export declare interface EmbeddedComponentAttribute--><!--Device-unnamed-export declare interface EmbeddedComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
attributeModifier(modifier: AttributeModifier<EmbeddedComponentAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

Set attributeModifier.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-EmbeddedComponentAttribute-attributeModifier(modifier: AttributeModifier<EmbeddedComponentAttribute> | AttributeModifier<CommonMethod> | undefined): this--><!--Device-EmbeddedComponentAttribute-attributeModifier(modifier: AttributeModifier<EmbeddedComponentAttribute> | AttributeModifier<CommonMethod> | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| modifier | [AttributeModifier](../../apis-arkui/arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[EmbeddedComponentAttribute](arkts-embeddedcomponent-attribute.md)&gt; \| [AttributeModifier](../../apis-arkui/arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../../apis-arkui/arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| [EmbeddedComponentAttribute](arkts-embeddedcomponent-attribute.md) |  |

## onDrawReady

```TypeScript
onDrawReady(callback: VoidCallback | undefined ): this
```

Callback called when the EmbeddedUIExtensionAbility draw the first frame.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-EmbeddedComponentAttribute-onDrawReady(callback: VoidCallback | undefined ): this--><!--Device-EmbeddedComponentAttribute-onDrawReady(callback: VoidCallback | undefined ): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [VoidCallback](../../apis-arkui/arkts-apis/arkts-arkui-voidcallback-t.md) \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| [EmbeddedComponentAttribute](arkts-embeddedcomponent-attribute.md) |  |

## onError

```TypeScript
onError(callback: ErrorCallback<BusinessError> | undefined ): this
```

Called when some error occurred.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-EmbeddedComponentAttribute-onError(callback: ErrorCallback<BusinessError> | undefined ): this--><!--Device-EmbeddedComponentAttribute-onError(callback: ErrorCallback<BusinessError> | undefined ): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [ErrorCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-errorcallback-t.md)&lt;[BusinessError](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-businesserror-c.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| [EmbeddedComponentAttribute](arkts-embeddedcomponent-attribute.md) |  |

## onTerminated

```TypeScript
onTerminated(callback: Callback<TerminationInfo> | undefined ): this
```

Called when the provider of the embedded UI is terminated.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-EmbeddedComponentAttribute-onTerminated(callback: Callback<TerminationInfo> | undefined ): this--><!--Device-EmbeddedComponentAttribute-onTerminated(callback: Callback<TerminationInfo> | undefined ): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;TerminationInfo&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| [EmbeddedComponentAttribute](arkts-embeddedcomponent-attribute.md) |  |

## setEmbeddedComponentOptions

```TypeScript
setEmbeddedComponentOptions(loader: Want, type?: EmbeddedType): this
```

Sets embedded component options.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-EmbeddedComponentAttribute-setEmbeddedComponentOptions(loader: Want, type?: EmbeddedType): this--><!--Device-EmbeddedComponentAttribute-setEmbeddedComponentOptions(loader: Want, type?: EmbeddedType): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| loader | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-appabilitywant-want-c.md) | Yes | indicates initialization parameter. |
| type | [EmbeddedType](../../apis-arkui/arkts-apis/arkts-arkui-embeddedtype-e.md) | No | indicates type of the EmbeddedComponent. |

**Return value:**

| Type | Description |
| --- | --- |
| this | EmbeddedComponentAttribute instance |

## setEmbeddedComponentOptions

```TypeScript
setEmbeddedComponentOptions(loader: Want, type?: EmbeddedType, options?: EmbeddedOptions): this
```

Sets embedded component options.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-EmbeddedComponentAttribute-setEmbeddedComponentOptions(loader: Want, type?: EmbeddedType, options?: EmbeddedOptions): this--><!--Device-EmbeddedComponentAttribute-setEmbeddedComponentOptions(loader: Want, type?: EmbeddedType, options?: EmbeddedOptions): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| loader | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-appabilitywant-want-c.md) | Yes | indicates initialization parameter. |
| type | [EmbeddedType](../../apis-arkui/arkts-apis/arkts-arkui-embeddedtype-e.md) | No | indicates type of the EmbeddedComponent. |
| options | [EmbeddedOptions](arkts-embeddedcomponent-embeddedoptions-i.md) | No | indicates type of the EmbeddedComponent options. |

**Return value:**

| Type | Description |
| --- | --- |
| this | EmbeddedComponentAttribute instance |

