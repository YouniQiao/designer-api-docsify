# on

## 导入模块

```TypeScript
import { ble } from '@kit.ConnectivityKit';
```

## on('advertisingStateChange')

```TypeScript
function on(type: 'advertisingStateChange', callback: Callback<AdvertisingStateChangeInfo>): void
```

订阅BLE广播状态。使用Callback异步回调。

**起始版本：** 11

**需要权限：** ohos.permission.ACCESS_BLUETOOTH

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ble-function on(type: 'advertisingStateChange', callback: Callback<AdvertisingStateChangeInfo>): void--><!--Device-ble-function on(type: 'advertisingStateChange', callback: Callback<AdvertisingStateChangeInfo>): void-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'advertisingStateChange' | 是 | 事件回调类型，支持的事件为'advertisingStateChange'，表示广播状态事件。当调用[ble.startAdvertising](arkts-connectivity-ble-startadvertising-f.md)、[ble.stopAdvertising](arkts-connectivity-ble-stopadvertising-f.md)、[ble.enableAdvertising](arkts-connectivity-ble-enableadvertising-f.md)、[ble.disableAdvertising](arkts-connectivity-ble-disableadvertising-f.md)，广播状态改变时，均会触发该事件。 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AdvertisingStateChangeInfo](arkts-connectivity-ble-advertisingstatechangeinfo-i.md)&gt; | 是 | 指定订阅的回调函数，会携带广播状态信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [201](../../errorcode-universal.md#201-api权限校验失败) | Permission verification failed. The application does not have the permission required to call the API. |
| [801](../../errorcode-universal.md#801-api功能在部分设备不支持) | Capability not supported. Possible causes: <br>1. The hardware does not support the capability; <br>2. The chip does not support the capability; <br>3. A dependent service feature is not supported. |
| [2900099](../errorcode-bluetoothManager.md#2900099-操作失败) | Operation failed. |

**示例**

```TypeScript
import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
function onReceiveEvent(data: ble.AdvertisingStateChangeInfo) {
    console.info('bluetooth advertising state = ' + JSON.stringify(data));
}
try {
    ble.on('advertisingStateChange', onReceiveEvent);
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```


## on('BLEDeviceFind')

```TypeScript
function on(type: 'BLEDeviceFind', callback: Callback<Array<ScanResult>>): void
```

订阅BLE设备扫描结果上报事件。使用Callback异步回调。

**起始版本：** 10

**需要权限：** ohos.permission.ACCESS_BLUETOOTH

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务中使用。

<!--Device-ble-function on(type: 'BLEDeviceFind', callback: Callback<Array<ScanResult>>): void--><!--Device-ble-function on(type: 'BLEDeviceFind', callback: Callback<Array<ScanResult>>): void-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'BLEDeviceFind' | 是 | 事件回调类型，支持的事件为'BLEDeviceFind'，表示BLE设备扫描结果上报事件。当调用[ble.startBLEScan](arkts-connectivity-ble-startblescan-f.md) 后，开始BLE扫描，若扫描到BLE设备，触发该事件。 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;[ScanResult](arkts-connectivity-ble-scanresult-i.md)&gt;&gt; | 是 | 指定订阅的回调函数，会携带扫描结果的集合。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [201](../../errorcode-universal.md#201-api权限校验失败) | Permission verification failed. The application does not have the permission required to call the API. |
| [801](../../errorcode-universal.md#801-api功能在部分设备不支持) | Capability not supported. Possible causes: <br>1. The hardware does not support the capability; <br>2. The chip does not support the capability; <br>3. A dependent service feature is not supported. |
| [2900099](../errorcode-bluetoothManager.md#2900099-操作失败) | Operation failed. |

**示例**

```TypeScript
import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
function onReceiveEvent(data: Array<ble.ScanResult>) {
    console.info('bluetooth device find = '+ JSON.stringify(data));
}
try {
    ble.on('BLEDeviceFind', onReceiveEvent);
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```
