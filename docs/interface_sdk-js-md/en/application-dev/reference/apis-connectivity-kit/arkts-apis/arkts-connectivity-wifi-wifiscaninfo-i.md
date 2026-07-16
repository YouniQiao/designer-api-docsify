# WifiScanInfo

Describes the scanned Wi-Fi information.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** WifiScanInfo

<!--Device-wifi-interface WifiScanInfo--><!--Device-wifi-interface WifiScanInfo-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

## Modules to Import

```TypeScript
import { wifi } from '@kit.ConnectivityKit';
```

## band

```TypeScript
band: number
```

Frequency band, 1: 2.4G, 2: 5G

**Type:** number

**Since:** 6

**Deprecated since:** 9

**Substitutes:** band

<!--Device-WifiScanInfo-band: number--><!--Device-WifiScanInfo-band: number-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

## bssid

```TypeScript
bssid: string
```

Wi-Fi bssid(MAC): the length is 6

**Type:** string

**Since:** 6

**Deprecated since:** 9

**Substitutes:** bssid

<!--Device-WifiScanInfo-bssid: string--><!--Device-WifiScanInfo-bssid: string-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

## capabilities

```TypeScript
capabilities: string
```

Hotspot capability

**Type:** string

**Since:** 6

**Deprecated since:** 9

**Substitutes:** capabilities

<!--Device-WifiScanInfo-capabilities: string--><!--Device-WifiScanInfo-capabilities: string-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

## channelWidth

```TypeScript
channelWidth: number
```

Channel width

**Type:** number

**Since:** 6

**Deprecated since:** 9

**Substitutes:** channelWidth

<!--Device-WifiScanInfo-channelWidth: number--><!--Device-WifiScanInfo-channelWidth: number-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

## frequency

```TypeScript
frequency: number
```

Frequency

**Type:** number

**Since:** 6

**Deprecated since:** 9

**Substitutes:** frequency

<!--Device-WifiScanInfo-frequency: number--><!--Device-WifiScanInfo-frequency: number-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

## rssi

```TypeScript
rssi: number
```

Received signal strength indicator (RSSI)

**Type:** number

**Since:** 6

**Deprecated since:** 9

**Substitutes:** rssi

<!--Device-WifiScanInfo-rssi: number--><!--Device-WifiScanInfo-rssi: number-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

## securityType

```TypeScript
securityType: WifiSecurityType
```

Security type: reference definition of WifiSecurityType

**Type:** WifiSecurityType

**Since:** 6

**Deprecated since:** 9

**Substitutes:** securityType

<!--Device-WifiScanInfo-securityType: WifiSecurityType--><!--Device-WifiScanInfo-securityType: WifiSecurityType-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

## ssid

```TypeScript
ssid: string
```

Wi-Fi SSID: the maximum length is 32

**Type:** string

**Since:** 6

**Deprecated since:** 9

**Substitutes:** ssid

<!--Device-WifiScanInfo-ssid: string--><!--Device-WifiScanInfo-ssid: string-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

## timestamp

```TypeScript
timestamp: number
```

Time stamp

**Type:** number

**Since:** 6

**Deprecated since:** 9

**Substitutes:** timestamp

<!--Device-WifiScanInfo-timestamp: number--><!--Device-WifiScanInfo-timestamp: number-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

