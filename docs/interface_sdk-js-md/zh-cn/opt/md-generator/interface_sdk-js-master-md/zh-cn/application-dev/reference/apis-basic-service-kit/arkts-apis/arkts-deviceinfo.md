# @ohos.deviceInfo

本模块提供终端设备信息查询，开发者不可配置。

> **说明：**
> 
> 本模块首批接口从API version 6开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
> hardwareProfile、incrementalVersion、buildType、buildUser、buildHost、buildTime、buildRootHash等参数返回值为default，这些参数会在设备正式商用版本中配置具体值。
> 本模块接口返回设备常量信息，建议应用只调用一次，不需要频繁调用。

**起始版本：** 6

<!--Device-unnamed-declare namespace deviceInfo--><!--Device-unnamed-declare namespace deviceInfo-End-->

**系统能力：** SystemCapability.Startup.SystemInfo

## 汇总

### 函数

| 名称 |
| --- |
| [apiAvailable](arkts-basicservices-deviceinfo-apiavailable-f.md#apiavailable) |

### 枚举

| 名称 |
| --- |
| [DeviceTypes](arkts-basicservices-deviceinfo-devicetypes-e.md) |
| [PerformanceClassLevel](arkts-basicservices-deviceinfo-performanceclasslevel-e.md) |

### 常量

| 名称 |
| --- |
| [ODID](arkts-basicservices-deviceinfo-con.md#odid) |
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
