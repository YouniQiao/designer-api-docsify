# Shape

## Shape

```TypeScript
export declare function Shape(
    value?: PixelMap, 
    content_?: CustomBuilder,
): ShapeAttribute
```

Shape is returned when the parameter is transferred.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function Shape(    value?: PixelMap,     content_?: CustomBuilder,): ShapeAttribute--><!--Device-unnamed-export declare function Shape(    value?: PixelMap,     content_?: CustomBuilder,): ShapeAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [PixelMap](../arkts-components/arkts-arkui-pixelmap-t.md) | No | A pixelMap can be drawn in the area of shape. |
| content_ | [CustomBuilder](arkts-arkui-custombuilder-t.md) | No |  |

**Return value:**

| Type | Description |
| --- | --- |
| [ShapeAttribute](arkts-arkui-shape-shapeattribute-i.md) | The attribute of the Shape. |


## Shape

```TypeScript
export declare function Shape(
    style: CustomBuilderT<ShapeAttribute>,
    content_?: CustomBuilder,
): ShapeAttribute
```

Defines Shape Component.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

**Decorator:** @Builder

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-export declare function Shape(    style: CustomBuilderT<ShapeAttribute>,    content_?: CustomBuilder,): ShapeAttribute--><!--Device-unnamed-export declare function Shape(    style: CustomBuilderT<ShapeAttribute>,    content_?: CustomBuilder,): ShapeAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| style | [CustomBuilderT](arkts-arkui-custombuildert-t.md)&lt;[ShapeAttribute](arkts-arkui-shape-shapeattribute-i.md)&gt; | Yes | the callback to set up component's attributes. |
| content_ | [CustomBuilder](arkts-arkui-custombuilder-t.md) | No | container. |

**Return value:**

| Type | Description |
| --- | --- |
| [ShapeAttribute](arkts-arkui-shape-shapeattribute-i.md) |  |

