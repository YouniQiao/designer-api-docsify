# createHttpResponseCache

## Modules to Import

```TypeScript
import { http } from '@kit.NetworkKit';
```

## createHttpResponseCache

```TypeScript
function createHttpResponseCache(cacheSize?: int): HttpResponseCache
```

Creates an **HttpResponseCache** object that stores the response data of HTTP requests. You can call [flush](arkts-network-http-httpresponsecache-i.md#flush) and [delete](arkts-network-http-httpresponsecache-i.md#delete) in the object.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-http-function createHttpResponseCache(cacheSize?: int): HttpResponseCache--><!--Device-http-function createHttpResponseCache(cacheSize?: int): HttpResponseCache-End-->

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| cacheSize | int | No | Cache size. The maximum value is 10*1024*1024 (10 MB). The maximum value is used by default. |

**Return value:**

| Type | Description |
| --- | --- |
| [HttpResponseCache](arkts-network-http-httpresponsecache-i.md) | Object that stores the response to the HTTP request. |

**Examples**

```TypeScript
import { http } from '@kit.NetworkKit';

let httpResponseCache = http.createHttpResponseCache();
```

```TypeScript
import { http } from '@kit.NetworkKit';

let httpResponseCache = http.createHttpResponseCache();
```

