# GridCol

## GridCol

```TypeScript
@ComponentBuilder
export declare function GridCol(
    option?: GridColOptions, 
    content_?: CustomBuilder,
): GridColAttribute
```

Defines GridCol Component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@ComponentBuilderexport declare function GridCol(    option?: GridColOptions,     content_?: CustomBuilder,): GridColAttribute--><!--Device-unnamed-@ComponentBuilderexport declare function GridCol(    option?: GridColOptions,     content_?: CustomBuilder,): GridColAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| option | [GridColOptions](arkts-arkui-gridcol-gridcoloptions-i.md) | No | GridCol options. |
| content_ | CustomBuilder | No | container |

**Return value:**

| Type | Description |
| --- | --- |
| GridColAttribute |  |


## GridCol

```TypeScript
@Builder
export declare function GridCol(
    style: CustomBuilderT<GridColAttribute>,
    content_?: CustomBuilder,
): GridColAttribute
```

Defines GridCol Component.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@Builderexport declare function GridCol(    style: CustomBuilderT<GridColAttribute>,    content_?: CustomBuilder,): GridColAttribute--><!--Device-unnamed-@Builderexport declare function GridCol(    style: CustomBuilderT<GridColAttribute>,    content_?: CustomBuilder,): GridColAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | CustomBuilderT&lt;GridColAttribute&gt; | Yes | the callback to set up component's attributes. |
| content_ | CustomBuilder | No | container. |

**Return value:**

| Type | Description |
| --- | --- |
| GridColAttribute |  |

