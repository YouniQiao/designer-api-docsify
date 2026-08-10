# NetFirewallIpParams

Firewall IP parameters.

**起始版本：** 15

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为15。

<!--Device-netFirewall-interface NetFirewallIpParams--><!--Device-netFirewall-interface NetFirewallIpParams-End-->

**系统能力：** SystemCapability.Communication.NetManager.NetFirewall

## 导入模块

```TypeScript
import { netFirewall } from 'kits/@kit.NetworkKit';
```

## address

```TypeScript
address?: string
```

IP address: Valid when type equals 1, otherwise it will be ignored.

**类型：** string

**起始版本：** 15

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为15。

<!--Device-NetFirewallIpParams-address?: string--><!--Device-NetFirewallIpParams-address?: string-End-->

**系统能力：** SystemCapability.Communication.NetManager.NetFirewall

## endIp

```TypeScript
endIp?: string
```

End IP: valid when type equals 2, otherwise it will be ignored.

**类型：** string

**起始版本：** 15

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为15。

<!--Device-NetFirewallIpParams-endIp?: string--><!--Device-NetFirewallIpParams-endIp?: string-End-->

**系统能力：** SystemCapability.Communication.NetManager.NetFirewall

## family

```TypeScript
family?: number
```

1: IPv4, 2: IPv6, default is IPv4.

**类型：** number

**起始版本：** 15

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为15。

<!--Device-NetFirewallIpParams-family?: number--><!--Device-NetFirewallIpParams-family?: number-End-->

**系统能力：** SystemCapability.Communication.NetManager.NetFirewall

## mask

```TypeScript
mask?: number
```

IPv4: subnet mask, IPv6: prefix, valid when type equals 1, otherwise it will be ignored.

**类型：** number

**起始版本：** 15

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为15。

<!--Device-NetFirewallIpParams-mask?: number--><!--Device-NetFirewallIpParams-mask?: number-End-->

**系统能力：** SystemCapability.Communication.NetManager.NetFirewall

## startIp

```TypeScript
startIp?: string
```

Start IP: valid when type equals 2, otherwise it will be ignored.

**类型：** string

**起始版本：** 15

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为15。

<!--Device-NetFirewallIpParams-startIp?: string--><!--Device-NetFirewallIpParams-startIp?: string-End-->

**系统能力：** SystemCapability.Communication.NetManager.NetFirewall

## type

```TypeScript
type: number
```

1: IP address or subnet, when using a single IP, the mask is 32; 2: IP segment.

**类型：** number

**起始版本：** 15

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为15。

<!--Device-NetFirewallIpParams-type: number--><!--Device-NetFirewallIpParams-type: number-End-->

**系统能力：** SystemCapability.Communication.NetManager.NetFirewall

