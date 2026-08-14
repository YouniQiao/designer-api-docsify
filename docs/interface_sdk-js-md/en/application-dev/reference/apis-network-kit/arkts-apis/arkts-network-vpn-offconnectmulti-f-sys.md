# off_connectMulti (System API)

## Modules to Import

```TypeScript
import { vpn } from 'vpn';
```

## off_connectMulti

```TypeScript
function off(type: 'connectMulti', callback?: Callback<MultiVpnConnectState>): void
```

Unsubscribes from vpn connect state changes.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

**Deprecated since:** -1

**Required permissions:** ohos.permission.MANAGE_VPN

<!--Device-vpn-function off(type: 'connectMulti', callback?: Callback<MultiVpnConnectState>): void--><!--Device-vpn-function off(type: 'connectMulti', callback?: Callback<MultiVpnConnectState>): void-End-->

**System capability:** SystemCapability.Communication.NetManager.Vpn

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'connectMulti' | Yes | Indicates multi vpn connect state changes. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;MultiVpnConnectState&gt; | No | The callback of the multi vpn connect state. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Non-system applications use system APIs. |
| [19900002](../errorcode-net-vpn.md#19900002-system-internal-error) | System internal error. |
| [19900001](../errorcode-net-vpn.md#19900001-invalid-parameter) | Invalid parameter value. |

