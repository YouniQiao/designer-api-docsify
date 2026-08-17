# getIfaceRxBytes

## Modules to Import

```TypeScript
import { statistics } from 'statistics';
```

## getIfaceRxBytes

```TypeScript
function getIfaceRxBytes(nic: string, callback: AsyncCallback<long>): void
```

Queries the data traffic (including all TCP and UDP data packets) received through a specified NIC.

**Since:** 23

<!--Device-statistics-function getIfaceRxBytes(nic: string, callback: AsyncCallback<long>): void--><!--Device-statistics-function getIfaceRxBytes(nic: string, callback: AsyncCallback<long>): void-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| nic | string | Yes | Network interface card. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;long&gt; | Yes | Returns the data traffic received through the specified NIC. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. |
| [2100002](../errorcode-net-connection.md#2100002-service-connection-failure) | Failed to connect to the service. |
| [2100003](../errorcode-net-connection.md#2100003-system-internal-error) | System internal error. |
| [2103011](../errorcode-net-statistics.md#2103011-failed-to-create-a-system-map) | Failed to create a system map. |
| [2103012](../errorcode-net-statistics.md#2103012-failed-to-obtain-the-nic-name) | Failed to obtain the NIC name. |
| [2103005](../errorcode-net-statistics.md#2103005-failed-to-read-the-system-map) | Failed to read the system map. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { statistics } from '@kit.NetworkKit';

statistics.getIfaceRxBytes("wlan0", (error: BusinessError, stats: number) => {
  console.error(JSON.stringify(error));
  console.info(JSON.stringify(stats));
});
```


## getIfaceRxBytes

```TypeScript
function getIfaceRxBytes(nic: string): Promise<long>
```

Queries the data traffic (including all TCP and UDP data packets) received through a specified NIC.

**Since:** 23

<!--Device-statistics-function getIfaceRxBytes(nic: string): Promise<long>--><!--Device-statistics-function getIfaceRxBytes(nic: string): Promise<long>-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| nic | string | Yes | Network interface card. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;long&gt; | The promise returned by the function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. |
| [2100002](../errorcode-net-connection.md#2100002-service-connection-failure) | Failed to connect to the service. |
| [2100003](../errorcode-net-connection.md#2100003-system-internal-error) | System internal error. |
| [2103011](../errorcode-net-statistics.md#2103011-failed-to-create-a-system-map) | Failed to create a system map. |
| [2103012](../errorcode-net-statistics.md#2103012-failed-to-obtain-the-nic-name) | Failed to obtain the NIC name. |
| [2103005](../errorcode-net-statistics.md#2103005-failed-to-read-the-system-map) | Failed to read the system map. |

**Examples**

```TypeScript
import { statistics } from '@kit.NetworkKit';

statistics.getIfaceRxBytes("wlan0").then((stats: number) => {
  console.info(JSON.stringify(stats));
});
```

