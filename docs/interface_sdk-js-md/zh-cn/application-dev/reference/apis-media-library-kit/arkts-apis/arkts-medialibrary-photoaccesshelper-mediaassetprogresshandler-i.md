# MediaAssetProgressHandler

**MediaAssetProgressHandler** is used to obtain the media asset processing progress from **onProgress()**.

**起始版本：** 15

**ArkTS模式：** ArkTS-Dyn起始版本为15；ArkTS-Sta起始版本为23。

<!--Device-photoAccessHelper-interface MediaAssetProgressHandler--><!--Device-photoAccessHelper-interface MediaAssetProgressHandler-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## 导入模块

```TypeScript
import { photoAccessHelper } from 'kits/@kit.MediaLibraryKit';
```

## onProgress

ArkTS-Dyn:
```TypeScript
onProgress(progress: number): void
```

ArkTS-Sta:
```TypeScript
onProgress(progress: int): void
```

Called when the progress of the requested video is returned.

**起始版本：** 15

**ArkTS模式：** ArkTS-Dyn起始版本为15；ArkTS-Sta起始版本为23。

<!--Device-MediaAssetProgressHandler-onProgress(progress: int): void--><!--Device-MediaAssetProgressHandler-onProgress(progress: int): void-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| progress | ArkTS-Dyn: number  <br>ArkTS-Sta：int | 是 | Progress in percentage. &lt;br&gt;Value range: [0, 100] |

