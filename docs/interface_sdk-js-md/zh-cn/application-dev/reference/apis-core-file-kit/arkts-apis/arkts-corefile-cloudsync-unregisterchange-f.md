# unregisterChange

## 导入模块

```TypeScript
import { cloudSync } from 'kits/@kit.CoreFileKit';
```

## unregisterChange

```TypeScript
function unregisterChange(uri: string): void
```

取消订阅监听指定文件的变化通知。

**起始版本：** 12

**系统能力：** SystemCapability.FileManagement.DistributedFileService.CloudSync.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| uri | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 13900001 |
| 13900002 |
| 13900012 |
| 14000002 |
