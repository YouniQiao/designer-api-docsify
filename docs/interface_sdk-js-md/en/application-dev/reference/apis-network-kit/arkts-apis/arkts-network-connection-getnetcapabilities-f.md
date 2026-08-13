# getNetCapabilities

## Modules to Import

```TypeScript
import { connection } from '@kit.NetworkKit';
```

## getNetCapabilities

```TypeScript
function getNetCapabilities(netHandle: NetHandle, callback: AsyncCallback<NetCapabilities>): void
```

Obtains [NetCapabilities](arkts-network-connection-netcapabilities-i.md#NetCapabilities) of a [NetHandle](arkts-network-connection-nethandle-i.md#NetHandle) object. To invoke this method, you must have the {@code ohos.permission.GET_NETWORK_INFO} permission.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Required permissions:** ohos.permission.GET_NETWORK_INFO

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-connection-function getNetCapabilities(netHandle: NetHandle, callback: AsyncCallback<NetCapabilities>): void--><!--Device-connection-function getNetCapabilities(netHandle: NetHandle, callback: AsyncCallback<NetCapabilities>): void-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| netHandle | NetHandle | Yes | Indicates the handle. See [NetHandle](arkts-network-connection-nethandle-i.md#NetHandle). |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[NetCapabilities](arkts-network-connection-netcapabilities-i.md)&gt; | Yes | the callback of getNetCapabilities.[NetCapabilities](arkts-network-connection-netcapabilities-i.md#NetCapabilities). |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. |
| [2100001](../errorcode-net-connection.md#2100001-invalid-parameter-value) | Invalid parameter value. |
| [2100002](../errorcode-net-connection.md#2100002-service-connection-failure) | Failed to connect to the service. |
| [2100003](../errorcode-net-connection.md#2100003-system-internal-error) | System internal error. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |

## Examples

```TypeScript
import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

connection.getDefaultNet().then((netHandle: connection.NetHandle) => {
  if (netHandle.netId == 0) {
    // If no network is connected, the obtained netId of netHandle is 0, which is abnormal. You can add specific processing based on the service requirements.
    return;
  }
  connection.getNetCapabilities(netHandle, (error: BusinessError, data: connection.NetCapabilities) => {
    if (error) {
      console.error(`Failed to get net capabilities. Code:${error.code}, message:${error.message}`);
      return;
    }
    console.info("Succeeded to get data: " + JSON.stringify(data));
  })
}).catch((error: BusinessError) => {
    console.error(JSON.stringify(error));
});
```


## getNetCapabilities

```TypeScript
function getNetCapabilities(netHandle: NetHandle): Promise<NetCapabilities>
```

Obtains [NetCapabilities](arkts-network-connection-netcapabilities-i.md#NetCapabilities) of a [NetHandle](arkts-network-connection-nethandle-i.md#NetHandle) object. To invoke this method, you must have the {@code ohos.permission.GET_NETWORK_INFO} permission.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Required permissions:** ohos.permission.GET_NETWORK_INFO

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-connection-function getNetCapabilities(netHandle: NetHandle): Promise<NetCapabilities>--><!--Device-connection-function getNetCapabilities(netHandle: NetHandle): Promise<NetCapabilities>-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| netHandle | NetHandle | Yes | Indicates the handle. See [NetHandle](arkts-network-connection-nethandle-i.md#NetHandle). |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[NetCapabilities](arkts-network-connection-netcapabilities-i.md)&gt; | The promise returned by the function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. |
| [2100001](../errorcode-net-connection.md#2100001-invalid-parameter-value) | Invalid parameter value. |
| [2100002](../errorcode-net-connection.md#2100002-service-connection-failure) | Failed to connect to the service. |
| [2100003](../errorcode-net-connection.md#2100003-system-internal-error) | System internal error. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |

## Examples

```TypeScript
import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

connection.getDefaultNet().then((netHandle: connection.NetHandle) => {
  if (netHandle.netId == 0) {
    // If no network is connected, the obtained netId of netHandle is 0, which is abnormal. You can add specific processing based on the service requirements.
    return;
  }
  connection.getNetCapabilities(netHandle).then((data: connection.NetCapabilities) => {
      console.info("Succeeded to get data: " + JSON.stringify(data));
  })
}).catch((error: BusinessError) => {
    console.error(JSON.stringify(error));
});
```

