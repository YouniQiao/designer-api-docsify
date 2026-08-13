# getAllBundleInfoByDeveloperId (System API)

## Modules to Import

```TypeScript
import { bundleManager } from '@kit.AbilityKit';
```

## getAllBundleInfoByDeveloperId

```TypeScript
function getAllBundleInfoByDeveloperId(developerId: string): Array<BundleInfo>
```

Obtains the information about all bundles of the current user based on the given developer ID.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

<!--Device-bundleManager-function getAllBundleInfoByDeveloperId(developerId: string): Array<BundleInfo>--><!--Device-bundleManager-function getAllBundleInfoByDeveloperId(developerId: string): Array<BundleInfo>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [developerId](arkts-ability-appprovisioninfo-i-sys.md) | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Array & lt;BundleInfo & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17700059](../errorcode-bundle.md#17700059-specified-developer-id-does-not-exist) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { bundleManager } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

let developerId = "123456.789";

try {
  let data = bundleManager.getAllBundleInfoByDeveloperId(developerId);
  hilog.info(0x0000, 'testTag', 'getAllBundleInfoByDeveloperId successfully. Data: %{public}s', JSON.stringify(data));
} catch (err) {
  let message = (err as BusinessError).message;
  hilog.error(0x0000, 'testTag', 'getAllBundleInfoByDeveloperId failed: %{public}s', message);
}
```
