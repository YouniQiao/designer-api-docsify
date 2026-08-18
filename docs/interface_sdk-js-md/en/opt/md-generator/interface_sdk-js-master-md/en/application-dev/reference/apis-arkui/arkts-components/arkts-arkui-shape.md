# Shape

The **Shape** component is the parent component of the drawing components. The attributes described in this topic are universal attributes supported by all the drawing components. 1. Drawing components use **Shape** as their parent to implement the effect similar to SVG. 2. Drawing components can be used independently to draw specified shapes. > **NOTE** > > This component supports dynamic constructor parameter updates using the > updateConstructorParams API of the > AttributeUpdater class since API version 20. > > **Child Components** > > The following child components are supported: Rect, Path, Circle, [Ellipse](arkts-arkui-ellipseoptions-i.md#ellipse), [Polyline](arkts-arkui-polylineoptions-i.md#polyline), [Polygon](arkts-arkui-polygonoptions-i.md#polygon), Image, Text, Column, Row, and **Shape**.

## Shape

```TypeScript
Shape(value?: PixelMap)
```

Use the new function to create Shape.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ShapeInterface-new (value?: PixelMap): ShapeAttribute--><!--Device-ShapeInterface-new (value?: PixelMap): ShapeAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [PixelMap](../../apis-image-kit/arkts-apis/arkts-image-image-pixelmap-i.md) | No |

## Shape

```TypeScript
Shape(value: PixelMap)
```

Since API version 9, this API is supported in ArkTS widgets, except that **PixelMap** objects are not supported.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ShapeInterface-(value: PixelMap): ShapeAttribute--><!--Device-ShapeInterface-(value: PixelMap): ShapeAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | [PixelMap](../../apis-image-kit/arkts-apis/arkts-image-image-pixelmap-i.md) | Yes |

## Shape

```TypeScript
Shape()
```

Called when a component is drawn.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

<!--Device-ShapeInterface-(): ShapeAttribute--><!--Device-ShapeInterface-(): ShapeAttribute-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Summary

- [ViewportRect](arkts-arkui-viewportrect-i.md)
