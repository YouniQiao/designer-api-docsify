# unzipFile

## Modules to Import

```TypeScript
import { zlib } from '@kit.BasicServicesKit';
```

## unzipFile

```TypeScript
function unzipFile(inFile: string, outFile: string, options: Options): Promise<void>
```

Unzips a file. The execution result is returned after the decompression is complete. This API uses a promise to return the result.

> **NOTE：**
> 
> The name of the zipped file or zipped folder cannot contain two consecutive periods and a slash (../). Otherwise,
> the error code -1 is returned.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [decompressFile](zlib.decompressFile(inFile:)

<!--Device-zlib-function unzipFile(inFile: string, outFile: string, options: Options): Promise<void>--><!--Device-zlib-function unzipFile(inFile: string, outFile: string, options: Options): Promise<void>-End-->

**System capability:** SystemCapability.BundleManager.Zlib

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| inFile | string | Yes |
| outFile | string | Yes |
| options | [Options](arkts-basicservices-zlib-options-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

## Examples

```TypeScript
// The path used in the code must be an application sandbox path, for example, /data/storage/el2/base/temp. You can obtain the path through the context.
import { zlib, BusinessError } from '@kit.BasicServicesKit';

let inFile = '/data/storage/el2/base/temp/xxx.zip';
let outFile = '/data/storage/el2/base/temp/xxx';
let options: zlib.Options = {
  level: zlib.CompressLevel.COMPRESS_LEVEL_DEFAULT_COMPRESSION,
  memLevel: zlib.MemLevel.MEM_LEVEL_DEFAULT,
  strategy: zlib.CompressStrategy.COMPRESS_STRATEGY_DEFAULT_STRATEGY
};

zlib.unzipFile(inFile, outFile, options).then((data: void) => {
  console.info('unzipFile result is ' + JSON.stringify(data));
}).catch((err: BusinessError) => {
  console.error('error is ' + JSON.stringify(err));
})
```
