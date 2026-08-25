# @ohos.deviceInfo

本模块提供终端设备信息查询能力，支持获取设备类型、品牌、型号、系统版本、安全补丁级别、设备唯一标识等多种设备信息，适用于设备适配、版本兼容性检查、设备识别、统计分析等场景，帮助开发者快速获取设备信息进行应用适配和优化。开发者不可配置这些信息。

> **说明：**&gt;
> 本模块首批接口从API version 6开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
> hardwareProfile、incrementalVersion、buildType、buildUser、buildHost、buildTime、buildRootHash等参数返回值为default，这些参数会在设备正式商用版本中配置具体值。
> 本模块接口返回设备常量信息，建议应用只调用一次，不需要频繁调用。未特殊说明的字段，数据长度最大值为96字节。
> 相关错误码请参考[deviceInfo错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-device-info)

**起始版本：** 6

**系统能力：** SystemCapability.Startup.SystemInfo

## 导入模块

```TypeScript
import { deviceInfo } from 'kits/@kit.BasicServicesKit';
```

## 汇总

### 函数

| 名称 |
| --- |
| [apiAvailable](arkts-basicservices-deviceinfo-apiavailable-f.md) |

### 枚举

| 名称 |
| --- |
| [DeviceTypes](arkts-basicservices-deviceinfo-devicetypes-e.md) |
| [PerformanceClassLevel](arkts-basicservices-deviceinfo-performanceclasslevel-e.md) |

### 常量

| 名称 |
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
