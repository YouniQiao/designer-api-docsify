# isAppRunning

## Modules to Import

```TypeScript
import { appManager } from '@kit.AbilityKit';
```

## isAppRunning

```TypeScript
function isAppRunning(bundleName: string, appCloneIndex?: number): Promise<boolean>
```

Checks whether the application with the specified bundle name and application clone index is running across all users. This API uses a promise to return the result. > **NOTE：**> > If the application is not installed for the current user, error code 16000073 is returned. If the application is > installed for the current user, the system checks whether the application is running across all users.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.GET_RUNNING_INFO

<!--Device-appManager-function isAppRunning(bundleName: string, appCloneIndex?: int): Promise<boolean>--><!--Device-appManager-function isAppRunning(bundleName: string, appCloneIndex?: int): Promise<boolean>-End-->

**System capability:** SystemCapability.Ability.AbilityRuntime.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |
| appCloneIndex | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;boolean & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [16000050](../errorcode-ability.md#16000050-internal-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [16000073](../errorcode-ability.md#16000073-appcloneindex-is-invalid) |

## Examples

```TypeScript
import { appManager } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let bundleName = "ohos.samples.etsclock";
  appManager.isAppRunning(bundleName).then((data: boolean) => {
      hilog.info(0x0000, 'testTag', `data: ${JSON.stringify(data)}`);
    }).catch((err: BusinessError) => {
      hilog.error(0x0000, 'testTag', `isAppRunning error, code: ${err.code}, msg:${err.message}`);
    })
} catch (err) {
  hilog.error(0x0000, 'testTag', `isAppRunning error, code: ${err.code}, msg:${err.message}`);
}
```
