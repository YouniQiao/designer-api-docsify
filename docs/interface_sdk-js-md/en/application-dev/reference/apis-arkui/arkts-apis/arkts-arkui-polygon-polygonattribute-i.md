# PolygonAttribute

Provides attribute for Polygon.

**Inheritance/Implementation:** PolygonAttribute extends [CommonShapeMethod](CommonShapeMethod)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface PolygonAttribute extends CommonShapeMethod--><!--Device-unnamed-export declare interface PolygonAttribute extends CommonShapeMethod-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
default attributeModifier(modifier: AttributeModifier<PolygonAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

Call attributeModifier.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PolygonAttribute-default attributeModifier(modifier: AttributeModifier<PolygonAttribute> | AttributeModifier<CommonMethod> | undefined): this--><!--Device-PolygonAttribute-default attributeModifier(modifier: AttributeModifier<PolygonAttribute> | AttributeModifier<CommonMethod> | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| modifier | [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[PolygonAttribute](arkts-arkui-polygon-polygonattribute-i.md)&gt; \| [AttributeModifier](../arkts-components/arkts-arkui-attributemodifier-i.md)&lt;[CommonMethod](../arkts-components/arkts-arkui-commonmethod-c.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## points

```TypeScript
default points(value: Array<ShapePoint> | undefined): this
```

Called when the vertex coordinate list of a polygon is set.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PolygonAttribute-default points(value: Array<ShapePoint> | undefined): this--><!--Device-PolygonAttribute-default points(value: Array<ShapePoint> | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | Array&lt;[ShapePoint](arkts-arkui-shapepoint-t.md)&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## setPolygonOptions

```TypeScript
default setPolygonOptions(options?: PolygonOptions): this
```

Set Polygon options.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-PolygonAttribute-default setPolygonOptions(options?: PolygonOptions): this--><!--Device-PolygonAttribute-default setPolygonOptions(options?: PolygonOptions): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [PolygonOptions](arkts-arkui-polygon-polygonoptions-i.md) | No | Polygon constructor options. |

**Return value:**

| Type | Description |
| --- | --- |
| this | Returns the instance of the PolygonAttribute. |

