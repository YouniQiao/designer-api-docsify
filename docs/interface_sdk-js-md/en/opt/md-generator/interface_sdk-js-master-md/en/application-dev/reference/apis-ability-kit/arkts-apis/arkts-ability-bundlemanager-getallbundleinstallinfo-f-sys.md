# getAllBundleInstallInfo (System API)

## Modules to Import

```TypeScript
import { bundleManager } from '@kit.AbilityKit';
```

## getAllBundleInstallInfo

```TypeScript
function getAllBundleInstallInfo(): Promise<Array<Record<string, Object>>>
```

Obtains the extended install information about all applications in the system. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.GET_INSTALLED_BUNDLE_LIST

**Model restriction:** This API can be used only in the stage model.

<!--Device-bundleManager-function getAllBundleInstallInfo(): Promise<Array<Record<string, Object>>>--><!--Device-bundleManager-function getAllBundleInstallInfo(): Promise<Array<Record<string, Object>>>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[Record](../../apis-na/arkts-apis/arkts-na-record-t.md)&lt;string, Object&gt;&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { bundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  bundleManager.getAllBundleInstallInfo().then((data) => {
    hilog.info(0x0000, 'testTag', 'getAllBundleInstallInfo successfully. Data: %{public}s', JSON.stringify(data));
  }).catch((err: BusinessError) => {
    hilog.error(0x0000, 'testTag', 'getAllBundleInstallInfo failed. Cause: %{public}s', err.message);
  });
} catch (err) {
  let message = (err as BusinessError).message;
  hilog.error(0x0000, 'testTag', 'getAllBundleInstallInfo failed. Cause: %{public}s', message);
}
```


## getAllBundleInstallInfo

```TypeScript
function getAllBundleInstallInfo(): Promise<Array<Record<string, RecordData>>>
```

Obtains the install information of all apps.

**Since:** 24

**Deprecated since:** -1

**Required permissions:** ohos.permission.GET_INSTALLED_BUNDLE_LIST

**Model restriction:** This API can be used only in the stage model.

<!--Device-bundleManager-function getAllBundleInstallInfo(): Promise<Array<Record<string, RecordData>>>--><!--Device-bundleManager-function getAllBundleInstallInfo(): Promise<Array<Record<string, RecordData>>>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[Record](../../apis-na/arkts-apis/arkts-na-record-t.md)&lt;string, [RecordData](../../apis-arkdata/arkts-apis/arkts-arkdata-preferences-recorddata-t.md)&gt;&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
