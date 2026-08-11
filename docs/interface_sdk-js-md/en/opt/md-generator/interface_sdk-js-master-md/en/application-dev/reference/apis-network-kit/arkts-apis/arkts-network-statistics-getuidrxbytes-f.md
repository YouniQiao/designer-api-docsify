# getUidRxBytes

## Modules to Import

```TypeScript
import { statistics } from 'kits/@kit.NetworkKit';
```

## getUidRxBytes

```TypeScript
function getUidRxBytes(uid: number, callback: AsyncCallback<number>): void
```

Queries the data traffic (including all TCP and UDP data packets) received by a specified application.

**Since:** 26.0.0

**Required permissions:** ohos.permission.GET_NETWORK_STATS

<!--Device-statistics-function getUidRxBytes(uid: int, callback: AsyncCallback<long>): void--><!--Device-statistics-function getUidRxBytes(uid: int, callback: AsyncCallback<long>): void-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uid | number | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [2100002](../errorcode-net-connection.md#2100002-service-connection-failure) |
| [2100003](../errorcode-net-connection.md#2100003-system-internal-error) |
| [2103011](../errorcode-net-statistics.md#2103011-failed-to-create-a-system-map) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [2103005](../errorcode-net-statistics.md#2103005-failed-to-read-the-system-map) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { statistics } from '@kit.NetworkKit';

let uid = 123456789;  // This is a sample UID. Replace it with the actual UID.
statistics.getUidRxBytes(uid, (error: BusinessError, stats: number) => {
  if (error) {
     console.error(JSON.stringify(error));
     return;
  }
  console.info(JSON.stringify(stats));
});
```


## getUidRxBytes

```TypeScript
function getUidRxBytes(uid: number): Promise<number>
```

Queries the data traffic (including all TCP and UDP data packets) received by a specified application.

**Since:** 26.0.0

**Required permissions:** ohos.permission.GET_NETWORK_STATS

<!--Device-statistics-function getUidRxBytes(uid: int): Promise<long>--><!--Device-statistics-function getUidRxBytes(uid: int): Promise<long>-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| uid | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;number&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [2100002](../errorcode-net-connection.md#2100002-service-connection-failure) |
| [2100003](../errorcode-net-connection.md#2100003-system-internal-error) |
| [2103011](../errorcode-net-statistics.md#2103011-failed-to-create-a-system-map) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [2103005](../errorcode-net-statistics.md#2103005-failed-to-read-the-system-map) |

## Examples

```TypeScript
import { statistics } from '@kit.NetworkKit';

let uid = 123456789;  // This is a sample UID. Replace it with the actual UID.
statistics.getUidRxBytes(uid).then((stats: number) => {
  console.info(JSON.stringify(stats));
});
```
