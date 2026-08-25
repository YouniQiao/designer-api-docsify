# onBluetoothScanResultChange

## 导入模块

```TypeScript
import { geoLocationManager } from '@kit.LocationKit';
```

## onBluetoothScanResultChange

```TypeScript
function onBluetoothScanResultChange(callback: Callback<BluetoothScanResult>): void
```

订阅蓝牙扫描信息上报事件，使用callback异步回调。本API会启动蓝牙扫描，为了避免产生较多功耗，需要开发者在适当的时机调用 geoLocationManager.off('bluetoothScanResultChange') 接口停止蓝牙扫描。当前仅支持扫描BLE设备。

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.LOCATION and ohos.permission.APPROXIMATELY_LOCATION

**系统能力：** SystemCapability.Location.Location.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[BluetoothScanResult](arkts-location-geolocationmanager-bluetoothscanresult-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [3301000](../errorcode-geoLocationManager.md#3301000-位置服务不可用) |
| [3301100](../errorcode-geoLocationManager.md#3301100-位置功能的开关未开启导致功能失败) |
