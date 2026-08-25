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

**Substitutes:** [compressFile](arkts-basicservices-zlib-compressfile-f.md)(inFile: string, outFile: string, options: Options, callback: AsyncCallback&lt;void&gt;)

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
