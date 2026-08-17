# GridRow

## GridRow

```TypeScript
@ComponentBuilder
export declare function GridRow(
    option?: GridRowOptions, 
    content_?: CustomBuilder,
): GridRowAttribute
```

Defines GridRow Component.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@ComponentBuilderexport declare function GridRow(    option?: GridRowOptions,     content_?: CustomBuilder,): GridRowAttribute--><!--Device-unnamed-@ComponentBuilderexport declare function GridRow(    option?: GridRowOptions,     content_?: CustomBuilder,): GridRowAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| option | [GridRowOptions](arkts-arkui-gridrow-gridrowoptions-i.md) | No | GridRow options. |
| content_ | CustomBuilder | No | container |

**Return value:**

| Type | Description |
| --- | --- |
| GridRowAttribute |  |


## GridRow

```TypeScript
@Builder
export declare function GridRow(
    style: CustomBuilderT<GridRowAttribute>,
    content_?: CustomBuilder,
): GridRowAttribute
```

Defines GridRow Component.

**Since:** 26.1.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@Builderexport declare function GridRow(    style: CustomBuilderT<GridRowAttribute>,    content_?: CustomBuilder,): GridRowAttribute--><!--Device-unnamed-@Builderexport declare function GridRow(    style: CustomBuilderT<GridRowAttribute>,    content_?: CustomBuilder,): GridRowAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | CustomBuilderT&lt;GridRowAttribute&gt; | Yes | the callback to set up component's attributes. |
| content_ | CustomBuilder | No | container. |

**Return value:**

| Type | Description |
| --- | --- |
| GridRowAttribute |  |

