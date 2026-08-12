# getIfaceConfig (System API)

## Modules to Import

```TypeScript
import { ethernet } from '@kit.NetworkKit';
```

## getIfaceConfig

```TypeScript
function getIfaceConfig(iface: string, callback: AsyncCallback<InterfaceConfiguration>): void
```

Get the specified network interface information.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Required permissions:** ohos.permission.GET_NETWORK_INFO

<!--Device-ethernet-function getIfaceConfig(iface: string, callback: AsyncCallback<InterfaceConfiguration>): void--><!--Device-ethernet-function getIfaceConfig(iface: string, callback: AsyncCallback<InterfaceConfiguration>): void-End-->

**System capability:** SystemCapability.Communication.NetManager.Ethernet

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| iface | string | Yes | Indicates the network interface name. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;[InterfaceConfiguration](arkts-network-ethernet-interfaceconfiguration-i-sys.md)&gt; | Yes | the callback of getIfaceConfig. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [2200001](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-network-kit/errorcode-net-ethernet.md#2200001-invalid-parameter-value) | Invalid parameter value. |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. |
| [2200003](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-network-kit/errorcode-net-ethernet.md#2200003-system-internal-error) | System internal error. |
| [2200002](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-network-kit/errorcode-net-ethernet.md#2200002-service-connection-failure) | Failed to connect to the service. |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Non-system applications use system APIs. |
| [2201005](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-network-kit/errorcode-net-ethernet.md#2201005-device-information-not-exist) | Device information does not exist. |

## Examples

```TypeScript
import { ethernet } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

ethernet.getIfaceConfig("eth0", (error: BusinessError, value: ethernet.InterfaceConfiguration) => {
  if (error) {
    console.error("getIfaceConfig  callback error = " + JSON.stringify(error));
  } else {
    console.info("getIfaceConfig callback mode = " + JSON.stringify(value.mode));
    console.info("getIfaceConfig callback ipAddr = " + JSON.stringify(value.ipAddr));
    console.info("getIfaceConfig callback route = " + JSON.stringify(value.route));
    console.info("getIfaceConfig callback gateway = " + JSON.stringify(value.gateway));
    console.info("getIfaceConfig callback netMask = " + JSON.stringify(value.netMask));
    console.info("getIfaceConfig callback dnsServers = " + JSON.stringify(value.dnsServers));
  }
});
```


## getIfaceConfig

```TypeScript
function getIfaceConfig(iface: string): Promise<InterfaceConfiguration>
```

Get the specified network interface information.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Required permissions:** ohos.permission.GET_NETWORK_INFO

<!--Device-ethernet-function getIfaceConfig(iface: string): Promise<InterfaceConfiguration>--><!--Device-ethernet-function getIfaceConfig(iface: string): Promise<InterfaceConfiguration>-End-->

**System capability:** SystemCapability.Communication.NetManager.Ethernet

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| iface | string | Yes | Indicates the network interface name. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[InterfaceConfiguration](arkts-network-ethernet-interfaceconfiguration-i-sys.md)&gt; | the promise returned by the function. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [2200001](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-network-kit/errorcode-net-ethernet.md#2200001-invalid-parameter-value) | Invalid parameter value. |
| [401](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. |
| [2200003](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-network-kit/errorcode-net-ethernet.md#2200003-system-internal-error) | System internal error. |
| [2200002](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-network-kit/errorcode-net-ethernet.md#2200002-service-connection-failure) | Failed to connect to the service. |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Non-system applications use system APIs. |
| [2201005](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-network-kit/errorcode-net-ethernet.md#2201005-device-information-not-exist) | Device information does not exist. |

## Examples

```TypeScript
import { ethernet } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

ethernet.getIfaceConfig("eth0").then((data: ethernet.InterfaceConfiguration) => {
  console.info("getIfaceConfig promise mode = " + JSON.stringify(data.mode));
  console.info("getIfaceConfig promise ipAddr = " + JSON.stringify(data.ipAddr));
  console.info("getIfaceConfig promise route = " + JSON.stringify(data.route));
  console.info("getIfaceConfig promise gateway = " + JSON.stringify(data.gateway));
  console.info("getIfaceConfig promise netMask = " + JSON.stringify(data.netMask));
  console.info("getIfaceConfig promise dnsServers = " + JSON.stringify(data.dnsServers));
}).catch((error: BusinessError) => {
  console.error("getIfaceConfig promise error = " + JSON.stringify(error));
});
```

