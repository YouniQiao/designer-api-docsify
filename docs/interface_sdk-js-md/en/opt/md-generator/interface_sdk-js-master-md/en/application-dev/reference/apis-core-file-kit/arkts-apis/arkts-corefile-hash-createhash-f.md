# createHash

## Modules to Import

```TypeScript
import { hash } from 'kits/@kit.CoreFileKit';
```

## createHash

```TypeScript
function createHash(algorithm: string): HashStream
```

Creates a **HashStream** instance, which can be used to generate a message digest (a hash value) using the given algorithm.

**Since:** 12

<!--Device-hash-function createHash(algorithm: string): HashStream--><!--Device-hash-function createHash(algorithm: string): HashStream-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| algorithm | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [HashStream](arkts-corefile-hash-hashstream-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| 13900042 |

## Examples

```TypeScript
// pages/xxx.ets
import { fileIo } from '@kit.CoreFileKit';

function hashFileWithStream() {
  const filePath = pathDir + "/test.txt";
  // Create a readable stream.
  const rs = fileIo.createReadStream(filePath);
  // Create a hash stream.
  const hs = hash.createHash('sha256');
  rs.on('data', (emitData) => {
    const data = emitData?.data;
    hs.update(new Uint8Array(data?.split('').map((x: string) => x.charCodeAt(0))).buffer);
  });
  rs.on('close', async () => {
    const hashResult = hs.digest();
    const fileHash = await hash.hash(filePath, 'sha256');
    console.info(`hashResult: ${hashResult}, fileHash: ${fileHash}`);
  });
}
```
