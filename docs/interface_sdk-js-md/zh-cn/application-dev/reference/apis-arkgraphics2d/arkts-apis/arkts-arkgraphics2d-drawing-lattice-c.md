# Lattice

矩形网格对象。该对象用于将图像按照矩形网格进行划分，支持固定指定网格区域、缩放其余网格实现局部拉伸、自定义网格绘制类型、网格颜色填充以及指定绘制边界矩形等能力。创建Lattice对象后，需配合 [Canvas.drawImageLattice](arkts-arkgraphics2d-drawing-canvas-c.md#drawimagelattice)方法使用以实现图像的局部拉伸绘制。

> **说明：**&gt;
> - 本Class首批接口从API version 12开始支持。&gt;
> - 本模块使用屏幕物理像素单位px。&gt;
> - 本模块为单线程模型策略，需要调用方自行管理线程安全和上下文状态的切换。

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Graphics.Drawing

## 导入模块

```TypeScript
import { drawing } from '@kit.ArkGraphics2D';
```

## createImageLattice

```TypeScript
static createImageLattice(xDivs: Array<number>, yDivs: Array<number>, fXCount: number, fYCount: number,
        fBounds?: common2D.Rect | null, fRectTypes?: Array<RectType> | null, fColors?: Array<common2D.Color> | null): Lattice
```

创建矩形网格对象。将图像划分为矩形网格，同时处于偶数列和偶数行上的网格是固定的，如果目标网格足够大，则这些固定网格以其原始大小进行绘制，其余网格将进行缩放，来适应剩余的空间。如果目标网格太小，无法容纳这些固定网格，则所有固定网 格都会按比例缩小以适应目标网格。

**起始版本：** 12

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为12。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| xDivs | Array & lt;number & gt; | 是 |
| yDivs | Array & lt;number & gt; | 是 |
| fXCount | number | 是 |
| fYCount | number | 是 |
| fBounds | common2D.Rect \| null | 否 |
| fRectTypes | Array & lt;RectType & gt; \ | null | 否 |
| fColors | Array & lt;common2D.Color & gt; \ | null | 否 |

**返回值：**

| 类型 |
| --- |
| [Lattice](arkts-arkgraphics2d-drawing-lattice-c.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

**示例**

ArkTS-Dyn示例：

```TypeScript
import { RenderNode, DrawContext } from '@kit.ArkUI';
import { drawing } from '@kit.ArkGraphics2D';

class DrawingRenderNode extends RenderNode {
  draw(context: DrawContext) {
    let xDivs: Array<number> = [1, 2, 4];
    let yDivs: Array<number> = [1, 2, 4];
    let lattice = drawing.Lattice.createImageLattice(xDivs, yDivs, 3, 3); // 划分(3+1)*(3+1)的网格，下图蓝色填充矩形为固定网格
  }
}
```

ArkTS-Sta示例：

```TypeScript
import { RenderNode, DrawContext } from '@kit.ArkUI';
import { drawing } from '@kit.ArkGraphics2D';

class DrawingRenderNode extends RenderNode {
  draw(context : DrawContext) {
    let xDivs : Array<int> = [1, 2, 4];
    let yDivs : Array<int> = [1, 2, 4];
    let lattice = drawing.Lattice.createImageLattice(xDivs, yDivs, 3, 3); // 划分(3+1)*(3+1)的网格，下图蓝色填充矩形为固定网格
  }
}
```

```TypeScript
import { RenderNode, DrawContext } from '@kit.ArkUI';
import { drawing } from '@kit.ArkGraphics2D';

class DrawingRenderNode extends RenderNode {
  draw(context: DrawContext) {
    let xDivs: Array<number> = [1, 2, 4];
    let yDivs: Array<number> = [1, 2, 4];
    let colorArray: Array<number> = [0xffffffff, 0x44444444, 0x99999999, 0xffffffff, 0x44444444, 0x99999999, 0xffffffff, 0x44444444, 0x99999999, 0x44444444, 0x99999999, 0xffffffff, 0x44444444, 0x99999999, 0xffffffff, 0x44444444];
    let lattice = drawing.Lattice.createImageLattice(xDivs, yDivs, 3, 3, null, null, colorArray);
  }
}
```

## createImageLattice

```TypeScript
static createImageLattice(xDivs: Array<int>, yDivs: Array<int>, fXCount: int, fYCount: int,
        fBounds?: common2D.Rect | null, fRectTypes?: Array<RectType> | null, fColors?: Array<common2D.Color> | null): Lattice | undefined
```

创建矩形网格对象。将图像划分为矩形网格，同时处于偶数列和偶数行上的网格是固定的，如果目标网格足够大，则这些固定网格以其原始大小进行绘制，其余网格将进行缩放，来适应剩余的空间。如果目标网格太小，无法容纳这些固定网格，则所有固定网 格都会按比例缩小以适应目标网格。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| xDivs | Array & lt;int & gt; | 是 |
| yDivs | Array & lt;int & gt; | 是 |
| fXCount | int | 是 |
| fYCount | int | 是 |
| fBounds | common2D.Rect \| null | 否 |
| fRectTypes | Array & lt;RectType & gt; \ | null | 否 |
| fColors | Array & lt;common2D.Color & gt; \ | null | 否 |

**返回值：**

| 类型 |
| --- |
| [Lattice](arkts-arkgraphics2d-drawing-lattice-c.md) \| undefined |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

**示例**

参见 [createImageLattice](#createimagelattice)

## createImageLattice

```TypeScript
static createImageLattice(xDivs: Array<number>, yDivs: Array<number>, fXCount: number, fYCount: number,
        fBounds?: common2D.Rect | null, fRectTypes?: Array<RectType> | null, fColors?: Array<number> | null): Lattice
```

创建矩形网格对象。将图像划分为矩形网格，同时处于偶数列和偶数行上的网格是固定的，如果目标网格足够大，则这些固定网格以其原始大小进行绘制，其余网格将进行缩放，以适应剩余的空间。如果目标网格太小，无法容纳这些固定网格，则所有固定网 格都会按比例缩小以适应目标网格。

**起始版本：** 18

**ArkTS模式：** 仅支持ArkTS-Dyn，ArkTS-Dyn起始版本为18。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| xDivs | Array & lt;number & gt; | 是 |
| yDivs | Array & lt;number & gt; | 是 |
| fXCount | number | 是 |
| fYCount | number | 是 |
| fBounds | common2D.Rect \| null | 否 |
| fRectTypes | Array & lt;RectType & gt; \ | null | 否 |
| fColors | Array & lt;number & gt; \ | null | 否 |

**返回值：**

| 类型 |
| --- |
| [Lattice](arkts-arkgraphics2d-drawing-lattice-c.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

**示例**

参见 [createImageLattice](#createimagelattice)

## createImageLatticeWithArrayInt

```TypeScript
static createImageLatticeWithArrayInt(xDivs: Array<int>, yDivs: Array<int>, fXCount: int, fYCount: int,
        fBounds?: common2D.Rect | null, fRectTypes?: Array<RectType> | null, fColors?: Array<int> | null): Lattice | undefined
```

创建矩形网格对象。将图像划分为矩形网格，同时处于偶数列和偶数行上的网格是固定的，如果目标网格足够大，则这些固定网格以其原始大小进行绘制，其余网格将进行缩放，以适应剩余的空间。如果目标网格太小，无法容纳这些固定网格，则所有固定网 格都会按比例缩小以适应目标网格。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| xDivs | Array & lt;int & gt; | 是 |
| yDivs | Array & lt;int & gt; | 是 |
| fXCount | int | 是 |
| fYCount | int | 是 |
| fBounds | common2D.Rect \| null | 否 |
| fRectTypes | Array & lt;RectType & gt; \ | null | 否 |
| fColors | Array & lt;int & gt; \ | null | 否 |

**返回值：**

| 类型 |
| --- |
| [Lattice](arkts-arkgraphics2d-drawing-lattice-c.md) \| undefined |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

**示例**

ArkTS-Sta示例：

```TypeScript
import { RenderNode, DrawContext } from '@kit.ArkUI';
import { drawing } from '@kit.ArkGraphics2D';

class DrawingRenderNode extends RenderNode {
  draw(context : DrawContext) {
    let xDivs : Array<int> = [1, 2, 4];
    let yDivs : Array<int> = [1, 2, 4];
    let colorArray: Array<int> = [(0xffffffff).toInt(), (0x44444444).toInt(), (0x99999999).toInt(), (0xffffffff).toInt(), (0x44444444).toInt(), (0x99999999).toInt(), (0xffffffff).toInt(), (0x44444444).toInt(), (0x99999999).toInt(), (0x44444444).toInt(), (0x99999999).toInt(), (0xffffffff).toInt(), (0x44444444).toInt(), (0x99999999).toInt(), (0xffffffff).toInt(), (0x44444444).toInt()];
    let lattice = drawing.Lattice.createImageLatticeWithArrayInt(xDivs, yDivs, 3, 3,null,null,colorArray);
  }
}
```
