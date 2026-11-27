# on

## 导入模块

```TypeScript
import { bluetooth } from '@kit.ConnectivityKit';
```

## on('BLEDeviceFind')

```TypeScript
function on(type: 'BLEDeviceFind', callback: Callback<Array<ScanResult>>): void
```

订阅BLE设备发现上报事件。

从API version 7开始支持，从API version 9开始废弃。

**起始版本：** 7

**废弃版本：** 9

**替代接口：** BLEDeviceFind

**需要权限：** ohos.permission.USE_BLUETOOTH

<!--Device-BLE-function on(type: 'BLEDeviceFind', callback: Callback<Array<ScanResult>>): void--><!--Device-BLE-function on(type: 'BLEDeviceFind', callback: Callback<Array<ScanResult>>): void-End-->

**系统能力：** SystemCapability.Communication.Bluetooth.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'BLEDeviceFind' | 是 | 填写"BLEDeviceFind"字符串，表示BLE设备发现事件。 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;ScanResult&gt;&gt; | 是 | 表示回调函数的入参，发现的设备集合。回调函数由用户创建通过该接口注册。 |

**示例**

```TypeScript
function onReceiveEvent(data : Array<bluetooth.ScanResult>) {
    console.info('bluetooth device find = '+ JSON.stringify(data));
}
bluetooth.BLE.on('BLEDeviceFind', onReceiveEvent);
```
