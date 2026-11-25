# cancelPairedDevice

## Modules to Import

```TypeScript
import { connection } from '@kit.ConnectivityKit';
```

## cancelPairedDevice

```TypeScript
function cancelPairedDevice(deviceId: string, callback: AsyncCallback<void>): void
```

Delete the paired peer device. Use the Callback asynchronous callback. The API version is 26.1.0 or later. When an NA calls this API, a confirmation dialog box is displayed before the pairing is deleted. The pairing is removed only after the confirmation dialog box is displayed.

**Since:** 26.1.0

**Required permissions:** ohos.permission.ACCESS_BLUETOOTH

**Model restriction:** This API can be used only in the stage model.

<!--Device-connection-function cancelPairedDevice(deviceId: string, callback: AsyncCallback<void>): void--><!--Device-connection-function cancelPairedDevice(deviceId: string, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| deviceId | string | Yes | Indicates the MAC address of the peer device to be deleted. The value consists of 12 hexadecimal characters and five colons(:), for example, 11:22:33:AA:BB:FF. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback function. If the paired device is deleted successfully, the value of err is undefined. Otherwise, the object is incorrect. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. The application does not have the permission required to call the API. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | [Sync] Parameter error. Possible causes: <br>1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; <br>3. Parameter verification failed. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. Possible causes: <br>1. The hardware does not support the capability; <br>2. The chip does not support the capability; <br>3. A dependent service feature is not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900013 | The user did not respond.<br>**Applicable version:** 26.1.0 and later |
| 2900014 | The user refused the action.<br>**Applicable version:** 26.1.0 and later |
| [2900016](../errorcode-bluetoothManager.md#2900016-device-not-paired) | Device unpaired.<br>**Applicable version:** 26.1.0 and later |
| 2900099 | Operation failed. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
// callback
try {
    connection.cancelPairedDevice('11:22:33:44:55:66', (err: BusinessError) => {
        console.info('cancelPairedDevice, device name err:' + JSON.stringify(err));
    });
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```


## cancelPairedDevice

```TypeScript
function cancelPairedDevice(deviceId: string): Promise<void>
```

Delete the paired peer device. Use Promise asynchronous callbacks. The API version is 26.1.0 or later. When an NA calls this API, a confirmation dialog box is displayed before the pairing is deleted. The pairing is removed only after the confirmation dialog box is displayed.

**Since:** 26.1.0

**Required permissions:** ohos.permission.ACCESS_BLUETOOTH

**Model restriction:** This API can be used only in the stage model.

<!--Device-connection-function cancelPairedDevice(deviceId: string): Promise<void>--><!--Device-connection-function cancelPairedDevice(deviceId: string): Promise<void>-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| deviceId | string | Yes | Indicates the MAC address of the peer device to be deleted. The value consists of 12 hexadecimal characters and five colons(:), for example, 11:22:33:AA:BB:FF. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise object. No result is returned. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. The application does not have the permission required to call the API. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | [Sync] Parameter error. Possible causes: <br>1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; <br>3. Parameter verification failed. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. Possible causes: <br>1. The hardware does not support the capability; <br>2. The chip does not support the capability; <br>3. A dependent service feature is not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900013 | The user did not respond.<br>**Applicable version:** 26.1.0 and later |
| 2900014 | The user refused the action.<br>**Applicable version:** 26.1.0 and later |
| [2900016](../errorcode-bluetoothManager.md#2900016-device-not-paired) | Device unpaired.<br>**Applicable version:** 26.1.0 and later |
| 2900099 | Operation failed. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
// promise
try {
    connection.cancelPairedDevice('11:22:33:44:55:66').then(() => {
        console.info('cancelPairedDevice');
    }, (error: BusinessError) => {
        console.error('cancelPairedDevice: errCode:' + error.code + ',errMessage' + error.message);
    })

} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```
