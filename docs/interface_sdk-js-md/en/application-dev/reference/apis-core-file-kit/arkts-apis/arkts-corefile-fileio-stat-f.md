# stat

## Modules to Import

```TypeScript
```

## stat

```TypeScript
declare function stat(path: string): Promise<Stat>
```

Obtains file information. This API uses a promise to return the result.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [stat](arkts-corefile-file-fs-stat-f.md)

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | string | Yes | Application sandbox path of the file. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[Stat](arkts-corefile-fileio-stat-depr-i.md)&gt; | Promise that returns the file information obtained. |

**Examples**

```TypeScript
import { BusinessError } from '@ohos.base';
let filePath = pathDir + "test.txt";
fileio.stat(filePath).then((stat: fileio.Stat) => {
  console.info("getFileInfo succeed, the size of file is " + stat.size);
}).catch((err: BusinessError) => {
  console.error("getFileInfo failed with error:" + err);
});
```


## stat

```TypeScript
declare function stat(path: string, callback: AsyncCallback<Stat>): void
```

Obtains file information. This API uses an asynchronous callback to return the result.

**Since:** 6

**Deprecated since:** 9

**Substitutes:** [stat](arkts-corefile-file-fs-stat-f.md)

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | string | Yes | Application sandbox path of the file. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[Stat](arkts-corefile-fileio-stat-depr-i.md)&gt; | Yes | Callback used to return the file information obtained. |

**Examples**

```TypeScript
import { BusinessError } from '@ohos.base';
fileio.stat(pathDir, (err: BusinessError, stat: fileio.Stat) => {
  // Example code in Stat
});
```
