# getAppClonePreference (System API)

## Modules to Import

```TypeScript
import { bundleManager } from '@kit.AbilityKit';
```

## getAppClonePreference

```TypeScript
function getAppClonePreference(bundleName: string): Promise<AppClonePreference>
```

Obtains the application clone preference configuration based on the given bundle name.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Required permissions:** ohos.permission.MANAGE_CLONE_BUNDLE_PREFERENCES

**Model restriction:** This API can be used only in the stage model.

<!--Device-bundleManager-function getAppClonePreference(bundleName: string): Promise<AppClonePreference>--><!--Device-bundleManager-function getAppClonePreference(bundleName: string): Promise<AppClonePreference>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bundleName | string | Yes | Bundle name of the target application. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;AppClonePreference&gt; | Promise used to return the application clone preference configuration. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 17700095 | The specified bundle not found app clone preference. |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission denied, non-system app called system api. |
| [17700001](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ability-kit/errorcode-bundle.md#17700001-bundle-name-does-not-exist) | The specified bundleName is not found. |

