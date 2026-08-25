# @ohos.telephony.esim(eSIM卡管理)

eSIM卡管理模块提供了eSIM卡管理的基础能力，包括获取指定卡槽是否支持eSIM功能，如果支持则允许用户添加单个配置文件。

**起始版本：** 18

**系统能力：** SystemCapability.Telephony.CoreService.Esim

## 导入模块

```TypeScript
import { eSIM } from 'kits/@kit.TelephonyKit';
```

## 汇总

### 函数

| 名称 |
| --- |
| [addProfile(eSIM卡管理)](arkts-telephony-esim-addprofile-f.md) |
| [isSupported(eSIM卡管理)](arkts-telephony-esim-issupported-f.md) |

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [cancelSession(eSIM卡管理)](arkts-telephony-esim-cancelsession-f-sys.md) |
| [deleteProfile(eSIM卡管理)](arkts-telephony-esim-deleteprofile-f-sys.md) |
| [downloadProfile(eSIM卡管理)](arkts-telephony-esim-downloadprofile-f-sys.md) |
| [getContractInfo(eSIM卡管理)](arkts-telephony-esim-getcontractinfo-f-sys.md) |
| [getDefaultSmdpAddress(eSIM卡管理)](arkts-telephony-esim-getdefaultsmdpaddress-f-sys.md) |
| [getDownloadableProfileMetadata(eSIM卡管理)](arkts-telephony-esim-getdownloadableprofilemetadata-f-sys.md) |
| [getDownloadableProfiles(eSIM卡管理)](arkts-telephony-esim-getdownloadableprofiles-f-sys.md) |
| [getEid(eSIM卡管理)](arkts-telephony-esim-geteid-f-sys.md) |
| [getEsimFreeStorage(eSIM卡管理)](arkts-telephony-esim-getesimfreestorage-f-sys.md) |
| [getEuiccInfo(eSIM卡管理)](arkts-telephony-esim-geteuiccinfo-f-sys.md) |
| [getEuiccProfileInfoList(eSIM卡管理)](arkts-telephony-esim-geteuiccprofileinfolist-f-sys.md) |
| [getOsuStatus(eSIM卡管理)](arkts-telephony-esim-getosustatus-f-sys.md) |
| [getSupportedPkids(eSIM卡管理)](arkts-telephony-esim-getsupportedpkids-f-sys.md) |
| [reserveProfilesForFactoryRestore(eSIM卡管理)](arkts-telephony-esim-reserveprofilesforfactoryrestore-f-sys.md) |
| [resetMemory(eSIM卡管理)](arkts-telephony-esim-resetmemory-f-sys.md) |
| [setDefaultSmdpAddress(eSIM卡管理)](arkts-telephony-esim-setdefaultsmdpaddress-f-sys.md) |
| [setProfileNickname(eSIM卡管理)](arkts-telephony-esim-setprofilenickname-f-sys.md) |
| [startOsu(eSIM卡管理)](arkts-telephony-esim-startosu-f-sys.md) |
| [switchToProfile(eSIM卡管理)](arkts-telephony-esim-switchtoprofile-f-sys.md) |
<!--DelEnd-->

### 接口

| 名称 |
| --- |
| [DownloadableProfile(eSIM卡管理)](arkts-telephony-esim-downloadableprofile-i.md) |

<!--Del-->
### 接口（系统接口）

| 名称 |
| --- |
| [AccessRule(eSIM卡管理)](arkts-telephony-esim-accessrule-i-sys.md) |
| [ContractRequestData(eSIM卡管理)](arkts-telephony-esim-contractrequestdata-i-sys.md) |
| [DownloadConfiguration(eSIM卡管理)](arkts-telephony-esim-downloadconfiguration-i-sys.md) |
| [DownloadProfileResult(eSIM卡管理)](arkts-telephony-esim-downloadprofileresult-i-sys.md) |
| [EuiccInfo(eSIM卡管理)](arkts-telephony-esim-euiccinfo-i-sys.md) |
| [EuiccProfile(eSIM卡管理)](arkts-telephony-esim-euiccprofile-i-sys.md) |
| [GetDownloadableProfileMetadataResult(eSIM卡管理)](arkts-telephony-esim-getdownloadableprofilemetadataresult-i-sys.md) |
| [GetDownloadableProfilesResult(eSIM卡管理)](arkts-telephony-esim-getdownloadableprofilesresult-i-sys.md) |
| [GetEuiccProfileInfoListResult(eSIM卡管理)](arkts-telephony-esim-geteuiccprofileinfolistresult-i-sys.md) |
| [OperatorId(eSIM卡管理)](arkts-telephony-esim-operatorid-i-sys.md) |
<!--DelEnd-->

<!--Del-->
### 枚举（系统接口）

| 名称 |
| --- |
| [CancelReason(eSIM卡管理)](arkts-telephony-esim-cancelreason-e-sys.md) |
| [OsuStatus(eSIM卡管理)](arkts-telephony-esim-osustatus-e-sys.md) |
| [PolicyRules(eSIM卡管理)](arkts-telephony-esim-policyrules-e-sys.md) |
| [ProfileClass(eSIM卡管理)](arkts-telephony-esim-profileclass-e-sys.md) |
| [ProfileState(eSIM卡管理)](arkts-telephony-esim-profilestate-e-sys.md) |
| [ResetOption(eSIM卡管理)](arkts-telephony-esim-resetoption-e-sys.md) |
| [ResultCode(eSIM卡管理)](arkts-telephony-esim-resultcode-e-sys.md) |
| [SolvableErrors(eSIM卡管理)](arkts-telephony-esim-solvableerrors-e-sys.md) |
<!--DelEnd-->
