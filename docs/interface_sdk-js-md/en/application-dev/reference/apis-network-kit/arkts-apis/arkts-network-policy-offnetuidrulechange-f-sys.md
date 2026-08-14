# off_netUidRuleChange (System API)

## Modules to Import

```TypeScript
import { policy } from 'policy';
```

## off_netUidRuleChange

```TypeScript
function off(type: 'netUidRuleChange', callback?: Callback<NetUidRuleInfo>): void
```

Unregister uid rule change listener.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Deprecated since:** -1

**Required permissions:** ohos.permission.MANAGE_NET_STRATEGY

<!--Device-policy-function off(type: 'netUidRuleChange', callback?: Callback<NetUidRuleInfo>): void--><!--Device-policy-function off(type: 'netUidRuleChange', callback?: Callback<NetUidRuleInfo>): void-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'netUidRuleChange' | Yes | Indicates Event name. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[NetUidRuleInfo](arkts-network-policy-netuidruleinfo-i-sys.md)&gt; | No | the callback of off. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. |
| [2100001](../errorcode-net-connection.md#2100001-invalid-parameter-value) | Invalid parameter value. |
| [2100002](../errorcode-net-connection.md#2100002-service-connection-failure) | Failed to connect to the service. |
| [2100003](../errorcode-net-connection.md#2100003-system-internal-error) | System internal error. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Non-system applications use system APIs. |

