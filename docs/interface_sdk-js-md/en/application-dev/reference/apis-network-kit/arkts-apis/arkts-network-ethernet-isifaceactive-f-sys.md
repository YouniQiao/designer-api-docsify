# isIfaceActive (System API)

## Modules to Import

```TypeScript
import { ethernet } from 'kits/@kit.NetworkKit';
```

## isIfaceActive

```TypeScript
function isIfaceActive(iface: string, callback: AsyncCallback<number>): void
```

Check whether the specified network is active.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Required permissions:** ohos.permission.GET_NETWORK_INFO

<!--Device-ethernet-function isIfaceActive(iface: string, callback: AsyncCallback<number>): void--><!--Device-ethernet-function isIfaceActive(iface: string, callback: AsyncCallback<number>): void-End-->

**System capability:** SystemCapability.Communication.NetManager.Ethernet

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| iface | string | Yes | Indicates the network interface name. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes | the callback of isIfaceActive. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 2200001 | Invalid parameter value. |
| 401 | Parameter error. |
| 2200003 | System internal error. |
| 2200002 | Failed to connect to the service. |
| 201 | Permission denied. |
| 202 | Non-system applications use system APIs. |
| 2201005 | Device information does not exist. |

## Examples

```TypeScript
import { ethernet } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

ethernet.isIfaceActive("eth0", (error: BusinessError, value: number) => {
  if (error) {
    console.error("whether2Activate callback error = " + JSON.stringify(error));
  } else {
    console.info("whether2Activate callback = " + JSON.stringify(value));
  }
});
```


## isIfaceActive

```TypeScript
function isIfaceActive(iface: string): Promise<number>
```

Check whether the specified network is active.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Required permissions:** ohos.permission.GET_NETWORK_INFO

<!--Device-ethernet-function isIfaceActive(iface: string): Promise<number>--><!--Device-ethernet-function isIfaceActive(iface: string): Promise<number>-End-->

**System capability:** SystemCapability.Communication.NetManager.Ethernet

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| iface | string | Yes | Indicates the network interface name. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;number&gt; | the promise returned by the function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 2200001 | Invalid parameter value. |
| 401 | Parameter error. |
| 2200003 | System internal error. |
| 2200002 | Failed to connect to the service. |
| 201 | Permission denied. |
| 202 | Non-system applications use system APIs. |
| 2201005 | Device information does not exist. |

## Examples

```TypeScript
import { ethernet } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

ethernet.isIfaceActive("eth0").then((data: number) => {
  console.info("isIfaceActive promise = " + JSON.stringify(data));
}).catch((error: BusinessError) => {
  console.error("isIfaceActive promise error = " + JSON.stringify(error));
});
```

