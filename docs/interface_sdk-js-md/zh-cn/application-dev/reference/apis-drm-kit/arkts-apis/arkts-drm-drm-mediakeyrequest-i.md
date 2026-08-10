# MediaKeyRequest

Provides the drm media key request definitions.

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

<!--Device-drm-interface MediaKeyRequest--><!--Device-drm-interface MediaKeyRequest-End-->

**系统能力：** SystemCapability.Multimedia.Drm.Core

## 导入模块

```TypeScript
import { drm } from 'kits/@kit.DrmKit';
```

## data

```TypeScript
data: Uint8Array
```

Media key request data sent to media key server.

**类型：** Uint8Array

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-MediaKeyRequest-data: Uint8Array--><!--Device-MediaKeyRequest-data: Uint8Array-End-->

**系统能力：** SystemCapability.Multimedia.Drm.Core

## defaultURL

```TypeScript
defaultURL: string
```

Media key server URL.

**类型：** string

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-MediaKeyRequest-defaultURL: string--><!--Device-MediaKeyRequest-defaultURL: string-End-->

**系统能力：** SystemCapability.Multimedia.Drm.Core

## mediaKeyRequestType

```TypeScript
mediaKeyRequestType: MediaKeyRequestType
```

Media key request type.

**类型：** [MediaKeyRequestType](arkts-drm-drm-mediakeyrequesttype-e.md)

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-MediaKeyRequest-mediaKeyRequestType: MediaKeyRequestType--><!--Device-MediaKeyRequest-mediaKeyRequestType: MediaKeyRequestType-End-->

**系统能力：** SystemCapability.Multimedia.Drm.Core

