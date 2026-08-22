# Scroll

## Scroll

```TypeScript
@ComponentBuilder
export declare function Scroll(
    scroller?: Scroller,
    content_?: CustomBuilder,
): ScrollAttribute
```

Defines Scroll Component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@ComponentBuilderexport declare function Scroll(    scroller?: Scroller,    content_?: CustomBuilder,): ScrollAttribute--><!--Device-unnamed-@ComponentBuilderexport declare function Scroll(    scroller?: Scroller,    content_?: CustomBuilder,): ScrollAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| scroller | [Scroller](arkts-scroll-scroller-c.md) | No | scroller |
| content_ | [CustomBuilder](../arkts-apis/arkts-custombuilder-t.md) | No | container |

**Return value:**

| Type | Description |
| --- | --- |
| [ScrollAttribute](arkts-scroll-attribute.md) |  |


## Scroll

```TypeScript
@Builder
export declare function Scroll(
    style_: CustomBuilderT<ScrollAttribute>,
    content_?: CustomBuilder
): ScrollAttribute
```

Defines Scroll Component.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@Builderexport declare function Scroll(    style_: CustomBuilderT<ScrollAttribute>,    content_?: CustomBuilder): ScrollAttribute--><!--Device-unnamed-@Builderexport declare function Scroll(    style_: CustomBuilderT<ScrollAttribute>,    content_?: CustomBuilder): ScrollAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style_ | [CustomBuilderT](../arkts-apis/arkts-custombuildert-t.md)&lt;[ScrollAttribute](arkts-scroll-attribute.md)&gt; | Yes | The style to create a Scroll. |
| content_ | [CustomBuilder](../arkts-apis/arkts-custombuilder-t.md) | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| [ScrollAttribute](arkts-scroll-attribute.md) | The attribute of the Scroll. |

