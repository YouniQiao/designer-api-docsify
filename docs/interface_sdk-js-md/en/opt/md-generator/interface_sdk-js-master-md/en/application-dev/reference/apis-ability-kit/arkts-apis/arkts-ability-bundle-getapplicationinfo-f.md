# getApplicationInfo

## Modules to Import

```TypeScript
import { bundle } from '@kit.AbilityKit';
```

## getApplicationInfo

```TypeScript
function getApplicationInfo(bundleName: string,
    bundleFlags: number, userId: number, callback: AsyncCallback<ApplicationInfo>): void
```

Obtains the application information of the specified user based on a given bundle name. This API uses an asynchronous callback to return the result. No permission is required for obtaining the caller's own information.

**Since:** 7

**Deprecated since:** 9

**Required permissions:** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED or ohos.permission.GET_BUNDLE_INFO

<!--Device-bundle-function getApplicationInfo(bundleName: string,    bundleFlags: number, userId: number, callback: AsyncCallback<ApplicationInfo>): void--><!--Device-bundle-function getApplicationInfo(bundleName: string,    bundleFlags: number, userId: number, callback: AsyncCallback<ApplicationInfo>): void-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |
| bundleFlags | number | Yes |
| userId | number | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[ApplicationInfo](arkts-ability-applicationinfo-applicationinfo-depr-i.md)&gt; | Yes |


## getApplicationInfo

```TypeScript
function getApplicationInfo(bundleName: string, bundleFlags: number, callback: AsyncCallback<ApplicationInfo>): void
```

Obtains the application information based on a given bundle name. This API uses an asynchronous callback to return the result. No permission is required for obtaining the caller's own information.

**Since:** 7

**Deprecated since:** 9

**Required permissions:** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED or ohos.permission.GET_BUNDLE_INFO

<!--Device-bundle-function getApplicationInfo(bundleName: string, bundleFlags: number, callback: AsyncCallback<ApplicationInfo>): void--><!--Device-bundle-function getApplicationInfo(bundleName: string, bundleFlags: number, callback: AsyncCallback<ApplicationInfo>): void-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |
| bundleFlags | number | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[ApplicationInfo](arkts-ability-applicationinfo-applicationinfo-depr-i.md)&gt; | Yes |


## getApplicationInfo

```TypeScript
function getApplicationInfo(bundleName: string, bundleFlags: number, userId?: number): Promise<ApplicationInfo>
```

Obtains the application information based on a given bundle name. This API uses a promise to return the result. No permission is required for obtaining the caller's own information.

**Since:** 7

**Deprecated since:** 9

**Required permissions:** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED or ohos.permission.GET_BUNDLE_INFO

<!--Device-bundle-function getApplicationInfo(bundleName: string, bundleFlags: number, userId?: number): Promise<ApplicationInfo>--><!--Device-bundle-function getApplicationInfo(bundleName: string, bundleFlags: number, userId?: number): Promise<ApplicationInfo>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |
| bundleFlags | number | Yes |
| userId | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[ApplicationInfo](arkts-ability-applicationinfo-applicationinfo-depr-i.md)&gt; |
