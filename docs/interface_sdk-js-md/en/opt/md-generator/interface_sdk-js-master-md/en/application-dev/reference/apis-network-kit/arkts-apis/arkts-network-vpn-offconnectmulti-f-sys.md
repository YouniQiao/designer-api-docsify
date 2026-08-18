# off_connectMulti (System API)

## Modules to Import

```TypeScript
```

## off_connectMulti

```TypeScript
function off(type: 'connectMulti', callback?: Callback<MultiVpnConnectState>): void
```

Unsubscribes from vpn connect state changes.

**Since:** 20

**Required permissions:** ohos.permission.MANAGE_VPN

<!--Device-vpn-function off(type: 'connectMulti', callback?: Callback<MultiVpnConnectState>): void--><!--Device-vpn-function off(type: 'connectMulti', callback?: Callback<MultiVpnConnectState>): void-End-->

**System capability:** SystemCapability.Communication.NetManager.Vpn

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'connectMulti' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;MultiVpnConnectState&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [19900002](../errorcode-net-vpn.md#19900002-system-internal-error) |
| [19900001](../errorcode-net-vpn.md#19900001-invalid-parameter) |
