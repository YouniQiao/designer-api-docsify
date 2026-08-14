# getStatsRxBytes (System API)

## Modules to Import

```TypeScript
import { sharing } from 'sharing';
```

## getStatsRxBytes

```TypeScript
function getStatsRxBytes(callback: AsyncCallback<int>): void
```

Obtains the number of downlink data bytes of the sharing network interfaces.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Required permissions:** ohos.permission.CONNECTIVITY_INTERNAL

<!--Device-sharing-function getStatsRxBytes(callback: AsyncCallback<int>): void--><!--Device-sharing-function getStatsRxBytes(callback: AsyncCallback<int>): void-End-->

**System capability:** SystemCapability.Communication.NetManager.NetSharing

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;int&gt; | Yes | Returns the number of downlink data bytes of the sharing network interfaces. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. |
| [2200003](../errorcode-net-ethernet.md#2200003-system-internal-error) | System internal error. |
| [2200002](../errorcode-net-ethernet.md#2200002-service-connection-failure) | Failed to connect to the service. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Non-system applications use system APIs. |

## Examples

```TypeScript
import { sharing } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

sharing.getStatsRxBytes((error: BusinessError, data: number) => {
  console.error(JSON.stringify(error));
  console.info(JSON.stringify(data));
});
```


## getStatsRxBytes

```TypeScript
function getStatsRxBytes(): Promise<int>
```

Obtains the number of downlink data bytes of the sharing network interfaces.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Required permissions:** ohos.permission.CONNECTIVITY_INTERNAL

<!--Device-sharing-function getStatsRxBytes(): Promise<int>--><!--Device-sharing-function getStatsRxBytes(): Promise<int>-End-->

**System capability:** SystemCapability.Communication.NetManager.NetSharing

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;int&gt; | The promise returned by the function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. |
| [2200003](../errorcode-net-ethernet.md#2200003-system-internal-error) | System internal error. |
| [2200002](../errorcode-net-ethernet.md#2200002-service-connection-failure) | Failed to connect to the service. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Non-system applications use system APIs. |

## Examples

```TypeScript
import { sharing } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

sharing
  .getStatsRxBytes()
  .then((data: number) => {
    console.info(JSON.stringify(data));
  })
  .catch((error: BusinessError) => {
    console.error(JSON.stringify(error));
  });
```

