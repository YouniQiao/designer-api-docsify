# rename

## Modules to Import

```TypeScript
```

## rename

```TypeScript
declare function rename(oldPath: string, newPath: string): Promise<void>
```

Renames a file. This API uses a promise to return the result.

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Deprecated since:** 9

**Substitutes:** [rename](arkts-corefile-file-fs-rename-f.md)

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| oldPath | string | Yes |
| newPath | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Examples**

```TypeScript
import { BusinessError } from '@ohos.base';
let srcFile = pathDir + "/test.txt";
let dstFile = pathDir + '/new.txt';
fileio.rename(srcFile, dstFile).then(() => {
  console.info("rename succeed");
}).catch((err: BusinessError) => {
  console.error("rename failed with error:" + err);
});
```

```TypeScript
import { BusinessError } from '@ohos.base';
let srcFile = pathDir + "/test.txt";
let dstFile = pathDir + '/new.txt';
fileio.rename(srcFile, dstFile, (err: BusinessError) => {
});
```


## rename

```TypeScript
declare function rename(oldPath: string, newPath: string, callback: AsyncCallback<void>): void
```

Renames a file. This API uses an asynchronous callback to return the result.

**Since:** 7

**ArkTS mode:** Supports only ArkTS-Dyn, since version 7.

**Deprecated since:** 9

**Substitutes:** [rename](arkts-corefile-file-fs-rename-f.md)

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| oldPath | string | Yes |
| newPath | string | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Examples**

See [rename](#rename)
