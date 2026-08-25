# getSystemResourceManager

## Modules to Import

```TypeScript
import { resourceManager } from 'kits/@kit.LocalizationKit';
```

## getSystemResourceManager

```TypeScript
export function getSystemResourceManager(): ResourceManager
```

Obtains a system resource management object for accessing preset system resources.

> **NOTE：**&gt;
> The **Configuration** parameter in the **ResourceManager** object obtained via this API uses the default value.
> The default value is
> **{"locale": "", "direction": -1, "deviceType": -1, "screenDensity": 0, "colorMode": 1, "mcc": 0, "mnc": 0}**.

**Since:** 10

**Deprecated since:** 20

**Substitutes:** [getSysResourceManager](arkts-localization-resourcemanager-getsysresourcemanager-f.md)

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Global.ResourceManager

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [ResourceManager](arkts-localization-resourcemanager-resourcemanager-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [9001009](../errorcode-resource-manager.md#9001009-failed-to-obtain-the-system-resource-management-object) |
