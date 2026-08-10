# AddFilterRule

添加网络包过滤规则。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

<!--Device-networkManager-interface AddFilterRule--><!--Device-networkManager-interface AddFilterRule-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## Modules to Import

```TypeScript
import { networkManager } from 'kits/@kit.MDMKit';
```

## action

```TypeScript
action: Action
```

接收或者丢弃数据包。

**Type:** [Action](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-agent-action-e.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AddFilterRule-action: Action--><!--Device-AddFilterRule-action: Action-End-->

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

<!--Device-AddFilterRule-destAddr?: string--><!--Device-AddFilterRule-destAddr?: string-End-->

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

<!--Device-AddFilterRule-destPort?: string--><!--Device-AddFilterRule-destPort?: string-End-->

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

<!--Device-AddFilterRule-direction: Direction--><!--Device-AddFilterRule-direction: Direction-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## method

```TypeScript
method: AddMethod
```

添加策略。

**Type:** [AddMethod](arkts-mdm-networkmanager-addmethod-e.md)

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AddFilterRule-method: AddMethod--><!--Device-AddFilterRule-method: AddMethod-End-->

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

<!--Device-AddFilterRule-protocol?: Protocol--><!--Device-AddFilterRule-protocol?: Protocol-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## ruleNo

```TypeScript
ruleNo?: number
```

规则序号。

**Type:** number

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Model restriction:** This API can be used only in the stage model.

<!--Device-AddFilterRule-ruleNo?: number--><!--Device-AddFilterRule-ruleNo?: number-End-->

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

<!--Device-AddFilterRule-srcAddr?: string--><!--Device-AddFilterRule-srcAddr?: string-End-->

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

<!--Device-AddFilterRule-srcPort?: string--><!--Device-AddFilterRule-srcPort?: string-End-->

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

<!--Device-AddFilterRule-uid?: string--><!--Device-AddFilterRule-uid?: string-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

