# AddFilterRule

Defines the network packet filtering rule to add.

**Since:** 10

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

Action to take, that is, receive or discard the data packets.

**Type:** [Action](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-agent-action-e.md)

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

<!--Device-AddFilterRule-action: Action--><!--Device-AddFilterRule-action: Action-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## destAddr

```TypeScript
destAddr?: string
```

Destination IP address.

**Type:** string

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

<!--Device-AddFilterRule-destAddr?: string--><!--Device-AddFilterRule-destAddr?: string-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## destPort

```TypeScript
destPort?: string
```

Port of the destination IP address.

**Type:** string

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

<!--Device-AddFilterRule-destPort?: string--><!--Device-AddFilterRule-destPort?: string-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## direction

```TypeScript
direction: Direction
```

Direction chains to which the rule applies.

**Type:** [Direction](../../apis-ime-kit/arkts-apis/arkts-ime-inputmethod-direction-e.md)

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

<!--Device-AddFilterRule-direction: Direction--><!--Device-AddFilterRule-direction: Direction-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## method

```TypeScript
method: AddMethod
```

Method used to add the data packets.

**Type:** [AddMethod](arkts-mdm-networkmanager-addmethod-e.md)

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

<!--Device-AddFilterRule-method: AddMethod--><!--Device-AddFilterRule-method: AddMethod-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## protocol

```TypeScript
protocol?: Protocol
```

Network protocol.

**Type:** [Protocol](arkts-mdm-networkmanager-protocol-e.md)

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

<!--Device-AddFilterRule-protocol?: Protocol--><!--Device-AddFilterRule-protocol?: Protocol-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## ruleNo

```TypeScript
ruleNo?: number
```

Sequence number of the rule.

**Type:** number

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

<!--Device-AddFilterRule-ruleNo?: number--><!--Device-AddFilterRule-ruleNo?: number-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## srcAddr

```TypeScript
srcAddr?: string
```

Source IP address.

**Type:** string

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

<!--Device-AddFilterRule-srcAddr?: string--><!--Device-AddFilterRule-srcAddr?: string-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## srcPort

```TypeScript
srcPort?: string
```

Port of the source IP address.

**Type:** string

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

<!--Device-AddFilterRule-srcPort?: string--><!--Device-AddFilterRule-srcPort?: string-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## uid

```TypeScript
uid?: string
```

UID of the application.

**Type:** string

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

<!--Device-AddFilterRule-uid?: string--><!--Device-AddFilterRule-uid?: string-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager
