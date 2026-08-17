# WifiLinkedInfo

Wi-Fi connection information.

**Since:** 23

<!--Device-wifiManager-interface WifiLinkedInfo--><!--Device-wifiManager-interface WifiLinkedInfo-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

## Modules to Import

```TypeScript
import { wifiManager } from 'wifiManager';
```

## band

```TypeScript
band: int
```

The frequency band of a Wi-Fi access point.

**Type:** int

**Since:** 23

<!--Device-WifiLinkedInfo-band: int--><!--Device-WifiLinkedInfo-band: int-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

## bssid

```TypeScript
bssid: string
```

The BSSID of the Wi-Fi hotspot

**Type:** string

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-WifiLinkedInfo-bssid: string--><!--Device-WifiLinkedInfo-bssid: string-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

## channelWidth

```TypeScript
channelWidth: WifiChannelWidth
```

Channel width of the connected hotspot.

**Type:** [WifiChannelWidth](arkts-connectivity-wifimanager-wifichannelwidth-e.md)

**Since:** 23

<!--Device-WifiLinkedInfo-channelWidth: WifiChannelWidth--><!--Device-WifiLinkedInfo-channelWidth: WifiChannelWidth-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

## connState

```TypeScript
connState: ConnState
```

The state of this Wi-Fi connection.

**Type:** ConnState

**Since:** 23

<!--Device-WifiLinkedInfo-connState: ConnState--><!--Device-WifiLinkedInfo-connState: ConnState-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

## frequency

```TypeScript
frequency: int
```

The frequency of a Wi-Fi access point.

**Type:** int

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-WifiLinkedInfo-frequency: int--><!--Device-WifiLinkedInfo-frequency: int-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

## ipAddress

```TypeScript
ipAddress: int
```

The IP address of this Wi-Fi connection.

**Type:** int

**Since:** 23

<!--Device-WifiLinkedInfo-ipAddress: int--><!--Device-WifiLinkedInfo-ipAddress: int-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

## isHiLinkNetwork

```TypeScript
isHiLinkNetwork: boolean
```

Whether the Wi-Fi hotspot is HiLink network.

**Type:** boolean

**Since:** 23

<!--Device-WifiLinkedInfo-isHiLinkNetwork: boolean--><!--Device-WifiLinkedInfo-isHiLinkNetwork: boolean-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

## isHidden

```TypeScript
isHidden: boolean
```

Whether the SSID of the access point (AP) of this Wi-Fi connection is hidden.

**Type:** boolean

**Since:** 23

<!--Device-WifiLinkedInfo-isHidden: boolean--><!--Device-WifiLinkedInfo-isHidden: boolean-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

## isRestricted

```TypeScript
isRestricted: boolean
```

Whether this Wi-Fi connection restricts the data volume.

**Type:** boolean

**Since:** 23

<!--Device-WifiLinkedInfo-isRestricted: boolean--><!--Device-WifiLinkedInfo-isRestricted: boolean-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

## linkSpeed

```TypeScript
linkSpeed: int
```

The speed of a Wi-Fi access point.

**Type:** int

**Since:** 23

<!--Device-WifiLinkedInfo-linkSpeed: int--><!--Device-WifiLinkedInfo-linkSpeed: int-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

## macAddress

```TypeScript
macAddress: string
```

The Wi-Fi MAC address of a device.

**Type:** string

**Since:** 23

<!--Device-WifiLinkedInfo-macAddress: string--><!--Device-WifiLinkedInfo-macAddress: string-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

## macType

```TypeScript
macType: int
```

Type of macAddress: 0 - real mac, 1 - random mac.

**Type:** int

**Since:** 23

<!--Device-WifiLinkedInfo-macType: int--><!--Device-WifiLinkedInfo-macType: int-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

## maxSupportedRxLinkSpeed

```TypeScript
maxSupportedRxLinkSpeed: int
```

Max rx speed of a Wi-Fi access point.

**Type:** int

**Since:** 23

<!--Device-WifiLinkedInfo-maxSupportedRxLinkSpeed: int--><!--Device-WifiLinkedInfo-maxSupportedRxLinkSpeed: int-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

## maxSupportedTxLinkSpeed

```TypeScript
maxSupportedTxLinkSpeed: int
```

Max tx speed of a Wi-Fi access point.

**Type:** int

**Since:** 23

<!--Device-WifiLinkedInfo-maxSupportedTxLinkSpeed: int--><!--Device-WifiLinkedInfo-maxSupportedTxLinkSpeed: int-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

## rssi

```TypeScript
rssi: int
```

The RSSI(dBm) of a Wi-Fi access point.

**Type:** int

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-WifiLinkedInfo-rssi: int--><!--Device-WifiLinkedInfo-rssi: int-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

## rxLinkSpeed

```TypeScript
rxLinkSpeed: int
```

The rx speed of a Wi-Fi access point.

**Type:** int

**Since:** 23

<!--Device-WifiLinkedInfo-rxLinkSpeed: int--><!--Device-WifiLinkedInfo-rxLinkSpeed: int-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

## ssid

```TypeScript
ssid: string
```

The SSID of the Wi-Fi hotspot

**Type:** string

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-WifiLinkedInfo-ssid: string--><!--Device-WifiLinkedInfo-ssid: string-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

## supportedWifiCategory

```TypeScript
supportedWifiCategory: WifiCategory
```

Supported wifi category

**Type:** [WifiCategory](arkts-connectivity-wifimanager-wificategory-e.md)

**Since:** 23

<!--Device-WifiLinkedInfo-supportedWifiCategory: WifiCategory--><!--Device-WifiLinkedInfo-supportedWifiCategory: WifiCategory-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

## wifiLinkType

```TypeScript
wifiLinkType?: WifiLinkType
```

Wi-Fi link type

**Type:** [WifiLinkType](arkts-connectivity-wifimanager-wifilinktype-e.md)

**Since:** 23

<!--Device-WifiLinkedInfo-wifiLinkType?: WifiLinkType--><!--Device-WifiLinkedInfo-wifiLinkType?: WifiLinkType-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

## wifiStandard

```TypeScript
wifiStandard: WifiStandard
```

Wifi standard of current connection.

**Type:** [WifiStandard](arkts-connectivity-wifimanager-wifistandard-e.md)

**Since:** 23

<!--Device-WifiLinkedInfo-wifiStandard: WifiStandard--><!--Device-WifiLinkedInfo-wifiStandard: WifiStandard-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

