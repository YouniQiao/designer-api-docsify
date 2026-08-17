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

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@ComponentBuilderexport declare function ListItemGroup(    options?: ListItemGroupOptions,     content_?: CustomBuilder,): ListItemGroupAttribute--><!--Device-unnamed-@ComponentBuilderexport declare function ListItemGroup(    options?: ListItemGroupOptions,     content_?: CustomBuilder,): ListItemGroupAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [ListItemGroupOptions](arkts-na-listitemgroup-listitemgroupoptions-i.md) | No | options |
| content_ | CustomBuilder | No | container |

**Return value:**

| Type | Description |
| --- | --- |
| ListItemGroupAttribute |  |


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

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@Builderexport declare function ListItemGroup(    style_: CustomBuilderT<ListItemGroupAttribute>,    content_?: CustomBuilder): ListItemGroupAttribute--><!--Device-unnamed-@Builderexport declare function ListItemGroup(    style_: CustomBuilderT<ListItemGroupAttribute>,    content_?: CustomBuilder): ListItemGroupAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style_ | CustomBuilderT&lt;ListItemGroupAttribute&gt; | Yes | The style to create a ListItemGroup. |
| content_ | CustomBuilder | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| ListItemGroupAttribute | The attribute of the ListItemGroup. |

