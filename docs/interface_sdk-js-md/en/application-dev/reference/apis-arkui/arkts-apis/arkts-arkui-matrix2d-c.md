# Matrix2D

**Matrix2D** allows you to perform matrix transformation, such as scaling, rotating, and translating.

**Since:** 8

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
```

## constructor

```TypeScript
constructor()
```

Constructs a two-dimensional transformation matrix object. The default value is a matrix whose attributes are all 0.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 10.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(unit: LengthMetricsUnit)
```

Constructs a two-dimensional transformation matrix object. The default value is a matrix whose attributes are all 0. The unit mode of the Matrix2D object can be configured.

**Since:** 12

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

**Widget capability:** This API can be used in ArkTS widgets since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| unit | [LengthMetricsUnit](arkts-arkui-graphics-lengthmetricsunit-e.md) | Yes |

## identity

```TypeScript
identity(): Matrix2D
```

Transforms the current 2D matrix back to the identity matrix (i.e., without any rotational translation scaling effect)

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Matrix2D](arkts-arkui-matrix2d-c.md) |

## invert

```TypeScript
invert(): Matrix2D
```

Transform the current 2D matrix into an inverse matrix (that is, the transformation effect is the opposite effect of the original)

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Matrix2D](arkts-arkui-matrix2d-c.md) |

## multiply

```TypeScript
multiply(other?: Matrix2D): Matrix2D
```

The matrix is superimposed in right multiplication mode. When the input parameter is empty, the matrix is superimposed.

**Since:** 8

**Deprecated since:** 10

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| other | [Matrix2D](arkts-arkui-matrix2d-c.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Matrix2D](arkts-arkui-matrix2d-c.md) |

## rotate

```TypeScript
rotate(rx?: number, ry?: number): Matrix2D
```

Adds the rotation effect of the X and Y axes to the current matrix.

**Since:** 8

**Deprecated since:** 10

**Substitutes:** [rotate](#rotate)

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| rx | number | No |
| ry | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Matrix2D](arkts-arkui-matrix2d-c.md) |

## rotate

```TypeScript
rotate(degree: number, rx?: number, ry?: number): Matrix2D
```

Adds the rotation effect of the X and Y axes to the current matrix.

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 10.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| degree | number | Yes |
| rx | number | No |
| ry | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Matrix2D](arkts-arkui-matrix2d-c.md) |

## scale

```TypeScript
scale(sx?: number, sy?: number): Matrix2D
```

Adds the scaling effect of the X and Y axes to the current matrix.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sx | number | No |
| sy | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Matrix2D](arkts-arkui-matrix2d-c.md) |

## translate

```TypeScript
translate(tx?: number, ty?: number): Matrix2D
```

Performs a left multiplication translation operation on this matrix.

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| tx | number | No |
| ty | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Matrix2D](arkts-arkui-matrix2d-c.md) |

## rotateX

```TypeScript
rotateX?: number
```

Horizontal skew coefficient. The value range is not limited.If the value is undefined, it is regarded as an invalid value. If the value is NaN or Infinity, the Matrix2D will be abnormal.

**Type:** number

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## rotateY

```TypeScript
rotateY?: number
```

Vertical skew coefficient. The value range is not limited.If the value is undefined, it is regarded as an invalid value. If the value is NaN or Infinity, the Matrix2D will be abnormal.

**Type:** number

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## scaleX

```TypeScript
scaleX?: number
```

Horizontal scaling coefficient. The value range is not limited.If the value is undefined, it is regarded as an invalid value. If the value is NaN or Infinity, the Matrix2D will be abnormal.

**Type:** number

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## scaleY

```TypeScript
scaleY?: number
```

Vertical scaling coefficient. The value range is not limited.If the value is undefined, it is regarded as an invalid value. If the value is NaN or Infinity, the Matrix2D will be abnormal.

**Type:** number

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## translateX

```TypeScript
translateX?: number
```

Horizontal translation distance. The value range is unlimited. The abnormal value undefined is processed as an invalid value. NaN and Infinity will cause Matrix2D exceptions. After the setting, the drawn content is not displayed. Default unit: vp.

**Type:** number

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## translateY

```TypeScript
translateY?: number
```

Vertical translation distance. The value range is unlimited. The abnormal value undefined is processed as an invalid value. NaN and Infinity will cause Matrix2D exceptions. After the setting, the drawn content is not displayed. Default unit: vp.

**Type:** number

**Since:** 8

**Atomic service API:** This API can be used in atomic services since API version 11.

**Widget capability:** This API can be used in ArkTS widgets since API version 9.

**System capability:** SystemCapability.ArkUI.ArkUI.Full
