# getAllBundleInstallInfo (System API)

## Modules to Import

```TypeScript
import { bundleManager } from 'bundleManager';
```

## getAllBundleInstallInfo

```TypeScript
function getAllBundleInstallInfo(): Promise<Array<Record<string, Object>>>
```

Obtains the extended install information about all applications in the system. This API uses a promise to return the result.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Required permissions:** ohos.permission.GET_INSTALLED_BUNDLE_LIST

**Model restriction:** This API can be used only in the stage model.

<!--Device-bundleManager-function getAllBundleInstallInfo(): Promise<Array<Record<string, Object>>>--><!--Device-bundleManager-function getAllBundleInstallInfo(): Promise<Array<Record<string, Object>>>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;Record&lt;string, Object&gt;&gt;&gt; | Promise used to return the list of extended install information set of all applications. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission denied, non-system app called system api. |


## getAllBundleInstallInfo

```TypeScript
function getAllBundleInstallInfo(): Promise<Array<Record<string, RecordData>>>
```

Obtains the install information of all apps.

**Since:** 24

**ArkTS mode:** ArkTS-Dyn only, since version 24.

**Deprecated since:** -1

**Required permissions:** ohos.permission.GET_INSTALLED_BUNDLE_LIST

**Model restriction:** This API can be used only in the stage model.

<!--Device-bundleManager-function getAllBundleInstallInfo(): Promise<Array<Record<string, RecordData>>>--><!--Device-bundleManager-function getAllBundleInstallInfo(): Promise<Array<Record<string, RecordData>>>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;Record&lt;string, [RecordData](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-recorddata-t.md)&gt;&gt;&gt; | The install information. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission denied, non-system app called system api. |

