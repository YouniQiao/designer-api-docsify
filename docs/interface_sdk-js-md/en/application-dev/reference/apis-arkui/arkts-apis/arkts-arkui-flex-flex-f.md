# Flex

## Flex

```TypeScript
export declare function Flex(
    value?: FlexOptions,
    content_?: CustomBuilder,
): FlexAttribute
```

Defines Flex Component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function Flex(    value?: FlexOptions,    content_?: CustomBuilder,): FlexAttribute--><!--Device-unnamed-export declare function Flex(    value?: FlexOptions,    content_?: CustomBuilder,): FlexAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [FlexOptions](../arkts-components/arkts-arkui-flexoptions-i.md) | No | Flex options. |
| content_ | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | No | container |

**Return value:**

| Type | Description |
| --- | --- |
| [FlexAttribute](../arkts-components/arkts-arkui-flex-attribute.md) |  |


## Flex

```TypeScript
export declare function Flex(
    style: CustomBuilderT<FlexAttribute>,
    content_?: CustomBuilder,
): FlexAttribute
```

Defines Flex Component.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function Flex(    style: CustomBuilderT<FlexAttribute>,    content_?: CustomBuilder,): FlexAttribute--><!--Device-unnamed-export declare function Flex(    style: CustomBuilderT<FlexAttribute>,    content_?: CustomBuilder,): FlexAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | [CustomBuilderT](../arkts-components/arkts-arkui-custombuildert-t.md)&lt;FlexAttribute&gt; | Yes | the callback to set up component's attributes. |
| content_ | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | No | container. |

**Return value:**

| Type | Description |
| --- | --- |
| [FlexAttribute](../arkts-components/arkts-arkui-flex-attribute.md) |  |

