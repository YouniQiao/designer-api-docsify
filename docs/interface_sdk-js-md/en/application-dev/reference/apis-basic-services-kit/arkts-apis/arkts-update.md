# @ohos.update

The **@ohos.update** module provides the core capabilities of online update, local SD card update, and factory reset. Version management, update control, and equipment maintenance can be implemented for the Over-The-Air (OTA) clients and system apps using this module. APIs provided by this module can be used for system version update, offline update, and data clearing.This module implements update of the entire system, including built-in resources and preset applications, but not third-party apps. This feature ensures system integrity, prevents compatibility issues with third-party apps, and improves update stability and security.There are two types of updates: local SD card update and OTA update.The design logic and use scenarios of each update type are as follows:  
- **Local SD card update:** For details, see Upgrading Service Terms  
Use scenarios: The system needs to be updated from a local storage device.  
**Benefits**This update mode applies to system update offline or with poor network connection when automatic update cannot be implemented. This mode does not depend on the upgrade package management server, reducing the update cost.  
- **Online update:** For details, see Upgrading Service Terms  
Use scenarios: The system needs to be automatically checked and updated by connecting to the network.This update mode is implemented by calling APIs of the **Updater** module. This mode depends on the upgrade package management server deployed by the vendor (the server system provides functions such as version check and upgrade package download). The APIs are implemented by the vendor.  
**Benefits**Users can obtain system updates in a timely manner, improving update efficiency and user experience. Functions such as automatic version check, background download, and resumable download are supported, reducing operation costs for users.  
**Reset**Use scenarios: This operation is performed to delete user data and restore the device to factory settings. It is applicable to scenarios such as troubleshooting, device transfer or scrapping, privacy protection, and storage space release. Traditional reset methods have problems such as residual data, uncleared keys, and incomplete data cleanup. This module provides hierarchical restoration capabilities to meet different security requirements.  
**Benefits**This module enables users to quickly troubleshoot, free up storage space, and protect the security of privacy data. Three reset modes are provided to meet the requirements for different security levels. Common reset applies to routine maintenance scenarios, forcible reset applies to data destruction scenarios, and deep reset applies to extreme scenarios such as device scrapping. In this way, hierarchical management of data clearing is implemented, reducing O&M costs.

> **NOTE：**&gt;
> The initial APIs of this module are supported since API version 9. Newly added APIs will be marked with a superscript to indicate their earliest API version.
> The APIs provided by this module are system APIs. For details about the system application permission request, see the system application development guide. For details about the application extension permission request, see the application extension development guide.

**Since:** 9

**System capability:** SystemCapability.Update.UpdateService

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { update } from 'kits/@kit.BasicServicesKit';
```

## Summary

<!--Del-->
### Functions(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [getLocalUpdater](arkts-basicservices-update-getlocalupdater-f-sys.md) |
| [getOnlineUpdater](arkts-basicservices-update-getonlineupdater-f-sys.md) |
| [getRestorer](arkts-basicservices-update-getrestorer-f-sys.md) |
<!--DelEnd-->

<!--Del-->
### Interfaces(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
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
### Enums(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
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
### Types(System API)

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [UpgradeTaskCallback](arkts-basicservices-update-upgradetaskcallback-t-sys.md) |
<!--DelEnd-->
