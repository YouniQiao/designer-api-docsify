# GridCol

## GridCol

```TypeScript
export declare function GridCol(
    option?: GridColOptions, 
    content_?: CustomBuilder,
): GridColAttribute
```

Defines GridCol Component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function GridCol(    option?: GridColOptions,     content_?: CustomBuilder,): GridColAttribute--><!--Device-unnamed-export declare function GridCol(    option?: GridColOptions,     content_?: CustomBuilder,): GridColAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| option | [GridColOptions](arkts-arkui-gridcol-gridcoloptions-i.md) | No | GridCol options. |
| content_ | [CustomBuilder](arkts-arkui-custombuilder-t.md) | No | container |

**Return value:**

| Type | Description |
| --- | --- |
| [GridColAttribute](arkts-arkui-gridcol-gridcolattribute-i.md) |  |


## GridCol

```TypeScript
export declare function GridCol(
    style: CustomBuilderT<GridColAttribute>,
    content_?: CustomBuilder,
): GridColAttribute
```

Defines GridCol Component.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function GridCol(    style: CustomBuilderT<GridColAttribute>,    content_?: CustomBuilder,): GridColAttribute--><!--Device-unnamed-export declare function GridCol(    style: CustomBuilderT<GridColAttribute>,    content_?: CustomBuilder,): GridColAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | [CustomBuilderT](arkts-arkui-custombuildert-t.md)&lt;[GridColAttribute](arkts-arkui-gridcol-gridcolattribute-i.md)&gt; | Yes | the callback to set up component's attributes. |
| content_ | [CustomBuilder](arkts-arkui-custombuilder-t.md) | No | container. |

**Return value:**

| Type | Description |
| --- | --- |
| [GridColAttribute](arkts-arkui-gridcol-gridcolattribute-i.md) |  |

