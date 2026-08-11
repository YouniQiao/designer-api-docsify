# PathEffect

路径效果对象，用于创建多种路径效果，包括虚线、圆角、离散、叠加和组合路径效果等。可通过[Pen.setPathEffect](arkts-arkgraphics2d-drawing-pen-c.md#setpatheffect)将其应用到画笔上，从而在绘制路径时改变路径的渲染样式。

> **说明：**
> 
> - 本Class首批接口从API version 12开始支持。
> 
> - 本模块使用屏幕物理像素单位px。
> 
> - 本模块为单线程模型策略，需要调用方自行管理线程安全和上下文状态的切换。

**起始版本：** 12

<!--Device-drawing-class PathEffect--><!--Device-drawing-class PathEffect-End-->

**系统能力：** SystemCapability.Graphics.Drawing

## createComposePathEffect

```TypeScript
static createComposePathEffect(outer: PathEffect, inner: PathEffect): PathEffect
```

创建组合路径效果对象，首先应用内部路径效果，然后应用外部路径效果。

**起始版本：** 18

<!--Device-PathEffect-static createComposePathEffect(outer: PathEffect, inner: PathEffect): PathEffect--><!--Device-PathEffect-static createComposePathEffect(outer: PathEffect, inner: PathEffect): PathEffect-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| outer | [PathEffect](arkts-arkgraphics2d-drawing-patheffect-c.md) | 是 |
| inner | [PathEffect](arkts-arkgraphics2d-drawing-patheffect-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [PathEffect](arkts-arkgraphics2d-drawing-patheffect-c.md) |

## createCornerPathEffect

```TypeScript
static createCornerPathEffect(radius: number): PathEffect
```

创建将路径的夹角变成指定半径的圆角的路径效果对象。该效果会在路径的每个夹角处插入指定半径的弧线段，将原有的尖锐转角替换为平滑的圆角过渡。

**起始版本：** 12

<!--Device-PathEffect-static createCornerPathEffect(radius: number): PathEffect--><!--Device-PathEffect-static createCornerPathEffect(radius: number): PathEffect-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| radius | number | 是 |

**返回值：**

| 类型 |
| --- |
| [PathEffect](arkts-arkgraphics2d-drawing-patheffect-c.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |

## createDashPathEffect

```TypeScript
static createDashPathEffect(intervals: Array<number>, phase: number): PathEffect
```

创建将路径变为虚线的路径效果对象，通过指定ON/OFF长度数组生成规则间距的虚线。当需要自定义形状作为虚线段填充时，可使用  
[createPathDashEffect](arkts-arkgraphics2d-drawing-patheffect-c.md#createpathdasheffect)。

**起始版本：** 12

<!--Device-PathEffect-static createDashPathEffect(intervals: Array<number>, phase: number): PathEffect--><!--Device-PathEffect-static createDashPathEffect(intervals: Array<number>, phase: number): PathEffect-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| intervals | Array&lt;number&gt; | 是 |
| phase | number | 是 |

**返回值：**

| 类型 |
| --- |
| [PathEffect](arkts-arkgraphics2d-drawing-patheffect-c.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |

## createDiscretePathEffect

```TypeScript
static createDiscretePathEffect(segLength: number, dev: number, seedAssist?: number): PathEffect
```

创建将路径打散为离散线段并对端点进行随机偏移的路径效果对象。

**起始版本：** 18

<!--Device-PathEffect-static createDiscretePathEffect(segLength: number, dev: number, seedAssist?: number): PathEffect--><!--Device-PathEffect-static createDiscretePathEffect(segLength: number, dev: number, seedAssist?: number): PathEffect-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| segLength | number | 是 |
| dev | number | 是 |
| seedAssist | number | 否 |

**返回值：**

| 类型 |
| --- |
| [PathEffect](arkts-arkgraphics2d-drawing-patheffect-c.md) |

## createPathDashEffect

```TypeScript
static createPathDashEffect(path: Path, advance: number, phase: number, style: PathDashStyle): PathEffect
```

创建一个虚线路径效果对象，通过路径描述的形状生成。与  
[createDashPathEffect](arkts-arkgraphics2d-drawing-patheffect-c.md#createdashpatheffect)使用intervals数组指定ON/OFF长度创建规则间距虚线不同，本接口通过Path指定虚线段的图形形状。

**起始版本：** 18

<!--Device-PathEffect-static createPathDashEffect(path: Path, advance: number, phase: number, style: PathDashStyle): PathEffect--><!--Device-PathEffect-static createPathDashEffect(path: Path, advance: number, phase: number, style: PathDashStyle): PathEffect-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | [Path](arkts-arkgraphics2d-drawing-path-c.md) | 是 |
| advance | number | 是 |
| phase | number | 是 |
| style | [PathDashStyle](arkts-arkgraphics2d-drawing-pathdashstyle-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [PathEffect](arkts-arkgraphics2d-drawing-patheffect-c.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |

## createSumPathEffect

```TypeScript
static createSumPathEffect(firstPathEffect: PathEffect, secondPathEffect: PathEffect): PathEffect
```

创建一个叠加的路径效果。与  
[createComposePathEffect](arkts-arkgraphics2d-drawing-patheffect-c.md#createcomposepatheffect)不同，此接口会分别对两个参数的效果各自独立进行表现，然后将两个效果简单重叠显示。

**起始版本：** 18

<!--Device-PathEffect-static createSumPathEffect(firstPathEffect: PathEffect, secondPathEffect: PathEffect): PathEffect--><!--Device-PathEffect-static createSumPathEffect(firstPathEffect: PathEffect, secondPathEffect: PathEffect): PathEffect-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| firstPathEffect | [PathEffect](arkts-arkgraphics2d-drawing-patheffect-c.md) | 是 |
| secondPathEffect | [PathEffect](arkts-arkgraphics2d-drawing-patheffect-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [PathEffect](arkts-arkgraphics2d-drawing-patheffect-c.md) |
