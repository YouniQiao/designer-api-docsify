# transcode

## Modules to Import

```TypeScript
import { buffer } from '@kit.ArkTS';
```

## transcode

```TypeScript
function transcode(source: Buffer | Uint8Array, fromEnc: string, toEnc: string): Buffer
```

Transcodes a **Buffer** or **Uint8Array** object from one encoding format to another.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn since version 9; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| source | Buffer \| Uint8Array | Yes |
| fromEnc | string | Yes |
| toEnc | string | Yes |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| Buffer |

**Examples**

```TypeScript
import { buffer } from '@kit.ArkTS';

let newBuf = buffer.transcode(buffer.from('€'), 'utf-8', 'ascii');
console.info("newBuf = " + newBuf.toString('ascii'));
// Output: newBuf = ,
```
