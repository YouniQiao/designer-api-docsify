# getDispatchInfo (System API)

## Modules to Import

```TypeScript
import { freeInstall } from '@kit.AbilityKit';
```

## getDispatchInfo

```TypeScript
function getDispatchInfo(callback: AsyncCallback<DispatchInfo>): void
```

Obtains the dispatch information. This API uses an asynchronous callback to return the result.

**Since:** 23

**Required permissions:** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

<!--Device-freeInstall-function getDispatchInfo(callback: AsyncCallback<DispatchInfo>): void--><!--Device-freeInstall-function getDispatchInfo(callback: AsyncCallback<DispatchInfo>): void-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.FreeInstall

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;DispatchInfo&gt; | Yes | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md) used to return the result. If the operation is successful, **err** is **null**, and **data** is the [DispatchInfo](arkts-ability-dispatchinfo-i-sys.md) object obtained. otherwise, **err** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission denied, non-system app called system api. |


## getDispatchInfo

```TypeScript
function getDispatchInfo(): Promise<DispatchInfo>
```

Obtains the dispatch information. This API uses a promise to return the result.

**Since:** 23

**Required permissions:** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

<!--Device-freeInstall-function getDispatchInfo(): Promise<DispatchInfo>--><!--Device-freeInstall-function getDispatchInfo(): Promise<DispatchInfo>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.FreeInstall

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;DispatchInfo&gt; | Promise used to return the [DispatchInfo]{ |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../errorcode-universal.md#801-api-not-supported) | Capability not supported. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission denied, non-system app called system api. |

