# byteLength

## Modules to Import

```TypeScript
import { fastbuffer } from 'kits/@kit.ArkTS';
```

## byteLength

```TypeScript
function byteLength(value: string | FastBuffer | TypedArray | DataView | ArrayBuffer | SharedArrayBuffer, encoding?: BufferEncoding): number
```

Returns the byte length of a string when encoded using `encoding`. This is not the same as [`String.prototype.length`], which does not account for the encoding that is used to convert the string into bytes.

**Since:** 20

**Atomic service API:** This API can be used in atomic services since API version 20.

**System capability:** SystemCapability.Utils.Lang

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | string \| [FastBuffer](arkts-arkts-fastbuffer-fastbuffer-c.md) \| TypedArray \| DataView \| ArrayBuffer \| SharedArrayBuffer | Yes |
| encoding | BufferEncoding | No |

**Return value:**

| [Type](arkts-arkts-util-type-e.md) |
| --- |
| number |
