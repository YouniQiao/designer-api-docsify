# HashStream

The **HashStream** class is a utility for creating a message digest of data. You can use  
[createHash](../../../reference/apis-core-file-kit/js-apis-file-hash.md#hashcreatehash12) to create a  
**HashStream** instance.

**Inheritance/Implementation:** HashStream extends [stream.Transform](../../apis-arkts/arkts-apis/arkts-arkts-stream-transform-c.md/arkts-arkts-stream-transform-c.md)

**Since:** 12

<!--Device-hash-class HashStream extends stream.Transform--><!--Device-hash-class HashStream extends stream.Transform-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

## Modules to Import

```TypeScript
import { hash } from 'kits/@kit.CoreFileKit';
```

## digest

```TypeScript
digest(): string
```

Generates a message digest.

**Since:** 12

<!--Device-HashStream-digest(): string--><!--Device-HashStream-digest(): string-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| 13900042 |

## Examples

```TypeScript
// Create a hash stream.
const hs = hash.createHash('sha256');
hs.update(new Uint8Array('1234567890'?.split('').map((x: string) => x.charCodeAt(0))).buffer);
hs.update(new Uint8Array('abcdefg'?.split('').map((x: string) => x.charCodeAt(0))).buffer);
const hashResult = hs.digest();
// 88A00F46836CD629D0B79DE98532AFDE3AEAD79A5C53E4848102F433046D0106
console.info(`hashResult: ${hashResult}`);
```

## update

```TypeScript
update(data: ArrayBuffer): void
```

Updates the data for generating a message digest. This API can be called multiple times.

**Since:** 12

<!--Device-HashStream-update(data: ArrayBuffer): void--><!--Device-HashStream-update(data: ArrayBuffer): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| data | ArrayBuffer | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| 13900042 |

## Examples

```TypeScript
// Create a hash stream.
const hs = hash.createHash('sha256');
hs.update(new Uint8Array('1234567890'?.split('').map((x: string) => x.charCodeAt(0))).buffer);
hs.update(new Uint8Array('abcdefg'?.split('').map((x: string) => x.charCodeAt(0))).buffer);
const hashResult = hs.digest();
// 88A00F46836CD629D0B79DE98532AFDE3AEAD79A5C53E4848102F433046D0106
console.info(`hashResult: ${hashResult}`);
```
