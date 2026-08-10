# HashStream

HashStream 类是用于创建数据的哈希摘要的实用工具。由 [createHash](arkts-corefile-hash-createhash-f.md#createhash) 接口获得。

**Inheritance/Implementation:** HashStream extends [stream.Transform](../../apis-arkts/arkts-apis/arkts-arkts-stream-transform-c.md/arkts-arkts-stream-transform-c.md)

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

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

计算传递给哈希处理的所有数据的摘要。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-HashStream-digest(): string--><!--Device-HashStream-digest(): string-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Return value:**

| Type | Description |
| --- | --- |
| string | 返回数据的哈希值。该哈希值表示为十六进制数字串，所有字母均大写。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error |
| 13900042 | Unknown error |

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

使用给定的 data 更新哈希内容，可多次调用。

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-HashStream-update(data: ArrayBuffer): void--><!--Device-HashStream-update(data: ArrayBuffer): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | ArrayBuffer | Yes | updated data. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error |
| 13900042 | Unknown error |

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

