# Matrix4Transit

矩阵对象。

**起始版本：** 7

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 导入模块

```TypeScript
import { matrix4 } from 'kits/@kit.ArkUI';
```

## combine

```TypeScript
combine(options: Matrix4Transit): Matrix4Transit
```

Matrix的叠加函数，可以将两个矩阵的效果叠加起来生成一个新的矩阵对象。会改变调用该函数的原始矩阵。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [Matrix4Transit](arkts-arkui-matrix4-matrix4transit-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [Matrix4Transit](arkts-arkui-matrix4-matrix4transit-i.md) |

## copy

```TypeScript
copy(): Matrix4Transit
```

Matrix的拷贝函数，可以拷贝一份当前的矩阵对象。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| [Matrix4Transit](arkts-arkui-matrix4-matrix4transit-i.md) |

## invert

```TypeScript
invert(): Matrix4Transit
```

Matrix的逆函数，可以返回一个当前矩阵对象的逆矩阵，即效果正好相反。会改变调用该函数的原始矩阵。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 |
| --- |
| [Matrix4Transit](arkts-arkui-matrix4-matrix4transit-i.md) |

## rotate

```TypeScript
rotate(options: RotateOption): Matrix4Transit
```

Matrix的旋转函数，可以为当前矩阵增加x轴/y轴/z轴旋转效果。会改变调用该函数的原始矩阵。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [RotateOption](arkts-arkui-matrix4-rotateoption-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [Matrix4Transit](arkts-arkui-matrix4-matrix4transit-i.md) |

## scale

```TypeScript
scale(options: ScaleOption): Matrix4Transit
```

Matrix的缩放函数，可以为当前矩阵增加x轴/y轴/z轴缩放效果。会改变调用该函数的原始矩阵。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [ScaleOption](arkts-arkui-matrix4-scaleoption-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [Matrix4Transit](arkts-arkui-matrix4-matrix4transit-i.md) |

## setPolyToPoly

```TypeScript
setPolyToPoly(options: PolyToPolyOptions): Matrix4Transit
```

将一个多边形的顶点坐标映射到另外一个多边形的顶点坐标。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [PolyToPolyOptions](arkts-arkui-matrix4-polytopolyoptions-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [Matrix4Transit](arkts-arkui-matrix4-matrix4transit-i.md) |

## skew

```TypeScript
skew(x: number, y: number): Matrix4Transit
```

Matrix的倾斜函数，可以为当前矩阵增加x轴/y轴倾斜效果。会改变调用该函数的原始矩阵。

**起始版本：** 12

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| x | number | 是 |
| y | number | 是 |

**返回值：**

| 类型 |
| --- |
| [Matrix4Transit](arkts-arkui-matrix4-matrix4transit-i.md) |

## transformPoint

```TypeScript
transformPoint(options: [number, number]): [number, number]
```

Matrix的坐标点转换函数，可以将当前的变换效果作用到一个坐标点上。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [number, number] | 是 |

**返回值：**

| 类型 |
| --- |
| [number, number] |

## translate

```TypeScript
translate(options: TranslateOption): Matrix4Transit
```

Matrix的平移函数，可以为当前矩阵增加x轴/y轴/z轴平移效果。会改变调用该函数的原始矩阵。

**起始版本：** 7

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [TranslateOption](arkts-arkui-matrix4-translateoption-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [Matrix4Transit](arkts-arkui-matrix4-matrix4transit-i.md) |
