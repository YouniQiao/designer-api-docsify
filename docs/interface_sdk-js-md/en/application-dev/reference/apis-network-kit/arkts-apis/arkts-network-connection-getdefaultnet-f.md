# getDefaultNet

## Modules to Import

```TypeScript
import { connection } from '@kit.NetworkKit';
```

## getDefaultNet

```TypeScript
function getDefaultNet(callback: AsyncCallback<NetHandle>): void
```

Obtains the network handle used by the system by default, including the network ID. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> - Default network used by the system. The network must have the
> [NET_CAPABILITY_INTERNET](arkts-network-connection-netcap-e.md) capability and is not a VPN network.&gt;
> - The return value of this interface is determined by the system and is irrelevant to whether the application
> specifies a network.&gt;
> - Generally, the priority is as follows: Ethernet (PC) | Bluetooth (watch)
> Wi-Fi
> Cellular. In special cases,
> the actual return result prevails.&gt;
> - [NetHandle](arkts-network-connection-nethandle-i.md) is the unique identifier of the network. If no network is available,
> **0** is returned. It can be used by [getNetCapabilities](arkts-network-connection-getnetcapabilities-f.md) to query more
> network information.
> **Required permission**: ohos.permission.GET_NETWORK_INFO

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.GET_NETWORK_INFO

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Communication.NetManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;NetHandle&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [2100002](../errorcode-net-connection.md#2100002-service-connection-failure) |
| [2100003](../errorcode-net-connection.md#2100003-system-internal-error) |

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

```TypeScript
import { connection } from '@kit.NetworkKit';

connection.getDefaultNet().then((data: connection.NetHandle) => {
  console.info("Succeeded to get data: " + JSON.stringify(data));
});
```


## getDefaultNet

```TypeScript
function getDefaultNet(): Promise<NetHandle>
```

Obtains the network handle used by the system by default, including the network ID. This API uses a promise to return the result.

> **NOTE：**&gt;
> - Default network used by the system. The network must have the
> [NET_CAPABILITY_INTERNET](arkts-network-connection-netcap-e.md) capability and is not a VPN network.&gt;
> - The return value of this interface is determined by the system and is irrelevant to whether the application
> specifies a network.&gt;
> - Generally, the priority is as follows: Ethernet (PC) | Bluetooth (watch)
> Wi-Fi
> Cellular. In special cases,
> the actual returned result prevails.&gt;
> - [NetHandle](arkts-network-connection-nethandle-i.md) is the unique identifier of the network. If no network is available,
> **0** is returned. It can be used by [getNetCapabilities](arkts-network-connection-getnetcapabilities-f.md) to query more
> network information.
> **Required permission**: ohos.permission.GET_NETWORK_INFO

**Since:** 8

**ArkTS mode:** ArkTS-Dyn since version 8; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.GET_NETWORK_INFO

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Communication.NetManager.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;NetHandle & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [2100002](../errorcode-net-connection.md#2100002-service-connection-failure) |
| [2100003](../errorcode-net-connection.md#2100003-system-internal-error) |

**Examples**

See [getDefaultNet](#getdefaultnet)
