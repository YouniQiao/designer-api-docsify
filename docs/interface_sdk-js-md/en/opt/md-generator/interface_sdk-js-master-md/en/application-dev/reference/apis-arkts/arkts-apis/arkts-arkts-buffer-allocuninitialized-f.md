# allocUninitialized

## Modules to Import

```TypeScript
```

## allocUninitialized

```TypeScript
function allocUninitialized(size: number): Buffer
```

Creates a **Buffer** object of the specified size, without initializing it. This API does not allocate memory from the buffer pool. You need to use [fill()](arkts-arkts-buffer-buffer-c.md#fill) to initialize the **Buffer** object created.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-buffer-function allocUninitialized(size: int): Buffer--><!--Device-buffer-function allocUninitialized(size: int): Buffer-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| size | number | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Buffer](arkts-arkts-buffer-buffer-c.md) |

**Examples**

```TypeScript
import { buffer, JSON } from '@kit.ArkTS';

let buf = buffer.allocUninitialized(10);
buf.fill(0);
console.info(JSON.stringify(buf)); // {"type":"Buffer","data":[0,0,0,0,0,0,0,0,0,0]}
```
