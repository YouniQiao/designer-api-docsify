# getAllTxBytes

## Modules to Import

```TypeScript
import { statistics } from '@kit.NetworkKit';
```

## getAllTxBytes

```TypeScript
function getAllTxBytes(callback: AsyncCallback<long>): void
```

Queries the data traffic (including all TCP and UDP data packets) sent through all NICs.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-statistics-function getAllTxBytes(callback: AsyncCallback<long>): void--><!--Device-statistics-function getAllTxBytes(callback: AsyncCallback<long>): void-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;long&gt; | Yes | Returns the data traffic sent through all NICs. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [2100002](../errorcode-net-connection.md#2100002-service-connection-failure) | Failed to connect to the service. |
| [2100003](../errorcode-net-connection.md#2100003-system-internal-error) | System internal error. |
| [2103011](../errorcode-net-statistics.md#2103011-failed-to-create-a-system-map) | Failed to create a system map. |
| [2103005](../errorcode-net-statistics.md#2103005-failed-to-read-the-system-map) | Failed to read the system map. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { statistics } from '@kit.NetworkKit';

statistics.getAllTxBytes((error: BusinessError, stats: number) => {
  console.error(JSON.stringify(error));
  console.info(JSON.stringify(stats));
});
```


## getAllTxBytes

```TypeScript
function getAllTxBytes(): Promise<long>
```

Queries the data traffic (including all TCP and UDP data packets) sent through all NICs.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-statistics-function getAllTxBytes(): Promise<long>--><!--Device-statistics-function getAllTxBytes(): Promise<long>-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;long&gt; | The promise returned by the function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [2100002](../errorcode-net-connection.md#2100002-service-connection-failure) | Failed to connect to the service. |
| [2100003](../errorcode-net-connection.md#2100003-system-internal-error) | System internal error. |
| [2103011](../errorcode-net-statistics.md#2103011-failed-to-create-a-system-map) | Failed to create a system map. |
| [2103005](../errorcode-net-statistics.md#2103005-failed-to-read-the-system-map) | Failed to read the system map. |

## Examples

```TypeScript
import { statistics } from '@kit.NetworkKit';

statistics.getAllTxBytes().then((stats: number) => {
  console.info(JSON.stringify(stats));
});
```

