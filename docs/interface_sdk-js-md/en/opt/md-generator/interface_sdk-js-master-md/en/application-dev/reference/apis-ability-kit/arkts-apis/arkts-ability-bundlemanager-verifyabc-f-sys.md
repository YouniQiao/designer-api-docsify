# verifyAbc (System API)

## Modules to Import

```TypeScript
import { bundleManager } from '@kit.AbilityKit';
```

## verifyAbc

```TypeScript
function verifyAbc(abcPaths: Array<string>, deleteOriginalFiles: boolean, callback: AsyncCallback<void>): void
```

Verifies an .abc file. This API uses an asynchronous callback to return the result.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.RUN_DYN_CODE

<!--Device-bundleManager-function verifyAbc(abcPaths: Array<string>, deleteOriginalFiles: boolean, callback: AsyncCallback<void>): void--><!--Device-bundleManager-function verifyAbc(abcPaths: Array<string>, deleteOriginalFiles: boolean, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| abcPaths | Array & lt;string & gt; | Yes |
| deleteOriginalFiles | boolean | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17700201](../errorcode-bundle.md#17700201-abc-file-verification-failure) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { bundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let abcPaths: Array<string> = ['/data/storage/el2/base/a.abc'];

try {
  bundleManager.verifyAbc(abcPaths, true, (err, data) => {
    if (err) {
      hilog.error(0x0000, 'testTag', 'verifyAbc failed: %{public}s', err.message);
    } else {
      hilog.info(0x0000, 'testTag', 'verifyAbc successfully');
    }
  });
} catch (err) {
  let message = (err as BusinessError).message;
  hilog.error(0x0000, 'testTag', 'verifyAbc failed: %{public}s', message);
}
```


## verifyAbc

```TypeScript
function verifyAbc(abcPaths: Array<string>, deleteOriginalFiles: boolean): Promise<void>
```

Verifies an .abc file. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.RUN_DYN_CODE

<!--Device-bundleManager-function verifyAbc(abcPaths: Array<string>, deleteOriginalFiles: boolean): Promise<void>--><!--Device-bundleManager-function verifyAbc(abcPaths: Array<string>, deleteOriginalFiles: boolean): Promise<void>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| abcPaths | Array & lt;string & gt; | Yes |
| deleteOriginalFiles | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [17700201](../errorcode-bundle.md#17700201-abc-file-verification-failure) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { bundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let abcPaths: Array<string> = ['/data/storage/el2/base/a.abc'];

try {
  bundleManager.verifyAbc(abcPaths, true).then((data) => {
    hilog.info(0x0000, 'testTag', 'verifyAbc successfully');
  }).catch((err: BusinessError) => {
    hilog.error(0x0000, 'testTag', 'verifyAbc failed. Cause: %{public}s', err.message);
  });
} catch (err) {
  let message = (err as BusinessError).message;
  hilog.error(0x0000, 'testTag', 'verifyAbc failed. Cause: %{public}s', message);
}
```
