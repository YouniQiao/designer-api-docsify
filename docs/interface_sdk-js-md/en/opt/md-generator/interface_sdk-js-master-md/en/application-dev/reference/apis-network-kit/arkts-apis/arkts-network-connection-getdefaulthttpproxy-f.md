# getDefaultHttpProxy

## Modules to Import

```TypeScript
import { connection } from '@kit.NetworkKit';
```

## getDefaultHttpProxy

```TypeScript
function getDefaultHttpProxy(callback: AsyncCallback<HttpProxy>): void
```

Obtains the default [HttpProxy](arkts-network-connection-httpproxy-i.md#HttpProxy) proxy settings. If an application level proxy is set, the application level proxy parameters are returned. If a global proxy is set, the global proxy parameters are returned. If the process is bound to a [NetHandle](arkts-network-connection-nethandle-i.md#NetHandle) using [setAppNet](arkts-network-connection-setappnet-f.md#setAppNet), the [NetHandle](arkts-network-connection-nethandle-i.md#NetHandle) proxy settings are returned. In other cases, the proxy settings of default network are returned.

**Since:** 23

**Deprecated since:** -1

<!--Device-connection-function getDefaultHttpProxy(callback: AsyncCallback<HttpProxy>): void--><!--Device-connection-function getDefaultHttpProxy(callback: AsyncCallback<HttpProxy>): void-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;HttpProxy&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [2100002](../errorcode-net-connection.md#2100002-service-connection-failure) |
| [2100003](../errorcode-net-connection.md#2100003-system-internal-error) |

## Examples

```TypeScript
import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

connection.getDefaultHttpProxy((error: BusinessError, data: connection.HttpProxy) => {
  if (error) {
    console.error(`Failed to get default http proxy. Code:${error.code}, message:${error.message}`);
    return;
  }
  console.info("Succeeded to get data" + JSON.stringify(data));
});
```


## getDefaultHttpProxy

```TypeScript
function getDefaultHttpProxy(): Promise<HttpProxy>
```

Obtains the default [HttpProxy](arkts-network-connection-httpproxy-i.md#HttpProxy) proxy settings. If an application level proxy is set, the application level proxy parameters are returned. If a global proxy is set, the global proxy parameters are returned. If the process is bound to a [NetHandle](arkts-network-connection-nethandle-i.md#NetHandle) using [setAppNet](arkts-network-connection-setappnet-f.md#setAppNet), the [NetHandle](arkts-network-connection-nethandle-i.md#NetHandle) proxy settings are returned. In other cases, the proxy settings of default network are returned.

**Since:** 23

**Deprecated since:** -1

<!--Device-connection-function getDefaultHttpProxy(): Promise<HttpProxy>--><!--Device-connection-function getDefaultHttpProxy(): Promise<HttpProxy>-End-->

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

## Examples

```TypeScript
import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

connection.getDefaultHttpProxy().then((data: connection.HttpProxy) => {
  console.info(JSON.stringify(data));
}).catch((error: BusinessError) => {
  console.info(JSON.stringify(error));
});
```
