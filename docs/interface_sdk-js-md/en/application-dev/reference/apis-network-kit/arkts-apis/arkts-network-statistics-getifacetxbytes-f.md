# getIfaceTxBytes

## Modules to Import

```TypeScript
import { statistics } from 'kits/@kit.NetworkKit';
```

## getIfaceTxBytes

```TypeScript
function getIfaceTxBytes(nic: string, callback: AsyncCallback<number>): void
```

Obtains the total uplink traffic (in bytes) of the specified NIC from the last startup to the time when this API is called. This API uses an asynchronous callback to return the result.

**Since:** 10

**System capability:** SystemCapability.Communication.NetManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| nic | string | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [2100002](../errorcode-net-connection.md#2100002-service-connection-failure) |
| [2100003](../errorcode-net-connection.md#2100003-system-internal-error) |
| [2103005](../errorcode-net-statistics.md#2103005-failed-to-read-the-system-map) |
| [2103011](../errorcode-net-statistics.md#2103011-failed-to-create-a-system-map) |
| [2103012](../errorcode-net-statistics.md#2103012-failed-to-obtain-the-nic-name) |


## getIfaceTxBytes

```TypeScript
function getIfaceTxBytes(nic: string): Promise<number>
```

Obtains the total uplink traffic (in bytes) of the specified NIC from the last startup to the time when this API is called. This API uses a promise to return the result.

**Since:** 10

**System capability:** SystemCapability.Communication.NetManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| nic | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [2100002](../errorcode-net-connection.md#2100002-service-connection-failure) |
| [2100003](../errorcode-net-connection.md#2100003-system-internal-error) |
| [2103005](../errorcode-net-statistics.md#2103005-failed-to-read-the-system-map) |
| [2103011](../errorcode-net-statistics.md#2103011-failed-to-create-a-system-map) |
| [2103012](../errorcode-net-statistics.md#2103012-failed-to-obtain-the-nic-name) |
