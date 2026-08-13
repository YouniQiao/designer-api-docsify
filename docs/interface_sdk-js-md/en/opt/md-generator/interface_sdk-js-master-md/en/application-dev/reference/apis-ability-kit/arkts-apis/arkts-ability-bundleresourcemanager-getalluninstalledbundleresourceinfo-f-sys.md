# getAllUninstalledBundleResourceInfo (System API)

## Modules to Import

```TypeScript
import { bundleResourceManager } from '@kit.AbilityKit';
```

## getAllUninstalledBundleResourceInfo

```TypeScript
function getAllUninstalledBundleResourceInfo(resourceFlags: number): Promise<Array<BundleResourceInfo>>
```

Obtains the bundle resource information of all uninstalled applications that have retained data based on the given resource flags. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.GET_BUNDLE_RESOURCES

<!--Device-bundleResourceManager-function getAllUninstalledBundleResourceInfo(resourceFlags: int): Promise<Array<BundleResourceInfo>>--><!--Device-bundleResourceManager-function getAllUninstalledBundleResourceInfo(resourceFlags: int): Promise<Array<BundleResourceInfo>>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Resource

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| resourceFlags | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Array & lt;BundleResourceInfo & gt; & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { bundleResourceManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let resourceFlag = bundleResourceManager.ResourceFlag.GET_RESOURCE_INFO_ALL;
try {
  bundleResourceManager.getAllUninstalledBundleResourceInfo(resourceFlag).then(data => {
    hilog.info(0x0000, 'testTag', 'getAllUninstalledBundleResourceInfo successfully. Data length: %{public}s',
      JSON.stringify(data.length));
  }).catch((err: BusinessError) => {
    hilog.error(0x0000, 'testTag', 'getAllUninstalledBundleResourceInfo failed. err: %{public}s', err.message);
  })
} catch (err) {
  let message = (err as BusinessError).message;
  hilog.error(0x0000, 'testTag', 'getAllUninstalledBundleResourceInfo failed: %{public}s', message);
}
```
