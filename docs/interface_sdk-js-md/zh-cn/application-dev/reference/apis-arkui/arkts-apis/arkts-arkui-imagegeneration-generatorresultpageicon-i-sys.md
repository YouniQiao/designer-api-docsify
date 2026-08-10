# GeneratorResultPageIcon（系统接口）

Custom icon object in the generation result page of ImageGeneratorDialog.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-imageGeneration-interface GeneratorResultPageIcon--><!--Device-imageGeneration-interface GeneratorResultPageIcon-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { imageGeneration } from 'kits/@kit.ArkUI';
```

## callback

```TypeScript
callback: Callback<GeneratorResult>
```

Icon click event callback.

**类型：** [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;GeneratorResult&gt;

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-GeneratorResultPageIcon-callback: Callback<GeneratorResult>--><!--Device-GeneratorResultPageIcon-callback: Callback<GeneratorResult>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

## image

```TypeScript
image: image.PixelMap | string | Resource
```

Icon image information.

**类型：** image.PixelMap \| string \| Resource

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-GeneratorResultPageIcon-image: image.PixelMap | string | Resource--><!--Device-GeneratorResultPageIcon-image: image.PixelMap | string | Resource-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

## text

```TypeScript
text: ResourceStr
```

Icon text description.

**类型：** [ResourceStr](arkts-arkui-resourcestr-t.md)

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-GeneratorResultPageIcon-text: ResourceStr--><!--Device-GeneratorResultPageIcon-text: ResourceStr-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

