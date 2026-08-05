# LineAttribute

Provides attribute for Line.

**Inheritance/Implementation:** LineAttribute extends [CommonShapeMethod](../arkts-arkui-arkui-shape-commonshapemethod-c.md)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare interface LineAttribute extends CommonShapeMethod--><!--Device-unnamed-export declare interface LineAttribute extends CommonShapeMethod-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## attributeModifier

```TypeScript
default attributeModifier(modifier: AttributeModifier<LineAttribute> | AttributeModifier<CommonMethod> | undefined): this
```

Call attributeModifier.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LineAttribute-default attributeModifier(modifier: AttributeModifier<LineAttribute> | AttributeModifier<CommonMethod> | undefined): this--><!--Device-LineAttribute-default attributeModifier(modifier: AttributeModifier<LineAttribute> | AttributeModifier<CommonMethod> | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| modifier | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;\_\_\_MD\_LINK\_USD\_1\_\_\_&gt; \| AttributeModifier&lt;CommonMethod&gt; \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## endPoint

```TypeScript
default endPoint(value: ShapePoint | undefined): this
```

Line end coordinates (relative coordinates).

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LineAttribute-default endPoint(value: ShapePoint | undefined): this--><!--Device-LineAttribute-default endPoint(value: ShapePoint | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | \_\_\_MD\_LINK\_USD\_0\_\_\_ \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

## setLineOptions

```TypeScript
default setLineOptions(options?: LineOptions): this
```

Set Line options.

**Since:** 26.1.0

**ArkTS mode:** ArkTS-Sta only, since version 26.1.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LineAttribute-default setLineOptions(options?: LineOptions): this--><!--Device-LineAttribute-default setLineOptions(options?: LineOptions): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | Line constructor options. |

**Return value:**

| Type | Description |
| --- | --- |
| this | Returns the instance of the LineAttribute. |

## startPoint

```TypeScript
default startPoint(value: ShapePoint | undefined): this
```

Coordinate of the start point of the line (relative coordinate).

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-LineAttribute-default startPoint(value: ShapePoint | undefined): this--><!--Device-LineAttribute-default startPoint(value: ShapePoint | undefined): this-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| value | \_\_\_MD\_LINK\_USD\_0\_\_\_ \| undefined | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| this |  |

