# off

## 导入模块

```TypeScript
import { ble } from '@kit.ConnectivityKit';
```

## off('advertisingStateChange')

```TypeScript
function off(type: 'advertisingStateChange', callback?: Callback<AdvertisingStateChangeInfo>): void
```

取消订阅BLE广播状态。广播停止或启动将不再收到通知。

**起始版本：** 11

**需要权限：** ohos.permission.ACCESS_BLUETOOTH

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-ble-function off(type: 'advertisingStateChange', callback?: Callback<AdvertisingStateChangeInfo>): void--><!--Device-ble-function off(type: 'advertisingStateChange', callback?: Callback<AdvertisingStateChangeInfo>): void-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'advertisingStateChange' | 是 | 事件回调类型，支持的事件为'advertisingStateChange'，表示广播状态事件。 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[AdvertisingStateChangeInfo](arkts-connectivity-ble-advertisingstatechangeinfo-i.md)&gt; | 否 | 指定取消订阅的回调函数通知。若传参，则需与[ble.on('advertisingStateChange')](arkts-connectivity-ble-on-f.md#onadvertisingstatechange)中的回调函数一致；若无传参，则取消订阅该type对应的所有回调函数通知。 |

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
    ble.off('advertisingStateChange', onReceiveEvent);
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```


## off('BLEDeviceFind')

```TypeScript
function off(type: 'BLEDeviceFind', callback?: Callback<Array<ScanResult>>): void
```

取消订阅BLE设备扫描结果上报事件。

若不再需要扫描BLE设备，调用[ble.stopBLEScan](arkts-connectivity-ble-stopblescan-f.md)方法后，需要调用此方法取消订阅。

**起始版本：** 10

**需要权限：** ohos.permission.ACCESS_BLUETOOTH

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务中使用。

<!--Device-ble-function off(type: 'BLEDeviceFind', callback?: Callback<Array<ScanResult>>): void--><!--Device-ble-function off(type: 'BLEDeviceFind', callback?: Callback<Array<ScanResult>>): void-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'BLEDeviceFind' | 是 | 事件回调类型，支持的事件为'BLEDeviceFind'，表示BLE设备扫描结果上报事件。 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;[ScanResult](arkts-connectivity-ble-scanresult-i.md)&gt;&gt; | 否 | 指定取消订阅的回调函数通知。若传参，则需与[ble.on('BLEDeviceFind')](arkts-connectivity-ble-on-f.md#onbledevicefind)中的回调函数一致；若无传参，则取消订阅该type对应的所有回调函数通知。 |

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
    ble.off('BLEDeviceFind', onReceiveEvent);
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
```
