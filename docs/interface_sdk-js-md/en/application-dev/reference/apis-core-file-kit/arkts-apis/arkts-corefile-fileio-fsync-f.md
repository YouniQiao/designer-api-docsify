# fsync

## Modules to Import

```TypeScript
```

## fsync

```TypeScript
declare function fsync(fd: number): Promise<void>
```

Synchronizes a file. This API uses a promise to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [fsync](arkts-corefile-file-fs-fsync-f.md)

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fd | number | Yes | File descriptor of the file to synchronize. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise & lt;void & gt; | Promise that returns no value. |

**Examples**

```TypeScript
import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
let fd = fileio.openSync(filePath);
fileio.fsync(fd).then(() => {
  console.info("sync data succeed");
}).catch((err: BusinessError) => {
  console.error("sync data failed with error:" + err);
});
```


## fsync

```TypeScript
declare function fsync(fd: number, callback: AsyncCallback<void>): void
```

Synchronizes a file. This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 9

**Substitutes:** [fsync](arkts-corefile-file-fs-fsync-f.md)

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| fd | number | Yes | File descriptor of the file to synchronize. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback invoked when the file is synchronized in asynchronous mode. |

**Examples**

```TypeScript
import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
let fd = fileio.openSync(filePath);
fileio.fsync(fd, (err: BusinessError) => {
  // Do something.
});
```
