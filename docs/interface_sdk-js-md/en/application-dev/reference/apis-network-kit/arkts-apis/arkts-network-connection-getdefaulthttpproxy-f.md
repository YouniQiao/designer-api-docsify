# getDefaultHttpProxy

## Modules to Import

```TypeScript
import { connection } from 'kits/@kit.NetworkKit';
```

## getDefaultHttpProxy

```TypeScript
function getDefaultHttpProxy(callback: AsyncCallback<HttpProxy>): void
```

Obtains the default HTTP proxy configuration of the network. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> - If the global proxy is set, the global proxy configuration is returned.&gt;
> - If [setAppNet](arkts-network-connection-setappnet-f.md) is used to bind the application to the network specified by
> [NetHandle](arkts-network-connection-nethandle-i.md), the HTTP proxy configuration of this network is returned. In other
> cases, the HTTP proxy configuration of the default network is returned.

**Since:** 10

**System capability:** SystemCapability.Communication.NetManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;HttpProxy&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [2100002](../errorcode-net-connection.md#2100002-service-connection-failure) |
| [2100003](../errorcode-net-connection.md#2100003-system-internal-error) |


## getDefaultHttpProxy

```TypeScript
function getDefaultHttpProxy(): Promise<HttpProxy>
```

Obtains the default HTTP proxy configuration of the network. This API uses a promise to return the result.

> **NOTE：**&gt;
> - If the global proxy is set, the global proxy configuration is returned.&gt;
> - If [setAppNet](arkts-network-connection-setappnet-f.md) is used to bind the application to the network specified by
> [NetHandle](arkts-network-connection-nethandle-i.md), the HTTP proxy configuration of this network is returned. In other
> cases, the HTTP proxy configuration of the default network is returned.

**Since:** 10

**System capability:** SystemCapability.Communication.NetManager.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;HttpProxy & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [2100002](../errorcode-net-connection.md#2100002-service-connection-failure) |
| [2100003](../errorcode-net-connection.md#2100003-system-internal-error) |
