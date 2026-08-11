# Lattice

矩形网格对象。该对象用于将图像按照矩形网格进行划分，支持固定指定网格区域、缩放其余网格实现局部拉伸、自定义网格绘制类型、网格颜色填充以及指定绘制边界矩形等能力。创建Lattice对象后，需配合  
[Canvas.drawImageLattice](arkts-arkgraphics2d-drawing-canvas-c.md#drawimagelattice)方法使用以实现图像的局部拉伸绘制。

> **说明：**
> 
> - 本Class首批接口从API version 12开始支持。
> 
> - 本模块使用屏幕物理像素单位px。
> 
> - 本模块为单线程模型策略，需要调用方自行管理线程安全和上下文状态的切换。

**起始版本：** 12

<!--Device-drawing-class Lattice--><!--Device-drawing-class Lattice-End-->

**系统能力：** SystemCapability.Graphics.Drawing

## createImageLattice

```TypeScript
static createImageLattice(xDivs: Array<number>, yDivs: Array<number>, fXCount: number, fYCount: number,
        fBounds?: common2D.Rect | null, fRectTypes?: Array<RectType> | null, fColors?: Array<common2D.Color> | null): Lattice
```

创建矩形网格对象。将图像划分为矩形网格，同时处于偶数列和偶数行上的网格是固定的，如果目标网格足够大，则这些固定网格以其原始大小进行绘制，其余网格将进行缩放，来适应剩余的空间。如果目标网格太小，无法容纳这些固定网格，则所有固定网格都会按比例缩小以适应目标网格。

**起始版本：** 12

<!--Device-Lattice-static createImageLattice(xDivs: Array<number>, yDivs: Array<number>, fXCount: number, fYCount: number,        fBounds?: common2D.Rect | null, fRectTypes?: Array<RectType> | null, fColors?: Array<common2D.Color> | null): Lattice--><!--Device-Lattice-static createImageLattice(xDivs: Array<number>, yDivs: Array<number>, fXCount: number, fYCount: number,        fBounds?: common2D.Rect | null, fRectTypes?: Array<RectType> | null, fColors?: Array<common2D.Color> | null): Lattice-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| xDivs | Array&lt;number&gt; | 是 |
| yDivs | Array&lt;number&gt; | 是 |
| fXCount | number | 是 |
| fYCount | number | 是 |
| fBounds | common2D.Rect \| null | 否 |
| fRectTypes | Array&lt;RectType&gt; \| null | 否 |
| fColors | Array&lt;common2D.Color&gt; \| null | 否 |

**返回值：**

| 类型 |
| --- |
| [Lattice](arkts-arkgraphics2d-drawing-lattice-c.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |

## createImageLattice

```TypeScript
static createImageLattice(xDivs: Array<number>, yDivs: Array<number>, fXCount: number, fYCount: number,
        fBounds?: common2D.Rect | null, fRectTypes?: Array<RectType> | null, fColors?: Array<number> | null): Lattice
```

创建矩形网格对象。将图像划分为矩形网格，同时处于偶数列和偶数行上的网格是固定的，如果目标网格足够大，则这些固定网格以其原始大小进行绘制，其余网格将进行缩放，以适应剩余的空间。如果目标网格太小，无法容纳这些固定网格，则所有固定网格都会按比例缩小以适应目标网格。

**起始版本：** 18

<!--Device-Lattice-static createImageLattice(xDivs: Array<number>, yDivs: Array<number>, fXCount: number, fYCount: number,        fBounds?: common2D.Rect | null, fRectTypes?: Array<RectType> | null, fColors?: Array<number> | null): Lattice--><!--Device-Lattice-static createImageLattice(xDivs: Array<number>, yDivs: Array<number>, fXCount: number, fYCount: number,        fBounds?: common2D.Rect | null, fRectTypes?: Array<RectType> | null, fColors?: Array<number> | null): Lattice-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| xDivs | Array&lt;number&gt; | 是 |
| yDivs | Array&lt;number&gt; | 是 |
| fXCount | number | 是 |
| fYCount | number | 是 |
| fBounds | common2D.Rect \| null | 否 |
| fRectTypes | Array&lt;RectType&gt; \| null | 否 |
| fColors | Array&lt;number&gt; \| null | 否 |

**返回值：**

| 类型 |
| --- |
| [Lattice](arkts-arkgraphics2d-drawing-lattice-c.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
