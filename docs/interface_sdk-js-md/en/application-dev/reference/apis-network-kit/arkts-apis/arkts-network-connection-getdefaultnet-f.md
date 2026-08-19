# getDefaultNet

## Modules to Import

```TypeScript
import { connection } from '@kit.NetworkKit';
```

## getDefaultNet

```TypeScript
function getDefaultNet(callback: AsyncCallback<NetHandle>): void
```

Obtains the network handle used by the system by default, including the network ID. This API uses an asynchronous callback to return the result. &gt; **NOTE：**&gt; &gt; - Default network used by the system. The network must have the &gt; [NET_CAPABILITY_INTERNET](arkts-network-connection-netcap-e.md) capability and is not a VPN network. &gt; &gt; - The return value of this interface is determined by the system and is irrelevant to whether the application &gt; specifies a network. &gt; &gt; - Generally, the priority is as follows: Ethernet (PC) | Bluetooth (watch) &gt; Wi-Fi &gt; Cellular. In special cases, &gt; the actual return result prevails. &gt; &gt; - [NetHandle](arkts-network-connection-nethandle-i.md) is the unique identifier of the network. If no network is available, &gt; **0** is returned. It can be used by [getNetCapabilities](arkts-network-connection-getnetcapabilities-f.md) to query more &gt; network information. &gt; **Required permission**: ohos.permission.GET_NETWORK_INFO

**Since:** 23

**Required permissions:** ohos.permission.GET_NETWORK_INFO

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-connection-function getDefaultNet(callback: AsyncCallback<NetHandle>): void--><!--Device-connection-function getDefaultNet(callback: AsyncCallback<NetHandle>): void-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;NetHandle&gt; | Yes | Callback used to return the result. When the network handle of the default activated network is successfully obtained, **error** is **undefined** and **data** is the network handle of the default network; otherwise, **error** is an error object. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. |
| [2100002](../errorcode-net-connection.md#2100002-service-connection-failure) | Failed to connect to the service. |
| [2100003](../errorcode-net-connection.md#2100003-system-internal-error) | System internal error. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |

**Examples**

```TypeScript
import { connection } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

connection.getDefaultNet((error: BusinessError, data: connection.NetHandle) => {
  if (error) {
    console.error(`Failed to get default net. Code:${error.code}, message:${error.message}`);
    return;
  }
  console.info("Succeeded to get data: " + JSON.stringify(data));
});
```


## getDefaultNet

```TypeScript
function getDefaultNet(): Promise<NetHandle>
```

Obtains the network handle used by the system by default, including the network ID. This API uses a promise to return the result. &gt; **NOTE：**&gt; &gt; - Default network used by the system. The network must have the &gt; [NET_CAPABILITY_INTERNET](arkts-network-connection-netcap-e.md) capability and is not a VPN network. &gt; &gt; - The return value of this interface is determined by the system and is irrelevant to whether the application &gt; specifies a network. &gt; &gt; - Generally, the priority is as follows: Ethernet (PC) | Bluetooth (watch) &gt; Wi-Fi &gt; Cellular. In special cases, &gt; the actual returned result prevails. &gt; &gt; - [NetHandle](arkts-network-connection-nethandle-i.md) is the unique identifier of the network. If no network is available, &gt; **0** is returned. It can be used by [getNetCapabilities](arkts-network-connection-getnetcapabilities-f.md) to query more &gt; network information. &gt; **Required permission**: ohos.permission.GET_NETWORK_INFO

**Since:** 23

**Required permissions:** ohos.permission.GET_NETWORK_INFO

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-connection-function getDefaultNet(): Promise<NetHandle>--><!--Device-connection-function getDefaultNet(): Promise<NetHandle>-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;NetHandle&gt; | Promise used to return the network handle of the default network. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [2100002](../errorcode-net-connection.md#2100002-service-connection-failure) | Failed to connect to the service. |
| [2100003](../errorcode-net-connection.md#2100003-system-internal-error) | System internal error. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |

**Examples**

```TypeScript
import { connection } from '@kit.NetworkKit';

connection.getDefaultNet().then((data: connection.NetHandle) => {
  console.info("Succeeded to get data: " + JSON.stringify(data));
});
```

