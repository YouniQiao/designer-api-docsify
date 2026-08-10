# getTotalBytes

## getTotalBytes

```TypeScript
function getTotalBytes(path: string, callback: AsyncCallback<number>): void
```

异步方法获取指定文件系统总字节数，使用callback形式返回结果。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [@ohos.file.statvfs:statfs.getTotalBytes](arkts-corefile-statfs-gettotalbytes-depr-f.md#gettotalbytes)

<!--Device-Statfs-function getTotalBytes(path: string, callback: AsyncCallback<number>): void--><!--Device-Statfs-function getTotalBytes(path: string, callback: AsyncCallback<number>): void-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | string | Yes | 需要查询的文件系统的文件路径 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes | 异步获取总字节数之后的回调 |

## Examples

```TypeScript
import common from '@ohos.app.ability.common';
import { BusinessError } from '@ohos.base';
let context = getContext(this) as common.UIAbilityContext;
let path = context.filesDir;
statfs.getTotalBytes(path, (err: BusinessError, totalBytes:Number) => {
    if (err) {
        console.error('getTotalBytes callback failed');
    } else {
        console.info('getTotalBytes callback success' + totalBytes);
    }
});
```


## getTotalBytes

```TypeScript
function getTotalBytes(path: string): Promise<number>
```

异步方法获取指定文件系统总字节数，以Promise形式返回结果。

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [@ohos.file.statvfs:statfs.getTotalBytes](arkts-corefile-statfs-gettotalbytes-depr-f.md#gettotalbytes)

<!--Device-Statfs-function getTotalBytes(path: string): Promise<number>--><!--Device-Statfs-function getTotalBytes(path: string): Promise<number>-End-->

**System capability:** SystemCapability.FileManagement.File.FileIO

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| path | string | Yes | 需要查询的文件系统的文件路径 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;number&gt; | 返回总字节数 |

## Examples

```TypeScript
import { BusinessError } from '@ohos.base';
let path = "/dev";
statfs.getTotalBytes(path).then((number: number) => {
  console.info("getTotalBytes promise successfully:" + number);
}).catch((err: BusinessError) => {
  console.error("getTotalBytes failed with error:" + JSON.stringify(err));
});
```

