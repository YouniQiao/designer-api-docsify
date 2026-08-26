# chown

## Modules to Import

```TypeScript
```

## chown

```TypeScript
declare function chown(path: string, uid: number, gid: number): Promise<void>
```

Changes the file owner based on the file path. This API uses a promise to return the result.

**Since:** 7

**Deprecated since:** 9

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | string | Yes | Application sandbox path of the file. |
| uid | number | Yes | New user ID (UID). |
| gid | number | Yes | New group ID (GID). |

**Return value:**

| Type | Description |
| --- | --- |
| Promise & lt;void & gt; | Promise that returns no value. |

**Examples**

```TypeScript
import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
let stat = fileio.statSync(filePath);
fileio.chown(filePath, stat.uid, stat.gid).then(() => {
  console.info("chown succeed");
}).catch((err: BusinessError) => {
  console.error("chown failed with error:" + err);
});
```


## chown

```TypeScript
declare function chown(path: string, uid: number, gid: number, callback: AsyncCallback<void>): void
```

Changes the file owner based on the file path. This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 9

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | string | Yes | Application sandbox path of the file. |
| uid | number | Yes | New UID. |
| gid | number | Yes | New GID. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback invoked when the file owner is changed asynchronously. |

**Examples**

```TypeScript
import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
let stat = fileio.statSync(filePath)
fileio.chown(filePath, stat.uid, stat.gid, (err: BusinessError) => {
  // Do something.
});
```
