# GridItem

## GridItem

```TypeScript
export declare function GridItem(
    value?: GridItemOptions, 
    content_?: CustomBuilder,
): GridItemAttribute
```

Defines GridItem Component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function GridItem(    value?: GridItemOptions,     content_?: CustomBuilder,): GridItemAttribute--><!--Device-unnamed-export declare function GridItem(    value?: GridItemOptions,     content_?: CustomBuilder,): GridItemAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [GridItemOptions](../arkts-components/arkts-arkui-griditemoptions-i.md) | No | options |
| content_ | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | No | container |

**Return value:**

| Type | Description |
| --- | --- |
| [GridItemAttribute](arkts-arkui-griditem-griditemattribute-i.md) |  |


## GridItem

```TypeScript
export declare function GridItem(
    style_: CustomBuilderT<GridItemAttribute>,
    content_?: CustomBuilder
): GridItemAttribute
```

Defines GridItem Component.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function GridItem(    style_: CustomBuilderT<GridItemAttribute>,    content_?: CustomBuilder): GridItemAttribute--><!--Device-unnamed-export declare function GridItem(    style_: CustomBuilderT<GridItemAttribute>,    content_?: CustomBuilder): GridItemAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style_ | [CustomBuilderT](../arkts-components/arkts-arkui-custombuildert-t.md)&lt;GridItemAttribute&gt; | Yes | The style to create a GridItem. |
| content_ | [CustomBuilder](../arkts-components/arkts-arkui-custombuilder-t.md) | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| [GridItemAttribute](arkts-arkui-griditem-griditemattribute-i.md) | The attribute of the GridItem. |

