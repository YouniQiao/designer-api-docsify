# getUidRxBytes

## Modules to Import

```TypeScript
import { statistics } from 'kits/@kit.NetworkKit';
```

## getUidRxBytes

```TypeScript
function getUidRxBytes(uid: int, callback: AsyncCallback<long>): void
```

Queries the data traffic (including all TCP and UDP data packets) received by a specified application.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Required permissions:** ohos.permission.GET_NETWORK_STATS

<!--Device-statistics-function getUidRxBytes(uid: int, callback: AsyncCallback<long>): void--><!--Device-statistics-function getUidRxBytes(uid: int, callback: AsyncCallback<long>): void-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uid | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Indicates the process ID of the application. |
| callback | ArkTS-Dyn: [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt;  <br>ArkTS-Sta：[AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;long&gt; | Yes | Returns the data traffic received by the specified application. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. |
| [2100002](../errorcode-net-connection.md#2100002-service-connection-failure) | Failed to connect to the service. |
| [2100003](../errorcode-net-connection.md#2100003-system-internal-error) | System internal error. |
| [2103011](../errorcode-net-statistics.md#2103011-failed-to-create-a-system-map) | Failed to create a system map. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [2103005](../errorcode-net-statistics.md#2103005-failed-to-read-the-system-map) | Failed to read the system map. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { statistics } from '@kit.NetworkKit';

statistics.getUidRxBytes(20010038, (error: BusinessError, stats: number) => {
  console.error(JSON.stringify(error));
  console.info(JSON.stringify(stats));
});
```


## getUidRxBytes

```TypeScript
function getUidRxBytes(uid: int): Promise<long>
```

Queries the data traffic (including all TCP and UDP data packets) received by a specified application.

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Required permissions:** ohos.permission.GET_NETWORK_STATS

<!--Device-statistics-function getUidRxBytes(uid: int): Promise<long>--><!--Device-statistics-function getUidRxBytes(uid: int): Promise<long>-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uid | ArkTS-Dyn: number  <br>ArkTS-Sta：int | Yes | Indicates the process ID of the application. |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: Promise&lt;number&gt;  <br>ArkTS-Sta：Promise&lt;long&gt; | The promise returned by the function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. |
| [2100002](../errorcode-net-connection.md#2100002-service-connection-failure) | Failed to connect to the service. |
| [2100003](../errorcode-net-connection.md#2100003-system-internal-error) | System internal error. |
| [2103011](../errorcode-net-statistics.md#2103011-failed-to-create-a-system-map) | Failed to create a system map. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [2103005](../errorcode-net-statistics.md#2103005-failed-to-read-the-system-map) | Failed to read the system map. |

## Examples

```TypeScript
import { statistics } from '@kit.NetworkKit';

statistics.getUidRxBytes(20010038).then((stats: number) => {
  console.info(JSON.stringify(stats));
});
```

