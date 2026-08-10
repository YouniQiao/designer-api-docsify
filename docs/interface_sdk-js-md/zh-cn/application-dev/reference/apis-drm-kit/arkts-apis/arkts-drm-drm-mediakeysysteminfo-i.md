# MediaKeySystemInfo

Used to indicate the media key system info of media source.

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

<!--Device-drm-interface MediaKeySystemInfo--><!--Device-drm-interface MediaKeySystemInfo-End-->

**系统能力：** SystemCapability.Multimedia.Drm.Core

## 导入模块

```TypeScript
import { drm } from 'kits/@kit.DrmKit';
```

## pssh

```TypeScript
pssh: Uint8Array
```

PSSH(protection scheme specific header) contain drm info.

**类型：** Uint8Array

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-MediaKeySystemInfo-pssh: Uint8Array--><!--Device-MediaKeySystemInfo-pssh: Uint8Array-End-->

**系统能力：** SystemCapability.Multimedia.Drm.Core

## uuid

```TypeScript
uuid: string
```

Drm system ID.

**类型：** string

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-MediaKeySystemInfo-uuid: string--><!--Device-MediaKeySystemInfo-uuid: string-End-->

**系统能力：** SystemCapability.Multimedia.Drm.Core

