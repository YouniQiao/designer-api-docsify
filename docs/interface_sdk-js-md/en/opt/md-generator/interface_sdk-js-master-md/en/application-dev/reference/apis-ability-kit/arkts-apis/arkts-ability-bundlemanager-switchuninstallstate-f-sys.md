# switchUninstallState (System API)

## Modules to Import

```TypeScript
import { bundleManager } from 'kits/@kit.AbilityKit';
```

## switchUninstallState

```TypeScript
function switchUninstallState(bundleName: string, state: boolean): void
```

Switches the uninstall state of an application. This API is independent of EDM application interception control.

**Since:** 12

**Required permissions:** ohos.permission.CHANGE_BUNDLE_UNINSTALL_STATE

<!--Device-bundleManager-function switchUninstallState(bundleName: string, state: boolean): void--><!--Device-bundleManager-function switchUninstallState(bundleName: string, state: boolean): void-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |
| state | boolean | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [17700060](../errorcode-bundle.md#17700060-specified-application-cannot-be-uninstalled) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [17700001](../errorcode-bundle.md#17700001-bundle-name-does-not-exist) |

## Examples

```TypeScript
import { bundleManager } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  bundleManager.switchUninstallState('com.example.myapplication', false);
} catch (err) {
  let message = (err as BusinessError).message;
  hilog.error(0x0000, 'testTag', 'switchUninstallState failed: %{public}s', message);
}
```
