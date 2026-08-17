# getDeveloperIds (System API)

## Modules to Import

```TypeScript
import { bundleManager } from 'bundleManager';
```

## getDeveloperIds

```TypeScript
function getDeveloperIds(appDistributionType?: int): Array<string>
```

Obtains all the developer IDs of the current user based on the given application [distribution type](arkts-ability-bundlemanager-appdistributiontype-e-sys.md#appdistributiontype-system-api).

**Since:** 23

**Required permissions:** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

<!--Device-bundleManager-function getDeveloperIds(appDistributionType?: int): Array<string>--><!--Device-bundleManager-function getDeveloperIds(appDistributionType?: int): Array<string>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| appDistributionType | int | No | Application distribution type. If this parameter is not specified, a list of developer IDs of all applications is returned. |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;string&gt; | An array of strings. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission denied, non-system app called system api. |

**Examples**

```TypeScript
import { bundleManager } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

let appDistributionType = bundleManager.AppDistributionType.ENTERPRISE;

try {
  let data = bundleManager.getDeveloperIds(appDistributionType);
  hilog.info(0x0000, 'testTag', 'getDeveloperIds successfully. Data: %{public}s', JSON.stringify(data));
} catch (err) {
  let message = (err as BusinessError).message;
  hilog.error(0x0000, 'testTag', 'getDeveloperIds failed: %{public}s', message);
}
```

