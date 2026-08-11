# off

## Modules to Import

```TypeScript
import { scan } from 'kits/@kit.BasicServicesKit';
```

## off('scanDeviceFound')

```TypeScript
function off(type: 'scanDeviceFound', callback?: Callback<ScannerDevice>): void
```

Unregisters a callback used to listen for the scanner discovery event. This API uses an asynchronous callback to return the result.

**Since:** 20

**Required permissions:** ohos.permission.PRINT

<!--Device-scan-function off(type: 'scanDeviceFound', callback?: Callback<ScannerDevice>): void--><!--Device-scan-function off(type: 'scanDeviceFound', callback?: Callback<ScannerDevice>): void-End-->

**System capability:** SystemCapability.Print.PrintFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'scanDeviceFound' | Yes |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;ScannerDevice&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |

## Examples

```TypeScript
import { scan } from '@kit.BasicServicesKit';

let callback = (device: scan.ScannerDevice) => {
    console.info('scan device found: ' + JSON.stringify(device));
};
scan.on('scanDeviceFound', callback);
// Unregister the callback.
scan.off('scanDeviceFound', callback);
```


## off('scanDeviceSync')

```TypeScript
function off(type: 'scanDeviceSync', callback?: Callback<ScannerSyncDevice>): void
```

Unregisters a callback used to listen for the scanner sync event. This API uses an asynchronous callback to return the result.

**Since:** 20

**Required permissions:** ohos.permission.MANAGE_PRINT_JOB

<!--Device-scan-function off(type: 'scanDeviceSync', callback?: Callback<ScannerSyncDevice>): void--><!--Device-scan-function off(type: 'scanDeviceSync', callback?: Callback<ScannerSyncDevice>): void-End-->

**System capability:** SystemCapability.Print.PrintFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'scanDeviceSync' | Yes |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;ScannerSyncDevice&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |

## Examples

```TypeScript
import { scan } from '@kit.BasicServicesKit';

let callback = (device: scan.ScannerSyncDevice) => {
    console.info('scan device sync: ' + JSON.stringify(device));
};
scan.on('scanDeviceSync', callback);
// Unregister the callback.
scan.off('scanDeviceSync', callback);
```
