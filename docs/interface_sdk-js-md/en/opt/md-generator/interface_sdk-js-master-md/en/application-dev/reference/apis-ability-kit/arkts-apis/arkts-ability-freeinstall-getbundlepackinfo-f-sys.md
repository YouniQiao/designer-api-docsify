# getBundlePackInfo (System API)

## Modules to Import

```TypeScript
import { freeInstall } from '@kit.AbilityKit';
```

## getBundlePackInfo

```TypeScript
function getBundlePackInfo(bundleName: string, 
    bundlePackFlag : BundlePackFlag, callback: AsyncCallback<BundlePackInfo>): void
```

Obtains bundlePackInfo based on **bundleName** and **bundlePackFlag**. This API uses an asynchronous callback to return the result.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

<!--Device-freeInstall-function getBundlePackInfo(bundleName: string,     bundlePackFlag : BundlePackFlag, callback: AsyncCallback<BundlePackInfo>): void--><!--Device-freeInstall-function getBundlePackInfo(bundleName: string,     bundlePackFlag : BundlePackFlag, callback: AsyncCallback<BundlePackInfo>): void-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.FreeInstall

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |
| bundlePackFlag | [BundlePackFlag](arkts-ability-freeinstall-bundlepackflag-e-sys.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;BundlePackInfo&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [17700001](../errorcode-bundle.md#17700001-bundle-name-does-not-exist) |


## getBundlePackInfo

```TypeScript
function getBundlePackInfo(bundleName: string, bundlePackFlag : BundlePackFlag): Promise<BundlePackInfo>
```

Obtains bundlePackInfo based on **bundleName** and **bundlePackFlag**. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

<!--Device-freeInstall-function getBundlePackInfo(bundleName: string, bundlePackFlag : BundlePackFlag): Promise<BundlePackInfo>--><!--Device-freeInstall-function getBundlePackInfo(bundleName: string, bundlePackFlag : BundlePackFlag): Promise<BundlePackInfo>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.FreeInstall

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |
| bundlePackFlag | [BundlePackFlag](arkts-ability-freeinstall-bundlepackflag-e-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;BundlePackInfo & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [17700001](../errorcode-bundle.md#17700001-bundle-name-does-not-exist) |
