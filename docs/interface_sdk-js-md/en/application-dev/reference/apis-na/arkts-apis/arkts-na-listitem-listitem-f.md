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

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@ComponentBuilderexport declare function ListItem(    value?: ListItemOptions,     content_?: CustomBuilder,): ListItemAttribute--><!--Device-unnamed-@ComponentBuilderexport declare function ListItem(    value?: ListItemOptions,     content_?: CustomBuilder,): ListItemAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ListItemOptions](arkts-na-listitem-listitemoptions-i.md) | No |  |
| content_ | CustomBuilder | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| ListItemAttribute |  |


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

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@Builderexport declare function ListItem(    style_: CustomBuilderT<ListItemAttribute>,    content_?: CustomBuilder): ListItemAttribute--><!--Device-unnamed-@Builderexport declare function ListItem(    style_: CustomBuilderT<ListItemAttribute>,    content_?: CustomBuilder): ListItemAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style_ | CustomBuilderT&lt;ListItemAttribute&gt; | Yes | The style to create a ListItem. |
| content_ | CustomBuilder | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| ListItemAttribute | The attribute of the ListItem. |

