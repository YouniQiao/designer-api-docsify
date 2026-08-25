# download

## 导入模块

```TypeScript
import { cacheDownload } from 'kits/@kit.BasicServicesKit';
```

## download

```TypeScript
function download(url: string, options: CacheDownloadOptions): void
```

启动一个缓存下载任务，若传输成功，则将数据下载到内存缓存和文件缓存中。  
- 目标资源经过HTTP传输自动解压后的大小不能超过20971520B（即20MB），否则不会保存到内存缓存或文件缓存中。  
- 在缓存下载数据时，如果在该url下已存在缓存内容，新的缓存内容会覆盖旧缓存内容。  
- 目标资源在存储到内存缓存或文件缓存中时，依照缓存下载组件的各类型缓存大小上限决定文件是否存储到指定位置，并默认使用“LRU”（最近最少使用）方式替换已有缓存内容。  
- 该方法为同步方法，不阻塞调用线程。

**起始版本：** 18

**需要权限：** ohos.permission.INTERNET

**系统能力：** SystemCapability.Request.FileTransferAgent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| url | string | 是 |
| options | [CacheDownloadOptions](arkts-basicservices-cachedownload-cachedownloadoptions-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
