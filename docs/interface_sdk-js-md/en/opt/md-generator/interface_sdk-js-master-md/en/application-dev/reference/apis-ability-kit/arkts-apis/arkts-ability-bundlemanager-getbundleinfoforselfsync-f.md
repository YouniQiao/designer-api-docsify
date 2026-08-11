# getBundleInfoForSelfSync

## Modules to Import

```TypeScript
import { bundleManager } from 'kits/@kit.AbilityKit';
```

## getBundleInfoForSelfSync

```TypeScript
function getBundleInfoForSelfSync(bundleFlags: number): BundleInfo
```

Obtains the bundle information of the current application based on the given bundle flags. This API returns the result synchronously.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-bundleManager-function getBundleInfoForSelfSync(bundleFlags: int): BundleInfo--><!--Device-bundleManager-function getBundleInfoForSelfSync(bundleFlags: int): BundleInfo-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleFlags | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [BundleInfo](arkts-ability-bundleinfo-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## Examples

```TypeScript
import { bundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let bundleFlags = bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_REQUESTED_PERMISSION;

try {
  let data = bundleManager.getBundleInfoForSelfSync(bundleFlags);
  hilog.info(0x0000, 'testTag', 'getBundleInfoForSelfSync successfully: %{public}s', JSON.stringify(data));
} catch (err) {
  let message = (err as BusinessError).message;
  hilog.error(0x0000, 'testTag', 'getBundleInfoForSelfSync failed: %{public}s', message);
}
```
