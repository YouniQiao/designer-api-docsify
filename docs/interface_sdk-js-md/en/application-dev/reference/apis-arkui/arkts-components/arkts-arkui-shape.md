# Shape

The **Shape** component is the parent component of the drawing components. The attributes described in this topic are universal attributes supported by all the drawing components.
1. Drawing components use **Shape** as their parent to implement the effect similar to SVG.
2. Drawing components can be used independently to draw specified shapes.
> **NOTE** > > This component supports dynamic constructor parameter updates using the > [updateConstructorParams](../../../reference/apis-arkui/js-apis-arkui-AttributeUpdater.md#properties) API of the > [AttributeUpdater](../../../reference/apis-arkui/js-apis-arkui-AttributeUpdater.md) class since API version 20. > > **Child Components** > > The following child components are supported: Rect, Path, Circle, Ellipse, Polyline, Polygon, Image, Text, Column, Row, and **Shape**.

## Shape

```TypeScript
Shape(value?: PixelMap)
```

Use the new function to create Shape.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [PixelMap](../../apis-image-kit/arkts-apis/arkts-image-image-pixelmap-i.md) | No |  |

## Shape

```TypeScript
Shape(value: PixelMap)
```

Since API version 9, this API is supported in ArkTS widgets, except that **PixelMap** objects are not supported.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [PixelMap](../../apis-image-kit/arkts-apis/arkts-image-image-pixelmap-i.md) | Yes | Drawing target. You can draw a shape in a specified **PixelMap** object. If this parameter is not set, the shape is drawn in the current drawing target by default. The **undefined** and **null** values are treated as invalid and will not take effect. |

## Shape

```TypeScript
Shape()
```

Called when a component is drawn.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Summary

### Interfaces

| Name | Description |
| --- | --- |
