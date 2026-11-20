# getThemeRefreshTime (System API)

## Modules to Import

```TypeScript
import { bundleManager } from '@kit.AbilityKit';
```

## getThemeRefreshTime

```TypeScript
function getThemeRefreshTime(): Promise<string>
```

Obtain the refresh timestamp of the current theme.

**Since:** 26.1.0

**Required permissions:** ohos.permission.GET_BUNDLE_RESOURCES

**Model restriction:** This API can be used only in the stage model.

<!--Device-bundleManager-function getThemeRefreshTime(): Promise<string>--><!--Device-bundleManager-function getThemeRefreshTime(): Promise<string>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;string&gt; | Promise used to return the refresh timestamp of the current theme. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission verification failed. The application does not have the permission required to call the API. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |
| [17700101](../errorcode-bundle.md#17700101-bundle-manager-service-abnormal) | Bundle manager service exception. |
