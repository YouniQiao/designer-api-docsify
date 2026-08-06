# isApplicationDisableForbidden (System API)

## isApplicationDisableForbidden

```TypeScript
function isApplicationDisableForbidden(bundleName: string, userId: int, appIndex: int): boolean
```

Synchronously queries whether a specified application or application clone of a specified user is set to forbid being disabled.If you need to check whether an application is forbidden to be disabled under the current user,ohos.permission.GET\_BUNDLE\_INFO\_PRIVILEGED needs to be applied for.If you need to check whether an application is forbidden to be disabled under other users,ohos.permission.GET\_BUNDLE\_INFO\_PRIVILEGED and ohos.permission.INTERACT\_ACROSS\_LOCAL\_ACCOUNTS need to be applied for.

**Since:** 24

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 24.

**Required permissions:** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED or (ohos.permission.GET_BUNDLE_INFO_PRIVILEGED and ohos.permission.INTERACT_ACROSS_LOCAL_ACCOUNTS)

**Model restriction:** This API can be used only in the stage model.

<!--Device-bundleManager-function isApplicationDisableForbidden(bundleName: string, userId: int, appIndex: int): boolean--><!--Device-bundleManager-function isApplicationDisableForbidden(bundleName: string, userId: int, appIndex: int): boolean-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bundleName | string | Yes | Bundle name of the application. |
| userId | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：int | Yes | User ID, which can be obtained by calling getOsAccountLocalId. The value is greater than or equal to 0. |
| appIndex | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：int | Yes | Index of the application. The value ranges from 0 to 5. The value 0 indicates the main application, and the values 1 to 5 indicate the indexes of application clones. |

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Whether a specified application is set to forbid being disabled. The value true indicates that the specified application is set to forbid being disabled, and false indicates that the specified application is not set to forbid being disabled. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission denied. Non-system APP calling system API. |
| [17700001](../errorcode-bundle.md#17700001-bundle-name-does-not-exist) | The specified bundle is not found. |
| [17700004](../errorcode-bundle.md#17700004-user-id-does-not-exist) | The specified user ID is not found. |
| [17700061](../errorcode-bundle.md#17700061-appindex-for-a-clone-is-invalid) | The specified app index is invalid. |

