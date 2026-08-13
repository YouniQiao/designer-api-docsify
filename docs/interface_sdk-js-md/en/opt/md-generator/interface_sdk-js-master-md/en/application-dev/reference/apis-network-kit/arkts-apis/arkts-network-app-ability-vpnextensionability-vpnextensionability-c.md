# VpnExtensionAbility

class of vpn extension ability.

**Since:** 11

**Deprecated since:** -1

<!--Device-unnamed-export default class VpnExtensionAbility--><!--Device-unnamed-export default class VpnExtensionAbility-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## Modules to Import

```TypeScript
import { VpnExtensionContext } from '@kit.NetworkKit';
```

## onCreate

```TypeScript
onCreate(want: Want): void
```

Called back when a vpn extension is started for initialization.

**Since:** 11

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-VpnExtensionAbility-onCreate(want: Want): void--><!--Device-VpnExtensionAbility-onCreate(want: Want): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| want | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |

## Examples

```TypeScript
import { VpnExtensionAbility } from '@kit.NetworkKit';
import { Want } from '@kit.AbilityKit';

class MyVpnExtAbility extends VpnExtensionAbility {
    onCreate(want: Want) {
       console.info('MyVpnExtAbility onCreate');
    }
}
```

## onDestroy

```TypeScript
onDestroy(): void
```

Called back before a vpn extension is destroyed.

**Since:** 11

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-VpnExtensionAbility-onDestroy(): void--><!--Device-VpnExtensionAbility-onDestroy(): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## Examples

```TypeScript
import { VpnExtensionAbility } from '@kit.NetworkKit';

class MyVpnExtAbility extends VpnExtensionAbility {
    onDestroy() {
       console.info('MyVpnExtAbility onDestroy');
    }
}
```

## context

```TypeScript
context: VpnExtensionContext
```

Indicates service extension ability context.

**Type:** [VpnExtensionContext](arkts-network-vpnextensioncontext-c.md)

**Since:** 11

**Deprecated since:** -1

**Model restriction:** This API can be used only in the stage model.

<!--Device-VpnExtensionAbility-context: VpnExtensionContext--><!--Device-VpnExtensionAbility-context: VpnExtensionContext-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core
