# off

## Modules to Import

```TypeScript
import { ble } from '@kit.ConnectivityKit';
```

## off('advertisingStateChange')

```TypeScript
function off(type: 'advertisingStateChange', callback?: Callback<AdvertisingStateChangeInfo>): void
```

Unsubscribe from advertising state change event.

**Since:** 11

**Required permissions:** ohos.permission.ACCESS_BLUETOOTH

**Model restriction:** This API can be used only in the stage model.

<!--Device-ble-function off(type: 'advertisingStateChange', callback?: Callback<AdvertisingStateChangeInfo>): void--><!--Device-ble-function off(type: 'advertisingStateChange', callback?: Callback<AdvertisingStateChangeInfo>): void-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'advertisingStateChange' | Yes | Type of the advertising state to listen for. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AdvertisingStateChangeInfo](arkts-connectivity-ble-advertisingstatechangeinfo-i.md)&gt; | No | Specifies the callback function notification for unsubscription. If the parameter is transferred, the parameter must be set to [ble.on('advertisingStateChange')] [on](arkts-connectivity-ble-on-f.md#onadvertisingstatechange) The callback functions in * are the same. If no parameter is transferred, all callback function notifications corresponding to the type are unsubscribed from. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. The application does not have the permission required to call the API. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. Possible causes: <br>1. The hardware does not support the capability; <br>2. The chip does not support the capability; <br>3. A dependent service feature is not supported. |
| 2900099 | Operation failed. |

**Examples**

```TypeScript
import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
function onReceiveEvent(data: ble.AdvertisingStateChangeInfo) {
    console.info('bluetooth advertising state = ' + JSON.stringify(data));
}
try {
    ble.on('advertisingStateChange', onReceiveEvent);
    ble.off('advertisingStateChange', onReceiveEvent);
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```


## off('BLEDeviceFind')

```TypeScript
function off(type: 'BLEDeviceFind', callback?: Callback<Array<ScanResult>>): void
```

Unsubscribe BLE scan result.

**Since:** 10

**Required permissions:** ohos.permission.ACCESS_BLUETOOTH

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-ble-function off(type: 'BLEDeviceFind', callback?: Callback<Array<ScanResult>>): void--><!--Device-ble-function off(type: 'BLEDeviceFind', callback?: Callback<Array<ScanResult>>): void-End-->

**System capability:** SystemCapability.Communication.Bluetooth.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'BLEDeviceFind' | Yes | Type of the scan result event to listen for. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;[ScanResult](arkts-connectivity-ble-scanresult-i.md)&gt;&gt; | No | Specifies the callback function notification for unsubscription. If the parameter is transferred, the parameter must be set to The callback functions in [ble.on('BLEDeviceFind')](arkts-connectivity-ble-on-f.md#onbledevicefind) are consistent; if If there is no input parameter, all callback function notifications corresponding to the type are unsubscribed. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. The application does not have the permission required to call the API. |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. Possible causes: <br>1. The hardware does not support the capability; <br>2. The chip does not support the capability; <br>3. A dependent service feature is not supported. |
| 2900099 | Operation failed. |

**Examples**

```TypeScript
import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
function onReceiveEvent(data: Array<ble.ScanResult>) {
    console.info('bluetooth device find = '+ JSON.stringify(data));
}
try {
    ble.on('BLEDeviceFind', onReceiveEvent);
    ble.off('BLEDeviceFind', onReceiveEvent);
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```
