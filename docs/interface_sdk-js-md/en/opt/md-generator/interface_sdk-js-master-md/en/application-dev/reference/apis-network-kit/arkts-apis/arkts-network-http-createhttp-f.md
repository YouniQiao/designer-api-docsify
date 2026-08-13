# createHttp

## Modules to Import

```TypeScript
import { http } from '@kit.NetworkKit';
```

## createHttp

```TypeScript
function createHttp(): HttpRequest
```

Creates an HTTP request task.

**Since:** 23

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-http-function createHttp(): HttpRequest--><!--Device-http-function createHttp(): HttpRequest-End-->

**System capability:** SystemCapability.Communication.NetStack

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [HttpRequest](arkts-network-http-httprequest-i.md) |

## Examples

```TypeScript
import { http } from '@kit.NetworkKit';

let httpRequest = http.createHttp();
```

```TypeScript
import { http } from '@kit.NetworkKit';

let httpRequest = http.createHttp();
```
