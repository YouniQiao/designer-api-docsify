# getApplicationInfoSync (System API)

## Modules to Import

```TypeScript
import { bundleManager } from '@kit.AbilityKit';
```

## getApplicationInfoSync

```TypeScript
function getApplicationInfoSync(bundleName: string, applicationFlags: number, userId: number) : ApplicationInfo
```

Obtains the application information based on the given bundle name, application flags, and user ID. This API returns the result synchronously. No permission is required for obtaining the caller's own information.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED or ohos.permission.GET_BUNDLE_INFO

<!--Device-bundleManager-function getApplicationInfoSync(bundleName: string, applicationFlags: int, userId: int) : ApplicationInfo--><!--Device-bundleManager-function getApplicationInfoSync(bundleName: string, applicationFlags: int, userId: int) : ApplicationInfo-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |
| applicationFlags | number | Yes |
| userId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ApplicationInfo](arkts-ability-bundlemanager-applicationinfo-t.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17700026](../errorcode-bundle.md#17700026-bundle-disabled) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [17700004](../errorcode-bundle.md#17700004-user-id-does-not-exist) |
| [17700001](../errorcode-bundle.md#17700001-bundle-name-does-not-exist) |

## Examples

```TypeScript
import { bundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let bundleName = 'com.example.myapplication';
let applicationFlags = bundleManager.ApplicationFlag.GET_APPLICATION_INFO_DEFAULT;
let userId = 100;

try {
  let data = bundleManager.getApplicationInfoSync(bundleName, applicationFlags, userId);
  hilog.info(0x0000, 'testTag', 'getApplicationInfoSync successfully: %{public}s', JSON.stringify(data));
} catch (err) {
  let message = (err as BusinessError).message;
  hilog.error(0x0000, 'testTag', 'getApplicationInfoSync failed: %{public}s', message);
}
```


## getApplicationInfoSync

```TypeScript
function getApplicationInfoSync(bundleName: string, applicationFlags: number) : ApplicationInfo
```

Obtains the application information based on the given bundle name and application flags. This API returns the result synchronously. No permission is required for obtaining the caller's own information.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED or ohos.permission.GET_BUNDLE_INFO

<!--Device-bundleManager-function getApplicationInfoSync(bundleName: string, applicationFlags: int) : ApplicationInfo--><!--Device-bundleManager-function getApplicationInfoSync(bundleName: string, applicationFlags: int) : ApplicationInfo-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |
| applicationFlags | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ApplicationInfo](arkts-ability-bundlemanager-applicationinfo-t.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17700026](../errorcode-bundle.md#17700026-bundle-disabled) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [17700001](../errorcode-bundle.md#17700001-bundle-name-does-not-exist) |

## Examples

```TypeScript
import { bundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let bundleName = 'com.example.myapplication';
let applicationFlags = bundleManager.ApplicationFlag.GET_APPLICATION_INFO_DEFAULT;

try {
  let data = bundleManager.getApplicationInfoSync(bundleName, applicationFlags);
  hilog.info(0x0000, 'testTag', 'getApplicationInfoSync successfully: %{public}s', JSON.stringify(data));
} catch (err) {
  let message = (err as BusinessError).message;
  hilog.error(0x0000, 'testTag', 'getApplicationInfoSync failed: %{public}s', message);
}
```
