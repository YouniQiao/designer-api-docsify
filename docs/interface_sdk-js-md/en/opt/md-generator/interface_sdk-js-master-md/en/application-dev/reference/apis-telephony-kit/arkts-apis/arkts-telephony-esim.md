# @ohos.telephony.esim

This indicates that the eSIM card performs the profile management operation synchronously.Includes methods defined by GSMA Spec (SGP.22) and customized methods.

**Since:** 18

<!--Device-unnamed-declare namespace eSIM--><!--Device-unnamed-declare namespace eSIM-End-->

**System capability:** SystemCapability.Telephony.CoreService.Esim

## Modules to Import

```TypeScript
import { eSIM } from 'kits/@kit.TelephonyKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [addProfile](arkts-telephony-esim-addprofile-f.md#addprofile) |
| [isSupported](arkts-telephony-esim-issupported-f.md#issupported) |

<!--Del-->
### Functions（系统接口）

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [cancelSession](arkts-telephony-esim-cancelsession-f-sys.md#cancelsession) |
| [deleteProfile](arkts-telephony-esim-deleteprofile-f-sys.md#deleteprofile) |
| [downloadProfile](arkts-telephony-esim-downloadprofile-f-sys.md#downloadprofile) |
| [getContractInfo](arkts-telephony-esim-getcontractinfo-f-sys.md#getcontractinfo) |
| [getDefaultSmdpAddress](arkts-telephony-esim-getdefaultsmdpaddress-f-sys.md#getdefaultsmdpaddress) |
| [getDownloadableProfileMetadata](arkts-telephony-esim-getdownloadableprofilemetadata-f-sys.md#getdownloadableprofilemetadata) |
| [getDownloadableProfiles](arkts-telephony-esim-getdownloadableprofiles-f-sys.md#getdownloadableprofiles) |
| [getEid](arkts-telephony-esim-geteid-f-sys.md#geteid) |
| [getEsimFreeStorage](arkts-telephony-esim-getesimfreestorage-f-sys.md#getesimfreestorage) |
| [getEuiccInfo](arkts-telephony-esim-geteuiccinfo-f-sys.md#geteuiccinfo) |
| [getEuiccProfileInfoList](arkts-telephony-esim-geteuiccprofileinfolist-f-sys.md#geteuiccprofileinfolist) |
| [getOsuStatus](arkts-telephony-esim-getosustatus-f-sys.md#getosustatus) |
| [getSupportedPkids](arkts-telephony-esim-getsupportedpkids-f-sys.md#getsupportedpkids) |
| [reserveProfilesForFactoryRestore](arkts-telephony-esim-reserveprofilesforfactoryrestore-f-sys.md#reserveprofilesforfactoryrestore) |
| [resetMemory](arkts-telephony-esim-resetmemory-f-sys.md#resetmemory) |
| [setDefaultSmdpAddress](arkts-telephony-esim-setdefaultsmdpaddress-f-sys.md#setdefaultsmdpaddress) |
| [setProfileNickname](arkts-telephony-esim-setprofilenickname-f-sys.md#setprofilenickname) |
| [startOsu](arkts-telephony-esim-startosu-f-sys.md#startosu) |
| [switchToProfile](arkts-telephony-esim-switchtoprofile-f-sys.md#switchtoprofile) |
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
