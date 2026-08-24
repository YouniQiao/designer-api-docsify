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

**ArkTS mode:** ArkTS-Sta since version 23.

**Decorator:** @ComponentBuilder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@ComponentBuilderexport declare function GridRow(    option?: GridRowOptions,     content_?: CustomBuilder,): GridRowAttribute--><!--Device-unnamed-@ComponentBuilderexport declare function GridRow(    option?: GridRowOptions,     content_?: CustomBuilder,): GridRowAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| option | [GridRowOptions](arkts-arkui-gridrow-gridrowoptions-i.md) | No | GridRow options. |
| content_ | [CustomBuilder](../../apis-default/arkts-apis/arkts-custombuilder-t.md) | No | container |

**Return value:**

| Type | Description |
| --- | --- |
| [GridRowAttribute](arkts-arkui-gridrow-attribute.md) |  |


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

**ArkTS mode:** ArkTS-Sta since version 26.1.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@Builderexport declare function GridRow(    style: CustomBuilderT<GridRowAttribute>,    content_?: CustomBuilder,): GridRowAttribute--><!--Device-unnamed-@Builderexport declare function GridRow(    style: CustomBuilderT<GridRowAttribute>,    content_?: CustomBuilder,): GridRowAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | [CustomBuilderT](../../apis-default/arkts-apis/arkts-custombuildert-t.md)&lt;[GridRowAttribute](arkts-arkui-gridrow-attribute.md)&gt; | Yes | the callback to set up component's attributes. |
| content_ | [CustomBuilder](../../apis-default/arkts-apis/arkts-custombuilder-t.md) | No | container. |

**Return value:**

| Type | Description |
| --- | --- |
| [GridRowAttribute](arkts-arkui-gridrow-attribute.md) |  |

