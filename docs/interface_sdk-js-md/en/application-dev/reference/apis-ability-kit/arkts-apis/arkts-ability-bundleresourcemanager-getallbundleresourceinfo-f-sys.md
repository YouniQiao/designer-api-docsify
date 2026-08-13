# getAllBundleResourceInfo (System API)

## Modules to Import

```TypeScript
import { bundleResourceManager } from '@kit.AbilityKit';
```

## getAllBundleResourceInfo

```TypeScript
function getAllBundleResourceInfo(resourceFlags: int, callback: AsyncCallback<Array<BundleResourceInfo>>): void
```

Obtains the bundle resource information of all applications based on the given resource flags. This API uses an asynchronous callback to return the result.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Required permissions:** ohos.permission.GET_INSTALLED_BUNDLE_LIST and ohos.permission.GET_BUNDLE_RESOURCES

<!--Device-bundleResourceManager-function getAllBundleResourceInfo(resourceFlags: int, callback: AsyncCallback<Array<BundleResourceInfo>>): void--><!--Device-bundleResourceManager-function getAllBundleResourceInfo(resourceFlags: int, callback: AsyncCallback<Array<BundleResourceInfo>>): void-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Resource

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| resourceFlags | int | Yes | Type of the resource information to obtain. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;BundleResourceInfo&gt;&gt; | Yes | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md#AsyncCallback) used to return the result. If the information is successfully obtained, **err** is **null** and **data** is a BundleResourceInfo array. Otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission denied, non-system app called system api. |


## getAllBundleResourceInfo

```TypeScript
function getAllBundleResourceInfo(resourceFlags: int): Promise<Array<BundleResourceInfo>>
```

Obtains the bundle resource information of all applications based on the given resource flags. This API uses a promise to return the result.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Required permissions:** ohos.permission.GET_INSTALLED_BUNDLE_LIST and ohos.permission.GET_BUNDLE_RESOURCES

<!--Device-bundleResourceManager-function getAllBundleResourceInfo(resourceFlags: int): Promise<Array<BundleResourceInfo>>--><!--Device-bundleResourceManager-function getAllBundleResourceInfo(resourceFlags: int): Promise<Array<BundleResourceInfo>>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Resource

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| resourceFlags | int | Yes | Type of the resource information to obtain. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;BundleResourceInfo&gt;&gt; | Promise used to return the BundleResourceInfo array. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission denied, non-system app called system api. |

