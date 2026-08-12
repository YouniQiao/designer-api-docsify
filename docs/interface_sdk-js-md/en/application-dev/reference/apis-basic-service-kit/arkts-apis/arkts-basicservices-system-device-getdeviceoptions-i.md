# GetDeviceOptions

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 6

<!--Device-unnamed-export interface GetDeviceOptions--><!--Device-unnamed-export interface GetDeviceOptions-End-->

**System capability:** SystemCapability.Startup.SystemInfo.Lite

## Modules to Import

```TypeScript
import { DeviceResponse, GetDeviceOptions } from '@kit.BasicServicesKit';
```

## complete

```TypeScript
complete?: () => void
```

Called when the execution is completed.

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 6

<!--Device-GetDeviceOptions-complete?: () => void--><!--Device-GetDeviceOptions-complete?: () => void-End-->

**System capability:** SystemCapability.Startup.SystemInfo.Lite

## fail

```TypeScript
fail?: (data: any, code: number) => void
```

Called when the device information fails to be obtained.

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 6

<!--Device-GetDeviceOptions-fail?: (data: any, code: number) => void--><!--Device-GetDeviceOptions-fail?: (data: any, code: number) => void-End-->

**System capability:** SystemCapability.Startup.SystemInfo.Lite

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | any | Yes |  |
| code | number | Yes |  |

## success

```TypeScript
success?: (data: DeviceResponse) => void
```

Called when the device information is obtained.

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 6

<!--Device-GetDeviceOptions-success?: (data: DeviceResponse) => void--><!--Device-GetDeviceOptions-success?: (data: DeviceResponse) => void-End-->

**System capability:** SystemCapability.Startup.SystemInfo.Lite

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | [DeviceResponse](arkts-basicservices-system-device-deviceresponse-i.md) | Yes |  |

