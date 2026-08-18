# off_connect (System API)

## Modules to Import

```TypeScript
import { vpn } from '@kit.NetworkKit';
import { vpnExtension } from '@kit.NetworkKit';
```

## off_connect('connect')

```TypeScript
function off(type: 'connect', callback?: Callback<VpnConnectState>): void
```

Unsubscribes from vpn connect state changes.

**Since:** 12

**Required permissions:** ohos.permission.MANAGE_VPN

<!--Device-vpn-function off(type: 'connect', callback?: Callback<VpnConnectState>): void--><!--Device-vpn-function off(type: 'connect', callback?: Callback<VpnConnectState>): void-End-->

**System capability:** SystemCapability.Communication.NetManager.Vpn

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'connect' | Yes | Indicates vpn connect state changes. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;VpnConnectState&gt; | No | The callback of the vpn connect state. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [2200001](../errorcode-net-ethernet.md#2200001-invalid-parameter-value) | Invalid parameter value. |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. |
| [2200003](../errorcode-net-ethernet.md#2200003-system-internal-error) | System internal error. |
| [2200002](../errorcode-net-ethernet.md#2200002-service-connection-failure) | Operation failed. Cannot connect to service. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Non-system applications use system APIs. |

