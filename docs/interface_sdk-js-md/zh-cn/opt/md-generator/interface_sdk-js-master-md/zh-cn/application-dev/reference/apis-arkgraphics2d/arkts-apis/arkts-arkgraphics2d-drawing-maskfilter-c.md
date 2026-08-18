# MaskFilter

蒙版滤镜对象，用于对绘制内容施加模糊效果。 > **说明：** > > - 本Class首批接口从API version 12开始支持。 > > - 本模块使用屏幕物理像素单位px。 > > - 本模块为单线程模型策略，需要调用方自行管理线程安全和上下文状态的切换。

**起始版本：** 23

<!--Device-drawing-class MaskFilter--><!--Device-drawing-class MaskFilter-End-->

**系统能力：** SystemCapability.Graphics.Drawing

## 导入模块

```TypeScript
```

## createBlurMaskFilter

```TypeScript
static createBlurMaskFilter(blurType: BlurType, sigma: number): MaskFilter
```

创建具有模糊效果的蒙版滤镜。

**起始版本：** 12

<!--Device-MaskFilter-static createBlurMaskFilter(blurType: BlurType, sigma: number): MaskFilter--><!--Device-MaskFilter-static createBlurMaskFilter(blurType: BlurType, sigma: number): MaskFilter-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| blurType | [BlurType](arkts-arkgraphics2d-drawing-blurtype-e.md) | 是 |
| sigma | number | 是 |

**返回值：**

| 类型 |
| --- |
| [MaskFilter](arkts-arkgraphics2d-drawing-maskfilter-c.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## createBlurMaskFilter

```TypeScript
static createBlurMaskFilter(blurType: BlurType, sigma: number): MaskFilter | undefined
```

创建具有模糊效果的蒙版滤镜。

**起始版本：** 23

<!--Device-MaskFilter-static createBlurMaskFilter(blurType: BlurType, sigma: double): MaskFilter | undefined--><!--Device-MaskFilter-static createBlurMaskFilter(blurType: BlurType, sigma: double): MaskFilter | undefined-End-->

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| blurType | [BlurType](arkts-arkgraphics2d-drawing-blurtype-e.md) | 是 |
| sigma | number | 是 |

**返回值：**

| 类型 |
| --- |
| [MaskFilter](arkts-arkgraphics2d-drawing-maskfilter-c.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
