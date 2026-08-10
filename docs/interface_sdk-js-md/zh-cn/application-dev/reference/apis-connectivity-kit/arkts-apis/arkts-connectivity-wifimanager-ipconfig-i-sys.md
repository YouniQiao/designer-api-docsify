# IpConfig（系统接口）

Wi-Fi IP configuration information.

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

<!--Device-wifiManager-interface IpConfig--><!--Device-wifiManager-interface IpConfig-End-->

**系统能力：** SystemCapability.Communication.WiFi.STA

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { wifiManager } from 'kits/@kit.ConnectivityKit';
```

## dnsServers

```TypeScript
dnsServers: int[]
```

DNS servers.

**类型：** ArkTS-Dyn: number[]  <br>ArkTS-Sta：int[]

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

<!--Device-IpConfig-dnsServers: int[]--><!--Device-IpConfig-dnsServers: int[]-End-->

**系统能力：** SystemCapability.Communication.WiFi.STA

**系统接口：** 此接口为系统接口。

## domains

```TypeScript
domains: Array<string>
```

Domains.

**类型：** Array&lt;string&gt;

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

<!--Device-IpConfig-domains: Array<string>--><!--Device-IpConfig-domains: Array<string>-End-->

**系统能力：** SystemCapability.Communication.WiFi.STA

**系统接口：** 此接口为系统接口。

## gateway

```TypeScript
gateway: int
```

Gate way.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

<!--Device-IpConfig-gateway: int--><!--Device-IpConfig-gateway: int-End-->

**系统能力：** SystemCapability.Communication.WiFi.STA

**系统接口：** 此接口为系统接口。

## ipAddress

```TypeScript
ipAddress: int
```

IP address.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

<!--Device-IpConfig-ipAddress: int--><!--Device-IpConfig-ipAddress: int-End-->

**系统能力：** SystemCapability.Communication.WiFi.STA

**系统接口：** 此接口为系统接口。

## prefixLength

```TypeScript
prefixLength: int
```

Prefix length.

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 9

**ArkTS模式：** ArkTS-Dyn起始版本为9；ArkTS-Sta起始版本为23。

<!--Device-IpConfig-prefixLength: int--><!--Device-IpConfig-prefixLength: int-End-->

**系统能力：** SystemCapability.Communication.WiFi.STA

**系统接口：** 此接口为系统接口。

