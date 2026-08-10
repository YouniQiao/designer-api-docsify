# LocalServiceInfo

Defines the mDNS service information.

**起始版本：** 11

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为11。

<!--Device-mdns-export interface LocalServiceInfo--><!--Device-mdns-export interface LocalServiceInfo-End-->

**系统能力：** SystemCapability.Communication.NetManager.MDNS

## 导入模块

```TypeScript
import { mdns } from 'kits/@kit.NetworkKit';
```

## host

```TypeScript
host?: NetAddress
```

IP address of the host.

**类型：** [NetAddress](arkts-network-connection-netaddress-i.md)

**起始版本：** 11

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为11。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-LocalServiceInfo-host?: NetAddress--><!--Device-LocalServiceInfo-host?: NetAddress-End-->

**系统能力：** SystemCapability.Communication.NetManager.MDNS

## port

```TypeScript
port?: number
```

Port number.

**类型：** number

**起始版本：** 11

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为11。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-LocalServiceInfo-port?: number--><!--Device-LocalServiceInfo-port?: number-End-->

**系统能力：** SystemCapability.Communication.NetManager.MDNS

## serviceAttribute

```TypeScript
serviceAttribute?: Array<ServiceAttribute>
```

DNS-SD TXT record pairs.

**类型：** Array&lt;ServiceAttribute&gt;

**起始版本：** 11

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为11。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-LocalServiceInfo-serviceAttribute?: Array<ServiceAttribute>--><!--Device-LocalServiceInfo-serviceAttribute?: Array<ServiceAttribute>-End-->

**系统能力：** SystemCapability.Communication.NetManager.MDNS

## serviceName

```TypeScript
serviceName: string
```

Service name.

**类型：** string

**起始版本：** 11

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为11。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-LocalServiceInfo-serviceName: string--><!--Device-LocalServiceInfo-serviceName: string-End-->

**系统能力：** SystemCapability.Communication.NetManager.MDNS

## serviceType

```TypeScript
serviceType: string
```

Service type. Use an underscore (_) as the prefix, for example, _http._tcp.

**类型：** string

**起始版本：** 11

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为11。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-LocalServiceInfo-serviceType: string--><!--Device-LocalServiceInfo-serviceType: string-End-->

**系统能力：** SystemCapability.Communication.NetManager.MDNS

