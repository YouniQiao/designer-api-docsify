# getApplicationLabel

## getApplicationLabel

```TypeScript
function getApplicationLabel(bundleName: string, appIndex: int): Promise<string>
```

Obtains the name of an application with the specified package name and clone index. This API uses a promise to return the result.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Required permissions:** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

**Model restriction:** This API can be used only in the stage model.

<!--Device-bundleManager-function getApplicationLabel(bundleName: string, appIndex: int): Promise<string>--><!--Device-bundleManager-function getApplicationLabel(bundleName: string, appIndex: int): Promise<string>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Resource

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| bundleName | string | Yes | Bundle name of the application. |
| appIndex | ArkTS-Dyn: number  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：int | Yes | Index of the application. The value ranges from 0 to 5.The value 0 indicates the main application, and the values 1 to 5 indicate the indexes of application clones. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;string&gt; | Promise used to return the result. If the operation is successful, the application |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [17700001](../errorcode-bundle.md#17700001-bundle-name-does-not-exist) | The specified bundle is not found. |
| [17700061](../errorcode-bundle.md#17700061-appindex-for-a-clone-is-invalid) | The specified app index is invalid. |

