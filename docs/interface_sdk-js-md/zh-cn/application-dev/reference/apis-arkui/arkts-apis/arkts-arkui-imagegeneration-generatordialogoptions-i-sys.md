# GeneratorDialogOptions（系统接口）

Parameters used to open the ImageGeneratorDialog.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

<!--Device-imageGeneration-interface GeneratorDialogOptions--><!--Device-imageGeneration-interface GeneratorDialogOptions-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { imageGeneration } from 'kits/@kit.ArkUI';
```

## content

```TypeScript
content?: ResourceStr
```

Initial text information used for AI-generated image tasks.

**类型：** [ResourceStr](arkts-arkui-resourcestr-t.md)

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-GeneratorDialogOptions-content?: ResourceStr--><!--Device-GeneratorDialogOptions-content?: ResourceStr-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

## customIcons

```TypeScript
customIcons?: Array<GeneratorResultPageIcon>
```

Custom icons used on the AI generated image results page.

**类型：** Array&lt;GeneratorResultPageIcon&gt;

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-GeneratorDialogOptions-customIcons?: Array<GeneratorResultPageIcon>--><!--Device-GeneratorDialogOptions-customIcons?: Array<GeneratorResultPageIcon>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

## customImportIcon

```TypeScript
customImportIcon?: CustomImportIcon
```

The following configuration parameters are used to customize the imported icon.

**类型：** [CustomImportIcon](arkts-arkui-imagegeneration-customimporticon-i-sys.md)

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-GeneratorDialogOptions-customImportIcon?: CustomImportIcon--><!--Device-GeneratorDialogOptions-customImportIcon?: CustomImportIcon-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

## imageGenerationModel

```TypeScript
imageGenerationModel?: ImageGenerationModel
```

Model used for AI generate image tasks.

**类型：** [ImageGenerationModel](arkts-arkui-imagegeneration-imagegenerationmodel-i-sys.md)

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-GeneratorDialogOptions-imageGenerationModel?: ImageGenerationModel--><!--Device-GeneratorDialogOptions-imageGenerationModel?: ImageGenerationModel-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

## images

```TypeScript
images?: Array<ImageItem>
```

Initial image parameters used for AI-generated image tasks.

**类型：** Array&lt;ImageItem&gt;

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-GeneratorDialogOptions-images?: Array<ImageItem>--><!--Device-GeneratorDialogOptions-images?: Array<ImageItem>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

## liveViewInfo

```TypeScript
liveViewInfo?: LiveViewInfo
```

Information for LiveView in AI image generation.

**类型：** [LiveViewInfo](arkts-arkui-imagegeneration-liveviewinfo-i-sys.md)

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-GeneratorDialogOptions-liveViewInfo?: LiveViewInfo--><!--Device-GeneratorDialogOptions-liveViewInfo?: LiveViewInfo-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

## minimizeDuringGeneration

```TypeScript
minimizeDuringGeneration?: boolean
```

Indicates whether to enable minimize during image generation.

**类型：** boolean

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-GeneratorDialogOptions-minimizeDuringGeneration?: boolean--><!--Device-GeneratorDialogOptions-minimizeDuringGeneration?: boolean-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

## onAreaDidChange

```TypeScript
onAreaDidChange?: Callback<common2D.Rect>
```

Callback triggered when the ImageGeneratorDialog changes in size or position.

**类型：** [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;common2D.Rect&gt;

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-GeneratorDialogOptions-onAreaDidChange?: Callback<common2D.Rect>--><!--Device-GeneratorDialogOptions-onAreaDidChange?: Callback<common2D.Rect>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

## recoverFromCache

```TypeScript
recoverFromCache?: boolean
```

Whether to recover from cache for AI image generation.The persistent cache file is used to store configuration parameters for AI image generation.

**类型：** boolean

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-GeneratorDialogOptions-recoverFromCache?: boolean--><!--Device-GeneratorDialogOptions-recoverFromCache?: boolean-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

## textGenerationModel

```TypeScript
textGenerationModel?: TextGenerationModel
```

Text polishing model used in AI generate image tasks.

**类型：** [TextGenerationModel](arkts-arkui-imagegeneration-textgenerationmodel-i-sys.md)

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-GeneratorDialogOptions-textGenerationModel?: TextGenerationModel--><!--Device-GeneratorDialogOptions-textGenerationModel?: TextGenerationModel-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

