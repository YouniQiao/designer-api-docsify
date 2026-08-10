# WirelessSignalFeature（系统接口）

Indicates wireless signal feature.

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Dyn起始版本为26.0.0；ArkTS-Sta起始版本为26.1.0。

<!--Device-geoLocationManager-export interface WirelessSignalFeature--><!--Device-geoLocationManager-export interface WirelessSignalFeature-End-->

**系统能力：** SystemCapability.Location.Location.Geofence

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { geoLocationManager } from 'kits/@kit.LocationKit';
```

## mac

```TypeScript
mac: Array<string>
```

Indicates MAC array.

**类型：** Array&lt;string&gt;

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Dyn起始版本为26.0.0；ArkTS-Sta起始版本为26.1.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-WirelessSignalFeature-mac: Array<string>--><!--Device-WirelessSignalFeature-mac: Array<string>-End-->

**系统能力：** SystemCapability.Location.Location.Geofence

**系统接口：** 此接口为系统接口。

## rssiAvg

```TypeScript
rssiAvg: int
```

Indicates average RSSI value.The value range is all integers.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Dyn起始版本为26.0.0；ArkTS-Sta起始版本为26.1.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-WirelessSignalFeature-rssiAvg: int--><!--Device-WirelessSignalFeature-rssiAvg: int-End-->

**系统能力：** SystemCapability.Location.Location.Geofence

**系统接口：** 此接口为系统接口。

## rssiStandardDeviation

```TypeScript
rssiStandardDeviation: double
```

Indicates RSSI standard deviation.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：double

**起始版本：** 26.0.0

**ArkTS模式：** ArkTS-Dyn起始版本为26.0.0；ArkTS-Sta起始版本为26.1.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-WirelessSignalFeature-rssiStandardDeviation: double--><!--Device-WirelessSignalFeature-rssiStandardDeviation: double-End-->

**系统能力：** SystemCapability.Location.Location.Geofence

**系统接口：** 此接口为系统接口。

