# WifiDeviceConfig

Wi-Fi device configuration information.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-wifiManager-interface WifiDeviceConfig--><!--Device-wifiManager-interface WifiDeviceConfig-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

## Modules to Import

```TypeScript
import { wifiManager } from '@kit.ConnectivityKit';
```

## configStatus

```TypeScript
configStatus?: int
```

Device config status: 0 - enabled, 1 - disabled, 2 - permanent disabled, 3 - unknown.

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-WifiDeviceConfig-configStatus?: int--><!--Device-WifiDeviceConfig-configStatus?: int-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

**System API:** This is a system API.

## creatorUid

```TypeScript
creatorUid?: int
```

The UID of the Wi-Fi configuration creator.

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-WifiDeviceConfig-creatorUid?: int--><!--Device-WifiDeviceConfig-creatorUid?: int-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

**System API:** This is a system API.

## disableReason

```TypeScript
disableReason?: int
```

Disable reason

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-WifiDeviceConfig-disableReason?: int--><!--Device-WifiDeviceConfig-disableReason?: int-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

**System API:** This is a system API.

## family

```TypeScript
family?: int
```

Static IP family: 0 - IPv4, 1 - Ipv6.

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-WifiDeviceConfig-family?: int--><!--Device-WifiDeviceConfig-family?: int-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

**System API:** This is a system API.

## ipType

```TypeScript
ipType?: IpType
```

IP Type

**Type:** IpType

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-WifiDeviceConfig-ipType?: IpType--><!--Device-WifiDeviceConfig-ipType?: IpType-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

**System API:** This is a system API.

## isAutoConnectAllowed

```TypeScript
isAutoConnectAllowed?: boolean
```

Allow auto connect config: false - not, true - yes.

**Type:** boolean

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-WifiDeviceConfig-isAutoConnectAllowed?: boolean--><!--Device-WifiDeviceConfig-isAutoConnectAllowed?: boolean-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

**System API:** This is a system API.

## isSecureWifi

```TypeScript
isSecureWifi?: boolean
```

Secure wifi detect config: false - not, true - yes.

**Type:** boolean

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-WifiDeviceConfig-isSecureWifi?: boolean--><!--Device-WifiDeviceConfig-isSecureWifi?: boolean-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

**System API:** This is a system API.

## proxyConfig

```TypeScript
proxyConfig?: WifiProxyConfig
```

Proxy config.

**Type:** [WifiProxyConfig](arkts-connectivity-wifimanager-wifiproxyconfig-i-sys.md)

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-WifiDeviceConfig-proxyConfig?: WifiProxyConfig--><!--Device-WifiDeviceConfig-proxyConfig?: WifiProxyConfig-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

**System API:** This is a system API.

## randomMacAddr

```TypeScript
randomMacAddr?: string
```

Random mac address, the length is 6.

**Type:** string

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-WifiDeviceConfig-randomMacAddr?: string--><!--Device-WifiDeviceConfig-randomMacAddr?: string-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

**System API:** This is a system API.

## randomMacType

```TypeScript
randomMacType?: int
```

Random mac type

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-WifiDeviceConfig-randomMacType?: int--><!--Device-WifiDeviceConfig-randomMacType?: int-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

**System API:** This is a system API.

## staticIp

```TypeScript
staticIp?: IpConfig
```

IP config of static

**Type:** IpConfig

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-WifiDeviceConfig-staticIp?: IpConfig--><!--Device-WifiDeviceConfig-staticIp?: IpConfig-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

**System API:** This is a system API.

## staticIpv6

```TypeScript
staticIpv6?: Ipv6Config
```

IPv6 config of static

**Type:** [Ipv6Config](arkts-connectivity-wifimanager-ipv6config-i-sys.md)

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-WifiDeviceConfig-staticIpv6?: Ipv6Config--><!--Device-WifiDeviceConfig-staticIpv6?: Ipv6Config-End-->

**System capability:** SystemCapability.Communication.WiFi.STA

**System API:** This is a system API.

