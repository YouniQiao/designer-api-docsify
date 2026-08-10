# FlowItem

## FlowItem

```TypeScript
export declare function FlowItem(
    content_?: CustomBuilder,
): FlowItemAttribute
```

创建瀑布流子组件。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function FlowItem(    content_?: CustomBuilder,): FlowItemAttribute--><!--Device-unnamed-export declare function FlowItem(    content_?: CustomBuilder,): FlowItemAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| content_ | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | No | 容器内容。 |

**Return value:**

| Type | Description |
| --- | --- |
| [FlowItemAttribute](../arkts-components/arkts-arkui-flowitem-attribute.md) |  |


## FlowItem

```TypeScript
export declare function FlowItem(
    style_: CustomBuilderT<FlowItemAttribute>,
    content_?: CustomBuilder
): FlowItemAttribute
```

定义FlowItem组件。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function FlowItem(    style_: CustomBuilderT<FlowItemAttribute>,    content_?: CustomBuilder): FlowItemAttribute--><!--Device-unnamed-export declare function FlowItem(    style_: CustomBuilderT<FlowItemAttribute>,    content_?: CustomBuilder): FlowItemAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style_ | [CustomBuilderT](../arkts-components/arkts-arkui-custombuildert-t.md)&lt;FlowItemAttribute&gt; | Yes | 用于创建FlowItem的样式 |
| content_ | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| [FlowItemAttribute](../arkts-components/arkts-arkui-flowitem-attribute.md) | FlowItem的属性。 |

