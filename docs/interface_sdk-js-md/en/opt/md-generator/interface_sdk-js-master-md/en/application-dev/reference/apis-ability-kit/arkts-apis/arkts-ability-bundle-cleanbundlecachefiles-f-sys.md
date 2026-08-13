# cleanBundleCacheFiles (System API)

## Modules to Import

```TypeScript
import { bundle } from '@kit.AbilityKit';
```

## cleanBundleCacheFiles

```TypeScript
function cleanBundleCacheFiles(bundleName: string, callback: AsyncCallback<void>): void
```

Clears the cache data of an application. This API uses an asynchronous callback to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** null

**Required permissions:** ohos.permission.REMOVE_CACHE_FILES

<!--Device-bundle-function cleanBundleCacheFiles(bundleName: string, callback: AsyncCallback<void>): void--><!--Device-bundle-function cleanBundleCacheFiles(bundleName: string, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |


## cleanBundleCacheFiles

```TypeScript
function cleanBundleCacheFiles(bundleName: string): Promise<void>
```

Clears the cache data of an application. This API uses a promise to return the result.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** null

**Required permissions:** ohos.permission.REMOVE_CACHE_FILES

<!--Device-bundle-function cleanBundleCacheFiles(bundleName: string): Promise<void>--><!--Device-bundle-function cleanBundleCacheFiles(bundleName: string): Promise<void>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |
