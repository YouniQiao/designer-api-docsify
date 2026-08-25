# isDoNotDisturbEnabled

## Modules to Import

```TypeScript
import { intelligentScene } from '@kit.BasicServicesKit';
```

## isDoNotDisturbEnabled

```TypeScript
function isDoNotDisturbEnabled(): Promise<boolean>
```

Checks whether Do Not Disturb is enabled on this device. The Do Not Disturb state defines if notifications are allowed to interrupt the user (e.g. via sound & vibration) and is applied globally.

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Required permissions:** ohos.permission.GET_DONOTDISTURB_STATE

**Model restriction:** This API can be used only in the stage model.

**System capability:** SystemCapability.Applications.IntelligentScene

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [35200001](../errorcode-intelligentScene.md#35200001-internal-error) |

**Examples**

```TypeScript
import { BusinessError, intelligentScene } from '@kit.BasicServicesKit';

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
```
