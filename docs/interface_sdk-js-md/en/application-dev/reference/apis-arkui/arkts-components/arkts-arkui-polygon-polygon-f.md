# Polygon

## Polygon

```TypeScript
@ComponentBuilder
export declare function Polygon(
    options?: PolygonOptions
): PolygonAttribute
```

Polygon is returned when the parameter is transferred.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Decorator:** @ComponentBuilder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@ComponentBuilderexport declare function Polygon(    options?: PolygonOptions): PolygonAttribute--><!--Device-unnamed-@ComponentBuilderexport declare function Polygon(    options?: PolygonOptions): PolygonAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [PolygonOptions](arkts-arkui-polygon-polygonoptions-i.md) | No | The options to create a Polygon. |

**Return value:**

| Type | Description |
| --- | --- |
| [PolygonAttribute](arkts-arkui-polygon-attribute.md) | The attribute of the Polygon. |


## Polygon

```TypeScript
@Builder
export declare function Polygon(
    style: CustomBuilderT<PolygonAttribute>,
): PolygonAttribute
```

Defines Polygon Component.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta since version 26.1.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@Builderexport declare function Polygon(    style: CustomBuilderT<PolygonAttribute>,): PolygonAttribute--><!--Device-unnamed-@Builderexport declare function Polygon(    style: CustomBuilderT<PolygonAttribute>,): PolygonAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | [CustomBuilderT](../../apis-default/arkts-apis/arkts-custombuildert-t.md)&lt;[PolygonAttribute](arkts-arkui-polygon-attribute.md)&gt; | Yes | the callback to set up component's attributes. |

**Return value:**

| Type | Description |
| --- | --- |
| [PolygonAttribute](arkts-arkui-polygon-attribute.md) |  |

