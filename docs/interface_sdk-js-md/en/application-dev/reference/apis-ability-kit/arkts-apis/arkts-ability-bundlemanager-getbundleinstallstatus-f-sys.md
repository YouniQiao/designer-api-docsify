# getBundleInstallStatus (System API)

## Modules to Import

```TypeScript
import { bundleManager } from 'kits/@kit.AbilityKit';
```

## getBundleInstallStatus

```TypeScript
function getBundleInstallStatus(bundleName: string): BundleInstallStatus
```

查询当前用户下指定应用的安装状态。

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Required permissions:** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

<!--Device-bundleManager-function getBundleInstallStatus(bundleName: string): BundleInstallStatus--><!--Device-bundleManager-function getBundleInstallStatus(bundleName: string): BundleInstallStatus-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bundleName | string | Yes | 指定应用的包名。 |

**Return value:**

| Type | Description |
| --- | --- |
| [BundleInstallStatus](arkts-ability-bundlemanager-bundleinstallstatus-e-sys.md) | 应用的安装状态。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 201 | Permission denied. |
| 202 | Permission denied. A non-system application is not allowed to call a system API. |

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

