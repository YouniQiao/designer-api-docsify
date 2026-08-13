# ShadowLayer

阴影层对象，通过设置模糊半径、偏移量和颜色，可为图形、文本等绘制内容添加阴影渲染效果。 > **说明：** > > - 本Class首批接口从API version 12开始支持。 > > - 本模块使用屏幕物理像素单位px。 > > - 本模块为单线程模型策略，需要调用方自行管理线程安全和上下文状态的切换。

**起始版本：** 23

**废弃版本：** -1

<!--Device-drawing-class ShadowLayer--><!--Device-drawing-class ShadowLayer-End-->

**系统能力：** SystemCapability.Graphics.Drawing

## create

```TypeScript
static create(blurRadius: number, x: number, y: number, color: common2D.Color): ShadowLayer
```

创建阴影层对象。

**起始版本：** 12

**废弃版本：** -1

<!--Device-ShadowLayer-static create(blurRadius: number, x: number, y: number, color: common2D.Color): ShadowLayer--><!--Device-ShadowLayer-static create(blurRadius: number, x: number, y: number, color: common2D.Color): ShadowLayer-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [blurRadius](arkts-arkgraphics2d-text-textshadow-i.md) | number | 是 |
| x | number | 是 |
| y | number | 是 |
| color | common2D.Color | 是 |

**返回值：**

| 类型 |
| --- |
| [ShadowLayer](arkts-arkgraphics2d-drawing-shadowlayer-c.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## create

```TypeScript
static create(blurRadius: number, x: number, y: number, color: common2D.Color): ShadowLayer | undefined
```

创建阴影层对象。

**起始版本：** 23

**废弃版本：** -1

<!--Device-ShadowLayer-static create(blurRadius: double, x: double, y: double, color: common2D.Color): ShadowLayer | undefined--><!--Device-ShadowLayer-static create(blurRadius: double, x: double, y: double, color: common2D.Color): ShadowLayer | undefined-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [blurRadius](arkts-arkgraphics2d-text-textshadow-i.md) | number | 是 |
| x | number | 是 |
| y | number | 是 |
| color | common2D.Color | 是 |

**返回值：**

| 类型 |
| --- |
| [ShadowLayer](arkts-arkgraphics2d-drawing-shadowlayer-c.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## create

```TypeScript
static create(blurRadius: number, x: number, y: number, color: common2D.Color | number): ShadowLayer
```

创建阴影层对象。

**起始版本：** 18

**废弃版本：** -1

<!--Device-ShadowLayer-static create(blurRadius: number, x: number, y: number, color: common2D.Color | number): ShadowLayer--><!--Device-ShadowLayer-static create(blurRadius: number, x: number, y: number, color: common2D.Color | number): ShadowLayer-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [blurRadius](arkts-arkgraphics2d-text-textshadow-i.md) | number | 是 |
| x | number | 是 |
| y | number | 是 |
| color | common2D.Color \| number | 是 |

**返回值：**

| 类型 |
| --- |
| [ShadowLayer](arkts-arkgraphics2d-drawing-shadowlayer-c.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## create

```TypeScript
static create(blurRadius: number, x: number, y: number, color: common2D.Color | number): ShadowLayer | undefined
```

创建阴影层对象。

**起始版本：** 23

**废弃版本：** -1

<!--Device-ShadowLayer-static create(blurRadius: double, x: double, y: double, color: common2D.Color | int): ShadowLayer | undefined--><!--Device-ShadowLayer-static create(blurRadius: double, x: double, y: double, color: common2D.Color | int): ShadowLayer | undefined-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [blurRadius](arkts-arkgraphics2d-text-textshadow-i.md) | number | 是 |
| x | number | 是 |
| y | number | 是 |
| color | common2D.Color \| number | 是 |

**返回值：**

| 类型 |
| --- |
| [ShadowLayer](arkts-arkgraphics2d-drawing-shadowlayer-c.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
