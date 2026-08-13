# getSockfdRxBytes

## Modules to Import

```TypeScript
import { statistics } from '@kit.NetworkKit';
```

## getSockfdRxBytes

```TypeScript
function getSockfdRxBytes(sockfd: int, callback: AsyncCallback<long>): void
```

Queries the data traffic (including all TCP and UDP data packets) received through a specified sockfd.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-statistics-function getSockfdRxBytes(sockfd: int, callback: AsyncCallback<long>): void--><!--Device-statistics-function getSockfdRxBytes(sockfd: int, callback: AsyncCallback<long>): void-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| sockfd | int | Yes | Indicates the file descriptor of the given socket. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;long&gt; | Yes | Returns the data traffic bytes received by the specified sockfd. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. |
| [2100001](../errorcode-net-connection.md#2100001-invalid-parameter-value) | Invalid parameter value. |
| [2100002](../errorcode-net-connection.md#2100002-service-connection-failure) | Failed to connect to the service. |
| [2100003](../errorcode-net-connection.md#2100003-system-internal-error) | System internal error. |

## Examples

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

Queries the data traffic (including all TCP and UDP data packets) received through a specified sockfd.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-statistics-function getSockfdRxBytes(sockfd: int): Promise<long>--><!--Device-statistics-function getSockfdRxBytes(sockfd: int): Promise<long>-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| sockfd | int | Yes | Indicates the file descriptor of the given socket. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;long&gt; | Returns the data traffic bytes received by the specified sockfd. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. |
| [2100001](../errorcode-net-connection.md#2100001-invalid-parameter-value) | Invalid parameter value. |
| [2100002](../errorcode-net-connection.md#2100002-service-connection-failure) | Failed to connect to the service. |
| [2100003](../errorcode-net-connection.md#2100003-system-internal-error) | System internal error. |

## Examples

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

