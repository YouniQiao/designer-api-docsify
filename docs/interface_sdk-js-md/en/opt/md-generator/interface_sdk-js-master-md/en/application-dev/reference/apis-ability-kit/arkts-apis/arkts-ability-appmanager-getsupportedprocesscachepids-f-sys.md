# getSupportedProcessCachePids (System API)

## Modules to Import

```TypeScript
import { appManager } from 'kits/@kit.AbilityKit';
```

## getSupportedProcessCachePids

```TypeScript
function getSupportedProcessCachePids(bundleName : string): Promise<Array<number>>
```

Obtains the PIDs of processes that support quick startup after caching in a specified application. This API uses a promise to return the result.

> **NOTE：**
> 
> This API can only be used to obtain the PIDs of the system account to which the caller belongs.

**Since:** 14

**Required permissions:** ohos.permission.GET_RUNNING_INFO

**Model restriction:** This API can be used only in the stage model.

<!--Device-appManager-function getSupportedProcessCachePids(bundleName : string): Promise<Array<int>>--><!--Device-appManager-function getSupportedProcessCachePids(bundleName : string): Promise<Array<int>>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;number&gt;&gt; |

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
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let bundleName = "ohos.samples.processcache";
  appManager.getSupportedProcessCachePids(bundleName).then((pids: Array<number>) => {
      hilog.info(0x0000, 'testTag', `pids: ${JSON.stringify(pids)}`);
    }).catch((err: BusinessError) => {
      hilog.error(0x0000, 'testTag', `get pids error, code: ${err.code}, msg:${err.message}`);
    })
} catch (err) {
  hilog.error(0x0000, 'testTag', `get pids error, code: ${err.code}, msg:${err.message}`);
}
```
