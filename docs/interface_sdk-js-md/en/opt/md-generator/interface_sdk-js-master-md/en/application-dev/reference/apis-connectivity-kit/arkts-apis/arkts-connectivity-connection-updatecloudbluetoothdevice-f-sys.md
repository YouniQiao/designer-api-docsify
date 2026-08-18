# updateCloudBluetoothDevice (System API)

## Modules to Import

```TypeScript
```

## updateCloudBluetoothDevice

```TypeScript
function updateCloudBluetoothDevice(trustedPairedDevices: TrustedPairedDevices): Promise<void>
```

update cloud devices.

**Since:** 23

**Required permissions:** ohos.permission.ACCESS_BLUETOOTH and ohos.permission.MANAGE_BLUETOOTH

**Model restriction:** This API can be used only in the stage model.

<!--Device-connection-function updateCloudBluetoothDevice(trustedPairedDevices: TrustedPairedDevices): Promise<void>--><!--Device-connection-function updateCloudBluetoothDevice(trustedPairedDevices: TrustedPairedDevices): Promise<void>-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [trustedPairedDevices](arkts-connectivity-connection-trustedpaireddevices-i-sys.md) | [TrustedPairedDevices](arkts-connectivity-connection-trustedpaireddevices-i-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 2900001 |
| 2900003 |
| 2900099 |

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
