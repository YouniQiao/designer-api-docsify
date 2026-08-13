# getSharedBundleInfo (System API)

## Modules to Import

```TypeScript
import { bundleManager } from '@kit.AbilityKit';
```

## getSharedBundleInfo

```TypeScript
function getSharedBundleInfo(bundleName: string,  moduleName: string, callback: AsyncCallback<Array<SharedBundleInfo>>): void
```

Obtains the shared bundle information based on the given bundle name. This API uses an asynchronous callback to return the result. No permission is required for obtaining the caller's own information.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

<!--Device-bundleManager-function getSharedBundleInfo(bundleName: string,  moduleName: string, callback: AsyncCallback<Array<SharedBundleInfo>>): void--><!--Device-bundleManager-function getSharedBundleInfo(bundleName: string,  moduleName: string, callback: AsyncCallback<Array<SharedBundleInfo>>): void-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |
| moduleName | string | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;SharedBundleInfo&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [17700002](../errorcode-bundle.md#17700002-module-name-does-not-exist) |
| [17700001](../errorcode-bundle.md#17700001-bundle-name-does-not-exist) |

## Examples

```TypeScript
import { bundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let bundleName = 'com.example.myapplication';
let moduleName = 'library';

try {
  bundleManager.getSharedBundleInfo(bundleName, moduleName, (err, data) => {
    if (err) {
      hilog.error(0x0000, 'testTag', 'getSharedBundleInfo failed: %{public}s', err.message);
    } else {
      hilog.info(0x0000, 'testTag', 'getSharedBundleInfo successfully: %{public}s', JSON.stringify(data));
    }
  });
} catch (err) {
  let message = (err as BusinessError).message;
  hilog.error(0x0000, 'testTag', 'getSharedBundleInfo failed: %{public}s', message);
}
```


## getSharedBundleInfo

```TypeScript
function getSharedBundleInfo(bundleName: string, moduleName: string): Promise<Array<SharedBundleInfo>>
```

Obtains the shared bundle information based on the given bundle name. This API uses a promise to return the result. No permission is required for obtaining the caller's own information.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

<!--Device-bundleManager-function getSharedBundleInfo(bundleName: string, moduleName: string): Promise<Array<SharedBundleInfo>>--><!--Device-bundleManager-function getSharedBundleInfo(bundleName: string, moduleName: string): Promise<Array<SharedBundleInfo>>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |
| moduleName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Array & lt;SharedBundleInfo & gt; & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [17700002](../errorcode-bundle.md#17700002-module-name-does-not-exist) |
| [17700001](../errorcode-bundle.md#17700001-bundle-name-does-not-exist) |

## Examples

```TypeScript
import { bundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let bundleName = 'com.example.myapplication';
let moduleName = 'library';

try {
  bundleManager.getSharedBundleInfo(bundleName, moduleName).then((data) => {
    hilog.info(0x0000, 'testTag', 'getSharedBundleInfo successfully. Data: %{public}s', JSON.stringify(data));
  }).catch((err: BusinessError) => {
    hilog.error(0x0000, 'testTag', 'getSharedBundleInfo failed. Cause: %{public}s', err.message);
  });
} catch (err) {
  let message = (err as BusinessError).message;
  hilog.error(0x0000, 'testTag', 'getSharedBundleInfo failed. Cause: %{public}s', message);
}
```
