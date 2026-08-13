# PathIterator

表示路径操作迭代器，可通过遍历迭代器逐段读取路径的操作指令。 迭代器按顺序遍历路径中的操作指令，便于实现对路径的细粒度分析与自定义处理。 > **说明：** > > - 本Class首批接口从API version 18开始支持。 > > - 本模块使用屏幕物理像素单位px。 > > - 本模块为单线程模型策略，需要调用方自行管理线程安全和上下文状态的切换。

**起始版本：** 23

**废弃版本：** -1

<!--Device-drawing-class PathIterator--><!--Device-drawing-class PathIterator-End-->

**系统能力：** SystemCapability.Graphics.Drawing

## constructor

```TypeScript
constructor(path: Path)
```

构造迭代器并绑定路径。

**起始版本：** 23

**废弃版本：** -1

<!--Device-PathIterator-constructor(path: Path)--><!--Device-PathIterator-constructor(path: Path)-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | [Path](arkts-arkgraphics2d-drawing-path-c.md) | 是 |

## hasNext

```TypeScript
hasNext(): boolean
```

判断迭代器中是否还有下一个操作。通常与next()或peek()方法配合使用实现路径遍历。

**起始版本：** 23

**废弃版本：** -1

<!--Device-PathIterator-hasNext(): boolean--><!--Device-PathIterator-hasNext(): boolean-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| boolean |

## next

```TypeScript
next(points: Array<common2D.Point>, offset?: number): PathIteratorVerb
```

返回当前路径的下一个操作，并将迭代器推进至该操作，同时将路径坐标点数据按操作类型写入传入的points数组。 若仅需预览下一个操作而不改变迭代器状态，请使用[peek](#peek)。 通常与[hasNext](#hasNext)方法配合使用实现路径遍历。

**起始版本：** 18

**废弃版本：** -1

<!--Device-PathIterator-next(points: Array<common2D.Point>, offset?: number): PathIteratorVerb--><!--Device-PathIterator-next(points: Array<common2D.Point>, offset?: number): PathIteratorVerb-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| points | Array & lt;common2D.Point & gt; | 是 |
| offset | number | 否 |

**返回值：**

| 类型 |
| --- |
| [PathIteratorVerb](arkts-arkgraphics2d-drawing-pathiteratorverb-e.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## next

```TypeScript
next(points: Array<common2D.Point>, offset?: number): PathIteratorVerb | undefined
```

返回当前路径的下一个操作，并将迭代器推进至该操作，同时将路径坐标点数据按操作类型写入传入的points数组。 若仅需预览下一个操作而不改变迭代器状态，请使用[peek](#peek)。 通常与[hasNext](#hasNext)方法配合使用实现路径遍历。

**起始版本：** 23

**废弃版本：** -1

<!--Device-PathIterator-next(points: Array<common2D.Point>, offset?: int): PathIteratorVerb | undefined--><!--Device-PathIterator-next(points: Array<common2D.Point>, offset?: int): PathIteratorVerb | undefined-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| points | Array & lt;common2D.Point & gt; | 是 |
| offset | number | 否 |

**返回值：**

| 类型 |
| --- |
| [PathIteratorVerb](arkts-arkgraphics2d-drawing-pathiteratorverb-e.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## peek

```TypeScript
peek(): PathIteratorVerb
```

返回当前路径的下一个操作，迭代器保持在原操作。与next不同，peek不会推进迭代器位置。

**起始版本：** 18

**废弃版本：** -1

<!--Device-PathIterator-peek(): PathIteratorVerb--><!--Device-PathIterator-peek(): PathIteratorVerb-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| [PathIteratorVerb](arkts-arkgraphics2d-drawing-pathiteratorverb-e.md) |

## peek

```TypeScript
peek(): PathIteratorVerb | undefined
```

返回当前路径的下一个操作，迭代器保持在原操作。与next不同，peek不会推进迭代器位置。

**起始版本：** 23

**废弃版本：** -1

<!--Device-PathIterator-peek(): PathIteratorVerb | undefined--><!--Device-PathIterator-peek(): PathIteratorVerb | undefined-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**返回值：**

| 类型 |
| --- |
| [PathIteratorVerb](arkts-arkgraphics2d-drawing-pathiteratorverb-e.md) |
