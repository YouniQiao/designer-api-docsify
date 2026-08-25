# byteLength

## Modules to Import

```TypeScript
import { buffer } from 'kits/@kit.ArkTS';
```

## byteLength

```TypeScript
function byteLength(
    string: string | Buffer | TypedArray | DataView | ArrayBuffer | SharedArrayBuffer,
    encoding?: BufferEncoding
  ): number
```

Obtains the number of bytes of a string based on the encoding format.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| string | string \| Buffer \| TypedArray \| DataView \| ArrayBuffer \| SharedArrayBuffer | Yes |
| encoding | BufferEncoding | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| number |
