# killProcessesInBatch (System API)

## Modules to Import

```TypeScript
import { appManager } from 'kits/@kit.AbilityKit';
```

## killProcessesInBatch

```TypeScript
function killProcessesInBatch(pids: Array<number>): Promise<void>
```

Kills processes in batches. This API uses a promise to return the result.This API can be properly called on PCs/2-in-1 devices. If it is called on other devices, error code 801 is returned.  
**Required permissions**: ohos.permission.KILL_APP_PROCESSES

**Since:** 14

**Required permissions:** ohos.permission.KILL_APP_PROCESSES

<!--Device-appManager-function killProcessesInBatch(pids: Array<int>): Promise<void>--><!--Device-appManager-function killProcessesInBatch(pids: Array<int>): Promise<void>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| pids | Array&lt;number&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [16000050](../errorcode-ability.md#16000050-internal-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { appManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let pids: Array<number> = [100, 101, 102];
  appManager.killProcessesInBatch(pids).then(() => {
    console.info(`killProcessesInBatch success`);
  }).catch((err: BusinessError) => {
    console.error(`killProcessesInBatch fail, err: ${JSON.stringify(err)}`);
  });
} catch (paramError) {
  let code = (paramError as BusinessError).code;
  let message = (paramError as BusinessError).message;
  console.error(`[appManager] killProcessesInBatch error: ${code}, ${message}`);
}
```
