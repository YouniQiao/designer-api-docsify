# setMemoryCacheSize

## 导入模块

```TypeScript
import { cacheDownload } from 'kits/@kit.BasicServicesKit';
```

## setMemoryCacheSize

```TypeScript
function setMemoryCacheSize(bytes: number): void
```

设置缓存下载组件能够保存的内存缓存上限。  
- 使用该接口调整缓存大小时，默认使用“LRU”（最近最少使用）方式清除多余的已缓存的内存缓存内容。  
- 该方法为同步方法，不阻塞调用线程。

**起始版本：** 18

**系统能力：** SystemCapability.Request.FileTransferAgent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| bytes | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
