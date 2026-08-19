# getSockfdRxBytes

## Modules to Import

```TypeScript
import { statistics } from '@kit.NetworkKit';
```

## getSockfdRxBytes

```TypeScript
function getSockfdRxBytes(sockfd: int, callback: AsyncCallback<long>): void
```

Obtains the downlink traffic (in bytes) of the specified socket. This API uses an asynchronous callback to return the result. &gt; **NOTE：**&gt; &gt; It is recommended to use this API when the socket is connected. Otherwise, the corresponding traffic data cannot &gt; be queried after the socket is closed.

**Since:** 23

<!--Device-statistics-function getSockfdRxBytes(sockfd: int, callback: AsyncCallback<long>): void--><!--Device-statistics-function getSockfdRxBytes(sockfd: int, callback: AsyncCallback<long>): void-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| sockfd | int | Yes | File description (FD) of the socket to query. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;long&gt; | Yes | Callback used to return the result. If the downlink traffic of the socket is obtained successfully, **error** is **undefined**; otherwise, it is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. |
| [2100001](../errorcode-net-connection.md#2100001-invalid-parameter-value) | Invalid parameter value. |
| [2100002](../errorcode-net-connection.md#2100002-service-connection-failure) | Failed to connect to the service. |
| [2100003](../errorcode-net-connection.md#2100003-system-internal-error) | System internal error. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { statistics } from '@kit.NetworkKit';

let sockfd = 50; // FD of the socket you created.
statistics.getSockfdRxBytes(sockfd, (error: BusinessError, stats: number) => {
  console.error(JSON.stringify(error));
  console.info(JSON.stringify(stats));
});
```


## getSockfdRxBytes

```TypeScript
function getSockfdRxBytes(sockfd: int): Promise<long>
```

Obtains the downlink traffic (in bytes) of the specified socket. This API uses a promise to return the result. &gt; **NOTE：**&gt; &gt; It is recommended to use this API when the socket is connected. Otherwise, the corresponding traffic data cannot &gt; be queried after the socket is closed.

**Since:** 23

<!--Device-statistics-function getSockfdRxBytes(sockfd: int): Promise<long>--><!--Device-statistics-function getSockfdRxBytes(sockfd: int): Promise<long>-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| sockfd | int | Yes | FD of the socket to query. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;long&gt; | Promise used to return the downlink traffic (in bytes) of the socket. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. |
| [2100001](../errorcode-net-connection.md#2100001-invalid-parameter-value) | Invalid parameter value. |
| [2100002](../errorcode-net-connection.md#2100002-service-connection-failure) | Failed to connect to the service. |
| [2100003](../errorcode-net-connection.md#2100003-system-internal-error) | System internal error. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { statistics } from '@kit.NetworkKit';

let sockfd = 50; // FD of the socket you created.
statistics.getSockfdRxBytes(sockfd).then((stats: number) => {
  console.info(JSON.stringify(stats));
}).catch((err: BusinessError) => {
  console.error(JSON.stringify(err));
});
```

