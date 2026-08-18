# transcode

## Modules to Import

```TypeScript
```

## transcode

```TypeScript
function transcode(source: Buffer | Uint8Array, fromEnc: string, toEnc: string): Buffer
```

Transcodes a **Buffer** or **Uint8Array** object from one encoding format to another.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-buffer-function transcode(source: Buffer | Uint8Array, fromEnc: string, toEnc: string): Buffer--><!--Device-buffer-function transcode(source: Buffer | Uint8Array, fromEnc: string, toEnc: string): Buffer-End-->

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| source | [Buffer](arkts-arkts-buffer-buffer-c.md) \| Uint8Array | Yes |
| fromEnc | string | Yes |
| toEnc | string | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| [Buffer](arkts-arkts-buffer-buffer-c.md) |

**Examples**

```TypeScript
import { buffer } from '@kit.ArkTS';

let newBuf = buffer.transcode(buffer.from('€'), 'utf-8', 'ascii');
console.info("newBuf = " + newBuf.toString('ascii'));
// Output: newBuf = ,
```
