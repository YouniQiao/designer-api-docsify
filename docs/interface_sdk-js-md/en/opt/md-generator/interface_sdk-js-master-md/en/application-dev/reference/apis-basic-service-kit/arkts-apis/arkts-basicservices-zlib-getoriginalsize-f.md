# getOriginalSize

## Modules to Import

```TypeScript
import { zlib } from 'kits/@kit.BasicServicesKit';
```

## getOriginalSize

```TypeScript
function getOriginalSize(compressedFile: string): Promise<number>
```

Obtains the original size of a compressed file. This API uses a promise to return the result.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-zlib-function getOriginalSize(compressedFile: string): Promise<long>--><!--Device-zlib-function getOriginalSize(compressedFile: string): Promise<long>-End-->

**System capability:** SystemCapability.BundleManager.Zlib

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| compressedFile | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;number&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [900001](../../apis-basic-services-kit/errorcode-zlib.md#900001-invalid-source-file) |
| [900003](../../apis-basic-services-kit/errorcode-zlib.md#900003-source-file-in-incorrect-format-or-damaged) |

## Examples

```TypeScript
// The path used in the code must be an application sandbox path, for example, /data/storage/el2/base/temp. You can obtain the path through the context.
import { zlib, BusinessError } from '@kit.BasicServicesKit';

let compressedFile = '/data/storage/el2/base/temp/test.zip';

try {
  zlib.getOriginalSize(compressedFile).then((data: number) => {
    console.info(`getOriginalSize success. getOriginalSize: ${data}`);
  }).catch((errData: BusinessError) => {
    console.error(`errData is errCode:${errData.code}  message:${errData.message}`);
  })
} catch (errData) {
  let code = (errData as BusinessError).code;
  let message = (errData as BusinessError).message;
  console.error(`errData is errCode:${code}  message:${message}`);
}
```
