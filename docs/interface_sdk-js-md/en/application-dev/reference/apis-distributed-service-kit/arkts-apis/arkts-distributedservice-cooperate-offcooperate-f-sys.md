# off_cooperate (System API)

## Modules to Import

```TypeScript
import { cooperate } from '@kit.DistributedServiceKit';
```

## off_cooperate

```TypeScript
function off(type: 'cooperate', callback?: Callback<void>): void
```

Disables listening for screen hopping status change events.

**Since:** 10

**Deprecated since:** 11

**Substitutes:** [off](#offcooperate)(type: 'cooperateMessage', callback?: Callback&lt;CooperateMessage&gt;)

<!--Device-cooperate-function off(type: 'cooperate', callback?: Callback<void>): void--><!--Device-cooperate-function off(type: 'cooperate', callback?: Callback<void>): void-End-->

**System capability:** SystemCapability.Msdp.DeviceStatus.Cooperate

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'cooperate' | Yes | Event type. The value is **cooperate**. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | No | Callback to be unregistered. If this parameter is not specified, all callbacks registered by the current application will be unregistered. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: <br>1. Mandatory parameters are left unspecified. <br>2. Incorrect parameter types. <br>3. Parameter verification failed. |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Permission verification failed. A non-system application calls a system API. |

