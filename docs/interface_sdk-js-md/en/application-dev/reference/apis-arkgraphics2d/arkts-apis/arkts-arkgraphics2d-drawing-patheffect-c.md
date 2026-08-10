# PathEffect

路径效果对象，用于创建多种路径效果，包括虚线、圆角、离散、叠加和组合路径效果等。可通过[Pen.setPathEffect](arkts-arkgraphics2d-drawing-pen-c.md#setpatheffect)将其应用到画笔上，从而在绘制路径时改变路径的渲染样式。

> **说明：**
> 
> - 本Class首批接口从API version 12开始支持。
> 
> - 本模块使用屏幕物理像素单位px。
> 
> - 本模块为单线程模型策略，需要调用方自行管理线程安全和上下文状态的切换。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-drawing-class PathEffect--><!--Device-drawing-class PathEffect-End-->

**System capability:** SystemCapability.Graphics.Drawing

## Modules to Import

```TypeScript
import { drawing } from 'kits/@kit.ArkGraphics2D';
```

## createComposePathEffect

```TypeScript
static createComposePathEffect(outer: PathEffect, inner: PathEffect): PathEffect
```

创建组合路径效果对象，首先应用内部路径效果，然后应用外部路径效果。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

<!--Device-PathEffect-static createComposePathEffect(outer: PathEffect, inner: PathEffect): PathEffect--><!--Device-PathEffect-static createComposePathEffect(outer: PathEffect, inner: PathEffect): PathEffect-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| outer | [PathEffect](arkts-arkgraphics2d-drawing-patheffect-c.md) | Yes | 组合路径效果中的外部路径效果，在内部路径效果应用之后进行叠加处理，决定最终呈现的叠加效果。 |
| inner | [PathEffect](arkts-arkgraphics2d-drawing-patheffect-c.md) | Yes | 组合路径效果中的内部路径效果，首先应用于原始路径，作为第一层效果处理，随后再由外部路径效果进行叠加。 |

**Return value:**

| Type | Description |
| --- | --- |
| [PathEffect](arkts-arkgraphics2d-drawing-patheffect-c.md) | 返回创建的组合路径效果对象，可通过[Pen.setPathEffect]{ |

## createComposePathEffect

```TypeScript
static createComposePathEffect(outer: PathEffect, inner: PathEffect): PathEffect | undefined
```

创建组合路径效果对象，首先应用内部路径效果，然后应用外部路径效果。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-PathEffect-static createComposePathEffect(outer: PathEffect, inner: PathEffect): PathEffect | undefined--><!--Device-PathEffect-static createComposePathEffect(outer: PathEffect, inner: PathEffect): PathEffect | undefined-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| outer | [PathEffect](arkts-arkgraphics2d-drawing-patheffect-c.md) | Yes | 组合路径效果中的外部路径效果，在内部路径效果应用之后进行叠加处理，决定最终呈现的叠加效果。 |
| inner | [PathEffect](arkts-arkgraphics2d-drawing-patheffect-c.md) | Yes | 组合路径效果中的内部路径效果，首先应用于原始路径，作为第一层效果处理，随后再由外部路径效果进行叠加。 |

**Return value:**

| Type | Description |
| --- | --- |
| [PathEffect](arkts-arkgraphics2d-drawing-patheffect-c.md) | 返回创建的组合路径效果对象，可通过[Pen.setPathEffect]{ |

## createCornerPathEffect

```TypeScript
static createCornerPathEffect(radius: number): PathEffect
```

创建将路径的夹角变成指定半径的圆角的路径效果对象。该效果会在路径的每个夹角处插入指定半径的弧线段，将原有的尖锐转角替换为平滑的圆角过渡。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-PathEffect-static createCornerPathEffect(radius: number): PathEffect--><!--Device-PathEffect-static createCornerPathEffect(radius: number): PathEffect-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| radius | number | Yes | 圆角的半径，取值范围>0，该参数为浮点数。单位为物理像素px。 |

**Return value:**

| Type | Description |
| --- | --- |
| [PathEffect](arkts-arkgraphics2d-drawing-patheffect-c.md) | 返回创建的圆角路径效果对象，可通过[Pen.setPathEffect]{ |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |

## createCornerPathEffect

```TypeScript
static createCornerPathEffect(radius: double): PathEffect | undefined
```

创建将路径的夹角变成指定半径的圆角的路径效果对象。该效果会在路径的每个夹角处插入指定半径的弧线段，将原有的尖锐转角替换为平滑的圆角过渡。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-PathEffect-static createCornerPathEffect(radius: double): PathEffect | undefined--><!--Device-PathEffect-static createCornerPathEffect(radius: double): PathEffect | undefined-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| radius | double | Yes | 圆角的半径，取值范围>0，该参数为浮点数。单位为物理像素px。 |

**Return value:**

| Type | Description |
| --- | --- |
| [PathEffect](arkts-arkgraphics2d-drawing-patheffect-c.md) | 返回创建的圆角路径效果对象，可通过[Pen.setPathEffect]{ |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |

## createDashPathEffect

```TypeScript
static createDashPathEffect(intervals: Array<number>, phase: number): PathEffect
```

创建将路径变为虚线的路径效果对象，通过指定ON/OFF长度数组生成规则间距的虚线。当需要自定义形状作为虚线段填充时，可使用  
[createPathDashEffect](arkts-arkgraphics2d-drawing-patheffect-c.md#createpathdasheffect)。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-PathEffect-static createDashPathEffect(intervals: Array<number>, phase: number): PathEffect--><!--Device-PathEffect-static createDashPathEffect(intervals: Array<number>, phase: number): PathEffect-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| intervals | Array&lt;number&gt; | Yes | 表示虚线的ON（实线部分）和OFF（空白部分）长度的数组，数组元素个数必须是偶数且>=2，数组元素为正整数。单位为物理像素px。 |
| phase | number | Yes | 绘制时的偏移量，用于调整虚线图案沿路径的起始位置，该参数为浮点数，偏移量会相对于intervals定义的虚线模式产生位移效果。单位为物理像素px。 |

**Return value:**

| Type | Description |
| --- | --- |
| [PathEffect](arkts-arkgraphics2d-drawing-patheffect-c.md) | 返回创建的虚线路径效果对象，可通过[Pen.setPathEffect]{ |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |

## createDashPathEffect

```TypeScript
static createDashPathEffect(intervals: Array<double>, phase: double): PathEffect | undefined
```

创建将路径变为虚线的路径效果对象，通过指定ON/OFF长度数组生成规则间距的虚线。当需要自定义形状作为虚线段填充时，可使用  
[createPathDashEffect](arkts-arkgraphics2d-drawing-patheffect-c.md#createpathdasheffect)。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-PathEffect-static createDashPathEffect(intervals: Array<double>, phase: double): PathEffect | undefined--><!--Device-PathEffect-static createDashPathEffect(intervals: Array<double>, phase: double): PathEffect | undefined-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| intervals | Array&lt;double&gt; | Yes | 表示虚线的ON（实线部分）和OFF（空白部分）长度的数组，数组元素个数必须是偶数且>=2，数组元素为正整数。单位为物理像素px。 |
| phase | double | Yes | 绘制时的偏移量，用于调整虚线图案沿路径的起始位置，该参数为浮点数，偏移量会相对于intervals定义的虚线模式产生位移效果。单位为物理像素px。 |

**Return value:**

| Type | Description |
| --- | --- |
| [PathEffect](arkts-arkgraphics2d-drawing-patheffect-c.md) | 返回创建的虚线路径效果对象，可通过[Pen.setPathEffect]{ |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |

## createDiscretePathEffect

```TypeScript
static createDiscretePathEffect(segLength: number, dev: number, seedAssist?: number): PathEffect
```

创建将路径打散为离散线段并对端点进行随机偏移的路径效果对象。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

<!--Device-PathEffect-static createDiscretePathEffect(segLength: number, dev: number, seedAssist?: number): PathEffect--><!--Device-PathEffect-static createDiscretePathEffect(segLength: number, dev: number, seedAssist?: number): PathEffect-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| segLength | number | Yes | 路径中每进行一次打散操作的长度，该参数为浮点数，传入负数或0时无效果。单位为物理像素px。 |
| dev | number | Yes | 绘制时每个离散线段端点的最大移动偏离量，该偏离量为浮点数。单位为物理像素px。 |
| seedAssist | number | No | 用于生成离散效果的伪随机种子，影响路径打散的随机分布模式。当需要可复现的离散效果时传入指定种子值；当不需要特定随机分布模式时可省略此参数，省略时默认值为0。该参 数为32位无符号整数。超出范围时，该参数值按32位无符号整数溢出回绕规则处理。 |

**Return value:**

| Type | Description |
| --- | --- |
| [PathEffect](arkts-arkgraphics2d-drawing-patheffect-c.md) | 返回创建的离散路径效果对象，可通过[Pen.setPathEffect]{ |

## createDiscretePathEffect

```TypeScript
static createDiscretePathEffect(segLength: double, dev: double, seedAssist?: int): PathEffect | undefined
```

创建将路径打散为离散线段并对端点进行随机偏移的路径效果对象。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-PathEffect-static createDiscretePathEffect(segLength: double, dev: double, seedAssist?: int): PathEffect | undefined--><!--Device-PathEffect-static createDiscretePathEffect(segLength: double, dev: double, seedAssist?: int): PathEffect | undefined-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| segLength | double | Yes | 路径中每进行一次打散操作的长度，该参数为浮点数，传入负数或0时无效果。单位为物理像素px。 |
| dev | double | Yes | 绘制时每个离散线段端点的最大移动偏离量，该偏离量为浮点数。单位为物理像素px。 |
| seedAssist | int | No | 用于生成离散效果的伪随机种子，影响路径打散的随机分布模式。当需要可复现的离散效果时传入指定种子值；当不需要特定随机分布模式时可省略此参数，省略时默认值为0。该参 数为32位无符号整数。超出范围时，该参数值按32位无符号整数溢出回绕规则处理。 |

**Return value:**

| Type | Description |
| --- | --- |
| [PathEffect](arkts-arkgraphics2d-drawing-patheffect-c.md) | 返回创建的离散路径效果对象，可通过[Pen.setPathEffect]{ |

## createPathDashEffect

```TypeScript
static createPathDashEffect(path: Path, advance: number, phase: number, style: PathDashStyle): PathEffect
```

创建一个虚线路径效果对象，通过路径描述的形状生成。与  
[createDashPathEffect](arkts-arkgraphics2d-drawing-patheffect-c.md#createdashpatheffect)使用intervals数组指定ON/OFF长度创建规则间距虚线不同，本接口通过Path指定虚线段的图形形状。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

<!--Device-PathEffect-static createPathDashEffect(path: Path, advance: number, phase: number, style: PathDashStyle): PathEffect--><!--Device-PathEffect-static createPathDashEffect(path: Path, advance: number, phase: number, style: PathDashStyle): PathEffect-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | [Path](arkts-arkgraphics2d-drawing-path-c.md) | Yes | 通过该路径生成一个图形，用来填充每个虚线段。 |
| advance | number | Yes | 虚线段的步长，取值范围>0，否则会抛错误码。单位为物理像素px。 |
| phase | number | Yes | 表示虚线段内图形在虚线步长范围内的偏移量，该参数为浮点数，效果为先对偏移量取绝对值，然后对步长取模。单位为物理像素px。 |
| style | [PathDashStyle](arkts-arkgraphics2d-drawing-pathdashstyle-e.md) | Yes | 指定虚线效果的样式，决定虚线段图形在路径上的变换方式。 |

**Return value:**

| Type | Description |
| --- | --- |
| [PathEffect](arkts-arkgraphics2d-drawing-patheffect-c.md) | 返回创建的虚线路径效果对象，可通过[Pen.setPathEffect]{ |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |

## createPathDashEffect

```TypeScript
static createPathDashEffect(path: Path, advance: double, phase: double,
        style: PathDashStyle): PathEffect | undefined
```

创建一个虚线路径效果对象，通过路径描述的形状生成。与  
[createDashPathEffect](arkts-arkgraphics2d-drawing-patheffect-c.md#createdashpatheffect)使用intervals数组指定ON/OFF长度创建规则间距虚线不同，本接口通过Path指定虚线段的图形形状。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-PathEffect-static createPathDashEffect(path: Path, advance: double, phase: double,        style: PathDashStyle): PathEffect | undefined--><!--Device-PathEffect-static createPathDashEffect(path: Path, advance: double, phase: double,        style: PathDashStyle): PathEffect | undefined-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | [Path](arkts-arkgraphics2d-drawing-path-c.md) | Yes | 通过该路径生成一个图形，用来填充每个虚线段。 |
| advance | double | Yes | 虚线段的步长，取值范围>0，否则会抛错误码。单位为物理像素px。 |
| phase | double | Yes | 表示虚线段内图形在虚线步长范围内的偏移量，该参数为浮点数，效果为先对偏移量取绝对值，然后对步长取模。单位为物理像素px。 |
| style | [PathDashStyle](arkts-arkgraphics2d-drawing-pathdashstyle-e.md) | Yes | 指定虚线效果的样式，决定虚线段图形在路径上的变换方式。 |

**Return value:**

| Type | Description |
| --- | --- |
| [PathEffect](arkts-arkgraphics2d-drawing-patheffect-c.md) | 返回创建的虚线路径效果对象，可通过[Pen.setPathEffect]{ |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; &lt;br&gt;2. Incorrect parameter types; 3. Parameter verification failed. |

## createSumPathEffect

```TypeScript
static createSumPathEffect(firstPathEffect: PathEffect, secondPathEffect: PathEffect): PathEffect
```

创建一个叠加的路径效果。与  
[createComposePathEffect](arkts-arkgraphics2d-drawing-patheffect-c.md#createcomposepatheffect)不同，此接口会分别对两个参数的效果各自独立进行表现，然后将两个效果简单重叠显示。

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

<!--Device-PathEffect-static createSumPathEffect(firstPathEffect: PathEffect, secondPathEffect: PathEffect): PathEffect--><!--Device-PathEffect-static createSumPathEffect(firstPathEffect: PathEffect, secondPathEffect: PathEffect): PathEffect-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| firstPathEffect | [PathEffect](arkts-arkgraphics2d-drawing-patheffect-c.md) | Yes | 表示第一个路径效果。 |
| secondPathEffect | [PathEffect](arkts-arkgraphics2d-drawing-patheffect-c.md) | Yes | 表示第二个路径效果。 |

**Return value:**

| Type | Description |
| --- | --- |
| [PathEffect](arkts-arkgraphics2d-drawing-patheffect-c.md) | 返回创建的叠加路径效果对象，可通过[Pen.setPathEffect]{ |

## createSumPathEffect

```TypeScript
static createSumPathEffect(firstPathEffect: PathEffect, secondPathEffect: PathEffect): PathEffect | undefined
```

创建一个叠加的路径效果。与  
[createComposePathEffect](arkts-arkgraphics2d-drawing-patheffect-c.md#createcomposepatheffect)不同，此接口会分别对两个参数的效果各自独立进行表现，然后将两个效果简单重叠显示。

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-PathEffect-static createSumPathEffect(firstPathEffect: PathEffect, secondPathEffect: PathEffect): PathEffect | undefined--><!--Device-PathEffect-static createSumPathEffect(firstPathEffect: PathEffect, secondPathEffect: PathEffect): PathEffect | undefined-End-->

**System capability:** SystemCapability.Graphics.Drawing

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| firstPathEffect | [PathEffect](arkts-arkgraphics2d-drawing-patheffect-c.md) | Yes | 表示第一个路径效果。 |
| secondPathEffect | [PathEffect](arkts-arkgraphics2d-drawing-patheffect-c.md) | Yes | 表示第二个路径效果。 |

**Return value:**

| Type | Description |
| --- | --- |
| [PathEffect](arkts-arkgraphics2d-drawing-patheffect-c.md) | 返回创建的叠加路径效果对象，可通过[Pen.setPathEffect]{ |

