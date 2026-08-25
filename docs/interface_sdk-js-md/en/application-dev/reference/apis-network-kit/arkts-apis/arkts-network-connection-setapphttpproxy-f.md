# setAppHttpProxy

## Modules to Import

```TypeScript
import { connection } from 'kits/@kit.NetworkKit';
```

## setAppHttpProxy

```TypeScript
function setAppHttpProxy(httpProxy: HttpProxy): void
```

Sets the application-level HTTP proxy configuration.

> **NOTE：**&gt;
> If you want to use the proxy information configured by this API, set **usingProxy** in
> [HttpRequestOptions](arkts-network-http-httprequestoptions-i.md) to **true** to enable proxy forwarding. This
> API is used only for configuring proxy rules. It does not verify the validity of the proxy service.

**Since:** 11

**System capability:** SystemCapability.Communication.NetManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [httpProxy](arkts-network-ethernet-interfaceconfiguration-i-sys.md) | [HttpProxy](arkts-network-ethernet-httpproxy-t.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [2100001](../errorcode-net-connection.md#2100001-invalid-parameter-value) |
