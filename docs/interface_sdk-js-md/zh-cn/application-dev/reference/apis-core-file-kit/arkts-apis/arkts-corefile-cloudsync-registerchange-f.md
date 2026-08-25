# registerChange

## 导入模块

```TypeScript
import { cloudSync } from 'kits/@kit.CoreFileKit';
```

## registerChange

```TypeScript
function registerChange(uri: string, recursion: boolean, callback: Callback<ChangeData>): void
```

订阅监听指定文件的变化通知。callback返回更改的数据。

**起始版本：** 12

**系统能力：** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |
| recursion | boolean | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;ChangeData&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 13900001 |
| 13900002 |
| 13900012 |
| 14000002 |
