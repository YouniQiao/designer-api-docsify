# CanvasPath

路径对象，提供基本的路径绘制方法。路径相关API的详细说明请参见CanvasRenderingContext2D中的描述。

**起始版本：** 8

**废弃版本：** -1

<!--Device-unnamed-declare class CanvasPath--><!--Device-unnamed-declare class CanvasPath-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## arc

```TypeScript
arc(x: number, y: number, radius: number, startAngle: number, endAngle: number, counterclockwise?: boolean): void
```

绘制弧线路径。

**起始版本：** 8

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

<!--Device-CanvasPath-arc(x: number, y: number, radius: number, startAngle: number, endAngle: number, counterclockwise?: boolean): void--><!--Device-CanvasPath-arc(x: number, y: number, radius: number, startAngle: number, endAngle: number, counterclockwise?: boolean): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| x | number | 是 |
| y | number | 是 |
| radius | number | 是 |
| startAngle | number | 是 |
| endAngle | number | 是 |
| counterclockwise | boolean | 否 |

## arcTo

```TypeScript
arcTo(x1: number, y1: number, x2: number, y2: number, radius: number): void
```

依据圆弧经过的点和圆弧半径创建圆弧路径。

**起始版本：** 8

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

<!--Device-CanvasPath-arcTo(x1: number, y1: number, x2: number, y2: number, radius: number): void--><!--Device-CanvasPath-arcTo(x1: number, y1: number, x2: number, y2: number, radius: number): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| x1 | number | 是 |
| y1 | number | 是 |
| x2 | number | 是 |
| y2 | number | 是 |
| radius | number | 是 |

## bezierCurveTo

```TypeScript
bezierCurveTo(cp1x: number, cp1y: number, cp2x: number, cp2y: number, x: number, y: number): void
```

创建三次贝塞尔曲线的路径。

**起始版本：** 8

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

<!--Device-CanvasPath-bezierCurveTo(cp1x: number, cp1y: number, cp2x: number, cp2y: number, x: number, y: number): void--><!--Device-CanvasPath-bezierCurveTo(cp1x: number, cp1y: number, cp2x: number, cp2y: number, x: number, y: number): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| cp1x | number | 是 |
| cp1y | number | 是 |
| cp2x | number | 是 |
| cp2y | number | 是 |
| x | number | 是 |
| y | number | 是 |

## closePath

```TypeScript
closePath(): void
```

将路径的当前点移回到路径的起点，当前点到起点间画一条直线。如果形状已经闭合或只有一个点，则此功能不执行任何操作。

**起始版本：** 8

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

<!--Device-CanvasPath-closePath(): void--><!--Device-CanvasPath-closePath(): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## ellipse

```TypeScript
ellipse(
    x: number,
    y: number,
    radiusX: number,
    radiusY: number,
    rotation: number,
    startAngle: number,
    endAngle: number,
    counterclockwise?: boolean,
  ): void
```

在规定的矩形区域绘制一个椭圆。

**起始版本：** 8

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

<!--Device-CanvasPath-ellipse(    x: number,    y: number,    radiusX: number,    radiusY: number,    rotation: number,    startAngle: number,    endAngle: number,    counterclockwise?: boolean,  ): void--><!--Device-CanvasPath-ellipse(    x: number,    y: number,    radiusX: number,    radiusY: number,    rotation: number,    startAngle: number,    endAngle: number,    counterclockwise?: boolean,  ): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| x | number | 是 |
| y | number | 是 |
| radiusX | number | 是 |
| radiusY | number | 是 |
| rotation | number | 是 |
| startAngle | number | 是 |
| endAngle | number | 是 |
| counterclockwise | boolean | 否 |

## lineTo

```TypeScript
lineTo(x: number, y: number): void
```

从当前点绘制一条直线到目标点。

**起始版本：** 8

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

<!--Device-CanvasPath-lineTo(x: number, y: number): void--><!--Device-CanvasPath-lineTo(x: number, y: number): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| x | number | 是 |
| y | number | 是 |

## moveTo

```TypeScript
moveTo(x: number, y: number): void
```

将路径的当前坐标点移动到目标点，移动过程中不绘制线条。

**起始版本：** 8

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

<!--Device-CanvasPath-moveTo(x: number, y: number): void--><!--Device-CanvasPath-moveTo(x: number, y: number): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| x | number | 是 |
| y | number | 是 |

## quadraticCurveTo

```TypeScript
quadraticCurveTo(cpx: number, cpy: number, x: number, y: number): void
```

创建二次贝塞尔曲线路径。

**起始版本：** 8

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

<!--Device-CanvasPath-quadraticCurveTo(cpx: number, cpy: number, x: number, y: number): void--><!--Device-CanvasPath-quadraticCurveTo(cpx: number, cpy: number, x: number, y: number): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| cpx | number | 是 |
| cpy | number | 是 |
| x | number | 是 |
| y | number | 是 |

## rect

```TypeScript
rect(x: number, y: number, w: number, h: number): void
```

创建矩形路径。

**起始版本：** 8

**废弃版本：** -1

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本9开始，该接口支持在ArkTS卡片中使用。

<!--Device-CanvasPath-rect(x: number, y: number, w: number, h: number): void--><!--Device-CanvasPath-rect(x: number, y: number, w: number, h: number): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| x | number | 是 |
| y | number | 是 |
| w | number | 是 |
| [h](../../apis-crypto-architecture-kit/arkts-apis/arkts-cryptoarchitecture-cryptoframework-ecccommonparamsspec-i.md) | number | 是 |

## roundRect

```TypeScript
roundRect(x: number, y: number, w: number, h: number, radii?: number | Array<number>): void
```

创建圆角矩形路径，此方法不会直接渲染内容，如需将圆角矩形绘制到画布上，可以使用fill或stroke方法。

**起始版本：** 20

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本20开始，该接口支持在ArkTS卡片中使用。

<!--Device-CanvasPath-roundRect(x: number, y: number, w: number, h: number, radii?: number | Array<number>): void--><!--Device-CanvasPath-roundRect(x: number, y: number, w: number, h: number, radii?: number | Array<number>): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| x | number | 是 |
| y | number | 是 |
| w | number | 是 |
| [h](../../apis-crypto-architecture-kit/arkts-apis/arkts-cryptoarchitecture-cryptoframework-ecccommonparamsspec-i.md) | number | 是 |
| radii | number \| Array & lt;number & gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [103701](../errorcode-canvas.md#103701-参数错误) |
