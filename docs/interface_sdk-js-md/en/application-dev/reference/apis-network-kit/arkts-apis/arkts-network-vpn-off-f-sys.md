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

**Required permissions:** ohos.permission.MANAGE_VPN

**System capability:** SystemCapability.Communication.NetManager.Vpn

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'connect' | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;VpnConnectState&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [2200001](../errorcode-net-ethernet.md#2200001-invalid-parameter-value) |
| [2200002](../errorcode-net-ethernet.md#2200002-service-connection-failure) |
| [2200003](../errorcode-net-ethernet.md#2200003-system-internal-error) |


## off('connectMulti')

```TypeScript
function off(type: 'connectMulti', callback?: Callback<MultiVpnConnectState>): void
```

Unsubscribes from vpn connect state changes.

**Since:** 20

**Required permissions:** ohos.permission.MANAGE_VPN

**System capability:** SystemCapability.Communication.NetManager.Vpn

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'connectMulti' | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;MultiVpnConnectState&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [19900001](../errorcode-net-vpn.md#19900001-invalid-parameter) |
| [19900002](../errorcode-net-vpn.md#19900002-system-internal-error) |
