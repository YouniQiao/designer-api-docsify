# on_cooperate (System API)

## Modules to Import

```TypeScript
import { cooperate } from '@kit.DistributedServiceKit';
```

## on_cooperate('cooperate')

```TypeScript
function on(type: 'cooperate', callback: Callback<{ networkId: string, msg: CooperateMsg }>): void
```

Enables listening for screen hopping status change events.

**Since:** 10

**Deprecated since:** 11

**Substitutes:** [on](#on_cooperatecooperate)(type: 'cooperateMessage', callback: Callback&lt;CooperateMessage&gt;)

<!--Device-cooperate-function on(type: 'cooperate', callback: Callback<{ networkId: string, msg: CooperateMsg }>): void--><!--Device-cooperate-function on(type: 'cooperate', callback: Callback<{ networkId: string, msg: CooperateMsg }>): void-End-->

**System capability:** SystemCapability.Msdp.DeviceStatus.Cooperate

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'cooperate' | Yes | Event type. The value is **cooperate**. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;{ networkId: string, msg: CooperateMsg }&gt; | Yes |  |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: <br>1. Mandatory parameters are left unspecified. <br>2. Incorrect parameter types. <br>3. Parameter verification failed. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |

