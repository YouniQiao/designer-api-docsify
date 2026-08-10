# GenerateImageTaskParams（系统接口）

Configuration parameter options for AI-generated image tasks.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-imageGeneration-interface GenerateImageTaskParams--><!--Device-imageGeneration-interface GenerateImageTaskParams-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { imageGeneration } from 'kits/@kit.ArkUI';
```

## imageCount

```TypeScript
imageCount?: int
```

the number of AI-generated image in one task.

**类型：** int

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-GenerateImageTaskParams-imageCount?: int--><!--Device-GenerateImageTaskParams-imageCount?: int-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

## imageSize

```TypeScript
imageSize: image.Size
```

the size information of AI-generated image in one task.

**类型：** image.Size

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-GenerateImageTaskParams-imageSize: image.Size--><!--Device-GenerateImageTaskParams-imageSize: image.Size-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

## images

```TypeScript
images: Array<ImageItem>
```

image information used for AI-generated image tasks.

**类型：** Array&lt;ImageItem&gt;

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-GenerateImageTaskParams-images: Array<ImageItem>--><!--Device-GenerateImageTaskParams-images: Array<ImageItem>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

## positionImage

```TypeScript
positionImage?: image.PixelMap
```

Location reference map for multi-image generated tasks.

**类型：** image.PixelMap

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-GenerateImageTaskParams-positionImage?: image.PixelMap--><!--Device-GenerateImageTaskParams-positionImage?: image.PixelMap-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

## prompt

```TypeScript
prompt: string
```

Description information for AI-generated image tasks.

**类型：** string

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-GenerateImageTaskParams-prompt: string--><!--Device-GenerateImageTaskParams-prompt: string-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

## selectPath

```TypeScript
selectPath?: Array<common2D.Point>
```

Path information for lasso selection in AI-generated image tasks.

**类型：** Array&lt;common2D.Point&gt;

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-GenerateImageTaskParams-selectPath?: Array<common2D.Point>--><!--Device-GenerateImageTaskParams-selectPath?: Array<common2D.Point>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

## style

```TypeScript
style?: string
```

the style of AI-generated image in one task.

**类型：** string

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-GenerateImageTaskParams-style?: string--><!--Device-GenerateImageTaskParams-style?: string-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

