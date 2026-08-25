# @ohos.deviceInfo

This module provides APIs for querying terminal device information, including the device type, brand, model, system version, security patch tag, and unique device ID. It is applicable to scenarios such as device adaptation, version compatibility check, device identification, and statistical analysis, helping you quickly obtain device information for application adaptation and optimization. You cannot configure this information.

> **NOTE：**&gt;
> The initial APIs of this module are supported since API version 6. New APIs added in later versions are marked with superscripts to indicate their initial version.
> The return values **hardwareProfile**, **incrementalVersion**, **buildType**, **buildUser**, **buildHost**, **buildTime**, and **buildRootHash** are **default**. These parameters will be configured in the official commercial version of the device.
> The APIs of this module return information about device constants. It is recommended that your app call the APIs only once.

**Since:** 6

**ArkTS mode:** ArkTS-Dyn since version 6; ArkTS-Sta since version 24.

**System capability:** SystemCapability.Startup.SystemInfo

## Modules to Import

```TypeScript
import { deviceInfo } from '@kit.BasicServicesKit';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [apiAvailable](arkts-basicservices-deviceinfo-apiavailable-f.md) |

### Enums

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [DeviceTypes](arkts-basicservices-deviceinfo-devicetypes-e.md) |
| [PerformanceClassLevel](arkts-basicservices-deviceinfo-performanceclasslevel-e.md) |

### Constants

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [abiList](arkts-basicservices-deviceinfo-con.md#abilist) |
| [bootCount](arkts-basicservices-deviceinfo-con.md#bootcount) |
| [bootloaderVersion](arkts-basicservices-deviceinfo-con.md#bootloaderversion) |
| [brand](arkts-basicservices-deviceinfo-con.md#brand) |
| [buildHost](arkts-basicservices-deviceinfo-con.md#buildhost) |
| [buildRootHash](arkts-basicservices-deviceinfo-con.md#buildroothash) |
| [buildTime](arkts-basicservices-deviceinfo-con.md#buildtime) |
| [buildType](arkts-basicservices-deviceinfo-con.md#buildtype) |
| [buildUser](arkts-basicservices-deviceinfo-con.md#builduser) |
| [buildVersion](arkts-basicservices-deviceinfo-con.md#buildversion) |
| [chipType](arkts-basicservices-deviceinfo-con.md#chiptype) |
| [deviceColor](arkts-basicservices-deviceinfo-con.md#devicecolor) |
| [deviceType](arkts-basicservices-deviceinfo-con.md#devicetype) |
| [diskSN](arkts-basicservices-deviceinfo-con.md#disksn) |
| [displayVersion](arkts-basicservices-deviceinfo-con.md#displayversion) |
| [distributionOSApiName](arkts-basicservices-deviceinfo-con.md#distributionosapiname) |
| [distributionOSApiVersion](arkts-basicservices-deviceinfo-con.md#distributionosapiversion) |
| [distributionOSName](arkts-basicservices-deviceinfo-con.md#distributionosname) |
| [distributionOSReleaseType](arkts-basicservices-deviceinfo-con.md#distributionosreleasetype) |
| [distributionOSVersion](arkts-basicservices-deviceinfo-con.md#distributionosversion) |
| [featureVersion](arkts-basicservices-deviceinfo-con.md#featureversion) |
| [firstApiVersion](arkts-basicservices-deviceinfo-con.md#firstapiversion) |
| [hardwareModel](arkts-basicservices-deviceinfo-con.md#hardwaremodel) |
| [hardwareProfile](arkts-basicservices-deviceinfo-con.md#hardwareprofile) |
| [incrementalVersion](arkts-basicservices-deviceinfo-con.md#incrementalversion) |
| [majorVersion](arkts-basicservices-deviceinfo-con.md#majorversion) |
| [manufacture](arkts-basicservices-deviceinfo-con.md#manufacture) |
| [marketName](arkts-basicservices-deviceinfo-con.md#marketname) |
| [ODID](arkts-basicservices-deviceinfo-con.md#odid) |
| [osFullName](arkts-basicservices-deviceinfo-con.md#osfullname) |
| [osReleaseType](arkts-basicservices-deviceinfo-con.md#osreleasetype) |
| [performanceClass](arkts-basicservices-deviceinfo-con.md#performanceclass) |
| [productModel](arkts-basicservices-deviceinfo-con.md#productmodel) |
| [productModelAlias](arkts-basicservices-deviceinfo-con.md#productmodelalias) |
| [productSeries](arkts-basicservices-deviceinfo-con.md#productseries) |
| [sdkApiVersion](arkts-basicservices-deviceinfo-con.md#sdkapiversion) |
| [sdkMinorApiVersion](arkts-basicservices-deviceinfo-con.md#sdkminorapiversion) |
| [sdkPatchApiVersion](arkts-basicservices-deviceinfo-con.md#sdkpatchapiversion) |
| [securityPatchTag](arkts-basicservices-deviceinfo-con.md#securitypatchtag) |
| [seniorVersion](arkts-basicservices-deviceinfo-con.md#seniorversion) |
| [serial](arkts-basicservices-deviceinfo-con.md#serial) |
| [softwareModel](arkts-basicservices-deviceinfo-con.md#softwaremodel) |
| [udid](arkts-basicservices-deviceinfo-con.md#udid) |
| [versionId](arkts-basicservices-deviceinfo-con.md#versionid) |
