# Hyperlink

## Hyperlink

```TypeScript
export declare function Hyperlink(
    address: string | Resource | undefined, content?: string | Resource, 
    content_?: CustomBuilder,
): HyperlinkAttribute
```

定义Hyperlink组件。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function Hyperlink(    address: string | Resource | undefined, content?: string | Resource,     content_?: CustomBuilder,): HyperlinkAttribute--><!--Device-unnamed-export declare function Hyperlink(    address: string | Resource | undefined, content?: string | Resource,     content_?: CustomBuilder,): HyperlinkAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| address | string \| Resource \| undefined | Yes | Hyperlink组件跳转的网页地址。&lt;br/&gt;取值为undefined时，按无跳转链接地址处理。 |
| content | string \| Resource | No | Hyperlink组件中超链接显示文本。&lt;br/&gt;若不传该参数且组件内无子组件时，默认显示address参数值链接地址。&lt;br/&gt; **说明：** &lt;br/&gt;组件内有子组件时，不显示超链接文本。 &lt;br&gt;默认值：''。 |
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

定义Hyperlink组件。

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function Hyperlink(    style: CustomBuilderT<HyperlinkAttribute>,    content_?: CustomBuilder,): HyperlinkAttribute--><!--Device-unnamed-export declare function Hyperlink(    style: CustomBuilderT<HyperlinkAttribute>,    content_?: CustomBuilder,): HyperlinkAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | [CustomBuilderT](../arkts-components/arkts-arkui-custombuildert-t.md)&lt;HyperlinkAttribute&gt; | Yes | Hyperlink属性实例。 |
| content_ | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | No | 容器。 |

**Return value:**

| Type | Description |
| --- | --- |
| [HyperlinkAttribute](../arkts-components/arkts-arkui-hyperlink-attribute.md) |  |

