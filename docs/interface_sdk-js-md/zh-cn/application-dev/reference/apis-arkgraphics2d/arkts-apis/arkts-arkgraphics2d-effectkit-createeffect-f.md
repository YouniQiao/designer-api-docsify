# createEffect

## 导入模块

```TypeScript
import { effectKit } from 'kits/@kit.ArkGraphics2D';
```

## createEffect

```TypeScript
function createEffect(source: image.PixelMap): Filter
```

通过传入的PixelMap创建Filter实例。后续可通过链式调用添加各种图像效果， 最终通过[getEffectPixelMap](arkts-arkgraphics2d-effectkit-filter-i.md#geteffectpixelmap)获取处理后的图像。

**起始版本：** 9

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本12开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.Multimedia.Image.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| source | image.PixelMap | 是 |

**返回值：**

| 类型 |
| --- |
| [Filter](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-agent-filter-i.md) |
