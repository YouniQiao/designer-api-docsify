# @ohos.deviceInfo

The **deviceInfo** module provides terminal device information query, which cannot be configured by developers.

> **NOTE：**
> 
> The initial APIs of this module are supported since API version 6. Newly added APIs
> will be marked with a superscript to indicate their earliest API version.
> Some parameters whose return value is the default value are not yet available.
> The APIs of this module return information about device getants. You are not expected to call these APIs
> frequently.

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Model restriction:** This API can be used only in the stage model.

<!--Device-unnamed-declare namespace deviceInfo--><!--Device-unnamed-declare namespace deviceInfo-End-->

**System capability:** SystemCapability.Startup.SystemInfo

## Modules to Import

```TypeScript
import { deviceInfo } from '@kit.BasicServicesKit';
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

