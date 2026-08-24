# Grid

## Grid

```TypeScript
@ComponentBuilder
export declare function Grid(
    scroller?: Scroller, layoutOptions?: GridLayoutOptions,
    content_?: CustomBuilder,
): GridAttribute
```

Grid is returned when the parameter is transferred.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Decorator:** @ComponentBuilder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@ComponentBuilderexport declare function Grid(    scroller?: Scroller, layoutOptions?: GridLayoutOptions,    content_?: CustomBuilder,): GridAttribute--><!--Device-unnamed-@ComponentBuilderexport declare function Grid(    scroller?: Scroller, layoutOptions?: GridLayoutOptions,    content_?: CustomBuilder,): GridAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| scroller | [Scroller](../../apis-arkui/arkts-components/arkts-arkui-scroller-c.md) | No | Controller bound to the grid |
| layoutOptions | [GridLayoutOptions](arkts-grid-gridlayoutoptions-i.md) | No | The options to help grid layout |
| content_ | [CustomBuilder](../arkts-apis/arkts-custombuilder-t.md) | No | container |

**Return value:**

| Type | Description |
| --- | --- |
| [GridAttribute](arkts-grid-attribute.md) |  |


## Grid

```TypeScript
@Builder
export declare function Grid(
    style_: CustomBuilderT<GridAttribute>,
    content_?: CustomBuilder
): GridAttribute
```

Grid is returned when the parameter is transferred.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta since version 26.1.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@Builderexport declare function Grid(    style_: CustomBuilderT<GridAttribute>,    content_?: CustomBuilder): GridAttribute--><!--Device-unnamed-@Builderexport declare function Grid(    style_: CustomBuilderT<GridAttribute>,    content_?: CustomBuilder): GridAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style_ | [CustomBuilderT](../arkts-apis/arkts-custombuildert-t.md)&lt;[GridAttribute](arkts-grid-attribute.md)&gt; | Yes | The style to create a Grid. |
| content_ | [CustomBuilder](../arkts-apis/arkts-custombuilder-t.md) | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| [GridAttribute](arkts-grid-attribute.md) | The attribute of the Grid. |

