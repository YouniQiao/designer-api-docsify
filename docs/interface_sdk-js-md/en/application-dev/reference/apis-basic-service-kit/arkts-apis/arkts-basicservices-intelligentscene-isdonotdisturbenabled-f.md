# isDoNotDisturbEnabled

## Modules to Import

```TypeScript
import { intelligentScene } from 'kits/@kit.BasicServicesKit';
```

## isDoNotDisturbEnabled

```TypeScript
function isDoNotDisturbEnabled(): Promise<boolean>
```

Checks whether Do Not Disturb is enabled on this device.The Do Not Disturb state defines if notifications are allowed to interrupt the user (e.g. via sound & vibration) and is applied globally.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Required permissions:** ohos.permission.GET_DONOTDISTURB_STATE

**Model restriction:** This API can be used only in the stage model.

<!--Device-intelligentScene-function isDoNotDisturbEnabled(): Promise<boolean>--><!--Device-intelligentScene-function isDoNotDisturbEnabled(): Promise<boolean>-End-->

**System capability:** SystemCapability.Applications.IntelligentScene

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | Returns whether Do Not Disturb is enabled. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 35200001 | Internal error. |
| 201 | Permission denied. |

## Examples

```TypeScript
import { BusinessError, intelligentScene } from '@kit.BasicServicesKit';

async function isDoNotDisturbEnabled(): Promise<boolean> {
  let isDoNotDisturbEnabled: boolean = false;
  try {
    isDoNotDisturbEnabled = await intelligentScene.isDoNotDisturbEnabled();
  } catch (err) {
    console.error(`Failed to get doNotDisturb state, code: ${err.code}, message: ${err.message}`);
  }
  if (isDoNotDisturbEnabled) {
    console.info('DoNotDisturb state is open');
  } else {
    console.info('DoNotDisturb state is closed');
  }
  return isDoNotDisturbEnabled;
}
```

