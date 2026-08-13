# Matrix4Transit

Implements a **Matrix4Transit** object.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** -1

<!--Device-matrix4-interface Matrix4Transit--><!--Device-matrix4-interface Matrix4Transit-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { matrix4 } from '@kit.ArkUI';
```

## combine

```TypeScript
combine(options: Matrix4Transit): Matrix4Transit
```

Combines the effects of two matrices to generate a new matrix object. The matrix that calls this API will be changed.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Matrix4Transit-combine(options: Matrix4Transit): Matrix4Transit--><!--Device-Matrix4Transit-combine(options: Matrix4Transit): Matrix4Transit-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | Matrix4Transit | Yes | Matrix object to be combined. |

**Return value:**

| Type | Description |
| --- | --- |
| Matrix4Transit | Object after matrix combination. |

## copy

```TypeScript
copy(): Matrix4Transit
```

Copies this matrix object.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Matrix4Transit-copy(): Matrix4Transit--><!--Device-Matrix4Transit-copy(): Matrix4Transit-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| Matrix4Transit | Copy object of the current matrix. |

## invert

```TypeScript
invert(): Matrix4Transit
```

Inverts this matrix object. The matrix that calls this API will be changed.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Matrix4Transit-invert(): Matrix4Transit--><!--Device-Matrix4Transit-invert(): Matrix4Transit-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Return value:**

| Type | Description |
| --- | --- |
| Matrix4Transit | Inverse matrix object of the current matrix. |

## rotate

```TypeScript
rotate(options: RotateOption): Matrix4Transit
```

Rotates this matrix object along the x, y, and z axes. The matrix that calls this API will be changed.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Matrix4Transit-rotate(options: RotateOption): Matrix4Transit--><!--Device-Matrix4Transit-rotate(options: RotateOption): Matrix4Transit-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [RotateOption](arkts-arkui-matrix4-rotateoption-i.md) | Yes | Rotation configuration. |

**Return value:**

| Type | Description |
| --- | --- |
| Matrix4Transit | Matrix object after the rotation. |

## scale

```TypeScript
scale(options: ScaleOption): Matrix4Transit
```

Scales this matrix object along the x, y, and z axes. The matrix that calls this API will be changed.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Matrix4Transit-scale(options: ScaleOption): Matrix4Transit--><!--Device-Matrix4Transit-scale(options: ScaleOption): Matrix4Transit-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [ScaleOption](arkts-arkui-matrix4-scaleoption-i.md) | Yes | Scaling configuration. |

**Return value:**

| Type | Description |
| --- | --- |
| Matrix4Transit | Matrix object after the scaling. |

## setPolyToPoly

```TypeScript
setPolyToPoly(options: PolyToPolyOptions): Matrix4Transit
```

Maps the vertex coordinates of a polygon to those of another polygon.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Matrix4Transit-setPolyToPoly(options: PolyToPolyOptions): Matrix4Transit--><!--Device-Matrix4Transit-setPolyToPoly(options: PolyToPolyOptions): Matrix4Transit-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [PolyToPolyOptions](arkts-arkui-matrix4-polytopolyoptions-i.md) | Yes | Parameters for mapping. |

**Return value:**

| Type | Description |
| --- | --- |
| Matrix4Transit | Matrix object after the mapping. |

## skew

```TypeScript
skew(x: number, y: number): Matrix4Transit
```

Skews this matrix object along the x and y axes. The matrix that calls this API will be changed.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-Matrix4Transit-skew(x: number, y: number): Matrix4Transit--><!--Device-Matrix4Transit-skew(x: number, y: number): Matrix4Transit-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| x | number | Yes | Amount of skewing on the x-axis. |
| y | number | Yes | Amount of skewing on the y-axis. |

**Return value:**

| Type | Description |
| --- | --- |
| Matrix4Transit | Matrix object after the skewing. |

## transformPoint

```TypeScript
transformPoint(options: [number, number]): [number, number]
```

Applies the current transformation effect to a coordinate point.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Matrix4Transit-transformPoint(options: [number, number]): [number, number]--><!--Device-Matrix4Transit-transformPoint(options: [number, number]): [number, number]-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [number, number] | Yes | Point to be transformed. |

**Return value:**

| Type | Description |
| --- | --- |
| [number, number] | Point object after matrix transformation |

## translate

```TypeScript
translate(options: TranslateOption): Matrix4Transit
```

Translates this matrix object along the x, y, and z axes. The matrix that calls this API will be changed.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-Matrix4Transit-translate(options: TranslateOption): Matrix4Transit--><!--Device-Matrix4Transit-translate(options: TranslateOption): Matrix4Transit-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | [TranslateOption](arkts-arkui-matrix4-translateoption-i.md) | Yes | Translation configuration. |

**Return value:**

| Type | Description |
| --- | --- |
| Matrix4Transit | Matrix object after the translation. |

