# Matrix4Transit

Matrix4Transit.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-matrix4-export interface Matrix4Transit--><!--Device-matrix4-export interface Matrix4Transit-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## combine

```TypeScript
combine(options: Matrix4Transit): Matrix4Transit
```

Matrix superposition function Which can superpose the effects of two matrices to generate a new matrix object.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Matrix4Transit-combine(options: Matrix4Transit): Matrix4Transit--><!--Device-Matrix4Transit-combine(options: Matrix4Transit): Matrix4Transit-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | Return to Matrix4Transit |

## copy

```TypeScript
copy(): Matrix4Transit
```

Copy function of Matrix, which can copy a copy of the current matrix object.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Matrix4Transit-copy(): Matrix4Transit--><!--Device-Matrix4Transit-copy(): Matrix4Transit-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | Return to Matrix4Transit |

## invert

```TypeScript
invert(): Matrix4Transit
```

The inverse function of Matrix returns an inverse matrix of the current matrix object That is, the effect is exactly the opposite.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Matrix4Transit-invert(): Matrix4Transit--><!--Device-Matrix4Transit-invert(): Matrix4Transit-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | Return to Matrix4Transit |

## rotate

```TypeScript
rotate(options: RotateOption): Matrix4Transit
```

Rotation function of the Matrix. You can add the x-axis, Y-axis, or Z-axis rotation effect to the current matrix.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Matrix4Transit-rotate(options: RotateOption): Matrix4Transit--><!--Device-Matrix4Transit-rotate(options: RotateOption): Matrix4Transit-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | Return to Matrix4Transit |

## scale

```TypeScript
scale(options: ScaleOption): Matrix4Transit
```

Scaling function of the Matrix Which can add the x-axis, Y-axis, or Z-axis scaling effect to the current matrix.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Matrix4Transit-scale(options: ScaleOption): Matrix4Transit--><!--Device-Matrix4Transit-scale(options: ScaleOption): Matrix4Transit-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | Return to Matrix4Transit |

## setPolyToPoly

```TypeScript
setPolyToPoly(options: PolyToPolyOptions): Matrix4Transit
```

Sets matrix to map src to dst.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Matrix4Transit-setPolyToPoly(options: PolyToPolyOptions): Matrix4Transit--><!--Device-Matrix4Transit-setPolyToPoly(options: PolyToPolyOptions): Matrix4Transit-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | polyToPoly options |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | Return to Matrix4Transit |

## skew

```TypeScript
skew(x: double, y: double): Matrix4Transit
```

Skew function of the Matrix, which can add the x-axis, y-axis skew effect to the current matrix. Skew function takes a generic point with coordinates (x0, y0, z0) to the point (x0 + x*y0, y0 + y*x0, z0), where x, y are fixed parameters, called the shear factors.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Matrix4Transit-skew(x: double, y: double): Matrix4Transit--><!--Device-Matrix4Transit-skew(x: double, y: double): Matrix4Transit-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| x | double | Yes | the shear factor of x-axis. |
| y | double | Yes | the shear factor of y-axis. |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | Return to Matrix4Transit |

## transformPoint

```TypeScript
transformPoint(options: [
            double,
            double
        ]): [
            double,
            double
        ]
```

Matrix coordinate point conversion function Which can apply the current transformation effect to a coordinate point.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Matrix4Transit-transformPoint(options: [            double,            double        ]): [            double,            double        ]--><!--Device-Matrix4Transit-transformPoint(options: [            double,            double        ]): [            double,            double        ]-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [             double,             double         ] | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| [             double,             double         ] | Return to Matrix4Transit |

## translate

```TypeScript
translate(options: TranslateOption): Matrix4Transit
```

Matrix translation function Which can add the x-axis, Y-axis, or Z-axis translation effect to the current matrix.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Matrix4Transit-translate(options: TranslateOption): Matrix4Transit--><!--Device-Matrix4Transit-translate(options: TranslateOption): Matrix4Transit-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes |  |

**Return value:**

| Type | Description |
| --- | --- |
| \_\_\_MD\_LINK\_USD\_0\_\_\_ | Return to Matrix4Transit |

