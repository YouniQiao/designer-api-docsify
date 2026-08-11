# off (System API)

## Modules to Import

```TypeScript
import { scan } from 'kits/@kit.BasicServicesKit';
```

## off('scanDeviceAdd')

```TypeScript
function off(type: 'scanDeviceAdd', callback?: Callback<ScannerDevice>): void
```

Unregisters the callback used to listen for the scanner addition event. This API uses an asynchronous callback to return the result.

**Since:** 20

**Required permissions:** ohos.permission.MANAGE_PRINT_JOB

<!--Device-scan-function off(type: 'scanDeviceAdd', callback?: Callback<ScannerDevice>): void--><!--Device-scan-function off(type: 'scanDeviceAdd', callback?: Callback<ScannerDevice>): void-End-->

**System capability:** SystemCapability.Print.PrintFramework

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'scanDeviceAdd' | Yes |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;ScannerDevice&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { scan } from '@kit.BasicServicesKit';

let callback = (device: scan.ScannerDevice) => {
    console.info('scan device add: ' + JSON.stringify(device));
};
scan.on('scanDeviceAdd', callback);
// Unregister the callback.
scan.off('scanDeviceAdd', callback);
```


## off('scanDeviceDel')

```TypeScript
function off(type: 'scanDeviceDel', callback?: Callback<ScannerDevice>): void
```

Unregisters the callback used to listen for the scanner deletion event. This API uses an asynchronous callback to return the result.

**Since:** 20

**Required permissions:** ohos.permission.MANAGE_PRINT_JOB

<!--Device-scan-function off(type: 'scanDeviceDel', callback?: Callback<ScannerDevice>): void--><!--Device-scan-function off(type: 'scanDeviceDel', callback?: Callback<ScannerDevice>): void-End-->

**System capability:** SystemCapability.Print.PrintFramework

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'scanDeviceDel' | Yes |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;ScannerDevice&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { scan } from '@kit.BasicServicesKit';

let callback = (device: scan.ScannerDevice) => {
    console.info('scan device delete: ' + JSON.stringify(device));
};
scan.on('scanDeviceDel', callback);
// Unregister the callback.
scan.off('scanDeviceDel', callback);
```
