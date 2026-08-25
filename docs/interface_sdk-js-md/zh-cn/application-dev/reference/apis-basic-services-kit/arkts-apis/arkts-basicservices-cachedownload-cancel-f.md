# cancel

## 导入模块

```TypeScript
import { cacheDownload } from 'kits/@kit.BasicServicesKit';
```

## cancel

```TypeScript
function cancel(url: string): void
```

根据url移除一个正在执行的缓存下载任务，已保存的内存缓存和文件缓存不会受到影响。  
- 当不存在对应url的任务时无其他效果。  
- 使用该方法同步执行时，不阻塞调用线程。

**起始版本：** 18

**系统能力：** SystemCapability.Request.FileTransferAgent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| url | string | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
