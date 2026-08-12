# ListItemGroup

## ListItemGroup

```TypeScript
export declare function ListItemGroup(
    options?: ListItemGroupOptions, 
    content_?: CustomBuilder,
): ListItemGroupAttribute
```

Defines ListItemGroup Component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function ListItemGroup(    options?: ListItemGroupOptions,     content_?: CustomBuilder,): ListItemGroupAttribute--><!--Device-unnamed-export declare function ListItemGroup(    options?: ListItemGroupOptions,     content_?: CustomBuilder,): ListItemGroupAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [ListItemGroupOptions](arkts-arkui-listitemgroup-listitemgroupoptions-i.md) | No | options |
| content_ | [CustomBuilder](arkts-arkui-custombuilder-t.md) | No | container |

**Return value:**

| Type | Description |
| --- | --- |
| [ListItemGroupAttribute](arkts-arkui-listitemgroup-listitemgroupattribute-i.md) |  |


## ListItemGroup

```TypeScript
export declare function ListItemGroup(
    style_: CustomBuilderT<ListItemGroupAttribute>,
    content_?: CustomBuilder
): ListItemGroupAttribute
```

Defines ListItemGroup Component.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function ListItemGroup(    style_: CustomBuilderT<ListItemGroupAttribute>,    content_?: CustomBuilder): ListItemGroupAttribute--><!--Device-unnamed-export declare function ListItemGroup(    style_: CustomBuilderT<ListItemGroupAttribute>,    content_?: CustomBuilder): ListItemGroupAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style_ | [CustomBuilderT](arkts-arkui-custombuildert-t.md)&lt;[ListItemGroupAttribute](arkts-arkui-listitemgroup-listitemgroupattribute-i.md)&gt; | Yes | The style to create a ListItemGroup. |
| content_ | [CustomBuilder](arkts-arkui-custombuilder-t.md) | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| [ListItemGroupAttribute](arkts-arkui-listitemgroup-listitemgroupattribute-i.md) | The attribute of the ListItemGroup. |

