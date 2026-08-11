# SecurityUIExtensionComponent (System API)

## SecurityUIExtensionComponent

```TypeScript
export declare function SecurityUIExtensionComponent(
    want: Want, options?: SecurityUIExtensionOptions, 
    content_?: CustomBuilder,
): SecurityUIExtensionComponentAttribute
```

Defines SecurityUIExtensionComponent Component.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function SecurityUIExtensionComponent(    want: Want, options?: SecurityUIExtensionOptions,     content_?: CustomBuilder,): SecurityUIExtensionComponentAttribute--><!--Device-unnamed-export declare function SecurityUIExtensionComponent(    want: Want, options?: SecurityUIExtensionOptions,     content_?: CustomBuilder,): SecurityUIExtensionComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes | Want object |
| options | [SecurityUIExtensionOptions](arkts-arkui-securityuiextensioncomponent-securityuiextensionoptions-i-sys.md) | No | The options |
| content_ | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | No | container |

**Return value:**

| Type | Description |
| --- | --- |
| [SecurityUIExtensionComponentAttribute](../arkts-components/arkts-arkui-securityuiextensioncomponent-attribute.md) |  |


## SecurityUIExtensionComponent

```TypeScript
export declare function SecurityUIExtensionComponent(
    style: CustomBuilderT<SecurityUIExtensionComponentAttribute>,
    content_?: CustomBuilder,
): SecurityUIExtensionComponentAttribute
```

Defines SecurityUIExtensionComponent Component.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function SecurityUIExtensionComponent(    style: CustomBuilderT<SecurityUIExtensionComponentAttribute>,    content_?: CustomBuilder,): SecurityUIExtensionComponentAttribute--><!--Device-unnamed-export declare function SecurityUIExtensionComponent(    style: CustomBuilderT<SecurityUIExtensionComponentAttribute>,    content_?: CustomBuilder,): SecurityUIExtensionComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | [CustomBuilderT](../arkts-components/arkts-arkui-custombuildert-t.md)&lt;SecurityUIExtensionComponentAttribute&gt; | Yes | the callback to set up SecurityUIExtensionComponent's attributes. |
| content_ | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | No | container |

**Return value:**

| Type | Description |
| --- | --- |
| [SecurityUIExtensionComponentAttribute](../arkts-components/arkts-arkui-securityuiextensioncomponent-attribute.md) | The attribute of the SecurityUIExtensionComponent. |

