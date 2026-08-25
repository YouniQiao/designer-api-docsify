# attachGroup

## 导入模块

```TypeScript
import { request } from 'kits/@kit.BasicServicesKit';
```

## attachGroup

```TypeScript
function attachGroup(gid: string, tids: string[]): Promise<void>
```

向指定分组id中绑定多个下载任务id。使用Promise异步回调。如果任意一个任务id不满足添加条件，则所有列表中的任务都不会添加到分组中。

**起始版本：** 15

**系统能力：** SystemCapability.Request.FileTransferAgent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| gid | string | 是 |
| tids | string[] | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [13400003](../errorcode-request.md#13400003-服务异常) |
| [21900005](../errorcode-request.md#21900005-任务模式错误) |
| [21900006](../errorcode-request.md#21900006-操作不存在的任务错误) |
| [21900007](../errorcode-request.md#21900007-在不支持的状态上的操作) |
| [21900008](../errorcode-request.md#21900008-任务分组不存在或已移除) |
