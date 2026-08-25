# findProxyForUrl

## Modules to Import

```TypeScript
import { connection } from 'kits/@kit.NetworkKit';
```

## findProxyForUrl

```TypeScript
function findProxyForUrl(url: string): string
```

Parses the specified URL proxy address based on the configured PAC script and returns the corresponding PAC proxy information.

> **NOTE：**&gt;
> 1. You can use [setPacFileUrl](arkts-network-connection-setpacfileurl-f.md) or [setPacUrl](arkts-network-connection-setpacurl-f.md) to set
> the PAC script.

> 2. If no PAC script is set before this interface is called, an empty string is returned.

> 3. The [setPacFileUrl](arkts-network-connection-setpacfileurl-f.md) API supports parsing scripts and enabling the PAC proxy
> capability on PC/2in1&lt;sup&gt;20+&lt;/sup&gt;, Phone&lt;sup&gt;23+&lt;/sup&gt;, Tablet&lt;sup&gt;23+&lt;/sup
&gt; and TV&lt;sup&gt;23+&lt;/sup
&gt; devices.
> Therefore, this API can be used to obtain the PAC proxy information on the preceding devices. For wearable
> devices, this API does not take effect, and an empty string is returned.

**Since:** 20

**System capability:** SystemCapability.Communication.NetManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| url | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| string |
