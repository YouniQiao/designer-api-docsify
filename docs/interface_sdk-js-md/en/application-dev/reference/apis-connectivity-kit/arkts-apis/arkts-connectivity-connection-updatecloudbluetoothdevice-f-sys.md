# updateCloudBluetoothDevice (System API)

## Modules to Import

```TypeScript
import { connection } from '@kit.ConnectivityKit';
```

## updateCloudBluetoothDevice

```TypeScript
function updateCloudBluetoothDevice(trustedPairedDevices: TrustedPairedDevices): Promise<void>
```

update cloud devices.

**Since:** 15

**Required permissions:** ohos.permission.ACCESS_BLUETOOTH and ohos.permission.MANAGE_BLUETOOTH

**Model restriction:** This API can be used only in the stage model.

<!--Device-connection-function updateCloudBluetoothDevice(trustedPairedDevices: TrustedPairedDevices): Promise<void>--><!--Device-connection-function updateCloudBluetoothDevice(trustedPairedDevices: TrustedPairedDevices): Promise<void>-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| trustedPairedDevices | [TrustedPairedDevices](arkts-connectivity-connection-trustedpaireddevices-i-sys.md) | Yes | Indicates the cloud devices. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Returns the promise object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. The application does not have the permission required to call the API. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | [Sync] Parameter error. Possible causes: <br>1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; <br>3. Parameter verification failed. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. Possible causes: <br>1. The hardware does not support the capability; <br>2. The chip does not support the capability; <br>3. A dependent service feature is not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900099 | Operation failed. |

<!--Del-->
**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
// promise
/**
 * Update cloud devices in Bluetooth settings.
 */
const trustPairDeviceArr: connection.TrustedPairedDevice[] = [];
let descBuffer = new ArrayBuffer(1);
trustPairDeviceArr.push({
    sn: '',
    deviceType: '',
    modelId: '',
    manufactory: '',
    productId: '',
    hiLinkVersion: '',
    macAddress: '11:22:33:44:55:66',
    serviceType: '',
    serviceId: '',
    deviceName: '',
    uuids: '',
    bluetoothClass: 0,
    token: descBuffer,
    deviceNameTime: 0,
    secureAdvertisingInfo: descBuffer,
    pairState: 0
    });
const trustPairDevices: connection.TrustedPairedDevices = { trustedPairedDevices: trustPairDeviceArr };
try {
    connection.updateCloudBluetoothDevice(trustPairDevices)
        .then(() => {
            console.info('updateCloudBluetoothDevice success!');
        })
        .catch((err: BusinessError) => {
            console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
        });
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```

<!--DelEnd-->
