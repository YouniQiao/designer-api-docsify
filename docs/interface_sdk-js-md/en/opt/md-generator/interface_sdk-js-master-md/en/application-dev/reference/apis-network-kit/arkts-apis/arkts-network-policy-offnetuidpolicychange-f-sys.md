# off_netUidPolicyChange (System API)

## Modules to Import

```TypeScript
import { policy } from '@kit.NetworkKit';
```

## off_netUidPolicyChange

```TypeScript
function off(type: 'netUidPolicyChange', callback?: Callback<NetUidPolicyInfo>): void
```

Unregister uid policy change listener.

**Since:** 11

**Deprecated since:** -1

**Required permissions:** ohos.permission.MANAGE_NET_STRATEGY

<!--Device-policy-function off(type: 'netUidPolicyChange', callback?: Callback<NetUidPolicyInfo>): void--><!--Device-policy-function off(type: 'netUidPolicyChange', callback?: Callback<NetUidPolicyInfo>): void-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'netUidPolicyChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[NetUidPolicyInfo](arkts-network-policy-netuidpolicyinfo-i-sys.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [2100001](../errorcode-net-connection.md#2100001-invalid-parameter-value) |
| [2100002](../errorcode-net-connection.md#2100002-service-connection-failure) |
| [2100003](../errorcode-net-connection.md#2100003-system-internal-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
