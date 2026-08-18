# off_netUidRuleChange (System API)

## Modules to Import

```TypeScript
```

## off_netUidRuleChange

```TypeScript
function off(type: 'netUidRuleChange', callback?: Callback<NetUidRuleInfo>): void
```

Unregister uid rule change listener.

**Since:** 11

**Required permissions:** ohos.permission.MANAGE_NET_STRATEGY

<!--Device-policy-function off(type: 'netUidRuleChange', callback?: Callback<NetUidRuleInfo>): void--><!--Device-policy-function off(type: 'netUidRuleChange', callback?: Callback<NetUidRuleInfo>): void-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'netUidRuleChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[NetUidRuleInfo](arkts-network-policy-netuidruleinfo-i-sys.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [2100001](../errorcode-net-connection.md#2100001-invalid-parameter-value) |
| [2100002](../errorcode-net-connection.md#2100002-service-connection-failure) |
| [2100003](../errorcode-net-connection.md#2100003-system-internal-error) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
