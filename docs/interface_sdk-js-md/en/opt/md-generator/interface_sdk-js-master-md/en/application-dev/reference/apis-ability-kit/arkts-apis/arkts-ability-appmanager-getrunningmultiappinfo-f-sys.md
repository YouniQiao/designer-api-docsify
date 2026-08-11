# getRunningMultiAppInfo (System API)

## Modules to Import

```TypeScript
import { appManager } from 'kits/@kit.AbilityKit';
```

## getRunningMultiAppInfo

```TypeScript
function getRunningMultiAppInfo(bundleName: string): Promise<RunningMultiAppInfo>
```

Obtains the information about running applications in multi-app mode. The multi-app mode means that an application can be simultaneously logged in with different accounts on the same device. This API uses a promise to return the result.

**Since:** 12

**Required permissions:** ohos.permission.GET_RUNNING_INFO

**Model restriction:** This API can be used only in the stage model.

<!--Device-appManager-function getRunningMultiAppInfo(bundleName: string): Promise<RunningMultiAppInfo>--><!--Device-appManager-function getRunningMultiAppInfo(bundleName: string): Promise<RunningMultiAppInfo>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;RunningMultiAppInfo&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [18500001](../errorcode-ability.md#18500001-invalid-bundle-name) |
| [16000072](../errorcode-ability.md#16000072-multiapp-mode-is-not-supported) |

## Examples

```TypeScript
import { appManager } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let bundleName = "ohos.samples.etsclock";
  appManager.getRunningMultiAppInfo(bundleName).then((info: appManager.RunningMultiAppInfo) => {
      hilog.info(0x0000, 'testTag', `getRunningMultiAppInfo success`);
    }).catch((err: BusinessError) => {
      hilog.error(0x0000, 'testTag', `getRunningMultiAppInfo error, code: ${err.code}, msg:${err.message}`);
    })
} catch (err) {
  hilog.error(0x0000, 'testTag', `getRunningMultiAppInfo error, code: ${err.code}, msg:${err.message}`);
}
```
