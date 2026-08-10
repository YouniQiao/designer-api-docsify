# WifiScanInfo（系统接口）

Describes the scanned WiFi information.

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

<!--Device-geoLocationManager-export interface WifiScanInfo--><!--Device-geoLocationManager-export interface WifiScanInfo-End-->

**系统能力：** SystemCapability.Location.Location.Core

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { geoLocationManager } from 'kits/@kit.LocationKit';
```

## bssid

```TypeScript
bssid: string
```

WiFi bssid(MAC): the length is 6.

**类型：** string

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

<!--Device-WifiScanInfo-bssid: string--><!--Device-WifiScanInfo-bssid: string-End-->

**系统能力：** SystemCapability.Location.Location.Core

**系统接口：** 此接口为系统接口。

## frequency

```TypeScript
frequency: int
```

Frequency

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

<!--Device-WifiScanInfo-frequency: int--><!--Device-WifiScanInfo-frequency: int-End-->

**系统能力：** SystemCapability.Location.Location.Core

**系统接口：** 此接口为系统接口。

## rssi

```TypeScript
rssi: int
```

Received signal strength indicator (RSSI).

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

<!--Device-WifiScanInfo-rssi: int--><!--Device-WifiScanInfo-rssi: int-End-->

**系统能力：** SystemCapability.Location.Location.Core

**系统接口：** 此接口为系统接口。

## ssid

```TypeScript
ssid: string
```

WiFi SSID: the maximum length is 32.

**类型：** string

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

<!--Device-WifiScanInfo-ssid: string--><!--Device-WifiScanInfo-ssid: string-End-->

**系统能力：** SystemCapability.Location.Location.Core

**系统接口：** 此接口为系统接口。

## timestamp

```TypeScript
timestamp: long
```

Time stamp.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：long

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

<!--Device-WifiScanInfo-timestamp: long--><!--Device-WifiScanInfo-timestamp: long-End-->

**系统能力：** SystemCapability.Location.Location.Core

**系统接口：** 此接口为系统接口。

