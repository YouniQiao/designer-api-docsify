# WifiDeviceConfig

Wi-Fi device configuration information.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** WifiDeviceConfig

<!--Device-wifi-interface WifiDeviceConfig--><!--Device-wifi-interface WifiDeviceConfig-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

## Modules to Import

```TypeScript
import { wifi } from '@kit.ConnectivityKit';
```

## bssid

```TypeScript
bssid: string
```

Wi-Fi bssid(MAC): the length is 6

**Type:** string

**Since:** 6

**Deprecated since:** 9

**Substitutes:** bssid

<!--Device-WifiDeviceConfig-bssid: string--><!--Device-WifiDeviceConfig-bssid: string-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

## isHiddenSsid

```TypeScript
isHiddenSsid: boolean
```

Hide SSID or not, false(default): not hide

**Type:** boolean

**Since:** 6

**Deprecated since:** 9

**Substitutes:** isHiddenSsid

<!--Device-WifiDeviceConfig-isHiddenSsid: boolean--><!--Device-WifiDeviceConfig-isHiddenSsid: boolean-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

## preSharedKey

```TypeScript
preSharedKey: string
```

Wi-Fi key: maximum length is 64

**Type:** string

**Since:** 6

**Deprecated since:** 9

**Substitutes:** preSharedKey

<!--Device-WifiDeviceConfig-preSharedKey: string--><!--Device-WifiDeviceConfig-preSharedKey: string-End-->

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

<!--Device-WifiDeviceConfig-securityType: WifiSecurityType--><!--Device-WifiDeviceConfig-securityType: WifiSecurityType-End-->

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

<!--Device-WifiDeviceConfig-ssid: string--><!--Device-WifiDeviceConfig-ssid: string-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

