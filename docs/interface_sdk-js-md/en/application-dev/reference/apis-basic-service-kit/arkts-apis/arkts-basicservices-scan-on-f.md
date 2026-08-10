# on

## Modules to Import

```TypeScript
import { scan } from 'kits/@kit.BasicServicesKit';
```

## on('scanDeviceFound')

```TypeScript
function on(type: 'scanDeviceFound', callback: Callback<ScannerDevice>): void
```

注册扫描仪设备发现事件回调。使用callback异步回调。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Required permissions:** ohos.permission.PRINT

<!--Device-scan-function on(type: 'scanDeviceFound', callback: Callback<ScannerDevice>): void--><!--Device-scan-function on(type: 'scanDeviceFound', callback: Callback<ScannerDevice>): void-End-->

**System capability:** SystemCapability.Print.PrintFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'scanDeviceFound' | Yes | 事件类型。 |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;ScannerDevice&gt; | Yes | 回调函数，返回扫描仪设备发现信息。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 201 | Permission denied. |

## Examples

```TypeScript
import { scan } from '@kit.BasicServicesKit';

scan.on('scanDeviceFound', (device: scan.ScannerDevice) => {
    console.info('scan device found: ' + JSON.stringify(device));
})
```


## on('scanDeviceSync')

```TypeScript
function on(type: 'scanDeviceSync', callback: Callback<ScannerSyncDevice>): void
```

注册扫描仪设备同步事件回调。使用callback异步回调。

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Required permissions:** ohos.permission.MANAGE_PRINT_JOB

<!--Device-scan-function on(type: 'scanDeviceSync', callback: Callback<ScannerSyncDevice>): void--><!--Device-scan-function on(type: 'scanDeviceSync', callback: Callback<ScannerSyncDevice>): void-End-->

**System capability:** SystemCapability.Print.PrintFramework

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'scanDeviceSync' | Yes | 事件类型。 |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;ScannerSyncDevice&gt; | Yes | 回调函数，返回扫描仪设备同步信息。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 201 | Permission denied. |

## Examples

```TypeScript
import { scan } from '@kit.BasicServicesKit';

scan.on('scanDeviceSync', (device: scan.ScannerSyncDevice) => {
    console.info('scan device sync: ' + JSON.stringify(device));
})
```

