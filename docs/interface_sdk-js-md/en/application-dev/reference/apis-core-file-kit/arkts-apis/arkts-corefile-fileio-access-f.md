# access

## Modules to Import

```TypeScript
```

## access

```TypeScript
declare function access(path: string, mode?: number): Promise<void>
```

Checks whether this process can access a file. This API uses a promise to return the result.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [access](arkts-corefile-file-fs-access-f.md)

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | string | Yes | Application sandbox path of the file. |
| mode | number | No | Options for accessing the file. You can specify multiple options, separated with a bitwise OR operator (\|). The default value is **0**.The options are as follows:   - **0**: Check whether the file exists.   - **1**: Check whether the process has the execute permission on the file.   - **2**: Check whether the process has the write permission on the file.   - **4**: Check whether the process has the read permission on the file. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Examples**

```TypeScript
import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
fileio.access(filePath).then(() => {
  console.info("access succeed");
}).catch((err: BusinessError) => {
  console.error("access failed with error:" + err);
});
```


## access

```TypeScript
declare function access(path: string, callback: AsyncCallback<void>): void
```

Checks whether this process can access a file. This API uses an asynchronous callback to return the result.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [access](arkts-corefile-file-fs-access-f.md)

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | string | Yes | Application sandbox path of the file. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback invoked when the file is asynchronously checked. |

**Examples**

```TypeScript
import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
fileio.access(filePath).then(() => {
  console.info("access succeed");
}).catch((err: BusinessError) => {
  console.error("access failed with error:" + err);
});
```

```TypeScript
import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
fileio.access(filePath, (err: BusinessError) => {
  // Do something.
});
```


## access

```TypeScript
declare function access(path: string, mode: number, callback: AsyncCallback<void>): void
```

Checks whether this process can access a file. This API uses an asynchronous callback to return the result.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [access](arkts-corefile-file-fs-access-f.md)

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | string | Yes | Application sandbox path of the file. |
| mode | number | Yes | Options for accessing the file. You can specify multiple options, separated with a bitwise OR operator (\|). The default value is **0**.The options are as follows:   - **0**: Check whether the file exists.   - **1**: Check whether the process has the execute permission on the file.   - **2**: Check whether the process has the write permission on the file.   - **4**: Check whether the process has the read permission on the file. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Callback invoked when the file is asynchronously checked. |

**Examples**

See [access](#access)
