# on_netUidRuleChange (System API)

## Modules to Import

```TypeScript
import { policy } from '@kit.NetworkKit';
```

## on('netUidRuleChange')

```TypeScript
function on(type: 'netUidRuleChange', callback: Callback<NetUidRuleInfo>): void
```

Registers the callback when the **rule** changes. This API uses an asynchronous callback to return the result.

**Since:** 10

**Required permissions:** ohos.permission.MANAGE_NET_STRATEGY

<!--Device-policy-function on(type: 'netUidRuleChange', callback: Callback<NetUidRuleInfo>): void--><!--Device-policy-function on(type: 'netUidRuleChange', callback: Callback<NetUidRuleInfo>): void-End-->

**System capability:** SystemCapability.Communication.NetManager.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'netUidRuleChange' | Yes | Event type.<br/> The value **netUidRuleChange** indicates a rule change event. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;[NetUidRuleInfo](arkts-network-policy-netuidruleinfo-i-sys.md)&gt; | Yes | Callback used to return the result. It is called when the rule changes.<br>**Since:** 11 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. |
| [2100001](../errorcode-net-connection.md#2100001-invalid-parameter-value) | Invalid parameter value. |
| [2100002](../errorcode-net-connection.md#2100002-service-connection-failure) | Failed to connect to the service. |
| [2100003](../errorcode-net-connection.md#2100003-system-internal-error) | System internal error. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Non-system applications use system APIs. |

