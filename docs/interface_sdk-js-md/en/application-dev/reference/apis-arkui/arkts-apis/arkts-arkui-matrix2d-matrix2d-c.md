# Matrix2D

2D transformation matrix, supporting rotation, translation, and scaling of the X-axis and Y-axis

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-unnamed-export declare class Matrix2D--><!--Device-unnamed-export declare class Matrix2D-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(unit?: LengthMetricsUnit)
```

Constructs a 2D change matrix object. The default value is the unit matrix.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Matrix2D-constructor(unit?: LengthMetricsUnit)--><!--Device-Matrix2D-constructor(unit?: LengthMetricsUnit)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| unit | [LengthMetricsUnit](arkts-arkui-graphics-lengthmetricsunit-e.md) | No | the unit mode |

## identity

```TypeScript
identity(): Matrix2D
```

Transforms the current 2D matrix back to the identity matrix (i.e., without any rotational translation scaling effect)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Matrix2D-identity(): Matrix2D--><!--Device-Matrix2D-identity(): Matrix2D-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [Matrix2D](arkts-arkui-matrix2d-c.md) |  |

## invert

```TypeScript
invert(): Matrix2D
```

Transform the current 2D matrix into an inverse matrix (that is, the transformation effect is the opposite effect of the original)

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Matrix2D-invert(): Matrix2D--><!--Device-Matrix2D-invert(): Matrix2D-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| [Matrix2D](arkts-arkui-matrix2d-c.md) |  |

## rotate

```TypeScript
rotate(degree: double, rx?: double, ry?: double): Matrix2D
```

Adds the rotation effect of the X and Y axes to the current matrix.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Matrix2D-rotate(degree: double, rx?: double, ry?: double): Matrix2D--><!--Device-Matrix2D-rotate(degree: double, rx?: double, ry?: double): Matrix2D-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| degree | double | Yes | The rotation angle, clockwise in radians. |
| rx | double | No | Rotation effect of the X-axis |
| ry | double | No | Rotation effect of the Y-axis |

**Return value:**

| Type | Description |
| --- | --- |
| [Matrix2D](arkts-arkui-matrix2d-c.md) |  |

## scale

```TypeScript
scale(sx?: double, sy?: double): Matrix2D
```

Adds the scaling effect of the X and Y axes to the current matrix.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Matrix2D-scale(sx?: double, sy?: double): Matrix2D--><!--Device-Matrix2D-scale(sx?: double, sy?: double): Matrix2D-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| sx | double | No | X-axis scaling effect |
| sy | double | No | Y-axis scaling effect |

**Return value:**

| Type | Description |
| --- | --- |
| [Matrix2D](arkts-arkui-matrix2d-c.md) |  |

## translate

```TypeScript
translate(tx?: double, ty?: double): Matrix2D
```

Adds the translation effect of the X and Y axes to the current matrix.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Matrix2D-translate(tx?: double, ty?: double): Matrix2D--><!--Device-Matrix2D-translate(tx?: double, ty?: double): Matrix2D-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| tx | double | No | X-axis translation effect |
| ty | double | No | Y-axis translation effect |

**Return value:**

| Type | Description |
| --- | --- |
| [Matrix2D](arkts-arkui-matrix2d-c.md) |  |

## rotateX

```TypeScript
set rotateX(rotateX: double | undefined)
```

Set the horizontal tilt.

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Matrix2D-set rotateX(rotateX: double | undefined)--><!--Device-Matrix2D-set rotateX(rotateX: double | undefined)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## rotateY

```TypeScript
set rotateY(rotateY: double | undefined)
```

Set the vertical tilt.

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Matrix2D-set rotateY(rotateY: double | undefined)--><!--Device-Matrix2D-set rotateY(rotateY: double | undefined)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## scaleX

```TypeScript
set scaleX(scaleX: double | undefined)
```

Set the horizontal zoom.

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Matrix2D-set scaleX(scaleX: double | undefined)--><!--Device-Matrix2D-set scaleX(scaleX: double | undefined)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## scaleY

```TypeScript
set scaleY(scaleY: double | undefined)
```

Set the vertical zoom.

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Matrix2D-set scaleY(scaleY: double | undefined)--><!--Device-Matrix2D-set scaleY(scaleY: double | undefined)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## translateX

```TypeScript
set translateX(translateX: double | undefined)
```

Set the horizontal movement.

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Matrix2D-set translateX(translateX: double | undefined)--><!--Device-Matrix2D-set translateX(translateX: double | undefined)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## translateY

```TypeScript
set translateY(translateY: double | undefined)
```

Set the vertical movement.

**Type:** double

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-Matrix2D-set translateY(translateY: double | undefined)--><!--Device-Matrix2D-set translateY(translateY: double | undefined)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

