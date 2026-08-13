# getAppProvisionInfoSync (System API)

## Modules to Import

```TypeScript
import { bundleManager } from '@kit.AbilityKit';
```

## getAppProvisionInfoSync

```TypeScript
function getAppProvisionInfoSync(bundleName: string, userId?: number): AppProvisionInfo
```

Obtains the provision profile based on the given bundle name and user ID. This API returns the result synchronously. No permission is required for obtaining the caller's own information.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

<!--Device-bundleManager-function getAppProvisionInfoSync(bundleName: string, userId?: int): AppProvisionInfo--><!--Device-bundleManager-function getAppProvisionInfoSync(bundleName: string, userId?: int): AppProvisionInfo-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |
| userId | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [AppProvisionInfo](arkts-ability-bundlemanager-appprovisioninfo-t-sys.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [17700004](../errorcode-bundle.md#17700004-user-id-does-not-exist) |
| [17700001](../errorcode-bundle.md#17700001-bundle-name-does-not-exist) |

## Examples

```TypeScript
import { bundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let bundleName = "com.ohos.myapplication";
let userId = 100;

try {
  let data = bundleManager.getAppProvisionInfoSync(bundleName);
  hilog.info(0x0000, 'testTag', 'getAppProvisionInfoSync successfully. Data: %{public}s', JSON.stringify(data));
} catch (err) {
  let message = (err as BusinessError).message;
  hilog.error(0x0000, 'testTag', 'getAppProvisionInfoSync failed. Cause: %{public}s', message);
}

try {
  let data = bundleManager.getAppProvisionInfoSync(bundleName, userId);
  hilog.info(0x0000, 'testTag', 'getAppProvisionInfoSync successfully. Data: %{public}s', JSON.stringify(data));
} catch (err) {
  let message = (err as BusinessError).message;
  hilog.error(0x0000, 'testTag', 'getAppProvisionInfoSync failed. Cause: %{public}s', message);
}
```
