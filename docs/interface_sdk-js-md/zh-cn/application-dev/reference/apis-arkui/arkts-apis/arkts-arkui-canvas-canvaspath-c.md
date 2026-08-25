# CanvasPath

Path object, which provides basic methods for drawing paths.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## arc

```TypeScript
arc(x: double, y: double, radius: double, startAngle: double, endAngle: double, counterclockwise?: boolean): void
```

Draw an arc path

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| x | double | 是 |
| y | double | 是 |
| radius | double | 是 |
| startAngle | double | 是 |
| endAngle | double | 是 |
| counterclockwise | boolean | 否 |

## arcTo

```TypeScript
arcTo(x1: double, y1: double, x2: double, y2: double, radius: double): void
```

Draw arc paths based on control points and radius

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| x1 | double | 是 |
| y1 | double | 是 |
| x2 | double | 是 |
| y2 | double | 是 |
| radius | double | 是 |

## bezierCurveTo

```TypeScript
bezierCurveTo(cp1x: double, cp1y: double, cp2x: double, cp2y: double, x: double, y: double): void
```

Drawing Cubic Bessel Curve Paths

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| cp1x | double | 是 |
| cp1y | double | 是 |
| cp2x | double | 是 |
| cp2y | double | 是 |
| x | double | 是 |
| y | double | 是 |

## closePath

```TypeScript
closePath(): void
```

Returns the pen point to the start point of the current sub-path

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## ellipse

```TypeScript
ellipse(x: double, y: double, radiusX: double, radiusY: double, rotation: double, startAngle: double,
    endAngle: double, counterclockwise?: boolean): void
```

Draw an Elliptic Path

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| x | double | 是 |
| y | double | 是 |
| radiusX | double | 是 |
| radiusY | double | 是 |
| rotation | double | 是 |
| startAngle | double | 是 |
| endAngle | double | 是 |
| counterclockwise | boolean | 否 |

## lineTo

```TypeScript
lineTo(x: double, y: double): void
```

Connect sub-path using straight lines

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| x | double | 是 |
| y | double | 是 |

## moveTo

```TypeScript
moveTo(x: double, y: double): void
```

Moves the start point of a new sub-path to the (x, y) coordinate.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| x | double | 是 |
| y | double | 是 |

## quadraticCurveTo

```TypeScript
quadraticCurveTo(cpx: double, cpy: double, x: double, y: double): void
```

Draw quadratic Bezier curve paths

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| cpx | double | 是 |
| cpy | double | 是 |
| x | double | 是 |
| y | double | 是 |

## rect

```TypeScript
rect(x: double, y: double, w: double, h: double): void
```

Draw Rectangular Paths

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| x | double | 是 |
| y | double | 是 |
| w | double | 是 |
| [h](../../apis-crypto-architecture-kit/arkts-apis/arkts-cryptoarchitecture-cryptoframework-ecccommonparamsspec-i.md) | double | 是 |

## roundRect

```TypeScript
roundRect(x: double, y: double, w: double, h: double, radii?: double | Array<double>): void
```

Draw rounded Rectangular Paths

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| x | double | 是 |
| y | double | 是 |
| w | double | 是 |
| [h](../../apis-crypto-architecture-kit/arkts-apis/arkts-cryptoarchitecture-cryptoframework-ecccommonparamsspec-i.md) | double | 是 |
| radii | double \| Array & lt;double & gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [103701](../errorcode-canvas.md#103701-参数错误) |
