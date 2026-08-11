# Hyperlink

## Hyperlink

```TypeScript
export declare function Hyperlink(
    address: string | Resource | undefined, content?: string | Resource, 
    content_?: CustomBuilder,
): HyperlinkAttribute
```

Defines Hyperlink Component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function Hyperlink(    address: string | Resource | undefined, content?: string | Resource,     content_?: CustomBuilder,): HyperlinkAttribute--><!--Device-unnamed-export declare function Hyperlink(    address: string | Resource | undefined, content?: string | Resource,     content_?: CustomBuilder,): HyperlinkAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| address | string \| Resource \| undefined | Yes | The link address of component. The default value is an empty string. Passing `undefined` resets it to the default value. |
| content | string \| Resource | No | The title of the component. |
| content_ | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | No | The node of component. |

**Return value:**

| Type | Description |
| --- | --- |
| [HyperlinkAttribute](../arkts-components/arkts-arkui-hyperlink-attribute.md) |  |


## Hyperlink

```TypeScript
export declare function Hyperlink(
    style: CustomBuilderT<HyperlinkAttribute>,
    content_?: CustomBuilder,
): HyperlinkAttribute
```

Defines Hyperlink Component.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function Hyperlink(    style: CustomBuilderT<HyperlinkAttribute>,    content_?: CustomBuilder,): HyperlinkAttribute--><!--Device-unnamed-export declare function Hyperlink(    style: CustomBuilderT<HyperlinkAttribute>,    content_?: CustomBuilder,): HyperlinkAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | [CustomBuilderT](../arkts-components/arkts-arkui-custombuildert-t.md)&lt;HyperlinkAttribute&gt; | Yes | Hyperlink attribute instance. |
| content_ | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | No | container. |

**Return value:**

| Type | Description |
| --- | --- |
| [HyperlinkAttribute](../arkts-components/arkts-arkui-hyperlink-attribute.md) |  |

