# setDownloadInfoListSize

## 导入模块

```TypeScript
import { cacheDownload } from 'kits/@kit.BasicServicesKit';
```

## setDownloadInfoListSize

```TypeScript
function setDownloadInfoListSize(size: number): void
```

设置下载信息列表的大小。  
- 下载信息列表用于存储预下载信息。  
- 下载信息和url一一对应，每次预下载都会生成一个下载信息，相同url下只会保存最新的下载信息。  
- 使用该接口调整列表大小时，size更新增大，列表中原有的信息不变，更新减小，默认使用“LRU”（最近最少使用）方式清除多余的已缓存信息。

**起始版本：** 20

**系统能力：** SystemCapability.Request.FileTransferAgent

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| size | number | 是 |
