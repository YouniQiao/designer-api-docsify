# @ohos.update

@ohos.update模块提供系统升级和恢复出厂设置功能，支持在线升级、本地SD卡升级和恢复出厂设置三大核心能力，帮助设备厂商OTA（Over-The-Air，空中下载）客户端、系统应用实现版本管理、升级控制和设备维护。适用于系统版 本更新、离线升级、设备数据清理等场景。升级范围：升级整个系统，包括内置资源和预置应用，不包括第三方应用。确保系统完整性，避免第三方应用兼容性问题，提升升级稳定性和安全性。升级类型：本地SD卡升级、在线升级。各升级类型的设计逻辑和适用场景如下：  
- **本地SD卡升级**：详见[术语](../../../basic-services/update/update-kit-term.md)。  
使用场景：需要从本地存储设备进行系统升级。  
**收益说明**：解决无法联网自动升级的问题，适合离线环境或网络不稳定场景下的系统升级需求，无需依赖升级包管理服务器，降低升级成本。  
- **在线升级**：详见[术语](../../../basic-services/update/update-kit-term.md)。  
使用场景：需要通过网络自动检查和升级系统。通过Updater对象实现接口的调用。依赖设备厂商部署的升级包管理服务器（服务端系统，提供版本检查、升级包下载等功能），接口由设备厂商实现。  
**收益说明**：支持用户及时获取系统更新，提升升级效率和用户体验。支持自动版本检查、后台下载、断点续传等功能，降低用户操作成本。  
**恢复出厂设置**：使用场景：需要清除用户数据、恢复设备出厂状态。适用于解决系统异常、设备转赠或报废、隐私保护、存储空间释放等场景。传统恢复方式存在数据残留、密钥未清除、清理不彻底等问题，本模块提供分级恢复能力满足不同安全需求。  
**收益说明**：支持用户快速解决系统异常问题、释放存储空间、保护隐私数据安全。提供三种恢复模式满足不同安全等级需求，普通恢复适用于日常维护场景，强制恢复适用于数据销毁场景，深度恢复适用于设备报废等极端场景，实现数据清理的分级管理，降低运维成本。

> **说明：**&gt;
> 本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。本模块接口为系统接口。系统应用权限申请请参考系统应用开发指南，应用扩展权限申请请参考应用扩展开发指南。

**起始版本：** 9

**系统能力：** SystemCapability.Update.UpdateService

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { update } from 'kits/@kit.BasicServicesKit';
```

## 汇总

<!--Del-->
### 函数（系统接口）

| 名称 |
| --- |
| [getLocalUpdater](arkts-basicservices-update-getlocalupdater-f-sys.md) |
| [getOnlineUpdater](arkts-basicservices-update-getonlineupdater-f-sys.md) |
| [getRestorer](arkts-basicservices-update-getrestorer-f-sys.md) |
<!--DelEnd-->

<!--Del-->
### 接口（系统接口）

| 名称 |
| --- |
| [BusinessType](arkts-basicservices-update-businesstype-i-sys.md) |
| [CheckResult](arkts-basicservices-update-checkresult-i-sys.md) |
| [ClearOptions](arkts-basicservices-update-clearoptions-i-sys.md) |
| [ComponentDescription](arkts-basicservices-update-componentdescription-i-sys.md) |
| [CurrentVersionInfo](arkts-basicservices-update-currentversioninfo-i-sys.md) |
| [DescriptionInfo](arkts-basicservices-update-descriptioninfo-i-sys.md) |
| [DescriptionOptions](arkts-basicservices-update-descriptionoptions-i-sys.md) |
| [DownloadOptions](arkts-basicservices-update-downloadoptions-i-sys.md) |
| [ErrorMessage](arkts-basicservices-update-errormessage-i-sys.md) |
| [EventClassifyInfo](arkts-basicservices-update-eventclassifyinfo-i-sys.md) |
| [EventInfo](arkts-basicservices-update-eventinfo-i-sys.md) |
| [FactoryResetInfo](arkts-basicservices-update-factoryresetinfo-i-sys.md) |
| [FactoryResetStrategy](arkts-basicservices-update-factoryresetstrategy-i-sys.md) |
| [LocalUpdater](arkts-basicservices-update-localupdater-i-sys.md) |
| [NewVersionInfo](arkts-basicservices-update-newversioninfo-i-sys.md) |
| [PauseDownloadOptions](arkts-basicservices-update-pausedownloadoptions-i-sys.md) |
| [Restorer](arkts-basicservices-update-restorer-i-sys.md) |
| [ResumeDownloadOptions](arkts-basicservices-update-resumedownloadoptions-i-sys.md) |
| [TaskBody](arkts-basicservices-update-taskbody-i-sys.md) |
| [TaskInfo](arkts-basicservices-update-taskinfo-i-sys.md) |
| [Updater](arkts-basicservices-update-updater-i-sys.md) |
| [UpgradeFile](arkts-basicservices-update-upgradefile-i-sys.md) |
| [UpgradeInfo](arkts-basicservices-update-upgradeinfo-i-sys.md) |
| [UpgradeOptions](arkts-basicservices-update-upgradeoptions-i-sys.md) |
| [UpgradePeriod](arkts-basicservices-update-upgradeperiod-i-sys.md) |
| [UpgradePolicy](arkts-basicservices-update-upgradepolicy-i-sys.md) |
| [VersionComponent](arkts-basicservices-update-versioncomponent-i-sys.md) |
| [VersionDigestInfo](arkts-basicservices-update-versiondigestinfo-i-sys.md) |
<!--DelEnd-->

<!--Del-->
### 枚举（系统接口）

| 名称 |
| --- |
| [BusinessSubType](arkts-basicservices-update-businesssubtype-e-sys.md) |
| [BusinessVendor](arkts-basicservices-update-businessvendor-e-sys.md) |
| [ComponentType](arkts-basicservices-update-componenttype-e-sys.md) |
| [DescriptionFormat](arkts-basicservices-update-descriptionformat-e-sys.md) |
| [DescriptionType](arkts-basicservices-update-descriptiontype-e-sys.md) |
| [EffectiveMode](arkts-basicservices-update-effectivemode-e-sys.md) |
| [EventClassify](arkts-basicservices-update-eventclassify-e-sys.md) |
| [EventId](arkts-basicservices-update-eventid-e-sys.md) |
| [FactoryResetScope](arkts-basicservices-update-factoryresetscope-e-sys.md) |
| [NetType](arkts-basicservices-update-nettype-e-sys.md) |
| [Order](arkts-basicservices-update-order-e-sys.md) |
| [OtaMode](arkts-basicservices-update-otamode-e-sys.md) |
| [UpgradeAction](arkts-basicservices-update-upgradeaction-e-sys.md) |
| [UpgradeStatus](arkts-basicservices-update-upgradestatus-e-sys.md) |
<!--DelEnd-->

<!--Del-->
### 类型（系统接口）

| 名称 |
| --- |
| [UpgradeTaskCallback](arkts-basicservices-update-upgradetaskcallback-t-sys.md) |
<!--DelEnd-->
