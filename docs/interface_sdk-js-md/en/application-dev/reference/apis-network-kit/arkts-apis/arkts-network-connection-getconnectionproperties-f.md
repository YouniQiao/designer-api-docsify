# getConnectionProperties

## Modules to Import

```TypeScript
import { connection } from '@kit.NetworkKit';
```

## getConnectionProperties

```TypeScript
function getConnectionProperties(netHandle: NetHandle, callback: AsyncCallback<ConnectionProperties>): void
```

Queries the connection properties of a network. This method requires the {@code ohos.permission.GET_NETWORK_INFO} permission.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Required permissions:** ohos.permission.GET_NETWORK_INFO

<!--Device-connection-function getConnectionProperties(netHandle: NetHandle, callback: AsyncCallback<ConnectionProperties>): void--><!--Device-connection-function getConnectionProperties(netHandle: NetHandle, callback: AsyncCallback<ConnectionProperties>): void-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| netHandle | NetHandle | Yes | Indicates the network to be queried. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[ConnectionProperties](arkts-network-connection-connectionproperties-i.md)&gt; | Yes | the callback of getConnectionProperties.[ConnectionProperties](arkts-network-connection-connectionproperties-i.md#ConnectionProperties). |

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

// Example: Obtain the connection information of the default network.
connection.getDefaultNet().then((netHandle: connection.NetHandle) => {
  if (netHandle.netId == 0) {
    // If no network is connected, the obtained netId of netHandle is 0, which is abnormal. You can add specific processing based on the service requirements.
    return;
  }
  connection.getConnectionProperties(netHandle, (error: BusinessError, data: connection.ConnectionProperties) => {
    if (error) {
      console.error(`Failed to get connection properties. Code:${error.code}, message:${error.message}`);
      return;
    }
    console.info("Succeeded to get data: " + JSON.stringify(data));
  })
});
```


## getConnectionProperties

```TypeScript
function getConnectionProperties(netHandle: NetHandle): Promise<ConnectionProperties>
```

Queries the connection properties of a network. This method requires the {@code ohos.permission.GET_NETWORK_INFO} permission.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

**Required permissions:** ohos.permission.GET_NETWORK_INFO

<!--Device-connection-function getConnectionProperties(netHandle: NetHandle): Promise<ConnectionProperties>--><!--Device-connection-function getConnectionProperties(netHandle: NetHandle): Promise<ConnectionProperties>-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| netHandle | NetHandle | Yes | Indicates the network to be queried. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[ConnectionProperties](arkts-network-connection-connectionproperties-i.md)&gt; | The promise returned by the function. |

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

connection.getDefaultNet().then((netHandle: connection.NetHandle) => {
  if (netHandle.netId == 0) {
    // If no network is connected, the obtained netId of netHandle is 0, which is abnormal. You can add specific processing based on the service requirements.
    return;
  }

  connection.getConnectionProperties(netHandle).then((data: connection.ConnectionProperties) => {
    console.info("Succeeded to get data: " + JSON.stringify(data));
  })
});
```

