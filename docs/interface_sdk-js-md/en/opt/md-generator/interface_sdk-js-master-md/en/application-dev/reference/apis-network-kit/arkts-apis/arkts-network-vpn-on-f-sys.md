# on (System API)

## Modules to Import

```TypeScript
import { vpn } from 'kits/@kit.NetworkKit';
```

## on('connect')

```TypeScript
function on(type: 'connect', callback: Callback<VpnConnectState>): void
```

Subscribes to vpn connect state changes.

**Since:** 12

**Required permissions:** ohos.permission.MANAGE_VPN

<!--Device-vpn-function on(type: 'connect', callback: Callback<VpnConnectState>): void--><!--Device-vpn-function on(type: 'connect', callback: Callback<VpnConnectState>): void-End-->

**System capability:** SystemCapability.Communication.NetManager.Vpn

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'connect' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;VpnConnectState&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [2200001](../errorcode-net-sharing.md#2200001-invalid-parameter-value) |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [2200003](../errorcode-net-sharing.md#2200003-system-internal-error) |
| [2200002](../errorcode-net-sharing.md#2200002-service-connection-failure) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |


## on('connectMulti')

```TypeScript
function on(type: 'connectMulti', callback: Callback<MultiVpnConnectState>): void
```

Subscribes to vpn connect state changes.

**Since:** 20

**Required permissions:** ohos.permission.MANAGE_VPN

<!--Device-vpn-function on(type: 'connectMulti', callback: Callback<MultiVpnConnectState>): void--><!--Device-vpn-function on(type: 'connectMulti', callback: Callback<MultiVpnConnectState>): void-End-->

**System capability:** SystemCapability.Communication.NetManager.Vpn

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'connectMulti' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;MultiVpnConnectState&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [19900002](../errorcode-net-vpn.md#19900002-system-internal-error) |
| [19900001](../errorcode-net-vpn.md#19900001-invalid-parameter) |
