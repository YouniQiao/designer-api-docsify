# isNotifyAllowedInDoNotDisturb

## Modules to Import

```TypeScript
import { intelligentScene } from '@kit.BasicServicesKit';
```

## isNotifyAllowedInDoNotDisturb

```TypeScript
function isNotifyAllowedInDoNotDisturb(): Promise<boolean>
```

Checks whether calling bundle is allow notify(e.g. sound & vibration) when system Do Not Disturb is on.

**Since:** 23

**Required permissions:** ohos.permission.GET_DONOTDISTURB_STATE

**Model restriction:** This API can be used only in the stage model.

<!--Device-intelligentScene-function isNotifyAllowedInDoNotDisturb(): Promise<boolean>--><!--Device-intelligentScene-function isNotifyAllowedInDoNotDisturb(): Promise<boolean>-End-->

**System capability:** SystemCapability.Applications.IntelligentScene

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [35200001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-basic-services-kit/errorcode-intelligentScene.md#35200001-internal-error) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |

## Examples

```TypeScript
import { BusinessError, intelligentScene } from '@kit.BasicServicesKit';

async function isNotifyAllowedInDoNotDisturb(): Promise<boolean> {
  let isNotifyAllowedInDoNotDisturb: boolean = false;
  try {
    isNotifyAllowedInDoNotDisturb = await intelligentScene.isNotifyAllowedInDoNotDisturb();
  } catch (err) {
    console.error(`Failed to get doNotDisturb state, code: ${err.code}, message: ${err.message}`);
  }
  if (isNotifyAllowedInDoNotDisturb) {
    console.info('Allowed to notify in doNotDisturb state');
  } else {
    console.info('Not allowed to notify in doNotDisturb state or doNotDisturb is closed');
  }
  return isNotifyAllowedInDoNotDisturb;
}
```
