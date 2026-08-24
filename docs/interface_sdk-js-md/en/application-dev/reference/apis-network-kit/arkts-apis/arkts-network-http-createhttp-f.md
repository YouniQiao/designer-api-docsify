# createHttp

## Modules to Import

```TypeScript
import { http } from '@kit.NetworkKit';
```

## createHttp

```TypeScript
function createHttp(): HttpRequest
```

Creates an HTTP request. You can use this API to initiate or destroy an HTTP request, or enable or disable listening for HTTP Response Header events. To initiate multiple HTTP requests, you must create an **HttpRequest** object for each HTTP request. An **HttpRequest** object corresponds to an HTTP request.

> **NOTE：**&gt;
> When the request is no longer needed, call destroy() to release resources. Otherwise, memory leaks may occur.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-http-function createHttp(): HttpRequest--><!--Device-http-function createHttp(): HttpRequest-End-->

**System capability:** SystemCapability.Communication.NetStack

**Return value:**

| Type | Description |
| --- | --- |
| HttpRequest | An **HttpRequest** object, which contains the **request**, **requestInStream**, **requestSync**, **enableAutoCookie**, **destroy**, **on**, and **off** methods. |

**Examples**

```TypeScript
import { http } from '@kit.NetworkKit';

let httpRequest = http.createHttp();
```

```TypeScript
import { http } from '@kit.NetworkKit';

let httpRequest = http.createHttp();
```

