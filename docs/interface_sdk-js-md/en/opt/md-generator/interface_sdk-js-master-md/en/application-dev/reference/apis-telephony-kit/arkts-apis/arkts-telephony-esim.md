# @ohos.telephony.esim

This indicates that the eSIM card performs the profile management operation synchronously. Includes methods defined by GSMA Spec (SGP.22) and customized methods.

**Since:** 23

**Deprecated since:** -1

<!--Device-unnamed-declare namespace eSIM--><!--Device-unnamed-declare namespace eSIM-End-->

**System capability:** SystemCapability.Telephony.CoreService.Esim

## Modules to Import

```TypeScript
import { eSIM } from '@kit.TelephonyKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [addProfile](arkts-telephony-esim-addprofile-f.md#addProfile) |
| [isSupported](arkts-telephony-esim-issupported-f.md#isSupported) |

<!--Del-->
### Functions（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [cancelSession](arkts-telephony-esim-cancelsession-f-sys.md#cancelSession-(System-API)) |
| [deleteProfile](arkts-telephony-esim-deleteprofile-f-sys.md#deleteProfile-(System-API)) |
| [downloadProfile](arkts-telephony-esim-downloadprofile-f-sys.md#downloadProfile-(System-API)) |
| [getContractInfo](arkts-telephony-esim-getcontractinfo-f-sys.md#getContractInfo-(System-API)) |
| [getDefaultSmdpAddress](arkts-telephony-esim-getdefaultsmdpaddress-f-sys.md#getDefaultSmdpAddress-(System-API)) |
| [getDownloadableProfileMetadata](arkts-telephony-esim-getdownloadableprofilemetadata-f-sys.md#getDownloadableProfileMetadata-(System-API)) |
| [getDownloadableProfiles](arkts-telephony-esim-getdownloadableprofiles-f-sys.md#getDownloadableProfiles-(System-API)) |
| [getEid](arkts-telephony-esim-geteid-f-sys.md#getEid-(System-API)) |
| [getEsimFreeStorage](arkts-telephony-esim-getesimfreestorage-f-sys.md#getEsimFreeStorage-(System-API)) |
| [getEuiccInfo](arkts-telephony-esim-geteuiccinfo-f-sys.md#getEuiccInfo-(System-API)) |
| [getEuiccProfileInfoList](arkts-telephony-esim-geteuiccprofileinfolist-f-sys.md#getEuiccProfileInfoList-(System-API)) |
| [getOsuStatus](arkts-telephony-esim-getosustatus-f-sys.md#getOsuStatus-(System-API)) |
| [getSupportedPkids](arkts-telephony-esim-getsupportedpkids-f-sys.md#getSupportedPkids-(System-API)) |
| [reserveProfilesForFactoryRestore](arkts-telephony-esim-reserveprofilesforfactoryrestore-f-sys.md#reserveProfilesForFactoryRestore-(System-API)) |
| [resetMemory](arkts-telephony-esim-resetmemory-f-sys.md#resetMemory-(System-API)) |
| [setDefaultSmdpAddress](arkts-telephony-esim-setdefaultsmdpaddress-f-sys.md#setDefaultSmdpAddress-(System-API)) |
| [setProfileNickname](arkts-telephony-esim-setprofilenickname-f-sys.md#setProfileNickname-(System-API)) |
| [startOsu](arkts-telephony-esim-startosu-f-sys.md#startOsu-(System-API)) |
| [switchToProfile](arkts-telephony-esim-switchtoprofile-f-sys.md#switchToProfile-(System-API)) |
<!--DelEnd-->

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [AccessRule](arkts-telephony-esim-accessrule-i.md) |
| [DownloadableProfile](arkts-telephony-esim-downloadableprofile-i.md) |

<!--Del-->
### Interfaces（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [ContractRequestData](arkts-telephony-esim-contractrequestdata-i-sys.md) |
| [DownloadConfiguration](arkts-telephony-esim-downloadconfiguration-i-sys.md) |
| [DownloadProfileResult](arkts-telephony-esim-downloadprofileresult-i-sys.md) |
| [EuiccInfo](arkts-telephony-esim-euiccinfo-i-sys.md) |
| [EuiccProfile](arkts-telephony-esim-euiccprofile-i-sys.md) |
| [GetDownloadableProfileMetadataResult](arkts-telephony-esim-getdownloadableprofilemetadataresult-i-sys.md) |
| [GetDownloadableProfilesResult](arkts-telephony-esim-getdownloadableprofilesresult-i-sys.md) |
| [GetEuiccProfileInfoListResult](arkts-telephony-esim-geteuiccprofileinfolistresult-i-sys.md) |
| [OperatorId](arkts-telephony-esim-operatorid-i-sys.md) |
<!--DelEnd-->

<!--Del-->
### Enums（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [CancelReason](arkts-telephony-esim-cancelreason-e-sys.md) |
| [OsuStatus](arkts-telephony-esim-osustatus-e-sys.md) |
| [PolicyRules](arkts-telephony-esim-policyrules-e-sys.md) |
| [ProfileClass](arkts-telephony-esim-profileclass-e-sys.md) |
| [ProfileState](arkts-telephony-esim-profilestate-e-sys.md) |
| [ResetOption](arkts-telephony-esim-resetoption-e-sys.md) |
| [ResultCode](arkts-telephony-esim-resultcode-e-sys.md) |
| [SolvableErrors](arkts-telephony-esim-solvableerrors-e-sys.md) |
<!--DelEnd-->
