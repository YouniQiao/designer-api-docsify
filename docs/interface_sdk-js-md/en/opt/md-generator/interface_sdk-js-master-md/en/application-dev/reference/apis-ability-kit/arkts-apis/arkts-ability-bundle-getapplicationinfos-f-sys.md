# getApplicationInfos (System API)

## Modules to Import

```TypeScript
import { bundle } from 'kits/@kit.AbilityKit';
```

## getApplicationInfos

```TypeScript
function getApplicationInfos(bundleFlags: number, userId: number, callback: AsyncCallback<Array<ApplicationInfo>>): void
```

Obtains information about all installed apps for a specified user. This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 8

**Substitutes:** ohos.bundle.bundleManager#getAllApplicationInfo

**Required permissions:** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

<!--Device-bundle-function getApplicationInfos(bundleFlags: number, userId: number, callback: AsyncCallback<Array<ApplicationInfo>>): void--><!--Device-bundle-function getApplicationInfos(bundleFlags: number, userId: number, callback: AsyncCallback<Array<ApplicationInfo>>): void-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleFlags | number | Yes |
| userId | number | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[ApplicationInfo](arkts-ability-applicationinfo-applicationinfo-depr-i.md)&gt;&gt; | Yes |

## Examples

```TypeScript
import bundle from '@ohos.bundle';

let bundleFlags: number = bundle.BundleFlag.GET_APPLICATION_INFO_WITH_PERMISSION;
let userId: number = 100;

bundle.getApplicationInfos(bundleFlags, userId, (err, data) => {
  if (err) {
    console.error('Operation failed. Cause: ' + JSON.stringify(err));
    return;
  }
  console.info('Operation successful. Data:' + JSON.stringify(data));
})
```


## getApplicationInfos

```TypeScript
function getApplicationInfos(bundleFlags: number, callback: AsyncCallback<Array<ApplicationInfo>>): void
```

Obtains information about installed apps for the user to which the caller belongs.This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 8

**Substitutes:** ohos.bundle.bundleManager#getAllApplicationInfo

**Required permissions:** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

<!--Device-bundle-function getApplicationInfos(bundleFlags: number, callback: AsyncCallback<Array<ApplicationInfo>>): void--><!--Device-bundle-function getApplicationInfos(bundleFlags: number, callback: AsyncCallback<Array<ApplicationInfo>>): void-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleFlags | number | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[ApplicationInfo](arkts-ability-applicationinfo-applicationinfo-depr-i.md)&gt;&gt; | Yes |

## Examples

```TypeScript
import bundle from '@ohos.bundle';

let bundleFlags: number = bundle.BundleFlag.GET_APPLICATION_INFO_WITH_PERMISSION;

bundle.getApplicationInfos(bundleFlags, (err, data) => {
  if (err) {
    console.error('Operation failed. Cause: ' + JSON.stringify(err));
    return;
  }
  console.info('Operation successful. Data:' + JSON.stringify(data));
})
```


## getApplicationInfos

```TypeScript
function getApplicationInfos(bundleFlags: number, userId?: number): Promise<Array<ApplicationInfo>>
```

Obtains information about all installed apps for a specified user. This API uses a promise to return the result.

**Since:** 7

**Deprecated since:** 8

**Substitutes:** ohos.bundle.bundleManager#getAllApplicationInfo

**Required permissions:** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

<!--Device-bundle-function getApplicationInfos(bundleFlags: number, userId?: number): Promise<Array<ApplicationInfo>>--><!--Device-bundle-function getApplicationInfos(bundleFlags: number, userId?: number): Promise<Array<ApplicationInfo>>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleFlags | number | Yes |
| userId | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[ApplicationInfo](arkts-ability-applicationinfo-applicationinfo-depr-i.md)&gt;&gt; |

## Examples

```TypeScript
import bundle from '@ohos.bundle';
import { BusinessError } from '@ohos.base';

let bundleFlags: number = bundle.BundleFlag.GET_APPLICATION_INFO_WITH_PERMISSION;
let userId: number = 100;

bundle.getApplicationInfos(bundleFlags, userId)
  .then((data) => {
    console.info('Operation successful. Data: ' + JSON.stringify(data));
  }).catch((error: BusinessError) => {
    console.error('Operation failed. Cause: ' + JSON.stringify(error));
  })
```
