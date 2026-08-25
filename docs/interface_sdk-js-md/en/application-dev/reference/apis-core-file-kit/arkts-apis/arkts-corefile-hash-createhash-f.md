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

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [algorithm](../../apis-device-certificate-kit/arkts-apis/arkts-devicecertificate-cert-certchainvalidator-i.md) | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [HashStream](arkts-corefile-hash-hashstream-c.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| 13900020 |
| 13900042 |
