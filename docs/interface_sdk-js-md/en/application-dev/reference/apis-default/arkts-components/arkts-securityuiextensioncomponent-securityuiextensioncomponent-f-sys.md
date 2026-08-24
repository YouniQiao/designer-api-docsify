# SecurityUIExtensionComponent (System API)

## SecurityUIExtensionComponent

```TypeScript
@ComponentBuilder
export declare function SecurityUIExtensionComponent(
    want: Want, options?: SecurityUIExtensionOptions, 
    content_?: CustomBuilder,
): SecurityUIExtensionComponentAttribute
```

Defines SecurityUIExtensionComponent Component.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta since version 26.0.0.

**Decorator:** @ComponentBuilder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@ComponentBuilderexport declare function SecurityUIExtensionComponent(    want: Want, options?: SecurityUIExtensionOptions,     content_?: CustomBuilder,): SecurityUIExtensionComponentAttribute--><!--Device-unnamed-@ComponentBuilderexport declare function SecurityUIExtensionComponent(    want: Want, options?: SecurityUIExtensionOptions,     content_?: CustomBuilder,): SecurityUIExtensionComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes | Want object |
| options | [SecurityUIExtensionOptions](arkts-securityuiextensioncomponent-securityuiextensionoptions-i-sys.md) | No | The options |
| content_ | [CustomBuilder](../arkts-apis/arkts-custombuilder-t.md) | No | container |

**Return value:**

| Type | Description |
| --- | --- |
| [SecurityUIExtensionComponentAttribute](arkts-securityuiextensioncomponent-attribute.md) |  |


## SecurityUIExtensionComponent

```TypeScript
@Builder
export declare function SecurityUIExtensionComponent(
    style: CustomBuilderT<SecurityUIExtensionComponentAttribute>,
    content_?: CustomBuilder,
): SecurityUIExtensionComponentAttribute
```

Defines SecurityUIExtensionComponent Component.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta since version 26.1.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@Builderexport declare function SecurityUIExtensionComponent(    style: CustomBuilderT<SecurityUIExtensionComponentAttribute>,    content_?: CustomBuilder,): SecurityUIExtensionComponentAttribute--><!--Device-unnamed-@Builderexport declare function SecurityUIExtensionComponent(    style: CustomBuilderT<SecurityUIExtensionComponentAttribute>,    content_?: CustomBuilder,): SecurityUIExtensionComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | [CustomBuilderT](../arkts-apis/arkts-custombuildert-t.md)&lt;[SecurityUIExtensionComponentAttribute](arkts-securityuiextensioncomponent-attribute.md)&gt; | Yes | the callback to set up SecurityUIExtensionComponent's attributes. |
| content_ | [CustomBuilder](../arkts-apis/arkts-custombuilder-t.md) | No | container |

**Return value:**

| Type | Description |
| --- | --- |
| [SecurityUIExtensionComponentAttribute](arkts-securityuiextensioncomponent-attribute.md) | The attribute of the SecurityUIExtensionComponent. |

