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

**Deprecated since:** -1

**Required permissions:** ohos.permission.GET_DONOTDISTURB_STATE

**Model restriction:** This API can be used only in the stage model.

<!--Device-intelligentScene-function isDoNotDisturbEnabled(): Promise<boolean>--><!--Device-intelligentScene-function isDoNotDisturbEnabled(): Promise<boolean>-End-->

**System capability:** SystemCapability.Applications.IntelligentScene

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [35200001](../../apis-basic-services-kit/errorcode-intelligentScene.md#35200001-internal-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |

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
