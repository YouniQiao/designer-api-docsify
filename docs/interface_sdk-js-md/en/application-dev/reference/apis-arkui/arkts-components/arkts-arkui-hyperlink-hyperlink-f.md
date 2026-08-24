# Hyperlink

## Hyperlink

```TypeScript
@ComponentBuilder
export declare function Hyperlink(
    address: string | Resource | undefined, content?: string | Resource, 
    content_?: CustomBuilder,
): HyperlinkAttribute
```

Defines Hyperlink Component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Decorator:** @ComponentBuilder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@ComponentBuilderexport declare function Hyperlink(    address: string | Resource | undefined, content?: string | Resource,     content_?: CustomBuilder,): HyperlinkAttribute--><!--Device-unnamed-@ComponentBuilderexport declare function Hyperlink(    address: string | Resource | undefined, content?: string | Resource,     content_?: CustomBuilder,): HyperlinkAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| address | string \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) \| undefined | Yes | The link address of component. The default value is an empty string. Passing `undefined` resets it to the default value. |
| content | string \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) | No | The title of the component. |
| content_ | [CustomBuilder](../../apis-default/arkts-apis/arkts-custombuilder-t.md) | No | The node of component. |

**Return value:**

| Type | Description |
| --- | --- |
| [HyperlinkAttribute](arkts-arkui-hyperlink-attribute.md) |  |


## Hyperlink

```TypeScript
@Builder
export declare function Hyperlink(
    style: CustomBuilderT<HyperlinkAttribute>,
    content_?: CustomBuilder,
): HyperlinkAttribute
```

Defines Hyperlink Component.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta since version 26.1.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@Builderexport declare function Hyperlink(    style: CustomBuilderT<HyperlinkAttribute>,    content_?: CustomBuilder,): HyperlinkAttribute--><!--Device-unnamed-@Builderexport declare function Hyperlink(    style: CustomBuilderT<HyperlinkAttribute>,    content_?: CustomBuilder,): HyperlinkAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | [CustomBuilderT](../../apis-default/arkts-apis/arkts-custombuildert-t.md)&lt;[HyperlinkAttribute](arkts-arkui-hyperlink-attribute.md)&gt; | Yes | Hyperlink attribute instance. |
| content_ | [CustomBuilder](../../apis-default/arkts-apis/arkts-custombuilder-t.md) | No | container. |

**Return value:**

| Type | Description |
| --- | --- |
| [HyperlinkAttribute](arkts-arkui-hyperlink-attribute.md) |  |

