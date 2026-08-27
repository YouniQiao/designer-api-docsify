# symlink

## Modules to Import

```TypeScript
```

## symlink

```TypeScript
declare function symlink(target: string, srcPath: string): Promise<void>
```

Creates a symbolic link based on the file path. This API uses a promise to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [symlink](arkts-corefile-file-fs-symlink-f.md)

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| target | string | Yes | Application sandbox path of the target file. |
| srcPath | string | Yes | Application sandbox path of the symbolic link. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Examples**

```TypeScript
import { BusinessError } from '@ohos.base';
let srcFile = pathDir + "/test.txt";
let dstFile = pathDir + '/test';
fileio.symlink(srcFile, dstFile).then(() => {
  console.info("symlink succeed");
}).catch((err: BusinessError) => {
  console.error("symlink failed with error:" + err);
});
```


## symlink

```TypeScript
declare function symlink(target: string, srcPath: string, callback: AsyncCallback<void>): void
```

Creates a symbolic link based on the file path. This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [symlink](arkts-corefile-file-fs-symlink-f.md)

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| target | string | Yes | Application sandbox path of the target file. |
| srcPath | string | Yes | Application sandbox path of the symbolic link. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback invoked when the symbolic link is created asynchronously. |

**Examples**

```TypeScript
import { BusinessError } from '@ohos.base';
let srcFile = pathDir + "/test.txt";
let dstFile = pathDir + '/test';
fileio.symlink(srcFile, dstFile, (err: BusinessError) => {
  // Do something.
});
```
