# createHttpResponseCache

## 导入模块

```TypeScript
import { http } from 'kits/@kit.NetworkKit';
```

## createHttpResponseCache

```TypeScript
function createHttpResponseCache(cacheSize?: int): HttpResponseCache
```

Creates a default {@code HttpResponseCache} object to store the responses of HTTP access requests.

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-http-function createHttpResponseCache(cacheSize?: int): HttpResponseCache--><!--Device-http-function createHttpResponseCache(cacheSize?: int): HttpResponseCache-End-->

**系统能力：** SystemCapability.Communication.NetStack

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| cacheSize | ArkTS-Dyn: number  <br>ArkTS-Sta：int | 否 | the size of cache(max value is 10MB), default is 10*1024*1024(10MB). |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [HttpResponseCache](arkts-network-http-httpresponsecache-i.md) | the HttpResponseCache of the createHttpResponseCache. |

## 示例

```TypeScript
import { http } from '@kit.NetworkKit';

let httpResponseCache = http.createHttpResponseCache();
```

