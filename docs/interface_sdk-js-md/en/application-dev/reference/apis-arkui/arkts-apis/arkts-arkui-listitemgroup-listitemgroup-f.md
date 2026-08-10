# ListItemGroup

## ListItemGroup

```TypeScript
export declare function ListItemGroup(
    options?: ListItemGroupOptions, 
    content_?: CustomBuilder,
): ListItemGroupAttribute
```

创建ListItemGroup组件。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function ListItemGroup(    options?: ListItemGroupOptions,     content_?: CustomBuilder,): ListItemGroupAttribute--><!--Device-unnamed-export declare function ListItemGroup(    options?: ListItemGroupOptions,     content_?: CustomBuilder,): ListItemGroupAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [ListItemGroupOptions](arkts-arkui-listitemgroup-listitemgroupoptions-i.md) | No |  |
| content_ | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | No | 容器内容。 |

**Return value:**

| Type | Description |
| --- | --- |
| [ListItemGroupAttribute](../arkts-components/arkts-arkui-listitemgroup-attribute.md) |  |


## ListItemGroup

```TypeScript
export declare function ListItemGroup(
    style_: CustomBuilderT<ListItemGroupAttribute>,
    content_?: CustomBuilder
): ListItemGroupAttribute
```

定义ListItemGroup组件。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Sta only, since version 26.0.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function ListItemGroup(    style_: CustomBuilderT<ListItemGroupAttribute>,    content_?: CustomBuilder): ListItemGroupAttribute--><!--Device-unnamed-export declare function ListItemGroup(    style_: CustomBuilderT<ListItemGroupAttribute>,    content_?: CustomBuilder): ListItemGroupAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style_ | [CustomBuilderT](../arkts-components/arkts-arkui-custombuildert-t.md)&lt;ListItemGroupAttribute&gt; | Yes | 创建ListItemGroup的样式 |
| content_ | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| [ListItemGroupAttribute](../arkts-components/arkts-arkui-listitemgroup-attribute.md) | ListItemGroup的属性。 |

