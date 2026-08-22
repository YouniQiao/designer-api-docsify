# ContinueState

Enumerates the mission continuation states of the application. It is used in the [setMissionContinueState](arkts-ability-uiabilitycontext-c.md#setmissioncontinuestate) API of [UIAbilityContext](arkts-ability-uiabilitycontext-c.md).

**Since:** 23

<!--Device-AbilityConstant-export enum ContinueState--><!--Device-AbilityConstant-export enum ContinueState-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## ACTIVE

```TypeScript
ACTIVE = 0
```

Mission continuation is activated for the current application.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ContinueState-ACTIVE = 0--><!--Device-ContinueState-ACTIVE = 0-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## INACTIVE

```TypeScript
INACTIVE = 1
```

Mission continuation is not activated for the current application.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-ContinueState-INACTIVE = 1--><!--Device-ContinueState-INACTIVE = 1-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Examples**

```TypeScript
import { UIAbility, Want, AbilityConstant } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export default class MyAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    this.context.setMissionContinueState(AbilityConstant.ContinueState.INACTIVE, (result: BusinessError) => {
      console.info(`setMissionContinueState: ${JSON.stringify(result)}`);
    });
  }
}
```

