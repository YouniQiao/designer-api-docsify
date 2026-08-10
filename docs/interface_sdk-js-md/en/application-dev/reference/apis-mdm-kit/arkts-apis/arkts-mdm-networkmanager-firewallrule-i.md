# FirewallRule

防火墙过滤规则。

API version 21及之前版本，仅支持IPv4。从API version 22开始，支持IPv4和IPv6。

从API version 23开始，支持[LogType](arkts-mdm-networkmanager-logtype-e.md)。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

<!--Device-networkManager-interface FirewallRule--><!--Device-networkManager-interface FirewallRule-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## Modules to Import

```TypeScript
import { networkManager } from 'kits/@kit.MDMKit';
```

## action

```TypeScript
action?: Action
```

接收或者丢弃数据包。

添加防火墙过滤规则时必填；

移除防火墙时非必填，当值为空时，表示清空所有的匹配[Action](arkts-mdm-networkmanager-action-e.md)规则的链，且srcAddr，destAddr，srcPort，destPort，appUid也必须传入空值。

**Type:** [Action](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-agent-action-e.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FirewallRule-action?: Action--><!--Device-FirewallRule-action?: Action-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## appUid

```TypeScript
appUid?: string
```

应用uid。

**Type:** string

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FirewallRule-appUid?: string--><!--Device-FirewallRule-appUid?: string-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## destAddr

```TypeScript
destAddr?: string
```

ip目标地址。支持IP段，例如：192.168.0.0/22或者192.168.1.100-192.168.1.200

**Type:** string

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FirewallRule-destAddr?: string--><!--Device-FirewallRule-destAddr?: string-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## destPort

```TypeScript
destPort?: string
```

目标端口。

**Type:** string

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FirewallRule-destPort?: string--><!--Device-FirewallRule-destPort?: string-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## direction

```TypeScript
direction?: Direction
```

规则链。

添加防火墙过滤规则时必填；

移除防火墙时非必填，当值为空时，表示清空所有的[Direction](arkts-mdm-networkmanager-direction-e.md)链，且srcAddr，destAddr，srcPort，destPort，appUid也必须传入空值。

**Type:** [Direction](arkts-mdm-networkmanager-direction-e.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FirewallRule-direction?: Direction--><!--Device-FirewallRule-direction?: Direction-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## family

```TypeScript
family?: number
```

IP协议版本。支持取值为1或2，取值为1表示IPv4，取值为2表示IPv6。

**Type:** number

**Since:** 22

**ArkTS mode:** ArkTS-Dyn only, since version 22.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FirewallRule-family?: number--><!--Device-FirewallRule-family?: number-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## logType

```TypeScript
logType?: LogType
```

日志类型，当前仅支持配置NFLOG类型，该参数仅支持PC/2in1设备。

添加防火墙过滤规则时，此参数非必填。若填写，仅在丢弃或拒绝数据包时生效。

移除防火墙过滤规则时，当清空某条链时非必填，不影响整条链的清空；当移除单条规则时，是否填写必须与该规则一致，否则可能导致过滤规则已经移除，但是日志还在记录的问题；相同过滤规则移除时必须按添加时的顺序移除。

获取防火墙过滤规则时，仅日志生效的场景可以获取到logType字段。

**Type:** [LogType](arkts-mdm-networkmanager-logtype-e.md)

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FirewallRule-logType?: LogType--><!--Device-FirewallRule-logType?: LogType-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## protocol

```TypeScript
protocol?: Protocol
```

网络协议。当值为ALL或者ICMP时，设置srcPort与destPort无效。

**Type:** [Protocol](../../apis-network-kit/arkts-apis/arkts-network-socket-protocol-e.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FirewallRule-protocol?: Protocol--><!--Device-FirewallRule-protocol?: Protocol-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## srcAddr

```TypeScript
srcAddr?: string
```

ip源地址。支持IP段，例如：192.168.0.0/22或者192.168.1.100-192.168.1.200

**Type:** string

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FirewallRule-srcAddr?: string--><!--Device-FirewallRule-srcAddr?: string-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## srcPort

```TypeScript
srcPort?: string
```

源端口。

**Type:** string

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Model restriction:** This API can be used only in the stage model.

<!--Device-FirewallRule-srcPort?: string--><!--Device-FirewallRule-srcPort?: string-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

