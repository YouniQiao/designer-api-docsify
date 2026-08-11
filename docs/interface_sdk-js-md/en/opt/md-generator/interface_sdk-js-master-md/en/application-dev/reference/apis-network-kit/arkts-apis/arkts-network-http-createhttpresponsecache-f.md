# createHttpResponseCache

## Modules to Import

```TypeScript
import { http } from 'kits/@kit.NetworkKit';
```

## createHttpResponseCache

```TypeScript
function createHttpResponseCache(cacheSize?: number): HttpResponseCache
```

Creates a default {@code HttpResponseCache} object to store the responses of HTTP access requests.

**Since:** 11

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-http-function createHttpResponseCache(cacheSize?: int): HttpResponseCache--><!--Device-http-function createHttpResponseCache(cacheSize?: int): HttpResponseCache-End-->

**System capability:** SystemCapability.Communication.NetStack

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| cacheSize | number | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [HttpResponseCache](arkts-network-http-httpresponsecache-i.md) |

## Examples

```TypeScript
import { http } from '@kit.NetworkKit';

let httpResponseCache = http.createHttpResponseCache();
```

```TypeScript
import { http } from '@kit.NetworkKit';

let httpResponseCache = http.createHttpResponseCache();
```
