# TransformObject

TransformObject@interface TransformObject

**Since:** 4

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## matrix

```TypeScript
matrix(scaleX: number, skewX: number, skewY: number, scaleY: number, translateX: number, translateY: number): void
```

Defines a 2D transformation, using a matrix of six values..

**Since:** 6

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [scaleX](#scalex) | number | Yes |
| [skewX](arkts-arkui-viewmodel-transformobject-i.md) | number | Yes |
| [skewY](arkts-arkui-viewmodel-transformobject-i.md) | number | Yes |
| [scaleY](#scaley) | number | Yes |
| [translateX](#translatex) | number | Yes |
| [translateY](#translatey) | number | Yes |

## matrix3d

```TypeScript
matrix3d(
    n00: number,
    n01: number,
    n02: number,
    n03: number,
    n10: number,
    n11: number,
    n12: number,
    n13: number,
    n20: number,
    n21: number,
    n22: number,
    n23: number,
    n30: number,
    n31: number,
    n32: number,
    n33: number,
  ): void
```

Defines a 3D transformation using a 4x4 matrix of 16 values.

**Since:** 6

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| n00 | number | Yes |
| n01 | number | Yes |
| n02 | number | Yes |
| n03 | number | Yes |
| n10 | number | Yes |
| n11 | number | Yes |
| n12 | number | Yes |
| n13 | number | Yes |
| n20 | number | Yes |
| n21 | number | Yes |
| n22 | number | Yes |
| n23 | number | Yes |
| n30 | number | Yes |
| n31 | number | Yes |
| n32 | number | Yes |
| n33 | number | Yes |

## perspective

```TypeScript
perspective(verticalDistance: number): void
```

Defines a perspective view for the 3D transformation element.

**Since:** 6

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| verticalDistance | number | Yes |

## rotate

```TypeScript
rotate(angle: number): void
```

Define the 2D rotation and specify the angle in the parameters.

**Since:** 4

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| angle | number | Yes |

## rotate3d

```TypeScript
rotate3d(x: number, y: number, z: number, angle: number): void
```

Defines a 3D transformation for rotating the X / Y / Z axes.

**Since:** 6

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| x | number | Yes |
| y | number | Yes |
| z | number | Yes |
| angle | number | Yes |

## rotateX

```TypeScript
rotateX(angle: number): void
```

Defines 3D transformations for rotating of the X axes.

**Since:** 4

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| angle | number | Yes |

## rotateY

```TypeScript
rotateY(angle: number): void
```

Defines 3D transformations for rotating of the Y axes.

**Since:** 4

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| angle | number | Yes |

## rotateZ

```TypeScript
rotateZ(angle: number): void
```

Defines 3D transformations for rotating of the Z axes.

**Since:** 6

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| angle | number | Yes |

## scale

```TypeScript
scale(x: number, y: number): void
```

Defines 2D transformations for scaling of the X and Y axes

**Since:** 4

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| x | number | Yes |
| y | number | Yes |

## scale3d

```TypeScript
scale3d(x: number, y: number, z: number): void
```

Defines 3D transformations for scaling of the X / Y / Z axes

**Since:** 6

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| x | number | Yes |
| y | number | Yes |
| z | number | Yes |

## scaleX

```TypeScript
scaleX(x: number): void
```

Defines 2D transformations for scaling of the X axes

**Since:** 4

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| x | number | Yes |

## scaleY

```TypeScript
scaleY(y: number): void
```

Defines 2D transformations for scaling of the Y axes

**Since:** 4

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| y | number | Yes |

## scaleZ

```TypeScript
scaleZ(z: number): void
```

Defines 3D transformations for scaling of the Z axes

**Since:** 6

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| z | number | Yes |

## skew

```TypeScript
skew(xAngle: number, yAngle: number): void
```

Defines the 2D skew transition along the X and Y axes.

**Since:** 6

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| xAngle | number | Yes |
| yAngle | number | Yes |

## skewX

```TypeScript
skewX(angle: number): void
```

Defines the 2D skew transition along the X axes.

**Since:** 6

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| angle | number | Yes |

## skewY

```TypeScript
skewY(angle: number): void
```

Defines the 2D skew transition along the Y axes.

**Since:** 6

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| angle | number | Yes |

## translate

```TypeScript
translate(x: number, y: number): void
```

Defines 2D transformations for translation of the X and Y axes

**Since:** 4

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| x | number | Yes |
| y | number | Yes |

## translate3d

```TypeScript
translate3d(x: number, y: number, z: number): void
```

Defines 3D transformations for translation of the X / Y / Z axes

**Since:** 6

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| x | number | Yes |
| y | number | Yes |
| z | number | Yes |

## translateX

```TypeScript
translateX(x: number): void
```

Defines 2D transformations for translation of the X axes

**Since:** 4

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| x | number | Yes |

## translateY

```TypeScript
translateY(y: number): void
```

Defines 2D transformations for translation of the Y axes

**Since:** 4

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| y | number | Yes |

## translateZ

```TypeScript
translateZ(z: number): void
```

Defines 3D transformations for translation of the Z axes

**Since:** 6

**Model restriction:** This API can be used only in the FA model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| z | number | Yes |
