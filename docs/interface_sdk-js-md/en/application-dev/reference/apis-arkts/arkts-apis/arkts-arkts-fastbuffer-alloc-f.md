# alloc

## Modules to Import

```TypeScript
import { fastbuffer } from 'kits/@kit.ArkTS';
```

## alloc

```TypeScript
function alloc(size: number, fill?: string | FastBuffer | number, encoding?: BufferEncoding): FastBuffer
```

Allocates a new FastBuffer for a fixed size bytes. If fill is undefined, the FastBuffer will be zero-filled.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| size | number | Yes |
| fill | string \| [FastBuffer](arkts-arkts-fastbuffer-fastbuffer-c.md) \| number | No |
| encoding | BufferEncoding | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [FastBuffer](arkts-arkts-fastbuffer-fastbuffer-c.md) |
