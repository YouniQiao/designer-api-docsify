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

**Deprecated since:** -1

**Required permissions:** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

<!--Device-freeInstall-function getDispatchInfo(callback: AsyncCallback<DispatchInfo>): void--><!--Device-freeInstall-function getDispatchInfo(callback: AsyncCallback<DispatchInfo>): void-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.FreeInstall

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;DispatchInfo&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |


## getDispatchInfo

```TypeScript
function getDispatchInfo(): Promise<DispatchInfo>
```

Obtains the dispatch information. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

<!--Device-freeInstall-function getDispatchInfo(): Promise<DispatchInfo>--><!--Device-freeInstall-function getDispatchInfo(): Promise<DispatchInfo>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.FreeInstall

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;DispatchInfo & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
