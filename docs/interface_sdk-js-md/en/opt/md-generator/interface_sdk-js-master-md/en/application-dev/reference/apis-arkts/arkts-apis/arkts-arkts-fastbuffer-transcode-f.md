# transcode

## Modules to Import

```TypeScript
import { fastbuffer } from 'kits/@kit.ArkTS';
```

## transcode

```TypeScript
function transcode(source: FastBuffer | Uint8Array, fromEnc: string, toEnc: string): FastBuffer
```

Re-encodes the given FastBuffer or Uint8Array instance from one character encoding to another.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

<!--Device-fastbuffer-function transcode(source: FastBuffer | Uint8Array, fromEnc: string, toEnc: string): FastBuffer--><!--Device-fastbuffer-function transcode(source: FastBuffer | Uint8Array, fromEnc: string, toEnc: string): FastBuffer-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| source | [FastBuffer](arkts-arkts-fastbuffer-fastbuffer-c.md) \| Uint8Array | Yes |
| fromEnc | string | Yes |
| toEnc | string | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [FastBuffer](arkts-arkts-fastbuffer-fastbuffer-c.md) |

## Examples

```TypeScript
import { fastbuffer } from '@kit.ArkTS';

let newBuf = fastbuffer.transcode(fastbuffer.from('buffer'), 'utf-8', 'ascii');
console.info("newBuf = " + newBuf.toString('ascii'));
// Output: newBuf = buffer
```
