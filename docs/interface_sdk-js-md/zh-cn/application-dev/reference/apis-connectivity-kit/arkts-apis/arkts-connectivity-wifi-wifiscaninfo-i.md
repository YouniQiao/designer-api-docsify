# WifiScanInfo

Describes the scanned Wi-Fi information.

**起始版本：** 6

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为6。

**废弃版本：** 9

**替代接口：** ohos.wifiManager/wifiManager.WifiScanInfo

<!--Device-wifi-interface WifiScanInfo--><!--Device-wifi-interface WifiScanInfo-End-->

**系统能力：** SystemCapability.Communication.WiFi.STA

## 导入模块

```TypeScript
import { wifi } from 'kits/@kit.ConnectivityKit';
```

## band

```TypeScript
band: number
```

Frequency band, 1: 2.4G, 2: 5G

**类型：** number

**起始版本：** 6

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为6。

**废弃版本：** 9

**替代接口：** ohos.wifiManager/wifiManager.WifiScanInfo.band

<!--Device-WifiScanInfo-band: number--><!--Device-WifiScanInfo-band: number-End-->

**系统能力：** SystemCapability.Communication.WiFi.STA

## bssid

```TypeScript
bssid: string
```

Wi-Fi bssid(MAC): the length is 6

**类型：** string

**起始版本：** 6

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为6。

**废弃版本：** 9

**替代接口：** ohos.wifiManager/wifiManager.WifiScanInfo.bssid

<!--Device-WifiScanInfo-bssid: string--><!--Device-WifiScanInfo-bssid: string-End-->

**系统能力：** SystemCapability.Communication.WiFi.STA

## capabilities

```TypeScript
capabilities: string
```

Hotspot capability

**类型：** string

**起始版本：** 6

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为6。

**废弃版本：** 9

**替代接口：** ohos.wifiManager/wifiManager.WifiScanInfo.capabilities

<!--Device-WifiScanInfo-capabilities: string--><!--Device-WifiScanInfo-capabilities: string-End-->

**系统能力：** SystemCapability.Communication.WiFi.STA

## channelWidth

```TypeScript
channelWidth: number
```

Channel width

**类型：** number

**起始版本：** 6

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为6。

**废弃版本：** 9

**替代接口：** ohos.wifiManager/wifiManager.WifiScanInfo.channelWidth

<!--Device-WifiScanInfo-channelWidth: number--><!--Device-WifiScanInfo-channelWidth: number-End-->

**系统能力：** SystemCapability.Communication.WiFi.STA

## frequency

```TypeScript
frequency: number
```

Frequency

**类型：** number

**起始版本：** 6

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为6。

**废弃版本：** 9

**替代接口：** ohos.wifiManager/wifiManager.WifiScanInfo.frequency

<!--Device-WifiScanInfo-frequency: number--><!--Device-WifiScanInfo-frequency: number-End-->

**系统能力：** SystemCapability.Communication.WiFi.STA

## rssi

```TypeScript
rssi: number
```

Received signal strength indicator (RSSI)

**类型：** number

**起始版本：** 6

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为6。

**废弃版本：** 9

**替代接口：** ohos.wifiManager/wifiManager.WifiScanInfo.rssi

<!--Device-WifiScanInfo-rssi: number--><!--Device-WifiScanInfo-rssi: number-End-->

**系统能力：** SystemCapability.Communication.WiFi.STA

## securityType

```TypeScript
securityType: WifiSecurityType
```

Security type: reference definition of WifiSecurityType

**类型：** [WifiSecurityType](../../apis-mdm-kit/arkts-apis/arkts-mdm-wifimanager-wifisecuritytype-e.md)

**起始版本：** 6

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为6。

**废弃版本：** 9

**替代接口：** ohos.wifiManager/wifiManager.WifiScanInfo.securityType

<!--Device-WifiScanInfo-securityType: WifiSecurityType--><!--Device-WifiScanInfo-securityType: WifiSecurityType-End-->

**系统能力：** SystemCapability.Communication.WiFi.STA

## ssid

```TypeScript
ssid: string
```

Wi-Fi SSID: the maximum length is 32

**类型：** string

**起始版本：** 6

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为6。

**废弃版本：** 9

**替代接口：** ohos.wifiManager/wifiManager.WifiScanInfo.ssid

<!--Device-WifiScanInfo-ssid: string--><!--Device-WifiScanInfo-ssid: string-End-->

**系统能力：** SystemCapability.Communication.WiFi.STA

## timestamp

```TypeScript
timestamp: number
```

Time stamp

**类型：** number

**起始版本：** 6

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为6。

**废弃版本：** 9

**替代接口：** ohos.wifiManager/wifiManager.WifiScanInfo.timestamp

<!--Device-WifiScanInfo-timestamp: number--><!--Device-WifiScanInfo-timestamp: number-End-->

**系统能力：** SystemCapability.Communication.WiFi.STA

