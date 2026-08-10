# PartnerAgentExtensionAbility

Class for the PartnerAgentExtensionAbility.Applications can use this ability to discover devices.

**继承/实现关系：** PartnerAgentExtensionAbility extends [ExtensionAbility](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-extensionability-extensionability-c.md/arkts-ability-app-ability-extensionability-extensionability-c.md)

**起始版本：** 23

**ArkTS模式：** ArkTS-Dyn起始版本为23；ArkTS-Sta起始版本为26.0.0。

<!--Device-unnamed-export default class PartnerAgentExtensionAbility extends ExtensionAbility--><!--Device-unnamed-export default class PartnerAgentExtensionAbility extends ExtensionAbility-End-->

**系统能力：** SystemCapability.Communication.FusionConnectivity.Core

## 导入模块

```TypeScript
import { PartnerAgentExtensionAbility } from 'kits/@kit.ConnectivityKit';
```

## onDestroyWithReason

```TypeScript
onDestroyWithReason(reason: PartnerAgentExtensionAbilityDestroyReason): void
```

Called when the PartnerAgentExtensionAbility is to be destroyed.Applications can clean up resources in this callback function.

**起始版本：** 23

**ArkTS模式：** ArkTS-Dyn起始版本为23；ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PartnerAgentExtensionAbility-onDestroyWithReason(reason: PartnerAgentExtensionAbilityDestroyReason): void--><!--Device-PartnerAgentExtensionAbility-onDestroyWithReason(reason: PartnerAgentExtensionAbilityDestroyReason): void-End-->

**系统能力：** SystemCapability.Communication.FusionConnectivity.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| reason | [PartnerAgentExtensionAbilityDestroyReason](arkts-connectivity-partneragentextensionabilitydestroyreason-t.md) | 是 | The reason for Ability destruction. |

## 示例

```TypeScript
export default class PartnerAgentExtAbility extends PartnerAgentExtensionAbility {
  onDestroyWithReason(reason: partnerAgent.PartnerAgentExtensionAbilityDestroyReason): void {
    console.info(`onDestroyWithReason is: ${reason}`);
  }
}
```

## onDeviceDiscovered

```TypeScript
onDeviceDiscovered(deviceAddress: PartnerDeviceAddress): void
```

Called when a device is discovered.

**起始版本：** 23

**ArkTS模式：** ArkTS-Dyn起始版本为23；ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PartnerAgentExtensionAbility-onDeviceDiscovered(deviceAddress: PartnerDeviceAddress): void--><!--Device-PartnerAgentExtensionAbility-onDeviceDiscovered(deviceAddress: PartnerDeviceAddress): void-End-->

**系统能力：** SystemCapability.Communication.FusionConnectivity.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| deviceAddress | [PartnerDeviceAddress](arkts-connectivity-partnerdeviceaddress-t.md) | 是 | Address of the discovered device. |

## 示例

```TypeScript
export default class PartnerAgentExtAbility extends PartnerAgentExtensionAbility {
  onDeviceDiscovered(deviceAddress: partnerAgent.PartnerDeviceAddress): void {
    console.info(`onDeviceDiscovered success: ${deviceAddress.bluetoothAddress}`);
  }
}
```

## context

```TypeScript
context: PartnerAgentExtensionContext
```

Context of the PartnerAgentExtensionAbility.

**类型：** [PartnerAgentExtensionContext](arkts-connectivity-fusionconnectivity-partneragentextensioncontext-partneragentextensioncontext-c.md)

**起始版本：** 23

**ArkTS模式：** ArkTS-Dyn起始版本为23；ArkTS-Sta起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PartnerAgentExtensionAbility-context: PartnerAgentExtensionContext--><!--Device-PartnerAgentExtensionAbility-context: PartnerAgentExtensionContext-End-->

**系统能力：** SystemCapability.Communication.FusionConnectivity.Core

