# Shape properties/events

In addition to the [universal attributes](arkts-arkui-commonmethod-c.md), the following attributes are supported.

**Inheritance/Implementation:** ShapeAttribute extends CommonMethod<ShapeAttribute>

**Since:** 7

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { RectShape, CircleShape, EllipseShape, PathShape } from '@ohos.arkui.@kit.ArkUI';
```

## antiAlias

```TypeScript
antiAlias(value: boolean)
```

Sets whether to enable anti-aliasing. This attribute can be dynamically set using attributeModifier.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | boolean | Yes | Whether to enable anti-aliasing.   **true**: enable anti-aliasing; **false**: disable anti-aliasing.Default value: **true**Invalid values **undefined** and **null** are treated as **false**. |

## fill

```TypeScript
fill(value: ResourceColor)
```

Sets the color of the fill area. This attribute can be dynamically set using attributeModifier. Invalid values are treated as the default value. If this attribute and the universal attribute **foregroundColor** are both set, whichever is set later takes effect.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md) | Yes | Color of the fill area.Default value: [Color](../arkts-apis/arkts-arkui-color-e.md).Black The **undefined**, **null**, **NaN**, and **Infinity** values are invalid and treated as the default value. |

## fillOpacity

```TypeScript
fillOpacity(value: number | string | Resource)
```

Sets the opacity of the fill area. This attribute can be dynamically set using attributeModifier.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | number \| string \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) | Yes | Opacity of the fill area.   **NOTE：**For the number type, the value range is [0.0, 1.0]. A value less than 0.0 is treated as **0.0**. A value greater than 1.0 is treated as **1.0**. Any other invalid value is treated as **1.0**.For the string type, the value is a character string of the number type. The value range is the same as that of the number type.For the Resource type, the value is a character string from the system resource or application resource. The value range is the same as that of the number type.Default value: **1.0 |

## mesh

```TypeScript
mesh(value: Array<any>, column: number, row: number)
```

Sets the mesh effect. An image is divided into (row + 1) × (column + 1) meshes. The coordinates of each mesh intersection point are stored in the array. (Every two elements indicate the x and y coordinates of an intersection point.) The mesh vertex position is relocated based on the coordinates in the array value to implement partial image distortion. This attribute can be dynamically set using attributeModifier.

> **NOTE：**
> 
> **mesh** takes effect only when a **pixelMap** object is passed to the shape, and the effect applies to the
> passed **pixelMap** object. It produces the same result as
> [drawPixelMapMesh&lt;sup&gt;12+&lt;/sup&gt;](../../apis-arkgraphics2d/arkts-apis/arkts-arkgraphics2d-drawing-canvas-c.md#drawpixelmapmesh) in the
> [drawing module](../../apis-arkgraphics2d/arkts-apis/arkts-graphics-drawing.md). It is recommended that you use
> **drawPixelMapMesh**.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | Array & lt;any & gt; | Yes | Array with a length of (row + 1) × (column + 1) × 2, which records the position of each vertex of the distorted bitmap.Invalid values **undefined** and **null** are treated as an empty array. If the value is set to an empty array, the values of **column** and **row** are handled as **0**, and the value is handled as an empty array. |
| column | number | Yes | Number of mesh matrix columns.If the value is **undefined**, **null**, **NaN**, or **Infinity**, the values of **column** and **row** are treated as **0**, and the value of **value** is treated as an empty array. |
| row | number | Yes | Number of mesh matrix rows.If the value is **undefined**, **null**, **NaN**, or **Infinity**, the values of **column** and **row** are treated as **0**, and the value of **value** is treated as an empty array. |

## stroke

```TypeScript
stroke(value: ResourceColor)
```

Sets the stroke color. This attribute can be dynamically set using attributeModifier. If this attribute is not set, the default stroke opacity is **0**, meaning no stroke is displayed.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ResourceColor](../arkts-apis/arkts-arkui-resourcecolor-t.md) | Yes | Stroke color.Default value: [Color](../arkts-apis/arkts-arkui-color-e.md).Transparent Invalid values **undefined** and **null** values are treated as the default value, and invalid values **NaN** and **Infinity** are treated as [Color](../arkts-apis/arkts-arkui-color-e.md).Black. |

## strokeDashArray

```TypeScript
strokeDashArray(value: Array<any>)
```

Sets the stroke dashes. This attribute can be dynamically set using attributeModifier. The value must be greater than or equal to 0. Invalid values are treated as the default value.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | Array & lt;any & gt; | Yes | Array defining the dash pattern for the shape outline. Elements alternate between dash length and gap length.Default value: **[]** (empty array)Default unit: vp The **undefined** and **null** values are invalid and treated as the default value.   **NOTE：**Empty array: solid line Even- numbered array: Elements cycle sequentially, for example, [a, b, c, d] represents: dash a - & gt; gap b - & gt; dash c - & gt; gap d - & gt; dash a - & gt; ...Odd-numbered array: Elements are duplicated to create an even-numbered array, for example, [a, b, c] becomes [a, b, c, a, b, c], representing: dash a - & gt; gap b - & gt; dash c - & gt; gap a - & gt; dash b - & gt; gap c - & gt; dash a - & gt; ... |

## strokeDashOffset

```TypeScript
strokeDashOffset(value: Length)
```

Sets the offset of the start point for drawing the stroke. This attribute can be dynamically set using attributeModifier. Invalid values are treated as the default value.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [Length](../arkts-apis/arkts-arkui-length-t.md) | Yes | Offset of the start point for drawing the stroke.Default value: **0**Default unit: vp Invalid values **undefined** and **null** are treated as the default value. If set to **NaN** or **Infinity**, **strokeDashArray** has no effect.<br>**Since:** 20 |

## strokeLineCap

```TypeScript
strokeLineCap(value: LineCapStyle)
```

Sets the cap style of the stroke. This attribute can be dynamically set using attributeModifier.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [LineCapStyle](../arkts-apis/arkts-arkui-linecapstyle-e.md) | Yes | Cap style of the stroke.Default value: **LineCapStyle.Butt**The **undefined**, **null**, **NaN**, and **Infinity** values are invalid and treated as the default value. |

## strokeLineJoin

```TypeScript
strokeLineJoin(value: LineJoinStyle)
```

Sets the join style of the stroke. This attribute can be dynamically set using attributeModifier.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [LineJoinStyle](../arkts-apis/arkts-arkui-linejoinstyle-e.md) | Yes | Join style of the stroke.Default value: **LineJoinStyle.Miter**The **undefined**, **null**, **NaN**, and **Infinity** values are invalid and treated as the default value. |

## strokeMiterLimit

```TypeScript
strokeMiterLimit(value: Length)
```

Sets the limit on the ratio of the miter length to the value of stroke width used to draw a miter join. This attribute can be dynamically set using attributeModifier. The miter length indicates the distance from the outer tip to the inner corner of the miter. The border width is the value of **strokeWidth**. This attribute works only when **strokeLineJoin** is set to **LineJoinStyle.Miter**.The value must be greater than or equal to 1.0. If the value is in the [0, 1) range, the value **1.0** will be used. In other cases, the default value will be used.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [Length](../arkts-apis/arkts-arkui-length-t.md) | Yes | Limit on the ratio of the miter length to the value of **strokeWidth** used to draw a miter join.Default value: **4**The **undefined**, **null**, and **NaN** values are invalid and treated as the default value. If set to **Infinity**, **stroke** has no effect.<br>**Since:** 20 |

## strokeOpacity

```TypeScript
strokeOpacity(value: number | string | Resource)
```

Sets the stroke opacity. This attribute can be dynamically set using attributeModifier. The value range is [0.0, 1.0]. If the set value is less than 0.0, **0.0** will be used. If the set value is greater than 1.0, **1.0** will be used.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | number \| string \| [Resource](../../apis-localization-kit/arkts-apis/arkts-localization-resource-resource-i.md) | Yes | Stroke opacity.Default value: opacity set by the [stroke](../../../reference/apis-arkui/arkui-ts/ts-drawing-components-shape.md#stroke) API Invalid value **NaN** is treated as **0.0**, while invalid values **undefined**, **null**, and **Infinity** are treated as **1.0**. |

## strokeWidth

```TypeScript
strokeWidth(value: Length)
```

Sets the stroke width. This attribute can be dynamically set using attributeModifier. If this attribute is of the string type, percentage values are not supported and will be treated as 1 px.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [Length](../arkts-apis/arkts-arkui-length-t.md) | Yes | Stroke width. The value must be greater than or equal to 0.Default value: **1**Default unit: vp Invalid values **undefined**, **null**, and **NaN** are treated as the default value, and invalid value **Infinity** is treated as **0**.<br>**Since:** 20 |

## viewPort

```TypeScript
viewPort(value: ViewportRect)
```

Sets the viewport of the shape.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | [ViewportRect](arkts-arkui-viewportrect-i.md) | Yes | Options of the viewport.Default value: **{}**The **undefined** and **null** values are invalid and treated as the default value.<br>**Since:** 18 |
