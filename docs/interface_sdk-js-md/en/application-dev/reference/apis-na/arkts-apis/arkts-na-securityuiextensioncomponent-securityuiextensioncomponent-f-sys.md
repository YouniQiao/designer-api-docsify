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

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@ComponentBuilderexport declare function SecurityUIExtensionComponent(    want: Want, options?: SecurityUIExtensionOptions,     content_?: CustomBuilder,): SecurityUIExtensionComponentAttribute--><!--Device-unnamed-@ComponentBuilderexport declare function SecurityUIExtensionComponent(    want: Want, options?: SecurityUIExtensionOptions,     content_?: CustomBuilder,): SecurityUIExtensionComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| want | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes | Want object |
| options | [SecurityUIExtensionOptions](arkts-na-securityuiextensioncomponent-securityuiextensionoptions-i-sys.md) | No | The options |
| content_ | CustomBuilder | No | container |

**Return value:**

| Type | Description |
| --- | --- |
| SecurityUIExtensionComponentAttribute |  |


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

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@Builderexport declare function SecurityUIExtensionComponent(    style: CustomBuilderT<SecurityUIExtensionComponentAttribute>,    content_?: CustomBuilder,): SecurityUIExtensionComponentAttribute--><!--Device-unnamed-@Builderexport declare function SecurityUIExtensionComponent(    style: CustomBuilderT<SecurityUIExtensionComponentAttribute>,    content_?: CustomBuilder,): SecurityUIExtensionComponentAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | CustomBuilderT&lt;SecurityUIExtensionComponentAttribute&gt; | Yes | the callback to set up SecurityUIExtensionComponent's attributes. |
| content_ | CustomBuilder | No | container |

**Return value:**

| Type | Description |
| --- | --- |
| SecurityUIExtensionComponentAttribute | The attribute of the SecurityUIExtensionComponent. |

