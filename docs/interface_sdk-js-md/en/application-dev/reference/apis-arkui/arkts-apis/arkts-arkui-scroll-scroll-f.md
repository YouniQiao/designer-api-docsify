# Scroll

## Scroll

```TypeScript
export declare function Scroll(
    scroller?: Scroller, 
    content_?: CustomBuilder,
): ScrollAttribute
```

创建Scroll滚动容器。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function Scroll(    scroller?: Scroller,     content_?: CustomBuilder,): ScrollAttribute--><!--Device-unnamed-export declare function Scroll(    scroller?: Scroller,     content_?: CustomBuilder,): ScrollAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| scroller | [Scroller](arkts-arkui-scroll-scroller-c.md) | No |  |
| content_ | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | No | 子组件。 |

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

定义滚动组件。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function Scroll(    style_: CustomBuilderT<ScrollAttribute>,     content_?: CustomBuilder): ScrollAttribute--><!--Device-unnamed-export declare function Scroll(    style_: CustomBuilderT<ScrollAttribute>,     content_?: CustomBuilder): ScrollAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style_ | [CustomBuilderT](../arkts-components/arkts-arkui-custombuildert-t.md)&lt;ScrollAttribute&gt; | Yes | 创建滚动的样式 |
| content_ | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| [ScrollAttribute](arkts-arkui-scroll-scrollattribute-i.md) | Scroll的属性。 |

