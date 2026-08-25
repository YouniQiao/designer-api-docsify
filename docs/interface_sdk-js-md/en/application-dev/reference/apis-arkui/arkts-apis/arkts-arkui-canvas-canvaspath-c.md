# CanvasPath

Path object, which provides basic methods for drawing paths.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## arc

```TypeScript
arc(x: double, y: double, radius: double, startAngle: double, endAngle: double, counterclockwise?: boolean): void
```

Draw an arc path

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| x | double | Yes |
| y | double | Yes |
| radius | double | Yes |
| startAngle | double | Yes |
| endAngle | double | Yes |
| counterclockwise | boolean | No |

## arcTo

```TypeScript
arcTo(x1: double, y1: double, x2: double, y2: double, radius: double): void
```

Draw arc paths based on control points and radius

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| x1 | double | Yes |
| y1 | double | Yes |
| x2 | double | Yes |
| y2 | double | Yes |
| radius | double | Yes |

## bezierCurveTo

```TypeScript
bezierCurveTo(cp1x: double, cp1y: double, cp2x: double, cp2y: double, x: double, y: double): void
```

Drawing Cubic Bessel Curve Paths

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| cp1x | double | Yes |
| cp1y | double | Yes |
| cp2x | double | Yes |
| cp2y | double | Yes |
| x | double | Yes |
| y | double | Yes |

## closePath

```TypeScript
closePath(): void
```

Returns the pen point to the start point of the current sub-path

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## ellipse

```TypeScript
ellipse(x: double, y: double, radiusX: double, radiusY: double, rotation: double, startAngle: double,
    endAngle: double, counterclockwise?: boolean): void
```

Draw an Elliptic Path

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| x | double | Yes |
| y | double | Yes |
| radiusX | double | Yes |
| radiusY | double | Yes |
| rotation | double | Yes |
| startAngle | double | Yes |
| endAngle | double | Yes |
| counterclockwise | boolean | No |

## lineTo

```TypeScript
lineTo(x: double, y: double): void
```

Connect sub-path using straight lines

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| x | double | Yes |
| y | double | Yes |

## moveTo

```TypeScript
moveTo(x: double, y: double): void
```

Moves the start point of a new sub-path to the (x, y) coordinate.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| x | double | Yes |
| y | double | Yes |

## quadraticCurveTo

```TypeScript
quadraticCurveTo(cpx: double, cpy: double, x: double, y: double): void
```

Draw quadratic Bezier curve paths

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| cpx | double | Yes |
| cpy | double | Yes |
| x | double | Yes |
| y | double | Yes |

## rect

```TypeScript
rect(x: double, y: double, w: double, h: double): void
```

Draw Rectangular Paths

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| x | double | Yes |
| y | double | Yes |
| w | double | Yes |
| [h](../../apis-crypto-architecture-kit/arkts-apis/arkts-cryptoarchitecture-cryptoframework-ecccommonparamsspec-i.md) | double | Yes |

## roundRect

```TypeScript
roundRect(x: double, y: double, w: double, h: double, radii?: double | Array<double>): void
```

Draw rounded Rectangular Paths

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| x | double | Yes |
| y | double | Yes |
| w | double | Yes |
| [h](../../apis-crypto-architecture-kit/arkts-apis/arkts-cryptoarchitecture-cryptoframework-ecccommonparamsspec-i.md) | double | Yes |
| radii | double \| Array & lt;double & gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [103701](../errorcode-canvas.md#103701-parameter-error) |
