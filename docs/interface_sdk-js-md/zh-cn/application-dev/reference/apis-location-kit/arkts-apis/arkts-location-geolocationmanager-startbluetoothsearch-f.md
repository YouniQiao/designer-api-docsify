# startBluetoothSearch

## 导入模块

```TypeScript
import { geoLocationManager } from 'kits/@kit.LocationKit';
```

## startBluetoothSearch

```TypeScript
function startBluetoothSearch(
      request: BluetoothSearchRequestParams, callback: Callback<BluetoothScanResult>): void
```

Starts Bluetooth scanning and matches the device ID list in the input parameter with the Bluetooth scanning result. If the matching is successful, the Bluetooth device information is returned through the callback.

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Dyn起始版本为26.0.0；ArkTS-Sta起始版本为26.1.0。

**需要权限：** ohos.permission.APPROXIMATELY_LOCATION

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-geoLocationManager-function startBluetoothSearch(      request: BluetoothSearchRequestParams, callback: Callback<BluetoothScanResult>): void--><!--Device-geoLocationManager-function startBluetoothSearch(      request: BluetoothSearchRequestParams, callback: Callback<BluetoothScanResult>): void-End-->

**系统能力：** SystemCapability.Location.Location.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| request | [BluetoothSearchRequestParams](arkts-location-geolocationmanager-bluetoothsearchrequestparams-i.md) | 是 | Indicates the configuration parameters for the Bluetooth search function. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;BluetoothScanResult&gt; | 是 | Callback used to return \\${BluetoothScanResult}. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Failed to call \\${geoLocationManager.startBluetoothSearch} due to limited device capabilities. |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 3301000 | The location service is unavailable. |
| 3301800 | Failed to start Bluetooth scanning. |

## 示例

```TypeScript
import { geoLocationManager } from '@kit.LocationKit';

private callback = (bluetoothScanResult: geoLocationManager.BluetoothScanResult) => {
  if (bluetoothScanResult) {
    console.info('bluetoothScanResult: deviceId=' + bluetoothScanResult.deviceId);
      try {
         // 开发者需要考虑在合适的时机调用stopBluetoothSearch停止蓝牙扫描以节省功耗，本代码仅作为参考
         geoLocationManager.stopBluetoothSearch(this.callback);
      } catch (err) {
         console.error("errCode:" + err.code + ", message:" + err.message);
      }
  }
};
let request: geoLocationManager.BluetoothSearchRequestParams = {
  'rssiThreshold': -=100,
  'deviceIdArray': ['98:56:07:E6:AA:46','4E:E6:D2:02:27:F9']
};
 
try {
  geoLocationManager.startBluetoothSearch(request, this.callback);
} catch (err) {
  console.error("errCode:" + err.code + ", message:" + err.message);
}
```

