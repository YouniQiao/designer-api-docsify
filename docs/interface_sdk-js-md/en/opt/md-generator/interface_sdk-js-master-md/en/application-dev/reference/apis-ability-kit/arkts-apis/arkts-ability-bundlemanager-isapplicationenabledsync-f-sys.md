# isApplicationEnabledSync (System API)

## Modules to Import

```TypeScript
import { bundleManager } from '@kit.AbilityKit';
```

## isApplicationEnabledSync

```TypeScript
function isApplicationEnabledSync(bundleName: string): boolean
```

Checks whether an application is enabled. This API returns the result synchronously.

**Since:** 23

**Deprecated since:** -1

<!--Device-bundleManager-function isApplicationEnabledSync(bundleName: string): boolean--><!--Device-bundleManager-function isApplicationEnabledSync(bundleName: string): boolean-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [17700001](../errorcode-bundle.md#17700001-bundle-name-does-not-exist) |

## Examples

```TypeScript
import { bundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let bundleName = 'com.example.myapplication';

try {
  let data = bundleManager.isApplicationEnabledSync(bundleName);
  hilog.info(0x0000, 'testTag', 'isApplicationEnabledSync successfully: %{public}s', JSON.stringify(data));
} catch (err) {
  let message = (err as BusinessError).message;
  hilog.error(0x0000, 'testTag', 'isApplicationEnabledSync failed: %{public}s', message);
}
```
