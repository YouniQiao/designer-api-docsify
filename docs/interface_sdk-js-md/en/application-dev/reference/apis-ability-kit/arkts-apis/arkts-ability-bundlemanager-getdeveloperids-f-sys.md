# getDeveloperIds (System API)

## Modules to Import

```TypeScript
import { bundleManager } from 'kits/@kit.AbilityKit';
```

## getDeveloperIds

```TypeScript
function getDeveloperIds(appDistributionType?: int): Array<string>
```

根据给定的应用[appDistributionType](arkts-ability-bundlemanager-appdistributiontype-e-sys.md)获取当前用户下的所有开发者ID列表。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

<!--Device-bundleManager-function getDeveloperIds(appDistributionType?: int): Array<string>--><!--Device-bundleManager-function getDeveloperIds(appDistributionType?: int): Array<string>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| appDistributionType | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | 表示应用的分发类型，当该参数缺省时，会返回所有应用的开发者ID列表。 |

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;string&gt; | 同步返回Array&lt;string&gt;。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 201 | Permission denied. |
| 202 | Permission denied, non-system app called system api. |

## Examples

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

