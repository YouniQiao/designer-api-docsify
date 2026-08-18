# RoundRect

圆角矩形对象。支持设置和获取指定圆角位置的圆角半径，以及对圆角矩形进行平移操作。 > **说明：** > > - 本Class首批接口从API version 12开始支持。 > > - 本模块使用屏幕物理像素单位px。 > > - 本模块为单线程模型策略，需要调用方自行管理线程安全和上下文状态的切换。

**起始版本：** 23

<!--Device-drawing-class RoundRect--><!--Device-drawing-class RoundRect-End-->

**系统能力：** SystemCapability.Graphics.Drawing

## 导入模块

```TypeScript
```

## constructor

```TypeScript
constructor(roundRect: RoundRect)
```

拷贝一个圆角矩形。

**起始版本：** 23

<!--Device-RoundRect-constructor(roundRect: RoundRect)--><!--Device-RoundRect-constructor(roundRect: RoundRect)-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| roundRect | [RoundRect](arkts-arkgraphics2d-drawing-roundrect-c.md) | 是 |

## constructor

```TypeScript
constructor(rect: common2D.Rect, xRadii: number, yRadii: number)
```

构造一个圆角矩形对象，当且仅当xRadii和yRadii均大于0时，圆角生效，否则只会构造一个矩形。

**起始版本：** 23

<!--Device-RoundRect-constructor(rect: common2D.Rect, xRadii: double, yRadii: double)--><!--Device-RoundRect-constructor(rect: common2D.Rect, xRadii: double, yRadii: double)-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| rect | common2D.Rect | 是 |
| xRadii | number | 是 |
| yRadii | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## getCorner

```TypeScript
getCorner(pos: CornerPos): common2D.Point
```

获取圆角矩形中指定圆角位置的圆角半径。

**起始版本：** 12

<!--Device-RoundRect-getCorner(pos: CornerPos): common2D.Point--><!--Device-RoundRect-getCorner(pos: CornerPos): common2D.Point-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| pos | [CornerPos](arkts-arkgraphics2d-drawing-cornerpos-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| common2D.Point |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## getCorner

```TypeScript
getCorner(pos: CornerPos): common2D.Point | undefined
```

获取圆角矩形中指定圆角位置的圆角半径。

**起始版本：** 23

<!--Device-RoundRect-getCorner(pos: CornerPos): common2D.Point | undefined--><!--Device-RoundRect-getCorner(pos: CornerPos): common2D.Point | undefined-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| pos | [CornerPos](arkts-arkgraphics2d-drawing-cornerpos-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| common2D.Point |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## offset

```TypeScript
offset(dx: number, dy: number): void
```

将圆角矩形沿x轴方向平移dx、沿y轴方向平移dy。

**起始版本：** 23

<!--Device-RoundRect-offset(dx: double, dy: double): void--><!--Device-RoundRect-offset(dx: double, dy: double): void-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| dx | number | 是 |
| dy | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## setCorner

```TypeScript
setCorner(pos: CornerPos, x: number, y: number): void
```

设置圆角矩形中指定圆角位置的圆角半径。

**起始版本：** 23

<!--Device-RoundRect-setCorner(pos: CornerPos, x: double, y: double): void--><!--Device-RoundRect-setCorner(pos: CornerPos, x: double, y: double): void-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| pos | [CornerPos](arkts-arkgraphics2d-drawing-cornerpos-e.md) | 是 |
| x | number | 是 |
| y | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
