# createHttpResponseCache

## 导入模块

```TypeScript
import { http } from 'kits/@kit.NetworkKit';
```

## createHttpResponseCache

```TypeScript
function createHttpResponseCache(cacheSize?: number): HttpResponseCache
```

创建一个HttpResponseCache对象，可用于存储HTTP请求的响应数据。对象中可调用 [flush](arkts-network-http-httpresponsecache-i.md#flush)与 [delete](arkts-network-http-httpresponsecache-i.md#delete)方法，cacheSize指定缓存大小。

**起始版本：** 9

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [cacheSize](../../apis-core-file-kit/arkts-apis/arkts-corefile-storagestatistics-bundlestats-i.md) | number | 否 |

**返回值：**

| 类型 |
| --- |
| [HttpResponseCache](arkts-network-http-httpresponsecache-i.md) |
