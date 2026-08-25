# unzipFile

## Modules to Import

```TypeScript
import { zlib } from 'kits/@kit.BasicServicesKit';
```

## unzipFile

```TypeScript
function unzipFile(inFile: string, outFile: string, options: Options): Promise<void>
```

Unzips a file. The execution result is returned after the decompression is complete. This API uses a promise to return the result.

> **NOTE：**&gt;
> The name of the zipped file or zipped folder cannot contain two consecutive periods and a slash (../). Otherwise,
> the error code -1 is returned.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [decompressFile](arkts-basicservices-zlib-decompressfile-f.md)(inFile: string, outFile: string, options: Options, callback: AsyncCallback&lt;void&gt;)

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
