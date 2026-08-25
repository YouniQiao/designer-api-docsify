# hash

## Modules to Import

```TypeScript
```

## hash

```TypeScript
declare function hash(path: string, algorithm: string): Promise<string>
```

Calculates the hash value of a file. This API uses a promise to return the result.

**Since:** 6

**ArkTS mode:** Supports only ArkTS-Dyn, since version 6.

**Deprecated since:** 9

**Substitutes:** [hash](arkts-file-hash.md)

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | string | Yes |
| [algorithm](../../apis-device-certificate-kit/arkts-apis/arkts-devicecertificate-cert-certchainvalidator-i.md) | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

**Examples**

```TypeScript
import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
fileio.hash(filePath, "sha256").then((str: string) => {
  console.info("calculate file hash succeed:" + str);
}).catch((err: BusinessError) => {
  console.error("calculate file hash failed with error:" + err);
});
```

```TypeScript
import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
fileio.hash(filePath, "sha256", (err: BusinessError, hashStr: string) => {
  if (hashStr) {
    console.info("calculate file hash succeed:" + hashStr);
  }
});
```


## hash

```TypeScript
declare function hash(path: string, algorithm: string, callback: AsyncCallback<string>): void
```

Calculates the hash value of a file. This API uses an asynchronous callback to return the result.

**Since:** 6

**ArkTS mode:** Supports only ArkTS-Dyn, since version 6.

**Deprecated since:** 9

**Substitutes:** [hash](arkts-file-hash.md)

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| path | string | Yes |
| [algorithm](../../apis-device-certificate-kit/arkts-apis/arkts-devicecertificate-cert-certchainvalidator-i.md) | string | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes |

**Examples**

See [hash](#hash)
