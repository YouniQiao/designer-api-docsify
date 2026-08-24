# ListItemGroup

## ListItemGroup

```TypeScript
@ComponentBuilder
export declare function ListItemGroup(
    options?: ListItemGroupOptions, 
    content_?: CustomBuilder,
): ListItemGroupAttribute
```

Defines ListItemGroup Component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Decorator:** @ComponentBuilder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@ComponentBuilderexport declare function ListItemGroup(    options?: ListItemGroupOptions,     content_?: CustomBuilder,): ListItemGroupAttribute--><!--Device-unnamed-@ComponentBuilderexport declare function ListItemGroup(    options?: ListItemGroupOptions,     content_?: CustomBuilder,): ListItemGroupAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [ListItemGroupOptions](arkts-listitemgroup-listitemgroupoptions-i.md) | No | options |
| content_ | [CustomBuilder](../arkts-apis/arkts-custombuilder-t.md) | No | container |

**Return value:**

| Type | Description |
| --- | --- |
| [ListItemGroupAttribute](arkts-listitemgroup-attribute.md) |  |


## ListItemGroup

```TypeScript
@Builder
export declare function ListItemGroup(
    style_: CustomBuilderT<ListItemGroupAttribute>,
    content_?: CustomBuilder
): ListItemGroupAttribute
```

Defines ListItemGroup Component.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta since version 26.1.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@Builderexport declare function ListItemGroup(    style_: CustomBuilderT<ListItemGroupAttribute>,    content_?: CustomBuilder): ListItemGroupAttribute--><!--Device-unnamed-@Builderexport declare function ListItemGroup(    style_: CustomBuilderT<ListItemGroupAttribute>,    content_?: CustomBuilder): ListItemGroupAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style_ | [CustomBuilderT](../arkts-apis/arkts-custombuildert-t.md)&lt;[ListItemGroupAttribute](arkts-listitemgroup-attribute.md)&gt; | Yes | The style to create a ListItemGroup. |
| content_ | [CustomBuilder](../arkts-apis/arkts-custombuilder-t.md) | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| [ListItemGroupAttribute](arkts-listitemgroup-attribute.md) | The attribute of the ListItemGroup. |

