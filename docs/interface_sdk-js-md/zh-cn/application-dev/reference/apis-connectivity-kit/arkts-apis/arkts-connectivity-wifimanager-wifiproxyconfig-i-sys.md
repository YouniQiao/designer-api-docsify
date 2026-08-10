# WifiProxyConfig（系统接口）

Wi-Fi Proxy config.

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

<!--Device-wifiManager-interface WifiProxyConfig--><!--Device-wifiManager-interface WifiProxyConfig-End-->

**系统能力：** SystemCapability.Communication.WiFi.STA

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { wifiManager } from 'kits/@kit.ConnectivityKit';
```

## exclusionObjects

```TypeScript
exclusionObjects?: string
```

Exclusion objects for manual configured proxy. objects are separated by ','.

**类型：** string

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

<!--Device-WifiProxyConfig-exclusionObjects?: string--><!--Device-WifiProxyConfig-exclusionObjects?: string-End-->

**系统能力：** SystemCapability.Communication.WiFi.STA

**系统接口：** 此接口为系统接口。

## pacWebAddress

```TypeScript
pacWebAddress?: string
```

PAC web address for auto configured proxy.

**类型：** string

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

<!--Device-WifiProxyConfig-pacWebAddress?: string--><!--Device-WifiProxyConfig-pacWebAddress?: string-End-->

**系统能力：** SystemCapability.Communication.WiFi.STA

**系统接口：** 此接口为系统接口。

## proxyMethod

```TypeScript
proxyMethod?: ProxyMethod
```

Wi-Fi proxy method

**类型：** [ProxyMethod](arkts-connectivity-wifimanager-proxymethod-e-sys.md)

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

<!--Device-WifiProxyConfig-proxyMethod?: ProxyMethod--><!--Device-WifiProxyConfig-proxyMethod?: ProxyMethod-End-->

**系统能力：** SystemCapability.Communication.WiFi.STA

**系统接口：** 此接口为系统接口。

## serverHostName

```TypeScript
serverHostName?: string
```

Server host name for manual configured proxy.

**类型：** string

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

<!--Device-WifiProxyConfig-serverHostName?: string--><!--Device-WifiProxyConfig-serverHostName?: string-End-->

**系统能力：** SystemCapability.Communication.WiFi.STA

**系统接口：** 此接口为系统接口。

## serverPort

```TypeScript
serverPort?: int
```

Server port for manual configured proxy.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

<!--Device-WifiProxyConfig-serverPort?: int--><!--Device-WifiProxyConfig-serverPort?: int-End-->

**系统能力：** SystemCapability.Communication.WiFi.STA

**系统接口：** 此接口为系统接口。

