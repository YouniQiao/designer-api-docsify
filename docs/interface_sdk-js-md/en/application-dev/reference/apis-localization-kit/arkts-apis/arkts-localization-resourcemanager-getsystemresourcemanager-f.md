# getSystemResourceManager

## Modules to Import

```TypeScript
import { resourceManager } from 'kits/@kit.LocalizationKit';
```

## getSystemResourceManager

```TypeScript
export function getSystemResourceManager(): ResourceManager
```

获取系统资源管理对象，用于访问系统预置的资源。

> **说明：**
> 
> 该接口获取到的系统资源管理ResourceManager对象中的Configuration为默认值。默认值如下：{"locale": "", "direction": -1, "deviceType": -1, "
> screenDensity": 0, "colorMode": 1, "mcc": 0, "mnc": 0}。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** 20

**Substitutes:** [resourceManager.getSysResourceManager](arkts-localization-resourcemanager-getsysresourcemanager-f.md#getsysresourcemanager)

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-resourceManager-export function getSystemResourceManager(): ResourceManager--><!--Device-resourceManager-export function getSystemResourceManager(): ResourceManager-End-->

**System capability:** SystemCapability.Global.ResourceManager

**Return value:**

| Type | Description |
| --- | --- |
| [ResourceManager](arkts-localization-resourcemanager-resourcemanager-i.md) | 系统资源管理对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 9001009 | Failed to access the system resource. which is not mapped to application sandbox, This error code will be thrown. |

## Examples

```TypeScript
import { resourceManager } from '@kit.LocalizationKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let systemResourceManager = resourceManager.getSystemResourceManager();
  systemResourceManager.getStringValue($r('sys.string.ohos_lab_vibrate').id).then((value: string) => {
    let str = value;
  }).catch((error: BusinessError) => {
    console.error("systemResourceManager getStringValue promise error is " + error);
  });
} catch (error) {
  let code = (error as BusinessError).code;
  let message = (error as BusinessError).message;
  console.error(`getSystemResourceManager failed, error code: ${code}, message: ${message}.`);
}
```

