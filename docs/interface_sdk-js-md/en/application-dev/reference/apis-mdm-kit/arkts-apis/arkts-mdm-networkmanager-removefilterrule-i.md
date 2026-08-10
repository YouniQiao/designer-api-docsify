# RemoveFilterRule

移除网络包过滤规则。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-networkManager-interface RemoveFilterRule--><!--Device-networkManager-interface RemoveFilterRule-End-->

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

**Type:** [Action](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-agent-action-e.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RemoveFilterRule-action?: Action--><!--Device-RemoveFilterRule-action?: Action-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## destAddr

```TypeScript
destAddr?: string
```

ip目标地址。

**Type:** string

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RemoveFilterRule-destAddr?: string--><!--Device-RemoveFilterRule-destAddr?: string-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## destPort

```TypeScript
destPort?: string
```

ip目标端口。

**Type:** string

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RemoveFilterRule-destPort?: string--><!--Device-RemoveFilterRule-destPort?: string-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## direction

```TypeScript
direction: Direction
```

规则链。

**Type:** [Direction](arkts-mdm-networkmanager-direction-e.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RemoveFilterRule-direction: Direction--><!--Device-RemoveFilterRule-direction: Direction-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## protocol

```TypeScript
protocol?: Protocol
```

网络协议。

**Type:** [Protocol](../../apis-network-kit/arkts-apis/arkts-network-socket-protocol-e.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RemoveFilterRule-protocol?: Protocol--><!--Device-RemoveFilterRule-protocol?: Protocol-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## srcAddr

```TypeScript
srcAddr?: string
```

ip源地址。

**Type:** string

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RemoveFilterRule-srcAddr?: string--><!--Device-RemoveFilterRule-srcAddr?: string-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## srcPort

```TypeScript
srcPort?: string
```

ip源端口。

**Type:** string

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RemoveFilterRule-srcPort?: string--><!--Device-RemoveFilterRule-srcPort?: string-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## uid

```TypeScript
uid?: string
```

应用uid。

**Type:** string

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RemoveFilterRule-uid?: string--><!--Device-RemoveFilterRule-uid?: string-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

