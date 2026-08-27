# mkdir

## Modules to Import

```TypeScript
```

## mkdir

```TypeScript
declare function mkdir(path: string, mode?: number): Promise<void>
```

Creates a directory. This API uses a promise to return the result.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [mkdir](arkts-corefile-file-fs-mkdir-f.md)

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | string | Yes | Application sandbox path of the directory. |
| mode | number | No | Permission on the directory to create. You can specify multiple permissions, separated using a bitwise OR operator (\|). The default value is **0o775**.   - **0o775**: The owner has the read, write, and execute permissions, and other users have the read and execute permissions.   - **0o700**: The owner has the read, write, and execute permissions.   - **0o400**: The owner has the read permission.   - **0o200**: The owner has the write permission.   - **0o100**: The owner has the execute permission.   - **0o070**: The user group has the read, write, and execute permissions.   - **0o040**: The user group has the read permission.   - **0o020**: The user group has the write permission.   - **0o010**: The user group has the execute permission.   - **0o007**: Other users have the read, write, and execute permissions.   - **0o004**: Other users have the read permission.   - **0o002**: Other users have the write permission.   - **0o001**: Other users have the execute permission. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Examples**

```TypeScript
import { BusinessError } from '@ohos.base';
let dirPath = pathDir + '/testDir';
fileio.mkdir(dirPath).then(() => {
  console.info("mkdir succeed");
}).catch((error: BusinessError) => {
  console.error("mkdir failed with error:" + error);
});
```


## mkdir

```TypeScript
declare function mkdir(path: string, callback: AsyncCallback<void>): void
```

Creates a directory. This API uses an asynchronous callback to return the result.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [mkdir](arkts-corefile-file-fs-mkdir-f.md)

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | string | Yes | Application sandbox path of the directory. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback invoked when the directory is created asynchronously. |

**Examples**

```TypeScript
import { BusinessError } from '@ohos.base';
let dirPath = pathDir + '/testDir';
fileio.mkdir(dirPath).then(() => {
  console.info("mkdir succeed");
}).catch((error: BusinessError) => {
  console.error("mkdir failed with error:" + error);
});
```

```TypeScript
import { BusinessError } from '@ohos.base';
let dirPath = pathDir + '/testDir';
fileio.mkdir(dirPath, (err: BusinessError) => {
  console.info("mkdir succeed");
});
```


## mkdir

```TypeScript
declare function mkdir(path: string, mode: number, callback: AsyncCallback<void>): void
```

Creates a directory. This API uses an asynchronous callback to return the result.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [mkdir](arkts-corefile-file-fs-mkdir-f.md)

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | string | Yes | Application sandbox path of the directory. |
| mode | number | Yes | Permission on the directory to create. You can specify multiple permissions, separated using a bitwise OR operator (\|). The default value is **0o775**.   - **0o775**: The owner has the read, write, and execute permissions, and other users have the read and execute permissions.   - **0o700**: The owner has the read, write, and execute permissions.   - **0o400**: The owner has the read permission.   - **0o200**: The owner has the write permission.   - **0o100**: The owner has the execute permission.   - **0o070**: The user group has the read, write, and execute permissions.   - **0o040**: The user group has the read permission.   - **0o020**: The user group has the write permission.   - **0o010**: The user group has the execute permission.   - **0o007**: Other users have the read, write, and execute permissions.   - **0o004**: Other users have the read permission.   - **0o002**: Other users have the write permission.   - **0o001**: Other users have the execute permission. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback invoked when the directory is created asynchronously. |

**Examples**

```TypeScript
import { BusinessError } from '@ohos.base';
let dirPath = pathDir + '/testDir';
fileio.mkdir(dirPath, (err: BusinessError) => {
  console.info("mkdir succeed");
});
```
