# Mask（系统接口）

Mask效果类，作为Filter以及VisualEffect的输入使用。不同类型的Mask提供不同的灰度分布模式，如波环遮罩、径向渐变、像素图遮罩等。

**起始版本：** 20

**系统能力：** SystemCapability.Graphics.Drawing

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { uiEffect } from 'kits/@kit.ArkGraphics2D';
```

## createPixelMapMask

```TypeScript
static createPixelMapMask(pixelMap: image.PixelMap, srcRect: common2D.Rect, dstRect: common2D.Rect,
      fillColor?: Color): Mask
```

通过输入的pixelMap，以及pixelMap的待绘制区域、挂载节点的绘制区域和绘制区域外填充的颜色创建具有缩放效果的Mask实例。

**起始版本：** 20

**系统能力：** SystemCapability.Graphics.Drawing

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| pixelMap | image.PixelMap | 是 |
| srcRect | common2D.Rect | 是 |
| dstRect | common2D.Rect | 是 |
| fillColor | [Color](../../apis-arkgraphics3d/arkts-apis/arkts-arkgraphics3d-scenetypes-color-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| [Mask](arkts-arkgraphics2d-uieffect-mask-c-sys.md) |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## createPixelMapMask

```TypeScript
static createPixelMapMask(pixelMap: image.PixelMap): Mask
```

通过输入的pixelMap创建Mask实例。该接口不会对传入的pixelMap进行缩放处理。

**起始版本：** 22

**系统能力：** SystemCapability.Graphics.Drawing

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| pixelMap | image.PixelMap | 是 |

**返回值：**

| 类型 |
| --- |
| [Mask](arkts-arkgraphics2d-uieffect-mask-c-sys.md) |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## createRadialGradientMask

```TypeScript
static createRadialGradientMask(center: common2D.Point, radiusX: number, radiusY: number,
      gradients: Array<[number, number]>): Mask
```

通过输入椭圆中心点的位置、长短轴和形状参数创建椭圆遮罩效果Mask实例。

**起始版本：** 20

**系统能力：** SystemCapability.Graphics.Drawing

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| center | common2D.Point | 是 |
| radiusX | number | 是 |
| radiusY | number | 是 |
| gradients | Array & lt;[number, number] & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| [Mask](arkts-arkgraphics2d-uieffect-mask-c-sys.md) |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## createRippleMask

```TypeScript
static createRippleMask(center: common2D.Point, radius: number, width: number, offset?: number): Mask
```

通过输入波环圆心的位置、半径和宽度创建波环遮罩效果Mask实例。

**起始版本：** 20

**系统能力：** SystemCapability.Graphics.Drawing

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| center | common2D.Point | 是 |
| radius | number | 是 |
| width | number | 是 |
| offset | number | 否 |

**返回值：**

| 类型 |
| --- |
| [Mask](arkts-arkgraphics2d-uieffect-mask-c-sys.md) |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## createUseEffectMask

```TypeScript
static createUseEffectMask(useEffect: boolean): Mask
```

创建并设置Mask实例是否使用模糊缓存。此Mask实例专为liquidMaterial方法的useEffectMask参数设计， 用于声明材质效果是否使用模糊缓存以提升性能。将此Mask实例用于其他Filter或VisualEffect方法时， useEffect属性可能不生效。

**起始版本：** 22

**系统能力：** SystemCapability.Graphics.Drawing

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [useEffect](../../apis-arkui/arkts-components/arkts-arkui-commonmethod-c.md) | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| [Mask](arkts-arkgraphics2d-uieffect-mask-c-sys.md) |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## createWaveGradientMask

```TypeScript
static createWaveGradientMask(center: common2D.Point, width: number, propagationRadius: number,
      blurRadius: number, turbulenceStrength?: number): Mask
```

输入波源中心位置、单波参数创建单波遮罩效果Mask实例。

**起始版本：** 20

**系统能力：** SystemCapability.Graphics.Drawing

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| center | common2D.Point | 是 |
| width | number | 是 |
| propagationRadius | number | 是 |
| [blurRadius](arkts-arkgraphics2d-text-textshadow-i.md) | number | 是 |
| turbulenceStrength | number | 否 |

**返回值：**

| 类型 |
| --- |
| [Mask](arkts-arkgraphics2d-uieffect-mask-c-sys.md) |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
