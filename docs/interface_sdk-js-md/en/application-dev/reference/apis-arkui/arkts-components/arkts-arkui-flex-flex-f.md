# Flex

## Flex

```TypeScript
@ComponentBuilder
export declare function Flex(
    value?: FlexOptions,
    content_?: CustomBuilder,
): FlexAttribute
```

Defines Flex Component.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@ComponentBuilderexport declare function Flex(    value?: FlexOptions,    content_?: CustomBuilder,): FlexAttribute--><!--Device-unnamed-@ComponentBuilderexport declare function Flex(    value?: FlexOptions,    content_?: CustomBuilder,): FlexAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [FlexOptions](arkts-arkui-flex-flexoptions-i.md) | No | Flex options. |
| content_ | [CustomBuilder](../../apis-default/arkts-apis/arkts-custombuilder-t.md) | No | container |

**Return value:**

| Type | Description |
| --- | --- |
| [FlexAttribute](arkts-arkui-flex-attribute.md) |  |


## Flex

```TypeScript
@Builder
export declare function Flex(
    style: CustomBuilderT<FlexAttribute>,
    content_?: CustomBuilder,
): FlexAttribute
```

Defines Flex Component.

**Since:** 26.1.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@Builderexport declare function Flex(    style: CustomBuilderT<FlexAttribute>,    content_?: CustomBuilder,): FlexAttribute--><!--Device-unnamed-@Builderexport declare function Flex(    style: CustomBuilderT<FlexAttribute>,    content_?: CustomBuilder,): FlexAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | [CustomBuilderT](../../apis-default/arkts-apis/arkts-custombuildert-t.md)&lt;[FlexAttribute](arkts-arkui-flex-attribute.md)&gt; | Yes | the callback to set up component's attributes. |
| content_ | [CustomBuilder](../../apis-default/arkts-apis/arkts-custombuilder-t.md) | No | container. |

**Return value:**

| Type | Description |
| --- | --- |
| [FlexAttribute](arkts-arkui-flex-attribute.md) |  |

