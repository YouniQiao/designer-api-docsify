# @ohos.telephony.esim(eSIM Management)

The **esim** module provides basic eSIM management capabilities, including checking whether a specified card slot supports the eSIM function.

**Since:** 18

**System capability:** SystemCapability.Telephony.CoreService.Esim

## Modules to Import

```TypeScript
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [addProfile(eSIM Management)](arkts-telephony-esim-addprofile-f.md) | Launches the download page for the user to add a single profile. This API uses a promise to return the result. |
| [isSupported(eSIM Management)](arkts-telephony-esim-issupported-f.md) | Checks whether the specified card slot supports the eSIM function. |

<!--Del-->
### Functions(System API)

| Name | Description |
| --- | --- |
| [cancelSession(eSIM Management)](arkts-telephony-esim-cancelsession-f-sys.md) | Cancels a session. This API uses a promise to return the result. |
| [deleteProfile(eSIM Management)](arkts-telephony-esim-deleteprofile-f-sys.md) | Deletes a profile. This API uses a promise to return the result. |
| [downloadProfile(eSIM Management)](arkts-telephony-esim-downloadprofile-f-sys.md) | Downloads a profile. This API uses a promise to return the result. |
| [getContractInfo(eSIM Management)](arkts-telephony-esim-getcontractinfo-f-sys.md) | Obtains the encrypted eSIM ID and other information required for enabling eSIM. |
| [getDefaultSmdpAddress(eSIM Management)](arkts-telephony-esim-getdefaultsmdpaddress-f-sys.md) | Obtains the default SM-DP+ address stored in the eUICC. This API uses a promise to return the result. |
| [getDownloadableProfileMetadata(eSIM Management)](arkts-telephony-esim-getdownloadableprofilemetadata-f-sys.md) | Obtains the metadata of the downloadable profile. This API uses a promise to return the result. |
| [getDownloadableProfiles(eSIM Management)](arkts-telephony-esim-getdownloadableprofiles-f-sys.md) | Obtains the list of downloadable profiles. This API uses a promise to return the result. |
| [getEid(eSIM Management)](arkts-telephony-esim-geteid-f-sys.md) | Obtains the equipment identifier (EID) of the eUICC hardware in a specified card slot. |
| [getEsimFreeStorage(eSIM Management)](arkts-telephony-esim-getesimfreestorage-f-sys.md) | This API is used to obtain the remaining storage space of the eUICC hardware. This API uses a promise to return the result. |
| [getEuiccInfo(eSIM Management)](arkts-telephony-esim-geteuiccinfo-f-sys.md) | Obtains eUICC information. This API uses a promise to return the result. |
| [getEuiccProfileInfoList(eSIM Management)](arkts-telephony-esim-geteuiccprofileinfolist-f-sys.md) | Obtains the profile information list. This API uses a promise to return the result. |
| [getOsuStatus(eSIM Management)](arkts-telephony-esim-getosustatus-f-sys.md) | Obtains the OS upgrade status for the eSIM in the specified slot. This API uses a promise to return the result. |
| [getSupportedPkids(eSIM Management)](arkts-telephony-esim-getsupportedpkids-f-sys.md) | Obtains the public key ID information supported by the phone. |
| [reserveProfilesForFactoryRestore(eSIM Management)](arkts-telephony-esim-reserveprofilesforfactoryrestore-f-sys.md) | Restores factory settings and retains profiles. This API uses a promise to return the result. |
| [resetMemory(eSIM Management)](arkts-telephony-esim-resetmemory-f-sys.md) | Clears all specific profiles and resets the eUICC. This API uses a promise to return the result. |
| [setDefaultSmdpAddress(eSIM Management)](arkts-telephony-esim-setdefaultsmdpaddress-f-sys.md) | Sets or updates the default SM-DP+ address stored in the eUICC. This API uses a promise to return the result. |
| [setProfileNickname(eSIM Management)](arkts-telephony-esim-setprofilenickname-f-sys.md) | Sets a nickname for the specified profile. This API uses a promise to return the result. |
| [startOsu(eSIM Management)](arkts-telephony-esim-startosu-f-sys.md) | Upgrades the OS if the OS version of the eSIM in the specified slot is not the latest. This API uses a promise to return the result. |
| [switchToProfile(eSIM Management)](arkts-telephony-esim-switchtoprofile-f-sys.md) | Switches to the specified profile. This API uses a promise to return the result. |
<!--DelEnd-->

### Interfaces

| Name | Description |
| --- | --- |
| [DownloadableProfile(eSIM Management)](arkts-telephony-esim-downloadableprofile-i.md) | Defines a downloadable profile. |

<!--Del-->
### Interfaces(System API)

| Name | Description |
| --- | --- |
| [AccessRule(eSIM Management)](arkts-telephony-esim-accessrule-i-sys.md) | Establishes a single UICC access rule pursuant to the GlobalPlatform Secure Element Access Control specification.@interface AccessRule |
| [ContractRequestData(eSIM Management)](arkts-telephony-esim-contractrequestdata-i-sys.md) | Information required for encryption. |
| [DownloadConfiguration(eSIM Management)](arkts-telephony-esim-downloadconfiguration-i-sys.md) | Defines the download configuration. |
| [DownloadProfileResult(eSIM Management)](arkts-telephony-esim-downloadprofileresult-i-sys.md) | Defines the profile download result. |
| [EuiccInfo(eSIM Management)](arkts-telephony-esim-euiccinfo-i-sys.md) | Defines the eUICC information. |
| [EuiccProfile(eSIM Management)](arkts-telephony-esim-euiccprofile-i-sys.md) | Profile information. |
| [GetDownloadableProfileMetadataResult(eSIM Management)](arkts-telephony-esim-getdownloadableprofilemetadataresult-i-sys.md) | Obtains the metadata of the downloadable profile. |
| [GetDownloadableProfilesResult(eSIM Management)](arkts-telephony-esim-getdownloadableprofilesresult-i-sys.md) | Obtains the list of default downloadable profiles. |
| [GetEuiccProfileInfoListResult(eSIM Management)](arkts-telephony-esim-geteuiccprofileinfolistresult-i-sys.md) | Obtains the profile information list. |
| [OperatorId(eSIM Management)](arkts-telephony-esim-operatorid-i-sys.md) | Obtains information about the eUICC chip or device. |
<!--DelEnd-->

<!--Del-->
### Enums(System API)

| Name | Description |
| --- | --- |
| [CancelReason(eSIM Management)](arkts-telephony-esim-cancelreason-e-sys.md) | Reason for canceling the session. |
| [OsuStatus(eSIM Management)](arkts-telephony-esim-osustatus-e-sys.md) | Defines the OS upgrade status. |
| [PolicyRules(eSIM Management)](arkts-telephony-esim-policyrules-e-sys.md) | Enumerates the profile policy rules. |
| [ProfileClass(eSIM Management)](arkts-telephony-esim-profileclass-e-sys.md) | Enumerates the profile classes. |
| [ProfileState(eSIM Management)](arkts-telephony-esim-profilestate-e-sys.md) | Enumerates the profile states. |
| [ResetOption(eSIM Management)](arkts-telephony-esim-resetoption-e-sys.md) | Defines the reset options. |
| [ResultCode(eSIM Management)](arkts-telephony-esim-resultcode-e-sys.md) | Enumerates the result codes. |
| [SolvableErrors(eSIM Management)](arkts-telephony-esim-solvableerrors-e-sys.md) | Enumerates the solvable errors. |
<!--DelEnd-->
