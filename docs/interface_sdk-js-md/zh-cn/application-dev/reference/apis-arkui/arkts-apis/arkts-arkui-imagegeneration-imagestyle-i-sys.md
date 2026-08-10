# ImageStyle（系统接口）

Style types supported by AI image generation models, like Graffiti, Watercolor.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-imageGeneration-interface ImageStyle--><!--Device-imageGeneration-interface ImageStyle-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { imageGeneration } from 'kits/@kit.ArkUI';
```

## icon

```TypeScript
icon: image.PixelMap | string | Resource
```

The style icon information which will display in style list.

**类型：** image.PixelMap \| string \| Resource

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ImageStyle-icon: image.PixelMap | string | Resource--><!--Device-ImageStyle-icon: image.PixelMap | string | Resource-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

## name

```TypeScript
name: ResourceStr
```

The style name information which will display in style list.

**类型：** [ResourceStr](arkts-arkui-resourcestr-t.md)

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ImageStyle-name: ResourceStr--><!--Device-ImageStyle-name: ResourceStr-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

