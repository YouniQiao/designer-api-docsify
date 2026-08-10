# GeneratorResult（系统接口）

The result of AI-generated images

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-imageGeneration-interface GeneratorResult--><!--Device-imageGeneration-interface GeneratorResult-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { imageGeneration } from 'kits/@kit.ArkUI';
```

## image

```TypeScript
image?: image.PixelMap
```

Decoded data of AI-generated images.

**类型：** image.PixelMap

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-GeneratorResult-image?: image.PixelMap--><!--Device-GeneratorResult-image?: image.PixelMap-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

## statistic

```TypeScript
statistic: TaskStatistic
```

Statistics of AI-generated image tasks.

**类型：** [TaskStatistic](arkts-arkui-imagegeneration-taskstatistic-i-sys.md)

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-GeneratorResult-statistic: TaskStatistic--><!--Device-GeneratorResult-statistic: TaskStatistic-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

## url

```TypeScript
url?: string
```

The path information of AI-generated images.

**类型：** string

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-GeneratorResult-url?: string--><!--Device-GeneratorResult-url?: string-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

