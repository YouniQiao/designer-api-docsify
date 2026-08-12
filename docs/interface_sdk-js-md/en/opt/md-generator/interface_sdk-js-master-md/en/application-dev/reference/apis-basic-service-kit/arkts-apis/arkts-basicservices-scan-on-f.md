# on

## Modules to Import

```TypeScript
import { scan } from '@kit.BasicServicesKit';
```

## on('scanDeviceFound')

```TypeScript
function on(type: 'scanDeviceFound', callback: Callback<ScannerDevice>): void
```

Registers a callback used to listen for the scanner discovery event. This API uses an asynchronous callback to return the result.

**Since:** 20

**Required permissions:** ohos.permission.PRINT

<!--Device-scan-function on(type: 'scanDeviceFound', callback: Callback<ScannerDevice>): void--><!--Device-scan-function on(type: 'scanDeviceFound', callback: Callback<ScannerDevice>): void-End-->

**System capability:** SystemCapability.Print.PrintFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'scanDeviceFound' | Yes |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[ScannerDevice](arkts-basicservices-scan-scannerdevice-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |

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

Registers a callback used to listen for the scanner sync event. This API uses an asynchronous callback to return the result.

**Since:** 20

**Required permissions:** ohos.permission.MANAGE_PRINT_JOB

<!--Device-scan-function on(type: 'scanDeviceSync', callback: Callback<ScannerSyncDevice>): void--><!--Device-scan-function on(type: 'scanDeviceSync', callback: Callback<ScannerSyncDevice>): void-End-->

**System capability:** SystemCapability.Print.PrintFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'scanDeviceSync' | Yes |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;[ScannerSyncDevice](arkts-basicservices-scan-scannersyncdevice-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |

## Examples

```TypeScript
import { scan } from '@kit.BasicServicesKit';

scan.on('scanDeviceSync', (device: scan.ScannerSyncDevice) => {
    console.info('scan device sync: ' + JSON.stringify(device));
})
```
