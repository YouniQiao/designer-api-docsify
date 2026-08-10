# WifiDeviceConfig

Wi-Fi device configuration information.

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

<!--Device-wifiManager-interface WifiDeviceConfig--><!--Device-wifiManager-interface WifiDeviceConfig-End-->

**系统能力：** SystemCapability.Communication.WiFi.STA

## 导入模块

```TypeScript
import { wifiManager } from 'kits/@kit.ConnectivityKit';
```

## configStatus

```TypeScript
configStatus?: int
```

Device config status: 0 - enabled, 1 - disabled, 2 - permanent disabled, 3 - unknown.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

<!--Device-WifiDeviceConfig-configStatus?: int--><!--Device-WifiDeviceConfig-configStatus?: int-End-->

**系统能力：** SystemCapability.Communication.WiFi.STA

**系统接口：** 此接口为系统接口。

## creatorUid

```TypeScript
creatorUid?: int
```

The UID of the Wi-Fi configuration creator.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

<!--Device-WifiDeviceConfig-creatorUid?: int--><!--Device-WifiDeviceConfig-creatorUid?: int-End-->

**系统能力：** SystemCapability.Communication.WiFi.STA

**系统接口：** 此接口为系统接口。

## disableReason

```TypeScript
disableReason?: int
```

Disable reason

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

<!--Device-WifiDeviceConfig-disableReason?: int--><!--Device-WifiDeviceConfig-disableReason?: int-End-->

**系统能力：** SystemCapability.Communication.WiFi.STA

**系统接口：** 此接口为系统接口。

## family

```TypeScript
family?: int
```

Static IP family: 0 - IPv4, 1 - Ipv6.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

<!--Device-WifiDeviceConfig-family?: int--><!--Device-WifiDeviceConfig-family?: int-End-->

**系统能力：** SystemCapability.Communication.WiFi.STA

**系统接口：** 此接口为系统接口。

## ipType

```TypeScript
ipType?: IpType
```

IP Type

**类型：** [IpType](../../apis-mdm-kit/arkts-apis/arkts-mdm-wifimanager-iptype-e.md)

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

<!--Device-WifiDeviceConfig-ipType?: IpType--><!--Device-WifiDeviceConfig-ipType?: IpType-End-->

**系统能力：** SystemCapability.Communication.WiFi.STA

**系统接口：** 此接口为系统接口。

## isAutoConnectAllowed

```TypeScript
isAutoConnectAllowed?: boolean
```

Allow auto connect config: false - not, true - yes.

**类型：** boolean

**起始版本：** 17

**ArkTS模式：** ArkTS-Dyn起始版本为17；ArkTS-Sta起始版本为23。

<!--Device-WifiDeviceConfig-isAutoConnectAllowed?: boolean--><!--Device-WifiDeviceConfig-isAutoConnectAllowed?: boolean-End-->

**系统能力：** SystemCapability.Communication.WiFi.STA

**系统接口：** 此接口为系统接口。

## isSecureWifi

```TypeScript
isSecureWifi?: boolean
```

Secure wifi detect config: false - not, true - yes.

**类型：** boolean

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

<!--Device-WifiDeviceConfig-isSecureWifi?: boolean--><!--Device-WifiDeviceConfig-isSecureWifi?: boolean-End-->

**系统能力：** SystemCapability.Communication.WiFi.STA

**系统接口：** 此接口为系统接口。

## proxyConfig

```TypeScript
proxyConfig?: WifiProxyConfig
```

Proxy config.

**类型：** [WifiProxyConfig](arkts-connectivity-wifimanager-wifiproxyconfig-i-sys.md)

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

<!--Device-WifiDeviceConfig-proxyConfig?: WifiProxyConfig--><!--Device-WifiDeviceConfig-proxyConfig?: WifiProxyConfig-End-->

**系统能力：** SystemCapability.Communication.WiFi.STA

**系统接口：** 此接口为系统接口。

## randomMacAddr

```TypeScript
randomMacAddr?: string
```

Random mac address, the length is 6.

**类型：** string

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

<!--Device-WifiDeviceConfig-randomMacAddr?: string--><!--Device-WifiDeviceConfig-randomMacAddr?: string-End-->

**系统能力：** SystemCapability.Communication.WiFi.STA

**系统接口：** 此接口为系统接口。

## randomMacType

```TypeScript
randomMacType?: int
```

Random mac type

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

<!--Device-WifiDeviceConfig-randomMacType?: int--><!--Device-WifiDeviceConfig-randomMacType?: int-End-->

**系统能力：** SystemCapability.Communication.WiFi.STA

**系统接口：** 此接口为系统接口。

## staticIp

```TypeScript
staticIp?: IpConfig
```

IP config of static

**类型：** [IpConfig](arkts-connectivity-wifi-ipconfig-i-sys.md)

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

<!--Device-WifiDeviceConfig-staticIp?: IpConfig--><!--Device-WifiDeviceConfig-staticIp?: IpConfig-End-->

**系统能力：** SystemCapability.Communication.WiFi.STA

**系统接口：** 此接口为系统接口。

## staticIpv6

```TypeScript
staticIpv6?: Ipv6Config
```

IPv6 config of static

**类型：** [Ipv6Config](arkts-connectivity-wifimanager-ipv6config-i-sys.md)

**起始版本：** 20

**ArkTS模式：** ArkTS-Dyn起始版本为20；ArkTS-Sta起始版本为23。

<!--Device-WifiDeviceConfig-staticIpv6?: Ipv6Config--><!--Device-WifiDeviceConfig-staticIpv6?: Ipv6Config-End-->

**系统能力：** SystemCapability.Communication.WiFi.STA

**系统接口：** 此接口为系统接口。

