# RequestInfo

Defines the request information, which is used as an input parameter for binding the modal dialog box.

**Since:** 9

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

## Modules to Import

```TypeScript
import dialogRequest from '@kit.AbilityKit';
```

## windowRect

```TypeScript
windowRect?: WindowRect
```

Location attributes of a modal dialog box.

**Type:** [WindowRect](arkts-ability-dialogrequest-windowrect-i.md)

**Since:** 10

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Examples**

```TypeScript
import { AbilityConstant, UIAbility, Want, dialogRequest } from '@kit.AbilityKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    try {
      let requestInfo = dialogRequest.getRequestInfo(want);
      console.info(`getRequestInfo windowRect=, ${JSON.stringify(requestInfo.windowRect)}` );
    } catch(err) {
      console.error(`getRequestInfo err= ${JSON.stringify(err)}`);
    }
  }
}
```
