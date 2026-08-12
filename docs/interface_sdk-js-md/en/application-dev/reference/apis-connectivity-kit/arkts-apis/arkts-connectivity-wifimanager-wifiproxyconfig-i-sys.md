# WifiProxyConfig (System API)

Wi-Fi Proxy config.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-wifiManager-interface WifiProxyConfig--><!--Device-wifiManager-interface WifiProxyConfig-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { wifiManager } from '@kit.ConnectivityKit';
```

## exclusionObjects

```TypeScript
exclusionObjects?: string
```

Exclusion objects for manual configured proxy. objects are separated by ','.

**Type:** string

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-WifiProxyConfig-exclusionObjects?: string--><!--Device-WifiProxyConfig-exclusionObjects?: string-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

**System API:** This is a system API.

## pacWebAddress

```TypeScript
pacWebAddress?: string
```

PAC web address for auto configured proxy.

**Type:** string

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-WifiProxyConfig-pacWebAddress?: string--><!--Device-WifiProxyConfig-pacWebAddress?: string-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

**System API:** This is a system API.

## proxyMethod

```TypeScript
proxyMethod?: ProxyMethod
```

Wi-Fi proxy method

**Type:** [ProxyMethod](arkts-connectivity-wifimanager-proxymethod-e-sys.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-WifiProxyConfig-proxyMethod?: ProxyMethod--><!--Device-WifiProxyConfig-proxyMethod?: ProxyMethod-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

**System API:** This is a system API.

## serverHostName

```TypeScript
serverHostName?: string
```

Server host name for manual configured proxy.

**Type:** string

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-WifiProxyConfig-serverHostName?: string--><!--Device-WifiProxyConfig-serverHostName?: string-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

**System API:** This is a system API.

## serverPort

```TypeScript
serverPort?: int
```

Server port for manual configured proxy.

**Type:** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

<!--Device-WifiProxyConfig-serverPort?: int--><!--Device-WifiProxyConfig-serverPort?: int-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

**System API:** This is a system API.

