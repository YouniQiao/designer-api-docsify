# getCellularRxBytes

## Modules to Import

```TypeScript
import { statistics } from '@kit.NetworkKit';
```

## getCellularRxBytes

```TypeScript
function getCellularRxBytes(callback: AsyncCallback<number>): void
```

Queries the data traffic (including all TCP and UDP data packets) received through the cellular network.

**Since:** 23

**Deprecated since:** -1

<!--Device-statistics-function getCellularRxBytes(callback: AsyncCallback<long>): void--><!--Device-statistics-function getCellularRxBytes(callback: AsyncCallback<long>): void-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [2100002](../errorcode-net-connection.md#2100002-service-connection-failure) |
| [2100003](../errorcode-net-connection.md#2100003-system-internal-error) |
| [2103011](../errorcode-net-statistics.md#2103011-failed-to-create-a-system-map) |
| [2103012](../errorcode-net-statistics.md#2103012-failed-to-obtain-the-nic-name) |
| [2103005](../errorcode-net-statistics.md#2103005-failed-to-read-the-system-map) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { statistics } from '@kit.NetworkKit';

statistics.getCellularRxBytes((error: BusinessError, stats: number) => {
  if (error) {
    console.error(`getCellularRxBytes error, ${JSON.stringify(error)}`);
    return;
  }
  console.info(`getCellularRxBytes success, ${JSON.stringify(stats)}`);
});
```


## getCellularRxBytes

```TypeScript
function getCellularRxBytes(): Promise<number>
```

Queries the data traffic (including all TCP and UDP data packets) received through the cellular network.

**Since:** 23

**Deprecated since:** -1

<!--Device-statistics-function getCellularRxBytes(): Promise<long>--><!--Device-statistics-function getCellularRxBytes(): Promise<long>-End-->

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
| [2103011](../errorcode-net-statistics.md#2103011-failed-to-create-a-system-map) |
| [2103012](../errorcode-net-statistics.md#2103012-failed-to-obtain-the-nic-name) |
| [2103005](../errorcode-net-statistics.md#2103005-failed-to-read-the-system-map) |

## Examples

```TypeScript
import { statistics } from '@kit.NetworkKit';

statistics.getCellularRxBytes().then((stats: number) => {
  console.info('getCellularRxBytes success', JSON.stringify(stats));
}).catch((error: Error) => {
   console.error('getCellularRxBytes error', JSON.stringify(error));
});
```
