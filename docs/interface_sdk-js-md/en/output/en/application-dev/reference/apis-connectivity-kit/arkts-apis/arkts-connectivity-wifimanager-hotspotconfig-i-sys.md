# HotspotConfig (System API)

Wi-Fi hotspot configuration information.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-wifiManager-interface HotspotConfig--><!--Device-wifiManager-interface HotspotConfig-End-->

**System capability:** SystemCapability.Communication.WiFi.AP.Core

**System API:** This is a system API.

## band

```TypeScript
band: int
```

The frequency band of the Wi-Fi hotspot

**Type:** int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-HotspotConfig-band: int--><!--Device-HotspotConfig-band: int-End-->

**System capability:** SystemCapability.Communication.WiFi.AP.Core

**System API:** This is a system API.

## channel

```TypeScript
channel?: int
```

The channel of the Wi-Fi hotspot.

**Type:** int

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-HotspotConfig-channel?: int--><!--Device-HotspotConfig-channel?: int-End-->

**System capability:** SystemCapability.Communication.WiFi.AP.Core

**System API:** This is a system API.

## ipAddress

```TypeScript
ipAddress?: string
```

IP address of the dhcp server, it's a string, For example 192.168.43.1

**Type:** string

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-HotspotConfig-ipAddress?: string--><!--Device-HotspotConfig-ipAddress?: string-End-->

**System capability:** SystemCapability.Communication.WiFi.AP.Core

**System API:** This is a system API.

## maxConn

```TypeScript
maxConn: int
```

The maximum number of connections allowed by the Wi-Fi hotspot

**Type:** int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-HotspotConfig-maxConn: int--><!--Device-HotspotConfig-maxConn: int-End-->

**System capability:** SystemCapability.Communication.WiFi.AP.Core

**System API:** This is a system API.

## preSharedKey

```TypeScript
preSharedKey: string
```

The password of the Wi-Fi hotspot

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-HotspotConfig-preSharedKey: string--><!--Device-HotspotConfig-preSharedKey: string-End-->

**System capability:** SystemCapability.Communication.WiFi.AP.Core

**System API:** This is a system API.

## securityType

```TypeScript
securityType: WifiSecurityType
```

The encryption mode of the Wi-Fi hotspot

**Type:** WifiSecurityType

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-HotspotConfig-securityType: WifiSecurityType--><!--Device-HotspotConfig-securityType: WifiSecurityType-End-->

**System capability:** SystemCapability.Communication.WiFi.AP.Core

**System API:** This is a system API.

## ssid

```TypeScript
ssid: string
```

The SSID of the Wi-Fi hotspot

**Type:** string

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

<!--Device-HotspotConfig-ssid: string--><!--Device-HotspotConfig-ssid: string-End-->

**System capability:** SystemCapability.Communication.WiFi.AP.Core

**System API:** This is a system API.

