# RectUtils

提供处理矩形的工具，支持矩形的快速构建与基本属性获取、边界计算与调整、平移与状态判断、边界规范化等功能。主要的使用场景：
1. 矩形快速构建与获取基本属性，如构造新矩形、拷贝矩形、获取矩形的宽高以及中心点等。
2. 边界计算与调整，如判断包含关系、计算与更新矩形之间交集和并集，更新边界值等。
3. 矩形平移与状态判断，如对矩形进行平移、将矩形平移到指定位置、判断矩形是否为空以及判断两个矩形是否相等。
4. 矩形边界规范化，如对存在反转情况的矩形边界值进行交换排序等。

> **说明：**&gt;
> - 本Class首批接口从API version 20开始支持。&gt;
> - 本模块使用屏幕物理像素单位px。&gt;
> - 本模块为单线程模型策略，需要调用方自行管理线程安全和上下文状态的切换。

**起始版本：** 20

**系统能力：** SystemCapability.Graphics.Drawing

## 导入模块

```TypeScript
import { drawing } from 'kits/@kit.ArkGraphics2D';
```

## centerX

```TypeScript
static centerX(rect: common2D.Rect): number
```

获取矩形中心的x轴坐标，中心x轴坐标为矩形左边界与右边界之和的一半。

**起始版本：** 20

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| rect | common2D.Rect | 是 |

**返回值：**

| 类型 |
| --- |
| number |

## centerY

```TypeScript
static centerY(rect: common2D.Rect): number
```

获取矩形中心的y轴坐标，中心y轴坐标为矩形上边界与下边界之和的一半。

**起始版本：** 20

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| rect | common2D.Rect | 是 |

**返回值：**

| 类型 |
| --- |
| number |

## contains

```TypeScript
static contains(rect: common2D.Rect, other: common2D.Rect): boolean
```

判断一个矩形是否完全包含另外一个矩形。

**起始版本：** 20

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| rect | common2D.Rect | 是 |
| other | common2D.Rect | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## contains

```TypeScript
static contains(rect: common2D.Rect, left: number, top: number, right: number, bottom: number): boolean
```

判断一个矩形是否完全包含另外一个矩形（另一个矩形分别用左上右下坐标表示）。

**起始版本：** 20

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| rect | common2D.Rect | 是 |
| left | number | 是 |
| top | number | 是 |
| right | number | 是 |
| bottom | number | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## contains

```TypeScript
static contains(rect: common2D.Rect, x: number, y: number): boolean
```

判断一个矩形是否完全包含一个点。

**起始版本：** 20

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| rect | common2D.Rect | 是 |
| x | number | 是 |
| y | number | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## getHeight

```TypeScript
static getHeight(rect: common2D.Rect): number
```

获取矩形的高度。

**起始版本：** 20

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| rect | common2D.Rect | 是 |

**返回值：**

| 类型 |
| --- |
| number |

## getWidth

```TypeScript
static getWidth(rect: common2D.Rect): number
```

获取矩形的宽度。

**起始版本：** 20

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| rect | common2D.Rect | 是 |

**返回值：**

| 类型 |
| --- |
| number |

## inset

```TypeScript
static inset(rect: common2D.Rect, left: number, top: number, right: number, bottom: number): void
```

将指定矩形的左边界、上边界、右边界和下边界分别和传入的“左上右下”的值相加。

**起始版本：** 20

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| rect | common2D.Rect | 是 |
| left | number | 是 |
| top | number | 是 |
| right | number | 是 |
| bottom | number | 是 |

## intersect

```TypeScript
static intersect(rect: common2D.Rect, other: common2D.Rect): boolean
```

计算两个矩形的交集区域，并将交集结果更新到第一个入参代表的矩形区域。

**起始版本：** 20

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| rect | common2D.Rect | 是 |
| other | common2D.Rect | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## isEmpty

```TypeScript
static isEmpty(rect: common2D.Rect): boolean
```

判断矩形是否为空（左边界大于等于右边界或者上边界大于等于下边界）。

**起始版本：** 20

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| rect | common2D.Rect | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## isEqual

```TypeScript
static isEqual(rect: common2D.Rect, other: common2D.Rect): boolean
```

判断两个矩形是否相等。

**起始版本：** 20

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| rect | common2D.Rect | 是 |
| other | common2D.Rect | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## isIntersect

```TypeScript
static isIntersect(rect: common2D.Rect, other: common2D.Rect): boolean
```

判断两个矩形是否相交。

**起始版本：** 20

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| rect | common2D.Rect | 是 |
| other | common2D.Rect | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

## makeCopy

```TypeScript
static makeCopy(src: common2D.Rect): common2D.Rect
```

拷贝一个矩形。

**起始版本：** 20

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| src | common2D.Rect | 是 |

**返回值：**

| 类型 |
| --- |
| common2D.Rect |

## makeEmpty

```TypeScript
static makeEmpty(): common2D.Rect
```

创建一个上下左右边界坐标都是0的矩形。

**起始版本：** 20

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| common2D.Rect |

## makeLtrb

```TypeScript
static makeLtrb(left: number, top: number, right: number, bottom: number): common2D.Rect
```

创建指定上下左右边界的矩形。

**起始版本：** 20

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| left | number | 是 |
| top | number | 是 |
| right | number | 是 |
| bottom | number | 是 |

**返回值：**

| 类型 |
| --- |
| common2D.Rect |

## offset

```TypeScript
static offset(rect: common2D.Rect, dx: number, dy: number): void
```

对矩形进行平移。

**起始版本：** 20

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| rect | common2D.Rect | 是 |
| [dx](../../apis-arkui/arkts-apis/arkts-arkui-actionsheetoffset-i.md) | number | 是 |
| [dy](../../apis-arkui/arkts-apis/arkts-arkui-actionsheetoffset-i.md) | number | 是 |

## offsetTo

```TypeScript
static offsetTo(rect: common2D.Rect, newLeft: number, newTop: number): void
```

将矩形平移到指定位置。

**起始版本：** 20

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| rect | common2D.Rect | 是 |
| newLeft | number | 是 |
| newTop | number | 是 |

## setEmpty

```TypeScript
static setEmpty(rect: common2D.Rect): void
```

将矩形的上下左右边界都设为0。

**起始版本：** 20

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| rect | common2D.Rect | 是 |

## setLtrb

```TypeScript
static setLtrb(rect: common2D.Rect, left: number, top: number, right: number, bottom: number): void
```

使用传入的“左上右下”的值更新当前矩形的左上右下边界值。

**起始版本：** 20

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| rect | common2D.Rect | 是 |
| left | number | 是 |
| top | number | 是 |
| right | number | 是 |
| bottom | number | 是 |

## setRect

```TypeScript
static setRect(rect: common2D.Rect, other: common2D.Rect): void
```

使用另一个矩形对当前矩形进行赋值。

**起始版本：** 20

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| rect | common2D.Rect | 是 |
| other | common2D.Rect | 是 |

## sort

```TypeScript
static sort(rect: common2D.Rect): void
```

如果矩形存在反转的情况（即左边界大于右边界或上边界大于下边界），则将发生反转的对应边界值进行交换（若左边界大于右边界，交换左右边界值；若上边界大于下边界，交换上下边界值），使得上边界小于下边界（左边界小于右边界）。如果矩形不存在反转的情况（即左边界小于等于右边界且上边界小于等于下边界），不做任何操作。

**起始版本：** 20

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| rect | common2D.Rect | 是 |

## union

```TypeScript
static union(rect: common2D.Rect, other: common2D.Rect): void
```

计算两个矩形的并集区域，并将并集结果更新到第一个入参代表的矩形区域。如果第一个入参矩形为空，则将并集结果更新到第二个入参代表的矩形区域；如果第二个入参的矩形为空，则不进行任何操作。

**起始版本：** 20

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| rect | common2D.Rect | 是 |
| other | common2D.Rect | 是 |
