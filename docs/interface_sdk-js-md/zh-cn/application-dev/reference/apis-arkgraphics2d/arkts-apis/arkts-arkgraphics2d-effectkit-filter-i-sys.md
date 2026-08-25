# Filter

图像效果类，用于通过链式调用将指定效果添加到效果链表中，适用于图片滤镜处理、视觉效果增强、图像美化等场景。 在调用Filter的方法前，需要先通过[createEffect](arkts-arkgraphics2d-effectkit-createeffect-f.md)创建一个Filter实例。 在添加效果后，需调用[getEffectPixelMap](arkts-arkgraphics2d-effectkit-filter-i.md#geteffectpixelmap)获取处理后的图像。

**起始版本：** 9

**系统能力：** SystemCapability.Multimedia.Image.Core

## 导入模块

```TypeScript
import { effectKit } from 'kits/@kit.ArkGraphics2D';
```

## ellipticalGradientBlur

```TypeScript
ellipticalGradientBlur(blurRadius: number, center: EllipticalMaskCenter,
      maskRadius: EllipticalMaskRadius, fractionStops: FractionStop[]): Filter
```

将带有椭圆形遮罩的渐变模糊效果添加到效果链表中，返回链表的头节点。

**起始版本：** 23

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [blurRadius](arkts-arkgraphics2d-text-textshadow-i.md) | number | 是 |
| center | [EllipticalMaskCenter](arkts-arkgraphics2d-effectkit-ellipticalmaskcenter-t-sys.md) | 是 |
| maskRadius | [EllipticalMaskRadius](arkts-arkgraphics2d-effectkit-ellipticalmaskradius-t-sys.md) | 是 |
| [fractionStops](../../apis-arkui/arkts-components/arkts-arkui-lineargradientbluroptions-i.md) | [FractionStop](../../apis-arkui/arkts-components/arkts-arkui-fractionstop-t.md)[] | 是 |

**返回值：**

| 类型 |
| --- |
| [Filter](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-agent-filter-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
