# RequestOptions

Represents request options.

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

<!--Device-photoAccessHelper-interface RequestOptions--><!--Device-photoAccessHelper-interface RequestOptions-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## 导入模块

```TypeScript
import { photoAccessHelper } from 'kits/@kit.MediaLibraryKit';
```

## compatibleMode

```TypeScript
compatibleMode?: CompatibleMode
```

HDR video transcoding policy, which can be **FAST_ORIGINAL_FORMAT_MODE** (maintaining the original HDR format) or  
**COMPATIBLE_FORMAT_MODE** (converting HDR content to SDR format). The default value is   
**FAST_ORIGINAL_FORMAT_MODE**.

**类型：** [CompatibleMode](arkts-medialibrary-photoaccesshelper-compatiblemode-e.md)

**起始版本：** 15

**ArkTS模式：** ArkTS-Dyn起始版本为15；ArkTS-Sta起始版本为23。

<!--Device-RequestOptions-compatibleMode?: CompatibleMode--><!--Device-RequestOptions-compatibleMode?: CompatibleMode-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## deliveryMode

```TypeScript
deliveryMode: DeliveryMode
```

Delivery mode of the requested asset. The value can be **FAST_MODE**, **HIGH_QUALITY_MODE**, or **BALANCE_MODE**.

**类型：** [DeliveryMode](arkts-medialibrary-photoaccesshelper-deliverymode-e.md)

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

<!--Device-RequestOptions-deliveryMode: DeliveryMode--><!--Device-RequestOptions-deliveryMode: DeliveryMode-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## mediaAssetProgressHandler

```TypeScript
mediaAssetProgressHandler?: MediaAssetProgressHandler
```

Callback used to return the HDR-to-SDR conversion progress.

**类型：** [MediaAssetProgressHandler](arkts-medialibrary-photoaccesshelper-mediaassetprogresshandler-i.md)

**起始版本：** 15

**ArkTS模式：** ArkTS-Dyn起始版本为15；ArkTS-Sta起始版本为23。

<!--Device-RequestOptions-mediaAssetProgressHandler?: MediaAssetProgressHandler--><!--Device-RequestOptions-mediaAssetProgressHandler?: MediaAssetProgressHandler-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

