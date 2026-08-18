# allocUninitialized

## Modules to Import

```TypeScript
```

## allocUninitialized

```TypeScript
function allocUninitialized(size: number): FastBuffer
```

Allocates a new un-pooled FastBuffer for a fixed size bytes. The FastBuffer will not be initially filled.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-fastbuffer-function allocUninitialized(size: number): FastBuffer--><!--Device-fastbuffer-function allocUninitialized(size: number): FastBuffer-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| size | number | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [FastBuffer](arkts-arkts-fastbuffer-fastbuffer-c.md) |

**Examples**

```TypeScript
import { fastbuffer } from '@kit.ArkTS';

let buf = fastbuffer.allocUninitialized(10);
buf.fill(0);
// "buf":[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
```
