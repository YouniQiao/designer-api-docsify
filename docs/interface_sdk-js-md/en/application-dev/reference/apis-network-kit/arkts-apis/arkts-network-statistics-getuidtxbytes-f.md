# getUidTxBytes

## Modules to Import

```TypeScript
import { statistics } from '@kit.NetworkKit';
```

## getUidTxBytes

```TypeScript
function getUidTxBytes(uid: int, callback: AsyncCallback<long>): void
```

Obtains the total uplink traffic (in bytes) of the specified application from the last startup to the time when this API is called. This API uses an asynchronous callback to return the result. > **NOTE：**> > If the application has not generated any traffic consumption after the restart, error code 2103005 will be > thrown.

**Since:** 23

**Required permissions:** 
- API version 26.0.0+: ohos.permission.GET_NETWORK_STATS

<!--Device-statistics-function getUidTxBytes(uid: int, callback: AsyncCallback<long>): void--><!--Device-statistics-function getUidTxBytes(uid: int, callback: AsyncCallback<long>): void-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uid | int | Yes | Application UID. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;long&gt; | Yes | Callback used to return the result. If the application's real-time uplink traffic is successfully obtained, **error** is **undefined** and **stats** is the obtained application uplink traffic (in bytes). Otherwise, it is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. |
| [2100002](../errorcode-net-connection.md#2100002-service-connection-failure) | Failed to connect to the service. |
| [2100003](../errorcode-net-connection.md#2100003-system-internal-error) | System internal error. |
| [2103011](../errorcode-net-statistics.md#2103011-failed-to-create-a-system-map) | Failed to create a system map. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied.<br>**Applicable version:** 26.0.0 and later |
| [2103005](../errorcode-net-statistics.md#2103005-failed-to-read-the-system-map) | Failed to read the system map. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { statistics } from '@kit.NetworkKit';

statistics.getUidTxBytes(20010038, (error: BusinessError, stats: number) => {
  console.error(JSON.stringify(error));
  console.info(JSON.stringify(stats));
});
```


## getUidTxBytes

```TypeScript
function getUidTxBytes(uid: int): Promise<long>
```

Obtains the total uplink traffic of the specified application from the last startup to the time when this API is called (in bytes). This API uses a promise to return the result. > **NOTE：**> > If the application has not generated any traffic consumption after the restart, error code 2103005 will be > thrown.

**Since:** 23

**Required permissions:** 
- API version 26.0.0+: ohos.permission.GET_NETWORK_STATS

<!--Device-statistics-function getUidTxBytes(uid: int): Promise<long>--><!--Device-statistics-function getUidTxBytes(uid: int): Promise<long>-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uid | int | Yes | Application UID. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;long&gt; | Promise used to return the total uplink traffic (in bytes) of the specified application from the last startup to the time when the API is called. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. |
| [2100002](../errorcode-net-connection.md#2100002-service-connection-failure) | Failed to connect to the service. |
| [2100003](../errorcode-net-connection.md#2100003-system-internal-error) | System internal error. |
| [2103011](../errorcode-net-statistics.md#2103011-failed-to-create-a-system-map) | Failed to create a system map. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied.<br>**Applicable version:** 26.0.0 and later |
| [2103005](../errorcode-net-statistics.md#2103005-failed-to-read-the-system-map) | Failed to read the system map. |

**Examples**

```TypeScript
import { statistics } from '@kit.NetworkKit';

statistics.getUidTxBytes(20010038).then((stats: number) => {
  console.info(JSON.stringify(stats));
});
```

