# AutoStartupCallback (System API)

The module defines the callback to be invoked when auto-startup is set or canceled for an application component.

**Since:** 11

<!--Device-unnamed-export interface AutoStartupCallback--><!--Device-unnamed-export interface AutoStartupCallback-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

## onAutoStartupOff

```TypeScript
onAutoStartupOff(info: AutoStartupInfo): void
```

Called when the auto-startup setting of an application component is canceled.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

<!--Device-AutoStartupCallback-onAutoStartupOff(info: AutoStartupInfo): void--><!--Device-AutoStartupCallback-onAutoStartupOff(info: AutoStartupInfo): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| info | [AutoStartupInfo](arkts-ability-autostartupinfo-i-sys.md) | Yes |

## Examples

```TypeScript
import { autoStartupManager, common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let autoStartupCallback: common.AutoStartupCallback = {
  onAutoStartupOn(data: common.AutoStartupInfo) {
    console.info(`autostartupmanager onAutoStartupOn, data: ${JSON.stringify(data)}.`);
  },
  onAutoStartupOff(data: common.AutoStartupInfo) {
    console.info(`autostartupmanager onAutoStartupOff, data: ${JSON.stringify(data)}.`);
  }
}

try {
  autoStartupManager.on('systemAutoStartup', autoStartupCallback);
} catch (err) {
  let code = (err as BusinessError).code;
  let msg = (err as BusinessError).message;
  console.error(`autoStartupManager.on failed, err code: ${code}, err msg: ${msg}.`);
}
```

## onAutoStartupOn

```TypeScript
onAutoStartupOn(info: AutoStartupInfo): void
```

Called when auto-startup is set for an application component.

**Since:** 11

**Model restriction:** This API can be used only in the stage model.

<!--Device-AutoStartupCallback-onAutoStartupOn(info: AutoStartupInfo): void--><!--Device-AutoStartupCallback-onAutoStartupOn(info: AutoStartupInfo): void-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| info | [AutoStartupInfo](arkts-ability-autostartupinfo-i-sys.md) | Yes |

## Examples

```TypeScript
import { autoStartupManager, common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let autoStartupCallback: common.AutoStartupCallback = {
  onAutoStartupOn(data: common.AutoStartupInfo) {
    console.info(`autostartupmanager onAutoStartupOn, data: ${JSON.stringify(data)}.`);
  },
  onAutoStartupOff(data: common.AutoStartupInfo) {
    console.info(`autostartupmanager onAutoStartupOff, data: ${JSON.stringify(data)}.`);
  }
}

try {
  autoStartupManager.on('systemAutoStartup', autoStartupCallback);
} catch (err) {
  let code = (err as BusinessError).code;
  let msg = (err as BusinessError).message;
  console.error(`autoStartupManager.on failed, err code: ${code}, err msg: ${msg}.`);
}
```
