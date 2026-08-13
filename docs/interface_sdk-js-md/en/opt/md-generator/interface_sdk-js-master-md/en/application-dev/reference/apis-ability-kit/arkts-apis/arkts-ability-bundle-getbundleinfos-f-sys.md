# getBundleInfos (System API)

## Modules to Import

```TypeScript
import { bundle } from '@kit.AbilityKit';
```

## getBundleInfos

```TypeScript
function getBundleInfos(bundleFlag: BundleFlag, userId: number, callback: AsyncCallback<Array<BundleInfo>>): void
```

Obtains all BundleInfo for a specified user in the system. This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 8

**Substitutes:** getAllBundleInfo

**Required permissions:** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

<!--Device-bundle-function getBundleInfos(bundleFlag: BundleFlag, userId: number, callback: AsyncCallback<Array<BundleInfo>>): void--><!--Device-bundle-function getBundleInfos(bundleFlag: BundleFlag, userId: number, callback: AsyncCallback<Array<BundleInfo>>): void-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleFlag | [BundleFlag](arkts-ability-bundle-bundleflag-e.md) | Yes |
| userId | number | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[BundleInfo](arkts-ability-bundleinfo-bundleinfo-depr-i.md)&gt;&gt; | Yes |

## Examples

```TypeScript
import bundle from '@ohos.bundle';

let bundleFlag: number = bundle.BundleFlag.GET_BUNDLE_DEFAULT;
let userId: number = 100;

bundle.getBundleInfos(bundleFlag, userId, (err, data) => {
  if (err) {
    console.error('Operation failed. Cause: ' + JSON.stringify(err));
    return;
  }
  console.info('Operation successful. Data:' + JSON.stringify(data));
})
```


## getBundleInfos

```TypeScript
function getBundleInfos(bundleFlag: BundleFlag, callback: AsyncCallback<Array<BundleInfo>>): void
```

Obtains all BundleInfo for the current user. This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 8

**Substitutes:** getAllBundleInfo

**Required permissions:** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

<!--Device-bundle-function getBundleInfos(bundleFlag: BundleFlag, callback: AsyncCallback<Array<BundleInfo>>): void--><!--Device-bundle-function getBundleInfos(bundleFlag: BundleFlag, callback: AsyncCallback<Array<BundleInfo>>): void-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleFlag | [BundleFlag](arkts-ability-bundle-bundleflag-e.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[BundleInfo](arkts-ability-bundleinfo-bundleinfo-depr-i.md)&gt;&gt; | Yes |

## Examples

```TypeScript
import bundle from '@ohos.bundle';

let bundleFlag: number = bundle.BundleFlag.GET_BUNDLE_DEFAULT;

bundle.getBundleInfos(bundleFlag, (err, data) => {
  if (err) {
    console.error('Operation failed. Cause: ' + JSON.stringify(err));
    return;
  }
  console.info('Operation successful. Data:' + JSON.stringify(data));
})
```


## getBundleInfos

```TypeScript
function getBundleInfos(bundleFlag: BundleFlag, userId?: number): Promise<Array<BundleInfo>>
```

Obtains all BundleInfo for a specified user. This API uses a promise to return the result.

**Since:** 7

**Deprecated since:** 8

**Substitutes:** getAllBundleInfo

**Required permissions:** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

<!--Device-bundle-function getBundleInfos(bundleFlag: BundleFlag, userId?: number): Promise<Array<BundleInfo>>--><!--Device-bundle-function getBundleInfos(bundleFlag: BundleFlag, userId?: number): Promise<Array<BundleInfo>>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleFlag | [BundleFlag](arkts-ability-bundle-bundleflag-e.md) | Yes |
| userId | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[BundleInfo](arkts-ability-bundleinfo-bundleinfo-depr-i.md)&gt;&gt; |

## Examples

```TypeScript
import bundle from '@ohos.bundle';
import { BusinessError } from '@ohos.base';

let bundleFlag: number = bundle.BundleFlag.GET_BUNDLE_DEFAULT;
let userId: number = 100;

bundle.getBundleInfos(bundleFlag, userId)
  .then((data) => {
    console.info('Operation successful. Data: ' + JSON.stringify(data));
  }).catch((error: BusinessError) => {
    console.error('Operation failed. Cause: ' + JSON.stringify(error));
  })
```
