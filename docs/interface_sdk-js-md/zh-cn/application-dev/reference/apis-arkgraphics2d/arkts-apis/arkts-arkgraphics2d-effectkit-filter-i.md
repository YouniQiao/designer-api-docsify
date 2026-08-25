# Filter

图像效果类，用于通过链式调用将指定效果添加到效果链表中，适用于图片滤镜处理、视觉效果增强、图像美化等场景。 在调用Filter的方法前，需要先通过[createEffect](arkts-arkgraphics2d-effectkit-createeffect-f.md)创建一个Filter实例。 在添加效果后，需调用[getEffectPixelMap](#geteffectpixelmap)获取处理后的图像。

**起始版本：** 9

**系统能力：** SystemCapability.Multimedia.Image.Core

## 导入模块

```TypeScript
import { effectKit } from 'kits/@kit.ArkGraphics2D';
```

## blur

```TypeScript
blur(radius: number): Filter
```

将模糊效果添加到效果链表中，返回链表的实例。着色器平铺模式使用DECAL，如需指定平铺模式， 可使用[blur](#blur)接口。 常用于实现背景虚化效果、隐私信息遮挡、毛玻璃背景效果、弹窗背景模糊等场景。

> **说明：**&gt;
> 该接口为静态模糊接口，为静态图像提供模糊化效果，如果要对组件进行实时渲染的模糊，可以使用[动态模糊](../../../ui/arkts-blur-effect.md)。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| radius | number | 是 |

**返回值：**

| 类型 |
| --- |
| [Filter](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-agent-filter-i.md) |

## blur

```TypeScript
blur(radius: number, tileMode: TileMode): Filter
```

将模糊效果添加到效果链表中，返回链表的实例。支持选择着色器效果平铺模式， 常用于实现背景虚化效果、隐私信息遮挡、毛玻璃背景效果、弹窗背景模糊等场景。

> **说明：**&gt;
> 该接口为静态模糊接口，为静态图像提供模糊化效果，如果要对组件进行实时渲染的模糊，可以使用[动态模糊](../../../ui/arkts-blur-effect.md)。

**起始版本：** 14

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| radius | number | 是 |
| tileMode | [TileMode](arkts-arkgraphics2d-effectkit-tilemode-e.md) | 是 |

**返回值：**

| 类型 |
| --- |
| [Filter](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-agent-filter-i.md) |

## brightness

```TypeScript
brightness(bright: number): Filter
```

将高亮效果添加到效果链表中，返回链表的实例。该方法通过调整图像亮度实现高亮效果， 常用于暗图增亮处理、图片预览亮度增强、夜间模式图片适配等场景。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bright | number | 是 |

**返回值：**

| 类型 |
| --- |
| [Filter](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-agent-filter-i.md) |

## getEffectPixelMap

```TypeScript
getEffectPixelMap(): Promise<image.PixelMap>
```

获取已添加链表效果的源图像的image.PixelMap，默认使用CPU渲染，使用Promise异步回调。 如需指定渲染模式，可使用[getEffectPixelMap](#geteffectpixelmap)接口。 常用于图片处理后需要保存或显示结果的场景。

> **说明：**&gt;
> 该方法默认使用CPU渲染，着色器平铺模式仅支持DECAL，其他模式（CLAMP、REPEAT、MIRROR）暂不支持。 如需使用GPU渲染或了解渲染模式对TileMode的影响，请参见[TileMode](arkts-arkgraphics2d-effectkit-tilemode-e.md)和 [getEffectPixelMap](#geteffectpixelmap)。

**起始版本：** 11

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

| 类型 |
| --- |
| Promise & lt;image.PixelMap & gt; |

## getEffectPixelMap

```TypeScript
getEffectPixelMap(useCpuRender : boolean): Promise<image.PixelMap>
```

获取已添加链表效果的源图像的image.PixelMap，支持指定渲染模式（CPU渲染或者GPU渲染），使用Promise异步回调。

**起始版本：** 20

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本20开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| useCpuRender | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;image.PixelMap & gt; |

## getPixelMap

```TypeScript
getPixelMap(): image.PixelMap
```

获取已添加链表效果的源图像的image.PixelMap。常用于图片处理后需要保存或显示结果的场景。

> **说明：**&gt;
> 从API version 9开始支持，从API version 11开始废弃，建议使用[getEffectPixelMap](#geteffectpixelmap)替代。

**起始版本：** 9

**废弃版本：** 11

**替代接口：** [getEffectPixelMap](#geteffectpixelmap)

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

| 类型 |
| --- |
| image.PixelMap |

## grayscale

```TypeScript
grayscale(): Filter
```

将灰度效果添加到效果链表中，返回链表的实例。该方法将彩色图像转换为灰度图像，通过加权计算RGB值得到灰度值。 常用于黑白风格照片生成、图片预处理去色、灰度图标制作等场景。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

| 类型 |
| --- |
| [Filter](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-agent-filter-i.md) |

## invert

```TypeScript
invert(): Filter
```

将反转效果添加到效果链表中，返回链表的实例。该方法将图像的RGB颜色值进行反转， 常用于实现底片效果、图片艺术处理、夜间模式适配等场景。

**起始版本：** 12

**系统能力：** SystemCapability.Multimedia.Image.Core

**返回值：**

| 类型 |
| --- |
| [Filter](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-agent-filter-i.md) |

## setColorMatrix

```TypeScript
setColorMatrix(colorMatrix: Array<number>): Filter
```

通过自定义颜色矩阵对图像进行颜色变换处理，将效果添加到效果链表中，返回链表的实例。 常用于实现预设滤镜不支持的自定义颜色效果，如复古色调、冷暖色调调整等场景。

**起始版本：** 12

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| colorMatrix | Array & lt;number & gt; | 是 |

**返回值：**

| 类型 |
| --- |
| [Filter](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-agent-filter-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
