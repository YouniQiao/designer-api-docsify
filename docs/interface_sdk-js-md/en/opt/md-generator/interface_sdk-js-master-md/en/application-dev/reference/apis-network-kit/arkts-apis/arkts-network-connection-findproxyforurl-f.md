# findProxyForUrl

## Modules to Import

```TypeScript
import { connection } from 'kits/@kit.NetworkKit';
```

## findProxyForUrl

```TypeScript
function findProxyForUrl(url: string): string
```

Find pac proxy info for the url.

**Since:** 20

<!--Device-connection-function findProxyForUrl(url: string): string--><!--Device-connection-function findProxyForUrl(url: string): string-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| url | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |

## Examples

```TypeScript
import { connection } from '@kit.NetworkKit';

let proxyInfo = connection.findProxyForUrl("http://example.com");
console.info(proxyInfo);
```
