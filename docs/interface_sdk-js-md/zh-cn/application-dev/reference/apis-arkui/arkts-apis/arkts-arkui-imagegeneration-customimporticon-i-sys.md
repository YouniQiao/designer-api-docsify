# CustomImportIcon（系统接口）

Customize the import icon, which is used to add images and text from the application side.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

<!--Device-imageGeneration-interface CustomImportIcon--><!--Device-imageGeneration-interface CustomImportIcon-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { imageGeneration } from 'kits/@kit.ArkUI';
```

## callback

```TypeScript
callback: CustomImportCallback
```

Async callback function for import operation.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-CustomImportIcon-callback: CustomImportCallback--><!--Device-CustomImportIcon-callback: CustomImportCallback-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

## image

```TypeScript
image: image.PixelMap | ResourceStr
```

Icon image information.

**类型：** image.PixelMap \| ResourceStr

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-CustomImportIcon-image: image.PixelMap | ResourceStr--><!--Device-CustomImportIcon-image: image.PixelMap | ResourceStr-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

## text

```TypeScript
text: ResourceStr
```

Icon text description.

**类型：** [ResourceStr](arkts-arkui-resourcestr-t.md)

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-CustomImportIcon-text: ResourceStr--><!--Device-CustomImportIcon-text: ResourceStr-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**系统接口：** 此接口为系统接口。

