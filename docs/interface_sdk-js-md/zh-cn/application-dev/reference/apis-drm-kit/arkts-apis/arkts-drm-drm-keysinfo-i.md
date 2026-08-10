# KeysInfo

Used to indicate the media key status with a key and its value.

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

<!--Device-drm-interface KeysInfo--><!--Device-drm-interface KeysInfo-End-->

**系统能力：** SystemCapability.Multimedia.Drm.Core

## 导入模块

```TypeScript
import { drm } from 'kits/@kit.DrmKit';
```

## keyId

```TypeScript
keyId: Uint8Array
```

Keys Id in media key.

**类型：** Uint8Array

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-KeysInfo-keyId: Uint8Array--><!--Device-KeysInfo-keyId: Uint8Array-End-->

**系统能力：** SystemCapability.Multimedia.Drm.Core

## value

```TypeScript
value: string
```

Keys status description.

**类型：** string

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-KeysInfo-value: string--><!--Device-KeysInfo-value: string-End-->

**系统能力：** SystemCapability.Multimedia.Drm.Core

