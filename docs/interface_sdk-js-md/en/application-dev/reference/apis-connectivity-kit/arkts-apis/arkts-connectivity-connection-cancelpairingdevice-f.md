# cancelPairingDevice

## Modules to Import

```TypeScript
import { connection } from '@kit.ConnectivityKit';
```

## cancelPairingDevice

```TypeScript
function cancelPairingDevice(deviceId: string, callback: AsyncCallback<void>): void
```

This interface is used to cancel the pairing between the current application and the peer device. Use the Callback asynchronous callback. This API is used to cancel an ongoing pairing process. If the peer device is not pairing, calling this API fails.

**Since:** 26.1.0

**Required permissions:** ohos.permission.ACCESS_BLUETOOTH

**Model restriction:** This API can be used only in the stage model.

<!--Device-connection-function cancelPairingDevice(deviceId: string, callback: AsyncCallback<void>): void--><!--Device-connection-function cancelPairingDevice(deviceId: string, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| deviceId | string | Yes | Indicates the MAC address of the peer device to be unpaired. The value consists of 12 hexadecimal characters and five colons(:), for example, 11:22:33:AA:BB:FF. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback function. If the pairing is successfully canceled, err is undefined. Otherwise, it is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. The application does not have the permission required to call the API. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | [Sync] Parameter error. Possible causes: <br>1. Mandatory parameters are left unspecified; <br>2. Incorrect parameter types; <br>3. Parameter verification failed. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. Possible causes: <br>1. The hardware does not support the capability; <br>2. The chip does not support the capability; <br>3. A dependent service feature is not supported. |
| 2900001 | Service stopped. |
| 2900003 | Bluetooth disabled. |
| 2900018 | The pairing is initiated by another application and cannot be cancelled.<br>**Applicable version:** 26.1.0 and later |
| 2900019 | The device is not in the pairing state.<br>**Applicable version:** 26.1.0 and later |
| 2900099 | Operation failed. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
try {
    connection.cancelPairingDevice('XX:XX:XX:XX:XX:XX');
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```


## cancelPairingDevice

```TypeScript
function cancelPairingDevice(deviceId: string): Promise<void>
```

This interface is used to cancel the pairing between the current application and the peer device. Use Promise asynchronous callback. This API is used to cancel an ongoing pairing process. If the peer device is not pairing, calling this API fails.

**Since:** 26.1.0

**Required permissions:** ohos.permission.ACCESS_BLUETOOTH

**Model restriction:** This API can be used only in the stage model.

<!--Device-connection-function cancelPairingDevice(deviceId: string): Promise<void>--><!--Device-connection-function cancelPairingDevice(deviceId: string): Promise<void>-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| deviceId | string | Yes | Indicates the MAC address of the peer device to be unpaired. The value consists of 12 hexadecimal characters and five colons(:), for example, 11:22:33:AA:BB:FF. |

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
| 2900018 | The pairing is initiated by another application and cannot be cancelled.<br>**Applicable version:** 26.1.0 and later |
| 2900019 | The device is not in the pairing state.<br>**Applicable version:** 26.1.0 and later |
| 2900099 | Operation failed. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
try {
    connection.cancelPairingDevice('XX:XX:XX:XX:XX:XX');
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```
