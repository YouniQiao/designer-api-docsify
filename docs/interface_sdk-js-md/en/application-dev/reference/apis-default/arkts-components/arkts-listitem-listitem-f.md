# ListItem

## ListItem

```TypeScript
@ComponentBuilder
export declare function ListItem(
    value?: ListItemOptions, 
    content_?: CustomBuilder,
): ListItemAttribute
```

Defines ListItem Component.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@ComponentBuilderexport declare function ListItem(    value?: ListItemOptions,     content_?: CustomBuilder,): ListItemAttribute--><!--Device-unnamed-@ComponentBuilderexport declare function ListItem(    value?: ListItemOptions,     content_?: CustomBuilder,): ListItemAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ListItemOptions](arkts-listitem-listitemoptions-i.md) | No |  |
| content_ | [CustomBuilder](../arkts-apis/arkts-custombuilder-t.md) | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| [ListItemAttribute](arkts-listitem-attribute.md) |  |


## ListItem

```TypeScript
@Builder
export declare function ListItem(
    style_: CustomBuilderT<ListItemAttribute>,
    content_?: CustomBuilder
): ListItemAttribute
```

Defines ListItem Component.

**Since:** 26.1.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@Builderexport declare function ListItem(    style_: CustomBuilderT<ListItemAttribute>,    content_?: CustomBuilder): ListItemAttribute--><!--Device-unnamed-@Builderexport declare function ListItem(    style_: CustomBuilderT<ListItemAttribute>,    content_?: CustomBuilder): ListItemAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style_ | [CustomBuilderT](../arkts-apis/arkts-custombuildert-t.md)&lt;[ListItemAttribute](arkts-listitem-attribute.md)&gt; | Yes | The style to create a ListItem. |
| content_ | [CustomBuilder](../arkts-apis/arkts-custombuilder-t.md) | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| [ListItemAttribute](arkts-listitem-attribute.md) | The attribute of the ListItem. |

