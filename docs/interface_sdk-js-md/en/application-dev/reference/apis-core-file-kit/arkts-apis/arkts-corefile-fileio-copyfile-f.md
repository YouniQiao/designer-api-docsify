# copyFile

## Modules to Import

```TypeScript
```

## copyFile

```TypeScript
declare function copyFile(src: string | number, dest: string | number, mode?: number): Promise<void>
```

Copies a file. This API uses a promise to return the result.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [copyFile](arkts-corefile-file-fs-copyfile-f.md)

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| src | string \| number | Yes | Path or file descriptor of the source file to copy. |
| dest | string \| number | Yes | Path or file descriptor of the destination file. |
| mode | number | No | Option for overwriting the destination file. The default value is **0**, which is the only value supported.   **0**: Overwrite the file with the same name completely and truncate the part that is not overwritten. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Examples**

```TypeScript
import { BusinessError } from '@ohos.base';
let srcPath = pathDir + "srcDir/test.txt";
let dstPath = pathDir + "dstDir/test.txt";
fileio.copyFile(srcPath, dstPath).then(() => {
  console.info("copyFile succeed");
}).catch((err: BusinessError) => {
  console.error("copyFile failed with error:" + err);
});
```


## copyFile

```TypeScript
declare function copyFile(src: string | number, dest: string | number, callback: AsyncCallback<void>): void
```

Copies a file. This API uses an asynchronous callback to return the result.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [copyFile](arkts-corefile-file-fs-copyfile-f.md)

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| src | string \| number | Yes | Path or file descriptor of the source file to copy. |
| dest | string \| number | Yes | Path or file descriptor of the destination file. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback invoked when the file is copied asynchronously. |

**Examples**

```TypeScript
import { BusinessError } from '@ohos.base';
let srcPath = pathDir + "srcDir/test.txt";
let dstPath = pathDir + "dstDir/test.txt";
fileio.copyFile(srcPath, dstPath).then(() => {
  console.info("copyFile succeed");
}).catch((err: BusinessError) => {
  console.error("copyFile failed with error:" + err);
});
```

```TypeScript
import { BusinessError } from '@ohos.base';
let srcPath = pathDir + "srcDir/test.txt";
let dstPath = pathDir + "dstDir/test.txt";
fileio.copyFile(srcPath, dstPath, (err: BusinessError) => {
  // Do something.
});
```


## copyFile

```TypeScript
declare function copyFile(
  src: string | number,
  dest: string | number,
  mode: number,
  callback: AsyncCallback<void>
): void
```

Copies a file. This API uses an asynchronous callback to return the result.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [copyFile](arkts-corefile-file-fs-copyfile-f.md)

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| src | string \| number | Yes | Path or file descriptor of the source file to copy. |
| dest | string \| number | Yes | Path or file descriptor of the destination file. |
| mode | number | Yes | Option for overwriting the destination file. The default value is **0**, which is the only value supported.   **0**: Overwrite the file with the same name completely and truncate the part that is not overwritten. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback invoked when the file is copied asynchronously. |

**Examples**

```TypeScript
import { BusinessError } from '@ohos.base';
let srcPath = pathDir + "srcDir/test.txt";
let dstPath = pathDir + "dstDir/test.txt";
fileio.copyFile(srcPath, dstPath, (err: BusinessError) => {
  // Do something.
});
```
