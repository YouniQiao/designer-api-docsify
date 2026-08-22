# WindowMode

Enumerates the window modes in which a UIAbility can be displayed at startup. It can be used in [startAbility](arkts-ability-uiabilitycontext-c.md#startability) .

**Since:** 23

<!--Device-AbilityConstant-export enum WindowMode--><!--Device-AbilityConstant-export enum WindowMode-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## WINDOW_MODE_UNDEFINED

```TypeScript
WINDOW_MODE_UNDEFINED = 0
```

Undefined window mode.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-WindowMode-WINDOW_MODE_UNDEFINED = 0--><!--Device-WindowMode-WINDOW_MODE_UNDEFINED = 0-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## WINDOW_MODE_FLOATING

```TypeScript
WINDOW_MODE_FLOATING = 102
```

The ability is displayed in a floating window.

**Since:** 23

**Model restriction:** This API can be used only in the stage model.

<!--Device-WindowMode-WINDOW_MODE_FLOATING = 102--><!--Device-WindowMode-WINDOW_MODE_FLOATING = 102-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Examples**

```TypeScript
import { UIAbility, StartOptions, Want, AbilityConstant } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let want: Want = {
  bundleName: 'com.example.myapplication',
  abilityName: 'EntryAbility'
};
let option: StartOptions = {
  windowMode: AbilityConstant.WindowMode.WINDOW_MODE_SPLIT_PRIMARY
};

// Ensure that the context is obtained.
export default class MyAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    this.context.startAbility(want, option).then(() => {
      console.info('Succeed to start ability.');
    }).catch((error: BusinessError) => {
      console.error(`Failed to start ability with error: ${JSON.stringify(error)}`);
    });
  }
}
```

```TypeScript
import { UIAbility, StartOptions, Want, AbilityConstant } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let want: Want = {
  bundleName: 'com.example.myapplication',
  abilityName: 'EntryAbility'
};
let option: StartOptions = {
  windowMode: AbilityConstant.WindowMode.WINDOW_MODE_FULLSCREEN
};

// Ensure that the context is obtained.
export default class MyAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
    this.context.startAbility(want, option).then(() => {
      console.info('Succeed to start ability.');
    }).catch((error: BusinessError) => {
      console.error(`Failed to start ability with error: ${JSON.stringify(error)}`);
    });
  }
}
```

