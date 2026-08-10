# GetDeviceOptions

定义设备信息获取的参数选项。

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 6

<!--Device-unnamed-export interface GetDeviceOptions--><!--Device-unnamed-export interface GetDeviceOptions-End-->

**System capability:** SystemCapability.Startup.SystemInfo.Lite

## Modules to Import

```TypeScript
import { DeviceResponse, GetDeviceOptions } from 'kits/@kit.BasicServicesKit';
```

## complete

```TypeScript
complete?: () => void
```

接口调用结束的回调函数，在接口调用完成后（无论成功或失败）执行，适用于需执行清理或收尾工作的场景。不传入时不执行结束回调。

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 6

<!--Device-GetDeviceOptions-complete?: () => void--><!--Device-GetDeviceOptions-complete?: () => void-End-->

**System capability:** SystemCapability.Startup.SystemInfo.Lite

## fail

```TypeScript
fail?: (data: any, code: number) => void
```

接口调用失败的回调函数，在接口调用失败时执行。data为失败时返回的错误信息对象或错误描述字符串，code为失败返回的错误码。

code:200，表示返回结果中存在无法获得的信息。

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

接口调用成功的回调函数，在接口调用成功时执行。data 为成功返回的设备信息。不传入时无法获取设备信息，建议设置此回调。

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 6

<!--Device-GetDeviceOptions-success?: (data: DeviceResponse) => void--><!--Device-GetDeviceOptions-success?: (data: DeviceResponse) => void-End-->

**System capability:** SystemCapability.Startup.SystemInfo.Lite

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | [DeviceResponse](arkts-basicservices-system-device-deviceresponse-i.md) | Yes |  |

