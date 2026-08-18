# offCallStateChangeEx

## Modules to Import

```TypeScript
```

## offCallStateChangeEx

```TypeScript
function offCallStateChangeEx(callback?: Callback<TelCallState>): void
```

Cancel callback when the telCall state is updated.

**Since:** 23

<!--Device-observer-function offCallStateChangeEx(callback?: Callback<TelCallState>): void--><!--Device-observer-function offCallStateChangeEx(callback?: Callback<TelCallState>): void-End-->

**System capability:** SystemCapability.Telephony.StateRegistry

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;TelCallState&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [8800999](../errorcode-telephony.md#8800999-internal-error) |
| [8800002](../errorcode-telephony.md#8800002-service-connection-error) |
| [8800003](../errorcode-telephony.md#8800003-system-internal-error) |
| [8800001](../errorcode-telephony.md#8800001-input-parameter-value-out-of-range) |
