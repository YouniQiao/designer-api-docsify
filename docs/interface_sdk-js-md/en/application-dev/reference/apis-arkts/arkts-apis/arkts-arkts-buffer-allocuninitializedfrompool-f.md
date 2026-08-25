# allocUninitializedFromPool

## Modules to Import

```TypeScript
import { buffer } from 'kits/@kit.ArkTS';
```

## allocUninitializedFromPool

```TypeScript
function allocUninitializedFromPool(size: number): Buffer
```

Creates a **Buffer** object of the specified size from the buffer pool, without initializing it. You need to use [fill()](arkts-arkts-buffer-buffer-c.md#fill) to initialize the **Buffer** object created.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| size | number | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Buffer |
