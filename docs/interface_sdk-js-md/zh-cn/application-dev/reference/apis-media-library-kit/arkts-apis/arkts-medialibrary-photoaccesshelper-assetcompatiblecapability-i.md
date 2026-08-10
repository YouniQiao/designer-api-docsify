# AssetCompatibleCapability

Defines the asset compatibility capability.

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

<!--Device-photoAccessHelper-interface AssetCompatibleCapability--><!--Device-photoAccessHelper-interface AssetCompatibleCapability-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## 导入模块

```TypeScript
import { photoAccessHelper } from 'kits/@kit.MediaLibraryKit';
```

## supportedHighResolution

```TypeScript
supportedHighResolution: boolean
```

Whether high-resolution assets are supported. **true**: yes; **false**: no.

**类型：** boolean

**起始版本：** 24

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为24。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本24开始，该接口支持在原子化服务API中使用。

<!--Device-AssetCompatibleCapability-supportedHighResolution: boolean--><!--Device-AssetCompatibleCapability-supportedHighResolution: boolean-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## supportedMimeType

```TypeScript
supportedMimeType?: Array<string>
```

Supported MIME types.

**类型：** Array&lt;string&gt;

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-AssetCompatibleCapability-supportedMimeType?: Array<string>--><!--Device-AssetCompatibleCapability-supportedMimeType?: Array<string>-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

