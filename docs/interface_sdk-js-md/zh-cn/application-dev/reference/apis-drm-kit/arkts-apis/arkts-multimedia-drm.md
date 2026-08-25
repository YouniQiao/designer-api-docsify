# @ohos.multimedia.drm

DRM（Digital Rights Management）框架组件支持音视频媒体业务数字版权管理功能的开发。开发者可以调用系统提供的DRM插件，完成以下功能：  
- DRM证书管理：生成证书请求、设置证书响应，实现对证书Provision（下载）功能。 - DRM媒体密钥管理：生成媒体密钥请求、设置媒体密钥响应、管理离线媒体密钥功能。 - DRM节目授权：支持DRM插件根据媒体密钥权限对DRM节目授权。 - DRM节目解密：支持媒体播放功能的解密调用，实现对DRM节目的解密。

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.Multimedia.Drm.Core

## 导入模块

```TypeScript
import { drm } from '@kit.DrmKit';
```

## 汇总

### 函数

| 名称 |
| --- |
| [createMediaKeySystem](arkts-drm-drm-createmediakeysystem-f.md) |
| [createMediaKeySystem](arkts-drm-drm-createmediakeysystem-f.md) |
| [getMediaKeySystems](arkts-drm-drm-getmediakeysystems-f.md) |
| [getMediaKeySystemUuid](arkts-drm-drm-getmediakeysystemuuid-f.md) |
| [isMediaKeySystemSupported](arkts-drm-drm-ismediakeysystemsupported-f.md) |
| [isMediaKeySystemSupported](arkts-drm-drm-ismediakeysystemsupported-f.md) |
| [isMediaKeySystemSupported](arkts-drm-drm-ismediakeysystemsupported-f.md) |

### 接口

| 名称 |
| --- |
| [EventInfo](arkts-drm-drm-eventinfo-i.md) |
| [KeysInfo](arkts-drm-drm-keysinfo-i.md) |
| [MediaKeyRequest](arkts-drm-drm-mediakeyrequest-i.md) |
| [MediaKeySession](arkts-drm-drm-mediakeysession-i.md) |
| [MediaKeyStatus](arkts-drm-drm-mediakeystatus-i.md) |
| [MediaKeySystem](arkts-drm-drm-mediakeysystem-i.md) |
| [MediaKeySystemDescription](arkts-drm-drm-mediakeysystemdescription-i.md) |
| [MediaKeySystemInfo](arkts-drm-drm-mediakeysysteminfo-i.md) |
| [OptionsData](arkts-drm-drm-optionsdata-i.md) |
| [ProvisionRequest](arkts-drm-drm-provisionrequest-i.md) |
| [StatisticKeyValue](arkts-drm-drm-statistickeyvalue-i.md) |

### 枚举

| 名称 |
| --- |
| [CertificateStatus](arkts-drm-drm-certificatestatus-e.md) |
| [ContentProtectionLevel](arkts-drm-drm-contentprotectionlevel-e.md) |
| [DrmErrorCode](arkts-drm-drm-drmerrorcode-e.md) |
| [MediaKeyRequestType](arkts-drm-drm-mediakeyrequesttype-e.md) |
| [MediaKeyType](arkts-drm-drm-mediakeytype-e.md) |
| [OfflineMediaKeyStatus](arkts-drm-drm-offlinemediakeystatus-e.md) |
| [PreDefinedConfigName](arkts-drm-drm-predefinedconfigname-e.md) |
