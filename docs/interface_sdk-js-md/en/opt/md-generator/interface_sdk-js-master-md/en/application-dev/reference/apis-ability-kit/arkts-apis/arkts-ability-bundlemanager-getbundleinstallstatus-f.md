# getBundleInstallStatus

## Modules to Import

```TypeScript
import { bundleManager } from '@kit.AbilityKit';
```

## getBundleInstallStatus

```TypeScript
function getBundleInstallStatus(bundleName: string): BundleInstallStatus
```

Obtains the installation status of a specified application under a given user.

**Since:** 26.1.0

**Required permissions:** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

<!--Device-bundleManager-function getBundleInstallStatus(bundleName: string): BundleInstallStatus--><!--Device-bundleManager-function getBundleInstallStatus(bundleName: string): BundleInstallStatus-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [BundleInstallStatus](arkts-ability-bundlemanager-bundleinstallstatus-e.md) |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { bundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

// Replace the bundle name with the actual one.
let bundleName: string = 'com.ohos.demo';

try {
  let bundleInstallStatus = bundleManager.getBundleInstallStatus(bundleName);
  hilog.info(0x0000, 'testTag', 'bundle install status:' + bundleInstallStatus);
} catch (err) {
  let message = (err as BusinessError).message;
  hilog.error(0x0000, 'testTag', 'getBundleInstallStatus failed. Cause: %{public}s', message);
}
```
