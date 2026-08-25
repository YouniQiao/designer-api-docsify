# getCellularTxBytes

## Modules to Import

```TypeScript
import { statistics } from 'kits/@kit.NetworkKit';
```

## getCellularTxBytes

```TypeScript
function getCellularTxBytes(callback: AsyncCallback<number>): void
```

Obtains the total uplink traffic (in bytes) of the NIC corresponding to the currently connected cellular network from the last startup to the time when this API is called. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> It is recommended to call this API when the cellular network is in the connected state. Otherwise, error code 210
> 3012 will be thrown.

**Since:** 10

**System capability:** SystemCapability.Communication.NetManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [2100002](../errorcode-net-connection.md#2100002-service-connection-failure) |
| [2100003](../errorcode-net-connection.md#2100003-system-internal-error) |
| [2103005](../errorcode-net-statistics.md#2103005-failed-to-read-the-system-map) |
| [2103011](../errorcode-net-statistics.md#2103011-failed-to-create-a-system-map) |
| [2103012](../errorcode-net-statistics.md#2103012-failed-to-obtain-the-nic-name) |


## getCellularTxBytes

```TypeScript
function getCellularTxBytes(): Promise<number>
```

Obtains the total uplink traffic (in bytes) of the NIC corresponding to the currently connected cellular network from the last startup to the time when this API is called. This API uses a promise to return the result.

> **NOTE：**&gt;
> It is recommended to call this API when the cellular network is in the connected state. Otherwise, error code 210
> 3012 will be thrown.

**Since:** 10

**System capability:** SystemCapability.Communication.NetManager.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [2100002](../errorcode-net-connection.md#2100002-service-connection-failure) |
| [2100003](../errorcode-net-connection.md#2100003-system-internal-error) |
| [2103005](../errorcode-net-statistics.md#2103005-failed-to-read-the-system-map) |
| [2103011](../errorcode-net-statistics.md#2103011-failed-to-create-a-system-map) |
| [2103012](../errorcode-net-statistics.md#2103012-failed-to-obtain-the-nic-name) |
