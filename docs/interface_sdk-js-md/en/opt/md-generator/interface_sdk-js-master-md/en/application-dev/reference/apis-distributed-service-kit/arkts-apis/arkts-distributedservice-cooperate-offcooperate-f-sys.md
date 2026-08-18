# off_cooperate (System API)

## Modules to Import

```TypeScript
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

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'cooperate' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
