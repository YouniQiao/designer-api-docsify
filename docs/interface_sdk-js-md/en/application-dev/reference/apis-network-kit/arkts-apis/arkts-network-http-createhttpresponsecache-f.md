# createHttpResponseCache

## Modules to Import

```TypeScript
```

## createHttpResponseCache

```TypeScript
function createHttpResponseCache(cacheSize?: number): HttpResponseCache
```

Creates an **HttpResponseCache** object that stores the response data of HTTP requests. You can call [flush](arkts-network-http-httpresponsecache-i.md#flush) and [delete](arkts-network-http-httpresponsecache-i.md#delete) in the object.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| cacheSize | number | No | Cache size. The maximum value is 10*1024*1024 (10 MB). The maximum value is used by default. |

**Return value:**

| Type | Description |
| --- | --- |
| [HttpResponseCache](arkts-network-http-httpresponsecache-i.md) | Object that stores the response to the HTTP request. |

**Examples**

createHttpResponseCache(cacheSize?: number): HttpResponseCache

```TypeScript
import { http } from '@kit.NetworkKit';

let httpResponseCache = http.createHttpResponseCache();
```
