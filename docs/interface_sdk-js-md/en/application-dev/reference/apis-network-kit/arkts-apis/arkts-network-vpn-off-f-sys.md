# off (System API)

## Modules to Import

```TypeScript
import { vpn } from 'kits/@kit.NetworkKit';
```

## off('connect')

```TypeScript
function off(type: 'connect', callback?: Callback<VpnConnectState>): void
```

Unsubscribes from vpn connect state changes.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn only, since version 12.

**Required permissions:** ohos.permission.MANAGE_VPN

<!--Device-vpn-function off(type: 'connect', callback?: Callback<VpnConnectState>): void--><!--Device-vpn-function off(type: 'connect', callback?: Callback<VpnConnectState>): void-End-->

**System capability:** SystemCapability.Communication.NetManager.Vpn

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'connect' | Yes | Indicates vpn connect state changes. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;VpnConnectState&gt; | No | The callback of the vpn connect state. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 2200001 | Invalid parameter value. |
| 401 | Parameter error. |
| 2200003 | System internal error. |
| 2200002 | Operation failed. Cannot connect to service. |
| 201 | Permission denied. |
| 202 | Non-system applications use system APIs. |


## off('connectMulti')

```TypeScript
function off(type: 'connectMulti', callback?: Callback<MultiVpnConnectState>): void
```

Unsubscribes from vpn connect state changes.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn only, since version 20.

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
| 201 | Permission denied. |
| 202 | Non-system applications use system APIs. |
| 19900002 | System internal error. |
| 19900001 | Invalid parameter value. |

