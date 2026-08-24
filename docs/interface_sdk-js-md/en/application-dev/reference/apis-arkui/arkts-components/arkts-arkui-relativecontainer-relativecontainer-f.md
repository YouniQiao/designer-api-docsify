# RelativeContainer

## RelativeContainer

```TypeScript
@ComponentBuilder
export declare function RelativeContainer(
    
    content_?: CustomBuilder,
): RelativeContainerAttribute
```

Defines RelativeContainer Component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Decorator:** @ComponentBuilder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@ComponentBuilderexport declare function RelativeContainer(        content_?: CustomBuilder,): RelativeContainerAttribute--><!--Device-unnamed-@ComponentBuilderexport declare function RelativeContainer(        content_?: CustomBuilder,): RelativeContainerAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| content_ | [CustomBuilder](../../apis-default/arkts-apis/arkts-custombuilder-t.md) | No | container |

**Return value:**

| Type | Description |
| --- | --- |
| [RelativeContainerAttribute](arkts-arkui-relativecontainer-attribute.md) |  |


## RelativeContainer

```TypeScript
@Builder
export declare function RelativeContainer(
    style: CustomBuilderT<RelativeContainerAttribute>,
    content_?: CustomBuilder,
): RelativeContainerAttribute
```

Defines RelativeContainer Component.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta since version 26.1.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@Builderexport declare function RelativeContainer(    style: CustomBuilderT<RelativeContainerAttribute>,    content_?: CustomBuilder,): RelativeContainerAttribute--><!--Device-unnamed-@Builderexport declare function RelativeContainer(    style: CustomBuilderT<RelativeContainerAttribute>,    content_?: CustomBuilder,): RelativeContainerAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | [CustomBuilderT](../../apis-default/arkts-apis/arkts-custombuildert-t.md)&lt;[RelativeContainerAttribute](arkts-arkui-relativecontainer-attribute.md)&gt; | Yes | the callback to set up component's attributes. |
| content_ | [CustomBuilder](../../apis-default/arkts-apis/arkts-custombuilder-t.md) | No | container |

**Return value:**

| Type | Description |
| --- | --- |
| [RelativeContainerAttribute](arkts-arkui-relativecontainer-attribute.md) |  |

