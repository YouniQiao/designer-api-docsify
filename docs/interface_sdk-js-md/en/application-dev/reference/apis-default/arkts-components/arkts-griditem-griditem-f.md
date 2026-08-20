# GridItem

## GridItem

```TypeScript
@ComponentBuilder
export declare function GridItem(
    value?: GridItemOptions, 
    content_?: CustomBuilder,
): GridItemAttribute
```

Defines GridItem Component.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@ComponentBuilderexport declare function GridItem(    value?: GridItemOptions,     content_?: CustomBuilder,): GridItemAttribute--><!--Device-unnamed-@ComponentBuilderexport declare function GridItem(    value?: GridItemOptions,     content_?: CustomBuilder,): GridItemAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [GridItemOptions](arkts-griditem-griditemoptions-i.md) | No | options |
| content_ | [CustomBuilder](../arkts-apis/arkts-custombuilder-t.md) | No | container |

**Return value:**

| Type | Description |
| --- | --- |
| [GridItemAttribute](arkts-griditem-attribute.md) |  |


## GridItem

```TypeScript
@Builder
export declare function GridItem(
    style_: CustomBuilderT<GridItemAttribute>,
    content_?: CustomBuilder
): GridItemAttribute
```

Defines GridItem Component.

**Since:** 26.1.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@Builderexport declare function GridItem(    style_: CustomBuilderT<GridItemAttribute>,    content_?: CustomBuilder): GridItemAttribute--><!--Device-unnamed-@Builderexport declare function GridItem(    style_: CustomBuilderT<GridItemAttribute>,    content_?: CustomBuilder): GridItemAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style_ | [CustomBuilderT](../arkts-apis/arkts-custombuildert-t.md)&lt;[GridItemAttribute](arkts-griditem-attribute.md)&gt; | Yes | The style to create a GridItem. |
| content_ | [CustomBuilder](../arkts-apis/arkts-custombuilder-t.md) | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| [GridItemAttribute](arkts-griditem-attribute.md) | The attribute of the GridItem. |

