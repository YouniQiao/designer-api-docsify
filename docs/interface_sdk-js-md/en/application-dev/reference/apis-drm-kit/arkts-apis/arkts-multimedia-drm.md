# @ohos.multimedia.drm(Defines the DRM capability.)

The Digital Rights Management (DRM) framework enables you to develop digital rights management features for audio and video services. By calling the DRM plugins provided by the system, you can achieve the following:  
- DRM certificate management: Generate certificate requests and handle certificate responses to facilitate  
certificate provisioning (downloading).  
- DRM media key management: Generate media key requests, manage media key responses, and handle offline media keys.  
- DRM content authorization: Allow DRM plugins to authorize content based on media key permissions.  
- DRM content decryption: Decrypt DRM content to support media playback functionality.

**Since:** 11

**System capability:** SystemCapability.Multimedia.Drm.Core

## Modules to Import

```TypeScript
import { drm } from 'kits/@kit.DrmKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [createMediaKeySystem(Defines the DRM capability.)](arkts-drm-drm-createmediakeysystem-f.md) |
| [getMediaKeySystems(Defines the DRM capability.)](arkts-drm-drm-getmediakeysystems-f.md) |
| [getMediaKeySystemUuid(Defines the DRM capability.)](arkts-drm-drm-getmediakeysystemuuid-f.md) |
| [isMediaKeySystemSupported(Defines the DRM capability.)](arkts-drm-drm-ismediakeysystemsupported-f.md) |
| [isMediaKeySystemSupported(Defines the DRM capability.)](arkts-drm-drm-ismediakeysystemsupported-f.md) |
| [isMediaKeySystemSupported(Defines the DRM capability.)](arkts-drm-drm-ismediakeysystemsupported-f.md) |

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [EventInfo(Defines the DRM capability.)](arkts-drm-drm-eventinfo-i.md) |
| [KeysInfo(Defines the DRM capability.)](arkts-drm-drm-keysinfo-i.md) |
| [MediaKeyRequest(Defines the DRM capability.)](arkts-drm-drm-mediakeyrequest-i.md) |
| [MediaKeySession(Defines the DRM capability.)](arkts-drm-drm-mediakeysession-i.md) |
| [MediaKeyStatus(Defines the DRM capability.)](arkts-drm-drm-mediakeystatus-i.md) |
| [MediaKeySystem(Defines the DRM capability.)](arkts-drm-drm-mediakeysystem-i.md) |
| [MediaKeySystemDescription(Defines the DRM capability.)](arkts-drm-drm-mediakeysystemdescription-i.md) |
| [MediaKeySystemInfo(Defines the DRM capability.)](arkts-drm-drm-mediakeysysteminfo-i.md) |
| [OptionsData(Defines the DRM capability.)](arkts-drm-drm-optionsdata-i.md) |
| [ProvisionRequest(Defines the DRM capability.)](arkts-drm-drm-provisionrequest-i.md) |
| [StatisticKeyValue(Defines the DRM capability.)](arkts-drm-drm-statistickeyvalue-i.md) |

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [CertificateStatus(Defines the DRM capability.)](arkts-drm-drm-certificatestatus-e.md) |
| [ContentProtectionLevel(Defines the DRM capability.)](arkts-drm-drm-contentprotectionlevel-e.md) |
| [DrmErrorCode(Defines the DRM capability.)](arkts-drm-drm-drmerrorcode-e.md) |
| [MediaKeyRequestType(Defines the DRM capability.)](arkts-drm-drm-mediakeyrequesttype-e.md) |
| [MediaKeyType(Defines the DRM capability.)](arkts-drm-drm-mediakeytype-e.md) |
| [OfflineMediaKeyStatus(Defines the DRM capability.)](arkts-drm-drm-offlinemediakeystatus-e.md) |
| [PreDefinedConfigName(Defines the DRM capability.)](arkts-drm-drm-predefinedconfigname-e.md) |
