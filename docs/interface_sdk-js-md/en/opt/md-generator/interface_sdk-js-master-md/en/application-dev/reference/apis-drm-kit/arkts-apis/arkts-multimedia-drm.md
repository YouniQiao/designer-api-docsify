# @ohos.multimedia.drm(Defines the DRM capability.)

The Digital Rights Management (DRM) framework enables you to develop digital rights management features for audio and video services. By calling the DRM plugins provided by the system, you can achieve the following:

- DRM certificate management: Generate certificate requests and handle certificate responses to facilitate   
certificate provisioning (downloading).  
- DRM media key management: Generate media key requests, manage media key responses, and handle offline media keys.  
- DRM content authorization: Allow DRM plugins to authorize content based on media key permissions.  
- DRM content decryption: Decrypt DRM content to support media playback functionality.

**Since:** 11

<!--Device-unnamed-declare namespace drm--><!--Device-unnamed-declare namespace drm-End-->

**System capability:** SystemCapability.Multimedia.Drm.Core

## Modules to Import

```TypeScript
import { drm } from '@kit.DrmKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [createMediaKeySystem](arkts-drm-drm-createmediakeysystem-f.md#createmediakeysystem) |
| [getMediaKeySystemUuid](arkts-drm-drm-getmediakeysystemuuid-f.md#getmediakeysystemuuid) |
| [getMediaKeySystems](arkts-drm-drm-getmediakeysystems-f.md#getmediakeysystems) |
| [isMediaKeySystemSupported](arkts-drm-drm-ismediakeysystemsupported-f.md#ismediakeysystemsupported) |
| [isMediaKeySystemSupported](arkts-drm-drm-ismediakeysystemsupported-f.md#ismediakeysystemsupported-1) |
| [isMediaKeySystemSupported](arkts-drm-drm-ismediakeysystemsupported-f.md#ismediakeysystemsupported-2) |

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
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

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [CertificateStatus](arkts-drm-drm-certificatestatus-e.md) |
| [ContentProtectionLevel](arkts-drm-drm-contentprotectionlevel-e.md) |
| [DrmErrorCode](arkts-drm-drm-drmerrorcode-e.md) |
| [MediaKeyRequestType](arkts-drm-drm-mediakeyrequesttype-e.md) |
| [MediaKeyType](arkts-drm-drm-mediakeytype-e.md) |
| [OfflineMediaKeyStatus](arkts-drm-drm-offlinemediakeystatus-e.md) |
| [PreDefinedConfigName](arkts-drm-drm-predefinedconfigname-e.md) |
