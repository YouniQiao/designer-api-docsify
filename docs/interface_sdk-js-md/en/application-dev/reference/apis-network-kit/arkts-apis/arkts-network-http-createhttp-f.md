# createHttp

## Modules to Import

```TypeScript
import { http } from 'kits/@kit.NetworkKit';
```

## createHttp

```TypeScript
function createHttp(): HttpRequest
```

Creates an HTTP request. You can use this API to initiate or destroy an HTTP request, or enable or disable listening for HTTP Response Header events. To initiate multiple HTTP requests, you must create an **HttpRequest** object for each HTTP request. An **HttpRequest** object corresponds to an HTTP request.

> **NOTE：**&gt;
> When the request is no longer needed, call destroy() to release resources. Otherwise, memory leaks may occur.

**Since:** 6

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Communication.NetStack

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [HttpRequest](arkts-network-connection-httprequest-t.md) |
