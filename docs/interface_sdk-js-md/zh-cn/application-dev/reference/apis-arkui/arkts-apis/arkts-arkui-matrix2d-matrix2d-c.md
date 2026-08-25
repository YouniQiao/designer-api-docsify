# Matrix2D

用于画布绘制CanvasRenderingContext2D、 OffscreenCanvasRenderingContext2D、 CanvasPattern和 Path2D的矩阵对象， 可以对矩阵进行缩放、旋转和平移等变换。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## constructor

```TypeScript
constructor(unit?: LengthMetricsUnit)
```

构造二维变换矩阵对象，默认值是属性全为0的矩阵。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| unit | [LengthMetricsUnit](arkts-arkui-graphics-lengthmetricsunit-e.md) | 否 |

## identity

```TypeScript
identity(): Matrix2D
```

创建单位矩阵。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| [Matrix2D](arkts-arkui-matrix2d-matrix2d-c.md) |

## invert

```TypeScript
invert(): Matrix2D
```

获取当前矩阵的逆矩阵。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| [Matrix2D](arkts-arkui-matrix2d-matrix2d-c.md) |

## rotate

```TypeScript
rotate(degree: double, rx?: double, ry?: double): Matrix2D
```

以旋转点为中心，对当前矩阵进行右乘旋转运算。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| degree | double | 是 |
| rx | double | 否 |
| ry | double | 否 |

**返回值：**

| 类型 |
| --- |
| [Matrix2D](arkts-arkui-matrix2d-matrix2d-c.md) |

## scale

```TypeScript
scale(sx?: double, sy?: double): Matrix2D
```

对当前矩阵进行右乘缩放运算。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| sx | double | 否 |
| sy | double | 否 |

**返回值：**

| 类型 |
| --- |
| [Matrix2D](arkts-arkui-matrix2d-matrix2d-c.md) |

## translate

```TypeScript
translate(tx?: double, ty?: double): Matrix2D
```

对当前矩阵进行左乘平移运算。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| tx | double | 否 |
| ty | double | 否 |

**返回值：**

| 类型 |
| --- |
| [Matrix2D](arkts-arkui-matrix2d-matrix2d-c.md) |

## rotateX

```TypeScript
set rotateX(rotateX: double | undefined)
```

水平倾斜系数，取值范围无限制。

**类型：** double

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## rotateY

```TypeScript
set rotateY(rotateY: double | undefined)
```

垂直倾斜系数，取值范围无限制。

**类型：** double

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## scaleX

```TypeScript
set scaleX(scaleX: double | undefined)
```

水平缩放系数，取值范围无限制。

**类型：** double

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## scaleY

```TypeScript
set scaleY(scaleY: double | undefined)
```

垂直缩放系数，取值范围无限制。

**类型：** double

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## translateX

```TypeScript
set translateX(translateX: double | undefined)
```

水平平移距离，取值范围无限制。

**类型：** double

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## translateY

```TypeScript
set translateY(translateY: double | undefined)
```

垂直平移距离，取值范围无限制。

**类型：** double

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full
