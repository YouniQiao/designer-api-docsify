# zipFile

## Modules to Import

```TypeScript
import { zlib } from 'kits/@kit.BasicServicesKit';
```

## zipFile

```TypeScript
function zipFile(inFile: string, outFile: string, options: Options): Promise<void>
```

Zips a file. The execution result is returned after the compression is complete. This API uses a promise to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [zlib.compressFile](arkts-basicservices-zlib-compressfile-f.md#compressfile)(inFile:

<!--Device-zlib-function zipFile(inFile: string, outFile: string, options: Options): Promise<void>--><!--Device-zlib-function zipFile(inFile: string, outFile: string, options: Options): Promise<void>-End-->

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
| Promise&lt;void&gt; |

## Examples

```TypeScript
// The path used in the code must be an application sandbox path, for example, /data/storage/el2/base/temp. You can obtain the path through the context.
import { zlib, BusinessError } from '@kit.BasicServicesKit';

let inFile = '/data/storage/el2/base/temp/filename.xxx';
let outFile = '/data/storage/el2/base/temp/xxx.zip';
let options: zlib.Options = {
  level: zlib.CompressLevel.COMPRESS_LEVEL_DEFAULT_COMPRESSION,
  memLevel: zlib.MemLevel.MEM_LEVEL_DEFAULT,
  strategy: zlib.CompressStrategy.COMPRESS_STRATEGY_DEFAULT_STRATEGY
};

zlib.zipFile(inFile, outFile, options).then((data: void) => {
  console.info('zipFile result is ' + JSON.stringify(data));
}).catch((err: BusinessError) => {
  console.error('error is ' + JSON.stringify(err));
});
```
