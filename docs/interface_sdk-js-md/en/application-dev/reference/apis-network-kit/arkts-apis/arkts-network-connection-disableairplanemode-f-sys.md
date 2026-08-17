# disableAirplaneMode (System API)

## Modules to Import

```TypeScript
import { connection } from 'connection';
```

## disableAirplaneMode

```TypeScript
function disableAirplaneMode(callback: AsyncCallback<void>): void
```

Disables the airplane mode for a device. To invoke this method, you must have the {@code ohos.permission.CONNECTIVITY_INTERNAL} permission.

**Since:** 23

**Required permissions:** ohos.permission.CONNECTIVITY_INTERNAL

<!--Device-connection-function disableAirplaneMode(callback: AsyncCallback<void>): void--><!--Device-connection-function disableAirplaneMode(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | the callback of disableAirplaneMode. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. |
| [2100002](../errorcode-net-connection.md#2100002-service-connection-failure) | Failed to connect to the service. |
| [2100003](../errorcode-net-connection.md#2100003-system-internal-error) | System internal error. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Non-system applications use system APIs. |

**Examples**

```TypeScript
import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

connection.disableAirplaneMode((error: BusinessError) => {
  console.error(JSON.stringify(error));
});
```


## disableAirplaneMode

```TypeScript
function disableAirplaneMode(): Promise<void>
```

Disables the airplane mode for a device. To invoke this method, you must have the {@code ohos.permission.CONNECTIVITY_INTERNAL} permission.

**Since:** 23

**Required permissions:** ohos.permission.CONNECTIVITY_INTERNAL

<!--Device-connection-function disableAirplaneMode(): Promise<void>--><!--Device-connection-function disableAirplaneMode(): Promise<void>-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | The promise returned by the function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [2100002](../errorcode-net-connection.md#2100002-service-connection-failure) | Failed to connect to the service. |
| [2100003](../errorcode-net-connection.md#2100003-system-internal-error) | System internal error. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Non-system applications use system APIs. |

**Examples**

```TypeScript
import { connection } from '@kit.NetworkKit';

connection.disableAirplaneMode().then((error: void) => {
  console.error(JSON.stringify(error));
});
```

