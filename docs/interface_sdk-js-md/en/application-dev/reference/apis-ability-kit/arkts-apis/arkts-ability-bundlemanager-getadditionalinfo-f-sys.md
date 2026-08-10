# getAdditionalInfo (System API)

## Modules to Import

```TypeScript
import { bundleManager } from 'kits/@kit.AbilityKit';
```

## getAdditionalInfo

```TypeScript
function getAdditionalInfo(bundleName: string): string
```

以同步接口查询指定bundleName的额外信息。该返回值是在调用install接口时传入的[InstallParam](arkts-ability-installer-installparam-i-sys.md)中的additionalInfo字段。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn since version 10; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

<!--Device-bundleManager-function getAdditionalInfo(bundleName: string): string--><!--Device-bundleManager-function getAdditionalInfo(bundleName: string): string-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bundleName | string | Yes | 指定的bundleName。 |

**Return value:**

| Type | Description |
| --- | --- |
| string | 返回指定bundleName的额外信息。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter bundleName is empty. |
| 201 | Permission denied. |
| 202 | Permission denied, non-system app called system api. |
| 17700001 | The specified bundleName is not found. |

## Examples

```TypeScript
import { bundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let bundleName = "com.example.myapplication";

try {
  let info = bundleManager.getAdditionalInfo(bundleName);
  hilog.info(0x0000, 'testTag', 'getAdditionalInfo successfully, additionInfo:%{public}s', info);
} catch (error) {
  let message = (error as BusinessError).message;
  hilog.error(0x0000, 'testTag', 'getAdditionalInfo failed. Cause: %{public}s', message);
}
```

