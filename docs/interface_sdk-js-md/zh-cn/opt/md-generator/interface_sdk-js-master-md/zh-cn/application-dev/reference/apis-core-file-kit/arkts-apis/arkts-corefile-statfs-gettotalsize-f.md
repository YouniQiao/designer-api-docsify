# getTotalSize

## getTotalSize

```TypeScript
function getTotalSize(path: string): Promise<number>
```

异步方法获取指定文件系统总字节数，以Promise形式返回结果。

**起始版本：** 9

<!--Device-statfs-function getTotalSize(path: string): Promise<long>--><!--Device-statfs-function getTotalSize(path: string): Promise<long>-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;number&gt; |

**错误码：**

| 错误码ID |
| --- |
| 13900018 |
| 13900030 |
| 13900031 |
| 13900004 |
| 13900005 |
| 13900038 |
| 13900033 |
| 13900002 |
| 13900012 |
| 13900013 |
| 13900008 |
| 13900042 |
| 13900011 |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let path = context.filesDir;
statfs.getTotalSize(path).then((totalSize: number) => {
  console.info("Succeeded in getting total size: " + totalSize);
}).catch((err: BusinessError) => {
  console.error("Failed to get total size. Code: " + err.code + ", message: " + err.message);
});
```


## getTotalSize

```TypeScript
function getTotalSize(path: string, callback: AsyncCallback<number>): void
```

异步方法获取指定文件系统总字节数，使用callback形式返回结果。

**起始版本：** 9

<!--Device-statfs-function getTotalSize(path: string, callback: AsyncCallback<long>): void--><!--Device-statfs-function getTotalSize(path: string, callback: AsyncCallback<long>): void-End-->

**系统能力：** SystemCapability.FileManagement.File.FileIO

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| path | string | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| 13900018 |
| 13900030 |
| 13900031 |
| 13900004 |
| 13900005 |
| 13900038 |
| 13900033 |
| 13900002 |
| 13900012 |
| 13900013 |
| 13900008 |
| 13900042 |
| 13900011 |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// 请在组件内获取context，确保this.getUIContext().getHostContext()返回结果为UIAbilityContext
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let path = context.filesDir;
statfs.getTotalSize(path, (err: BusinessError, totalSize: number) => {
  if (err) {
    console.error("Failed to get total size. Code: " + err.code + ", message: " + err.message);
  } else {
    console.info("Succeeded in getting total size: " + totalSize);
  }
});
```
