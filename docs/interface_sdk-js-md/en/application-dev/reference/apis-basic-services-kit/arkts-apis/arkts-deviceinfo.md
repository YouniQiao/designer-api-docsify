# @ohos.deviceInfo

This module provides APIs for querying terminal device information, including the device type, brand, model, system version, security patch tag, and unique device ID. It is applicable to scenarios such as device adaptation, version compatibility check, device identification, and statistical analysis, helping you quickly obtain device information for application adaptation and optimization. You cannot configure this information.

> **NOTE：**
> 
> The initial APIs of this module are supported since API version 6. New APIs added in later versions are marked with superscripts to indicate their initial version.
> The return values **hardwareProfile**, **incrementalVersion**, **buildType**, **buildUser**, **buildHost**, **buildTime**, and **buildRootHash** are **default**. These parameters will be configured in the official commercial version of the device.
> The APIs of this module return information about device constants. It is recommended that your app call the APIs only once.

**Since:** 6

**System capability:** SystemCapability.Startup.SystemInfo

## Modules to Import

```TypeScript
import deviceInfo from '@kit.BasicServicesKit';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [apiAvailable](arkts-basicservices-deviceinfo-apiavailable-f.md) | Checks whether a specified API version is available on the current device. This API provides compatibility check across different OpenHarmony/Distribution OS versions. A suitable version check method is automatically selected based on the input format and supported API versions. |

### Enums

| Name | Description |
| --- | --- |
| [DeviceTypes](arkts-basicservices-deviceinfo-devicetypes-e.md) | Enumerates device types, which can be used to verify the return value of **deviceType**. |
| [PerformanceClassLevel](arkts-basicservices-deviceinfo-performanceclasslevel-e.md) | Enumerates the device capability levels. |

### Constants

| Name | Description |
| --- | --- |
| [abiList](arkts-basicservices-deviceinfo-con.md#abilist) | Application binary interface (Abi) list.Example: arm64-v8a |
| [bootCount](arkts-basicservices-deviceinfo-con.md#bootcount) | Number of device reboots. If the number cannot be obtained, **-1** is returned.Example: 100 |
| [bootloaderVersion](arkts-basicservices-deviceinfo-con.md#bootloaderversion) | Bootloader version, which identifies the version of the device bootloader.Example: bootloader |
| [brand](arkts-basicservices-deviceinfo-con.md#brand) | Device brand. |
| [buildHost](arkts-basicservices-deviceinfo-con.md#buildhost) | Build host.Example: default |
| [buildRootHash](arkts-basicservices-deviceinfo-con.md#buildroothash) | Build root hash.Example: default |
| [buildTime](arkts-basicservices-deviceinfo-con.md#buildtime) | Build time.Example: default |
| [buildType](arkts-basicservices-deviceinfo-con.md#buildtype) | Build type.Example: default |
| [buildUser](arkts-basicservices-deviceinfo-con.md#builduser) | Build user.Example: default |
| [buildVersion](arkts-basicservices-deviceinfo-con.md#buildversion) | Build version number. The value is the fourth digit in **osFullName**. You are advised to use **deviceInfo.buildVersion** instead of parsing **osFullName** to obtain the value, facilitating efficiency improvement.Example: 1 |
| [chipType](arkts-basicservices-deviceinfo-con.md#chiptype) | Obtains the device CPU chipType by a string.Example: xxxxx |
| [deviceColor](arkts-basicservices-deviceinfo-con.md#devicecolor) | Device color. If the value cannot be obtained, an empty string is returned. |
| [deviceType](arkts-basicservices-deviceinfo-con.md#devicetype) | Device type. For details, see [deviceTypes tag](../../../quick-start/module-configuration-file.md#devicetypes).Example: <!--RP1-->wearable<!--RP1End--> |
| [diskSN](arkts-basicservices-deviceinfo-con.md#disksn) | Serial number of the disk. This API will start a temporary process during execution. When the system load is high, blocking may occur. To ensure the response of the main thread of your application, you are advised not to call this API in the main thread. This value varies depending on the device and is fixed. To improve performance, you can store this information on a local device after obtaining it for the first time.  **NOTE：**This field can be queried only on the 2-in-1 device. For other devices, the query result is empty.ohos.permission.ACCESS_DISK_PHY_INFO Example: 2502EM400567 |
| [displayVersion](arkts-basicservices-deviceinfo-con.md#displayversion) | Product version.Example:<!--RP8-->XXX X.X.X.X<!--RP8End--> |
| [distributionOSApiName](arkts-basicservices-deviceinfo-con.md#distributionosapiname) | Distribution OS API name.<!--Del--> It is defined by the issuer.<!--DelEnd--> |
| [distributionOSApiVersion](arkts-basicservices-deviceinfo-con.md#distributionosapiversion) | Distribution OS API version.<!--Del--> It is defined by the issuer.<!--DelEnd-->Example: 50001 |
| [distributionOSName](arkts-basicservices-deviceinfo-con.md#distributionosname) | Distribution OS name.<!--Del--> It is defined by the issuer.<!--DelEnd-->Example: OpenHarmony |
| [distributionOSReleaseType](arkts-basicservices-deviceinfo-con.md#distributionosreleasetype) | Distribution OS release type.<!--Del--> It is defined by the issuer.<!--DelEnd-->Example: Release |
| [distributionOSVersion](arkts-basicservices-deviceinfo-con.md#distributionosversion) | Distribution OS version.<!--Del--> It is defined by the issuer.<!--DelEnd--><!--RP11--><!--RP11End-->Example: 5.0.0 |
| [featureVersion](arkts-basicservices-deviceinfo-con.md#featureversion) | Feature version number. The value is the third digit in **osFullName**. You are advised to use **deviceInfo.featureVersion** instead of parsing **osFullName** to obtain the value, facilitating efficiency improvement.Example: 0 |
| [firstApiVersion](arkts-basicservices-deviceinfo-con.md#firstapiversion) | First API version.Example: 3 |
| [hardwareModel](arkts-basicservices-deviceinfo-con.md#hardwaremodel) | Hardware model.Example:<!--RP6-->TASA00CVN1<!--RP6End--> |
| [hardwareProfile](arkts-basicservices-deviceinfo-con.md#hardwareprofile) | Hardware profile.  **NOTE：**This API is supported since API version 6 and deprecated since API version 9. You are advised to use [SystemCapability](../../../reference/syscap.md) instead.Example: default |
| [incrementalVersion](arkts-basicservices-deviceinfo-con.md#incrementalversion) | Incremental version, which is the Ohos version number generated during compilation.Example: default |
| [majorVersion](arkts-basicservices-deviceinfo-con.md#majorversion) | Major version number, which increments with the main version. The value is the first digit in **osFullName**. You are advised to use **deviceInfo.majorVersion** instead of parsing **osFullName** to obtain the value, facilitating efficiency improvement.Example: 5 |
| [manufacture](arkts-basicservices-deviceinfo-con.md#manufacture) | Device manufacturer. |
| [marketName](arkts-basicservices-deviceinfo-con.md#marketname) | Marketing name.Example:<!--RP2-->Mate XX<!--RP2End--> |
| [ODID](arkts-basicservices-deviceinfo-con.md#odid) | Open device identifier.An ODID will be regenerated in the following scenarios:Restore a phone to its factory settings.Uninstall and reinstall all applications with the same **developerId** on one device.An ODID is generated based on the following rules:The value is generated based on the **groupId** parsed from the **developerId** in the signature information. As **groupId.developerId** is the rule, if no **groupId** exists, the **developerId** is used as the **groupId**.Applications with the same **developerId** use the same ODID on one device.Applications with different **developerId**s use different ODIDs on one device.Applications with the same **developerId** use different ODIDs on different devices.Applications with different **developerId**s use different ODIDs on different devices.  **NOTE：**The data length is 37 bytes (including the terminator).Example: 1234a567-XXXX-XXXX-XXXX-XXXXXXXXXXXX |
| [osFullName](arkts-basicservices-deviceinfo-con.md#osfullname) | System version. The version number is in the format of **<!--RP12-->OpenHarmony-x.x.x.x**, where **x** is a placeholder for digits. <!--RP12End-->To obtain the value of a segment in the version number, you are advised to use **majorVersion**, **seniorVersion**, **featureVersion**, or **buildVersion**, which can improve efficiency. Parsing **osFullName** is not recommended.Example: <!--RP10-->Openharmony-5.0.0.1<!--RP10End--> |
| [osReleaseType](arkts-basicservices-deviceinfo-con.md#osreleasetype) | OS release type. The options are as follows:  - **Canary**: Preliminary release open only to specific developers. This release does not promise API stability  and may require tolerance of instability.  - **Beta**: Release open to all developers. This release does not promise API stability and may require tolerance  of instability.  - **Release**: Official release open to all developers. This release promises that all APIs are stable.  Example:<!--RP9-->Canary/Beta/Release<!--RP9End--> |
| [performanceClass](arkts-basicservices-deviceinfo-con.md#performanceclass) | Device capability level, which is evaluated based on factors such as CPU, memory, storage read/write performance, and screen resolution.Example: 0 |
| [productModel](arkts-basicservices-deviceinfo-con.md#productmodel) | Product model.Example:<!--RP4-->TAS-AL00<!--RP4End--> |
| [productModelAlias](arkts-basicservices-deviceinfo-con.md#productmodelalias) | Product model alias.Example: TAS-AL00 |
| [productSeries](arkts-basicservices-deviceinfo-con.md#productseries) | Product series.Example:<!--RP3-->TAS<!--RP3End--> |
| [sdkApiVersion](arkts-basicservices-deviceinfo-con.md#sdkapiversion) | SDK API version.Example: 12 |
| [sdkMinorApiVersion](arkts-basicservices-deviceinfo-con.md#sdkminorapiversion) | Starting from API version 26.0.0, the minor version is introduced as part of semantic versioning. It is the middle field in the semantic version and is an integer. The complete API version is represented by sdkApiVersion.sdkMinorApiVersion.sdkPatchApiVersion.Example: If the API version of the system software is 26.0.1, sdkMinorApiVersion is 0. If the API version of the system software is 26.1.0, sdkMinorApiVersion is 1. |
| [sdkPatchApiVersion](arkts-basicservices-deviceinfo-con.md#sdkpatchapiversion) | Starting from API version 26.0.0, the patch version is introduced as part of semantic versioning. It is the third field in the semantic version and is an integer. The complete API version is represented by sdkApiVersion.sdkMinorApiVersion.sdkPatchApiVersion.Example: If the API version of the system software is 26.0.1, sdkPatchApiVersion is 1. If the API version of the system software is 26.1.0, sdkPatchApiVersion is 0. |
| [securityPatchTag](arkts-basicservices-deviceinfo-con.md#securitypatchtag) | Security patch tag.Example:<!--RP7-->2021/01/01<!--RP7End--> |
| [seniorVersion](arkts-basicservices-deviceinfo-con.md#seniorversion) | Senior version number, which increments with architecture and feature updates. The value is the second digit in **osFullName**. You are advised to use **deviceInfo.seniorVersion** instead of parsing **osFullName** to obtain the value, facilitating efficiency improvement.Example: 0 |
| [serial](arkts-basicservices-deviceinfo-con.md#serial) | Serial number of the device. This API will start a temporary process during execution. When the system load is high, blocking may occur. To ensure the response of the main thread of your application, you are advised not to call this API in the main thread. This value varies depending on the device and is fixed. To improve performance, you can store this information on a local device after obtaining it for the first time..  **NOTE：**The device SN can be used as the unique identifier of a device. **Required permission**: ohos.permission.sec.ACCESS_UDID (for system applications and enterprise applications only)Example: The SN varies with the device. |
| [softwareModel](arkts-basicservices-deviceinfo-con.md#softwaremodel) | Software model.Example:<!--RP5-->TAS-AL00<!--RP5End--> |
| [udid](arkts-basicservices-deviceinfo-con.md#udid) | UDID of the device. This API will start a temporary process during execution. When the system load is high, blocking may occur. To ensure the response of the main thread of your application, you are advised not to call this API in the main thread. This value varies depending on the device and is fixed. To improve performance, you can store this information on a local device after obtaining it for the first time.  **NOTE：**The data length is 65 bytes. The UDID can be used as the unique identifier of a device. **Required permission**: ohos.permission.sec.ACCESS_UDID (for system applications and enterprise applications only)Example: 9D6AABD147XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXE5536412 |
| [versionId](arkts-basicservices-deviceinfo-con.md#versionid) | Version ID, which is a concatenation of **deviceType**, **manufacture**, **brand**, **productSeries**, **osFullName**, **productModel**, **softwareModel**, **sdkApiVersion**, **incrementalVersion**, and **buildType**. To obtain a specific field value, you are advised to use the corresponding field directly (such as **deviceType** and **manufacture**) instead of parsing **versionId**, facilitating efficiency improvement. |
