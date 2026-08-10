# createHttpResponseCache

## Modules to Import

```TypeScript
import { http } from 'kits/@kit.NetworkKit';
```

## createHttpResponseCache

```TypeScript
function createHttpResponseCache(cacheSize?: int): HttpResponseCache
```

Creates a default {@code HttpResponseCache} object to store the responses of HTTP access requests.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-http-function createHttpResponseCache(cacheSize?: int): HttpResponseCache--><!--Device-http-function createHttpResponseCache(cacheSize?: int): HttpResponseCache-End-->

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| cacheSize | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | the size of cache(max value is 10MB), default is 10*1024*1024(10MB). |

**Return value:**

| Type | Description |
| --- | --- |
| [HttpResponseCache](arkts-network-http-httpresponsecache-i.md) | the HttpResponseCache of the createHttpResponseCache. |

## Examples

```TypeScript
import { http } from '@kit.NetworkKit';

let httpResponseCache = http.createHttpResponseCache();
```

```TypeScript
import { http } from '@kit.NetworkKit';

let httpResponseCache = http.createHttpResponseCache();
```

