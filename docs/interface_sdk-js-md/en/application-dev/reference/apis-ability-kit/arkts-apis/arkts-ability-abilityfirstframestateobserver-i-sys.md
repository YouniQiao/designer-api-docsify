# AbilityFirstFrameStateObserver (System API)

The module defines the observer used to listen for the first frame rendering completion event of a given ability. It is used as an input parameter of [on](arkts-ability-appmanager-onapplicationstate-f.md#on_applicationState) to listen for the completion event.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-export interface AbilityFirstFrameStateObserver--><!--Device-unnamed-export interface AbilityFirstFrameStateObserver-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## onAbilityFirstFrameDrawn

```TypeScript
onAbilityFirstFrameDrawn(data: AbilityFirstFrameStateData): void
```

Called when the first frame of the ability is rendered.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-AbilityFirstFrameStateObserver-onAbilityFirstFrameDrawn(data: AbilityFirstFrameStateData): void--><!--Device-AbilityFirstFrameStateObserver-onAbilityFirstFrameDrawn(data: AbilityFirstFrameStateData): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | [AbilityFirstFrameStateData](arkts-ability-abilityfirstframestatedata-i-sys.md) | Yes | Data returned after the first frame is rendered. |

## Examples

```TypeScript
import { appManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let observer: appManager.AbilityFirstFrameStateObserver = {
  onAbilityFirstFrameDrawn(data: appManager.AbilityFirstFrameStateData) {
    console.info(`onAbilityFirstFrameDrawn success, abilityFirstFrameStateData: ${data}.`);
  }
};

try {
  appManager.on('abilityFirstFrameState', observer);
} catch (e) {
  let code = (e as BusinessError).code;
  let msg = (e as BusinessError).message;
  console.error(`appmanager.on failed, err code: ${code}, err msg: ${msg}.`);
}
```

