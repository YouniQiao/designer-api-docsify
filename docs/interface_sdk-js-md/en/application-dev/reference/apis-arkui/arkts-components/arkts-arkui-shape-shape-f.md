# Shape

## Shape

```TypeScript
@ComponentBuilder
export declare function Shape(
    value?: PixelMap, 
    content_?: CustomBuilder,
): ShapeAttribute
```

Shape is returned when the parameter is transferred.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@ComponentBuilderexport declare function Shape(    value?: PixelMap,     content_?: CustomBuilder,): ShapeAttribute--><!--Device-unnamed-@ComponentBuilderexport declare function Shape(    value?: PixelMap,     content_?: CustomBuilder,): ShapeAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [PixelMap](arkts-arkui-pixelmap-t.md) | No | A pixelMap can be drawn in the area of shape. |
| content_ | [CustomBuilder](../../apis-default/arkts-apis/arkts-custombuilder-t.md) | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| [ShapeAttribute](arkts-arkui-shape-attribute.md) | The attribute of the Shape. |


## Shape

```TypeScript
@Builder
export declare function Shape(
    style: CustomBuilderT<ShapeAttribute>,
    content_?: CustomBuilder,
): ShapeAttribute
```

Defines Shape Component.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-@Builderexport declare function Shape(    style: CustomBuilderT<ShapeAttribute>,    content_?: CustomBuilder,): ShapeAttribute--><!--Device-unnamed-@Builderexport declare function Shape(    style: CustomBuilderT<ShapeAttribute>,    content_?: CustomBuilder,): ShapeAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | [CustomBuilderT](../../apis-default/arkts-apis/arkts-custombuildert-t.md)&lt;[ShapeAttribute](arkts-arkui-shape-attribute.md)&gt; | Yes | the callback to set up component's attributes. |
| content_ | [CustomBuilder](../../apis-default/arkts-apis/arkts-custombuilder-t.md) | No | container. |

**Return value:**

| Type | Description |
| --- | --- |
| [ShapeAttribute](arkts-arkui-shape-attribute.md) |  |

