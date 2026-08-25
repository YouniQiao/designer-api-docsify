# PartnerAgentExtensionAbility

Class for the PartnerAgentExtensionAbility. Applications can use this ability to discover devices.@extends ExtensionAbility

**Inheritance/Implementation:** PartnerAgentExtensionAbility extends ExtensionAbility

**Since:** 23

**System capability:** SystemCapability.Communication.FusionConnectivity.Core

## Modules to Import

```TypeScript
import { PartnerAgentExtensionAbility } from 'kits/@kit.ConnectivityKit';
```

## onDestroyWithReason

```TypeScript
onDestroyWithReason(reason: PartnerAgentExtensionAbilityDestroyReason): void
```

Called when the PartnerAgentExtensionAbility is to be destroyed. Applications can clean up resources in this callback function.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Communication.FusionConnectivity.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| reason | [PartnerAgentExtensionAbilityDestroyReason](arkts-connectivity-partneragentextensionabilitydestroyreason-t.md) | Yes |

## onDeviceDiscovered

```TypeScript
onDeviceDiscovered(deviceAddress: PartnerDeviceAddress): void
```

Called when a device is discovered.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Communication.FusionConnectivity.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| deviceAddress | [PartnerDeviceAddress](arkts-connectivity-partnerdeviceaddress-t.md) | Yes |

## context

```TypeScript
context: PartnerAgentExtensionContext
```

Context of the PartnerAgentExtensionAbility.

**Type:** [PartnerAgentExtensionContext](arkts-connectivity-fusionconnectivity-partneragentextensioncontext-partneragentextensioncontext-c.md)

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Communication.FusionConnectivity.Core
