# BluetoothSearchRequestParams

Indicates request parameters for Bluetooth search function.

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Dyn起始版本为26.0.0；ArkTS-Sta起始版本为26.1.0。

<!--Device-geoLocationManager-export interface BluetoothSearchRequestParams--><!--Device-geoLocationManager-export interface BluetoothSearchRequestParams-End-->

**系统能力：** SystemCapability.Location.Location.Core

## 导入模块

```TypeScript
import { geoLocationManager } from 'kits/@kit.LocationKit';
```

## deviceIdArray

```TypeScript
deviceIdArray: Array<string>
```

Indicates the list of Bluetooth device ID that need to be search.

**类型：** Array&lt;string&gt;

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Dyn起始版本为26.0.0；ArkTS-Sta起始版本为26.1.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-BluetoothSearchRequestParams-deviceIdArray: Array<string>--><!--Device-BluetoothSearchRequestParams-deviceIdArray: Array<string>-End-->

**系统能力：** SystemCapability.Location.Location.Core

## rssiThreshold

```TypeScript
rssiThreshold?: int
```

Indicates the Bluetooth RSSI threshold,only search Bluetooth BSSID with RSSI greater than this threshold.The value range is all integers.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Dyn起始版本为26.0.0；ArkTS-Sta起始版本为26.1.0。

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-BluetoothSearchRequestParams-rssiThreshold?: int--><!--Device-BluetoothSearchRequestParams-rssiThreshold?: int-End-->

**系统能力：** SystemCapability.Location.Location.Core

