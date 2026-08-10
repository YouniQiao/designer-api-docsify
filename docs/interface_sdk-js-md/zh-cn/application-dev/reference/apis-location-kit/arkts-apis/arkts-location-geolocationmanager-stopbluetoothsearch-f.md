# stopBluetoothSearch

## 导入模块

```TypeScript
import { geoLocationManager } from 'kits/@kit.LocationKit';
```

## stopBluetoothSearch

```TypeScript
function stopBluetoothSearch(callback?: Callback<BluetoothScanResult>): void
```

Stop Bluetooth scanning and searching.

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Dyn起始版本为26.0.0；ArkTS-Sta起始版本为26.1.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-geoLocationManager-function stopBluetoothSearch(callback?: Callback<BluetoothScanResult>): void--><!--Device-geoLocationManager-function stopBluetoothSearch(callback?: Callback<BluetoothScanResult>): void-End-->

**系统能力：** SystemCapability.Location.Location.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;BluetoothScanResult&gt; | 否 | Callback used to return \\${BluetoothScanResult}. It should be the same as the callback passed to \\${geoLocationManager.startBluetoothSearch}. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call \\${geoLocationManager.stopBluetoothSearch} due to limited device capabilities. |
| 3301000 | The location service is unavailable. |

## 示例

```TypeScript
import { geoLocationManager } from '@kit.LocationKit';
 
let request: geoLocationManager.BluetoothSearchRequestParams = {
  'rssiThreshold': -100,
  'deviceIdArray': ['98:56:07:E6:AA:46','4E:E6:D2:02:27:F9']
};
let callback = (bluetoothScanResult: geoLocationManager.BluetoothScanResult) => {
  if (bluetoothScanResult) {
    console.info('bluetoothScanResult: deviceId=' + bluetoothScanResult.deviceId);
  }
};
try {
  geoLocationManager.startBluetoothSearch(request, callback);
  geoLocationManager.stopBluetoothSearch(callback);
} catch (err) {
  console.error("errCode:" + err.code + ", message:" + err.message);
}
```

