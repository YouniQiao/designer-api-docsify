# HotspotConfig (System API)

Wi-Fi hotspot configuration information.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Communication.WiFi.AP.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { wifiManager } from '@kit.ConnectivityKit';
```

## band

```TypeScript
band: int
```

The frequency band of the Wi-Fi hotspot

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**System capability:** SystemCapability.Communication.WiFi.AP.Core

**System API:** This is a system API.

## channel

```TypeScript
channel?: int
```

The channel of the Wi-Fi hotspot.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

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

**System capability:** SystemCapability.Communication.WiFi.AP.Core

**System API:** This is a system API.

## maxConn

```TypeScript
maxConn: int
```

The maximum number of connections allowed by the Wi-Fi hotspot

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

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

**System capability:** SystemCapability.Communication.WiFi.AP.Core

**System API:** This is a system API.
