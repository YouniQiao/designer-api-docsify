# getDynamicIcon (System API)

## Modules to Import

```TypeScript
import { bundleManager } from '@kit.AbilityKit';
```

## getDynamicIcon

```TypeScript
function getDynamicIcon(bundleName: string): Promise<string>
```

Obtains the module name corresponding to the dynamic icon based on the specified bundle name. This API uses a promise to return the result.

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.GET_BUNDLE_INFO_PRIVILEGED or ohos.permission.GET_BUNDLE_INFO

<!--Device-bundleManager-function getDynamicIcon(bundleName: string): Promise<string>--><!--Device-bundleManager-function getDynamicIcon(bundleName: string): Promise<string>-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| bundleName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [17700306](../errorcode-bundle.md#17700306-failed-to-obtain-the-dynamic-icon) |
| [17700001](../errorcode-bundle.md#17700001-bundle-name-does-not-exist) |

## Examples

```TypeScript
import { bundleManager } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let bundleName: string = 'com.ohos.demo';

try {
  bundleManager.getDynamicIcon(bundleName).then((data) => {
    hilog.info(0x0000, 'testTag', 'getDynamicIcon successfully %{public}s', JSON.stringify(data));
  }).catch((err: BusinessError) => {
    hilog.error(0x0000, 'testTag', 'getDynamicIcon failed. Cause: %{public}s', err.message);
  });
} catch (err) {
  let message = (err as BusinessError).message;
  hilog.error(0x0000, 'testTag', 'getDynamicIcon failed. Cause: %{public}s', message);
}
```
