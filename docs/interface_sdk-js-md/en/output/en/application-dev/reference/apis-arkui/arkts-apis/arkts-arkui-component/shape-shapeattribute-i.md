# ShapeAttribute

Provides attribute for Shape.

**Inheritance/Implementation:** ShapeAttribute extends [CommonMethod](../../../apis-na/arkts-apis/arkts-na-component/common-commonmethod-i.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface ShapeAttribute extends CommonMethod--><!--Device-unnamed-export declare interface ShapeAttribute extends CommonMethod-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## antiAlias

```TypeScript
default antiAlias(value: boolean | undefined): this
```

Called when setting whether anti aliasing is on.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ShapeAttribute-default antiAlias(value: boolean | undefined): this--><!--Device-ShapeAttribute-default antiAlias(value: boolean | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | boolean \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## attributeModifier

```TypeScript
default attributeModifier(modifier: AttributeModifier<ShapeAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

Call attributeModifier.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ShapeAttribute-default attributeModifier(modifier: AttributeModifier<ShapeAttribute> | AttributeModifier<CommonMethod> | undefined): this--><!--Device-ShapeAttribute-default attributeModifier(modifier: AttributeModifier<ShapeAttribute> | AttributeModifier<CommonMethod> | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| modifier | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;\_\_\_MD\_LINK\_USD\_1\_\_\_&gt; \| AttributeModifier&lt;CommonMethod&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## fill

```TypeScript
default fill(value: ResourceColor | undefined): this
```

Called when the fill color is set.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ShapeAttribute-default fill(value: ResourceColor | undefined): this--><!--Device-ShapeAttribute-default fill(value: ResourceColor | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | \_\_\_MD\_LINK\_USD\_0\_\_\_ \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## fillOpacity

```TypeScript
default fillOpacity(value: double | string | Resource | undefined): this
```

Called when the transparency of the border is set.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ShapeAttribute-default fillOpacity(value: double | string | Resource | undefined): this--><!--Device-ShapeAttribute-default fillOpacity(value: double | string | Resource | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | double \| string \| Resource \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## mesh

```TypeScript
default mesh(value: Array<double> | undefined, column: int | undefined, row: int | undefined): this
```

Called when shape mesh.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ShapeAttribute-default mesh(value: Array<double> | undefined, column: int | undefined, row: int | undefined): this--><!--Device-ShapeAttribute-default mesh(value: Array<double> | undefined, column: int | undefined, row: int | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | Array&lt;double&gt; \| undefined | Yes |  |
| column | int \| undefined | Yes |  |
| row | int \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## setShapeOptions

```TypeScript
default setShapeOptions(value?: PixelMap): this
```

Set Shape options.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ShapeAttribute-default setShapeOptions(value?: PixelMap): this--><!--Device-ShapeAttribute-default setShapeOptions(value?: PixelMap): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | Shape constructor options. |

**Return value:**

| Type | Description |
| --- | --- |
| this | Returns the instance of the ShapeAttribute. |

## stroke

```TypeScript
default stroke(value: ResourceColor | undefined): this
```

Called when the border color is set.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ShapeAttribute-default stroke(value: ResourceColor | undefined): this--><!--Device-ShapeAttribute-default stroke(value: ResourceColor | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | \_\_\_MD\_LINK\_USD\_0\_\_\_ \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## strokeDashArray

```TypeScript
default strokeDashArray(value: Array<Length> | undefined): this
```

Called when the gap of the border is set.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ShapeAttribute-default strokeDashArray(value: Array<Length> | undefined): this--><!--Device-ShapeAttribute-default strokeDashArray(value: Array<Length> | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | Array&lt;\_\_\_MD\_LINK\_USD\_0\_\_\_&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## strokeDashOffset

```TypeScript
default strokeDashOffset(value: Length | undefined): this
```

Called when the offset of the starting point of border drawing is set.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ShapeAttribute-default strokeDashOffset(value: Length | undefined): this--><!--Device-ShapeAttribute-default strokeDashOffset(value: Length | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | \_\_\_MD\_LINK\_USD\_0\_\_\_ \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## strokeLineCap

```TypeScript
default strokeLineCap(value: LineCapStyle | undefined): this
```

Called when the path endpoint drawing style is set.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ShapeAttribute-default strokeLineCap(value: LineCapStyle | undefined): this--><!--Device-ShapeAttribute-default strokeLineCap(value: LineCapStyle | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | \_\_\_MD\_LINK\_USD\_0\_\_\_ \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## strokeLineJoin

```TypeScript
default strokeLineJoin(value: LineJoinStyle | undefined): this
```

Called when the border corner drawing style is set.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ShapeAttribute-default strokeLineJoin(value: LineJoinStyle | undefined): this--><!--Device-ShapeAttribute-default strokeLineJoin(value: LineJoinStyle | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | \_\_\_MD\_LINK\_USD\_0\_\_\_ \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## strokeMiterLimit

```TypeScript
default strokeMiterLimit(value: Length | undefined): this
```

Called when the limit value for drawing acute angles as oblique angles is set.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ShapeAttribute-default strokeMiterLimit(value: Length | undefined): this--><!--Device-ShapeAttribute-default strokeMiterLimit(value: Length | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | \_\_\_MD\_LINK\_USD\_0\_\_\_ \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## strokeOpacity

```TypeScript
default strokeOpacity(value: double | string | Resource | undefined): this
```

Called when the opacity of the border is set.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ShapeAttribute-default strokeOpacity(value: double | string | Resource | undefined): this--><!--Device-ShapeAttribute-default strokeOpacity(value: double | string | Resource | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | double \| string \| Resource \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## strokeWidth

```TypeScript
default strokeWidth(value: Length | undefined): this
```

Called when the width of the border is set.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ShapeAttribute-default strokeWidth(value: Length | undefined): this--><!--Device-ShapeAttribute-default strokeWidth(value: Length | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | \_\_\_MD\_LINK\_USD\_0\_\_\_ \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## viewPort

```TypeScript
default viewPort(value: ViewportRect | undefined): this
```

Viewport of shape

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-ShapeAttribute-default viewPort(value: ViewportRect | undefined): this--><!--Device-ShapeAttribute-default viewPort(value: ViewportRect | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | \_\_\_MD\_LINK\_USD\_0\_\_\_ \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

