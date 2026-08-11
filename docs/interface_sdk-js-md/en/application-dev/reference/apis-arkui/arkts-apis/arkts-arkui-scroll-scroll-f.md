# Scroll

## Scroll

```TypeScript
export declare function Scroll(
    scroller?: Scroller,
    content_?: CustomBuilder,
): ScrollAttribute
```

Defines Scroll Component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function Scroll(    scroller?: Scroller,    content_?: CustomBuilder,): ScrollAttribute--><!--Device-unnamed-export declare function Scroll(    scroller?: Scroller,    content_?: CustomBuilder,): ScrollAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| scroller | [Scroller](arkts-arkui-scroll-scroller-c.md) | No | scroller |
| content_ | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | No | container |

**Return value:**

| Type | Description |
| --- | --- |
| [ScrollAttribute](arkts-arkui-scroll-scrollattribute-i.md) |  |


## Scroll

```TypeScript
export declare function Scroll(
    style_: CustomBuilderT<ScrollAttribute>,
    content_?: CustomBuilder
): ScrollAttribute
```

Defines Scroll Component.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function Scroll(    style_: CustomBuilderT<ScrollAttribute>,    content_?: CustomBuilder): ScrollAttribute--><!--Device-unnamed-export declare function Scroll(    style_: CustomBuilderT<ScrollAttribute>,    content_?: CustomBuilder): ScrollAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style_ | [CustomBuilderT](../arkts-components/arkts-arkui-custombuildert-t.md)&lt;ScrollAttribute&gt; | Yes | The style to create a Scroll. |
| content_ | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| [ScrollAttribute](arkts-arkui-scroll-scrollattribute-i.md) | The attribute of the Scroll. |

