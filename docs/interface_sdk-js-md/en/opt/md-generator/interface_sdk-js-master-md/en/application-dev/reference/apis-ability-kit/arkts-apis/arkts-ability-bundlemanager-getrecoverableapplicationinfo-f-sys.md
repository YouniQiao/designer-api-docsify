# getRecoverableApplicationInfo (System API)

## Modules to Import

```TypeScript
import { bundleManager } from '@kit.AbilityKit';
```

## getRecoverableApplicationInfo

```TypeScript
function getRecoverableApplicationInfo(callback: AsyncCallback<Array<RecoverableApplicationInfo>>): void
```

Obtains information about all preinstalled applications that can be restored. This API uses an asynchronous callback to return the result.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

<!--Device-bundleManager-function getRecoverableApplicationInfo(callback: AsyncCallback<Array<RecoverableApplicationInfo>>): void--><!--Device-bundleManager-function getRecoverableApplicationInfo(callback: AsyncCallback<Array<RecoverableApplicationInfo>>): void-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;RecoverableApplicationInfo&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { bundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  bundleManager.getRecoverableApplicationInfo((err, data) => {
    if (err) {
      hilog.error(0x0000, 'testTag', 'getRecoverableApplicationInfo failed: %{public}s', err.message);
    } else {
      hilog.info(0x0000, 'testTag', 'getRecoverableApplicationInfo successfully: %{public}s', JSON.stringify(data));
    }
  });
} catch (err) {
  let message = (err as BusinessError).message;
  hilog.error(0x0000, 'testTag', 'getRecoverableApplicationInfo failed: %{public}s', message);
}
```


## getRecoverableApplicationInfo

```TypeScript
function getRecoverableApplicationInfo(): Promise<Array<RecoverableApplicationInfo>>
```

Obtains information about all preinstalled applications that can be restored. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED

<!--Device-bundleManager-function getRecoverableApplicationInfo(): Promise<Array<RecoverableApplicationInfo>>--><!--Device-bundleManager-function getRecoverableApplicationInfo(): Promise<Array<RecoverableApplicationInfo>>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Array & lt;RecoverableApplicationInfo & gt; & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { bundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  bundleManager.getRecoverableApplicationInfo().then((data) => {
    hilog.info(0x0000, 'testTag', 'getRecoverableApplicationInfo successfully: %{public}s', JSON.stringify(data));
  }).catch((err: BusinessError) => {
    hilog.error(0x0000, 'testTag', 'getRecoverableApplicationInfo failed: %{public}s', err.message);
  });
} catch (err) {
  let message = (err as BusinessError).message;
  hilog.error(0x0000, 'testTag', 'getRecoverableApplicationInfo failed: %{public}s', message);
}
```
