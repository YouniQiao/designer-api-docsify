# getSysResourceManager

## Modules to Import

```TypeScript
import { resourceManager } from 'kits/@kit.LocalizationKit';
```

## getSysResourceManager

```TypeScript
export function getSysResourceManager(): ResourceManager
```

Obtains a system resource management object for accessing preset system resources.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-resourceManager-export function getSysResourceManager(): ResourceManager--><!--Device-resourceManager-export function getSysResourceManager(): ResourceManager-End-->

**System capability:** SystemCapability.Global.ResourceManager

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ResourceManager](arkts-localization-resourcemanager-resourcemanager-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [9001009](../errorcode-resource-manager.md#9001009-failed-to-obtain-the-system-resource-management-object) |

## Examples

```TypeScript
import { resourceManager } from '@kit.LocalizationKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let systemResourceManager = resourceManager.getSysResourceManager();
  // Replace 'sys.string.ohos_lab_vibrate' with the actual resource.
  systemResourceManager.getStringValue($r('sys.string.ohos_lab_vibrate').id).then((value: string) => {
    let str = value;
  }).catch((error: BusinessError) => {
    console.error(`systemResourceManager getStringValue promise error: ${error}`);
  });
} catch (error) {
  let code = (error as BusinessError).code;
  let message = (error as BusinessError).message;
  console.error(`getSysResourceManager failed, error code: ${code}, message: ${message}.`);
}
```
