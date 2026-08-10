# InterfaceConfiguration（系统接口）

Defines the network configuration for the Ethernet connection.

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为9。

<!--Device-ethernet-export interface InterfaceConfiguration--><!--Device-ethernet-export interface InterfaceConfiguration-End-->

**系统能力：** SystemCapability.Communication.NetManager.Ethernet

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { ethernet } from 'kits/@kit.NetworkKit';
```

## dnsServers

```TypeScript
dnsServers: string
```

The Ethernet connection is configured with the dns service address.The address value range is 0-255.0-255.0-255.0-255.0-255(DHCP mode does not need to be configured, Multiple addresses are separated by ",")

**类型：** string

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为9。

<!--Device-InterfaceConfiguration-dnsServers: string--><!--Device-InterfaceConfiguration-dnsServers: string-End-->

**系统能力：** SystemCapability.Communication.NetManager.Ethernet

**系统接口：** 此接口为系统接口。

## gateway

```TypeScript
gateway: string
```

Ethernet connection static configuration gateway information.The address value range is 0-255.0-255.0-255.0-255.0-255(DHCP mode does not need to be configured)

**类型：** string

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为9。

<!--Device-InterfaceConfiguration-gateway: string--><!--Device-InterfaceConfiguration-gateway: string-End-->

**系统能力：** SystemCapability.Communication.NetManager.Ethernet

**系统接口：** 此接口为系统接口。

## httpProxy

```TypeScript
httpProxy?: HttpProxy
```

Indicates the HttpProxy settings, no proxy is to be used as default.

**类型：** [HttpProxy](arkts-network-ethernet-httpproxy-t.md)

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为10。

<!--Device-InterfaceConfiguration-httpProxy?: HttpProxy--><!--Device-InterfaceConfiguration-httpProxy?: HttpProxy-End-->

**系统能力：** SystemCapability.Communication.NetManager.Ethernet

**系统接口：** 此接口为系统接口。

## ipAddr

```TypeScript
ipAddr: string
```

Ethernet connection static configuration IP information.The address value range is 0-255.0-255.0-255.0-255.0-255(DHCP mode does not need to be configured)

**类型：** string

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为9。

<!--Device-InterfaceConfiguration-ipAddr: string--><!--Device-InterfaceConfiguration-ipAddr: string-End-->

**系统能力：** SystemCapability.Communication.NetManager.Ethernet

**系统接口：** 此接口为系统接口。

## mode

```TypeScript
mode: IPSetMode
```

**类型：** [IPSetMode](arkts-network-ethernet-ipsetmode-e-sys.md)

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为9。

<!--Device-InterfaceConfiguration-mode: IPSetMode--><!--Device-InterfaceConfiguration-mode: IPSetMode-End-->

**系统能力：** SystemCapability.Communication.NetManager.Ethernet

**系统接口：** 此接口为系统接口。

## netMask

```TypeScript
netMask: string
```

Ethernet connection static configuration netMask information.The address value range is 0-255.0-255.0-255.0-255.0-255(DHCP mode does not need to be configured)

**类型：** string

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为9。

<!--Device-InterfaceConfiguration-netMask: string--><!--Device-InterfaceConfiguration-netMask: string-End-->

**系统能力：** SystemCapability.Communication.NetManager.Ethernet

**系统接口：** 此接口为系统接口。

## route

```TypeScript
route: string
```

Ethernet connection static configuration route information.The address value range is 0-255.0-255.0-255.0-255.0-255(DHCP mode does not need to be configured)

**类型：** string

**起始版本：** 9

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为9。

<!--Device-InterfaceConfiguration-route: string--><!--Device-InterfaceConfiguration-route: string-End-->

**系统能力：** SystemCapability.Communication.NetManager.Ethernet

**系统接口：** 此接口为系统接口。

