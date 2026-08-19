# onSignalInfoChange

## Modules to Import

```TypeScript
import { observer } from '@kit.TelephonyKit';
```

## onSignalInfoChange

```TypeScript
function onSignalInfoChange(callback: Callback<Array<SignalInformation>>): void
```

Callback when the signal strength corresponding to the default sim card is updated.

**Since:** 23

<!--Device-observer-function onSignalInfoChange(callback: Callback<Array<SignalInformation>>): void--><!--Device-observer-function onSignalInfoChange(callback: Callback<Array<SignalInformation>>): void-End-->

**System capability:** SystemCapability.Telephony.StateRegistry

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;Array&lt;SignalInformation&gt;&gt; | Yes | Indicates the callback for getting an array of instances of the classes derived from [SignalInformation](arkts-telephony-observer-signalinformation-t.md). |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| [8300999](../errorcode-telephony.md#8300999-internal-error) | Unknown error. |
| [8300002](../errorcode-telephony.md#8300002-service-connection-error) | Service connection failed. |
| [8300003](../errorcode-telephony.md#8300003-system-internal-error) | System internal error. |
| [8300001](../errorcode-telephony.md#8300001-input-parameter-value-out-of-range) | Invalid parameter value. |


## onSignalInfoChange

```TypeScript
function onSignalInfoChange(options: ObserverOptions, callback: Callback<Array<SignalInformation>>): void
```

Callback when the signal strength corresponding to a monitored {@code slotId} is updated.

**Since:** 23

<!--Device-observer-function onSignalInfoChange(options: ObserverOptions, callback: Callback<Array<SignalInformation>>): void--><!--Device-observer-function onSignalInfoChange(options: ObserverOptions, callback: Callback<Array<SignalInformation>>): void-End-->

**System capability:** SystemCapability.Telephony.StateRegistry

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | ObserverOptions | Yes | Indicates the options for observer. |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-callback-t.md)&lt;Array&lt;SignalInformation&gt;&gt; | Yes | Indicates the callback for getting an array of instances of the classes derived from [SignalInformation](arkts-telephony-observer-signalinformation-t.md). |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| [8300999](../errorcode-telephony.md#8300999-internal-error) | Unknown error. |
| [8300002](../errorcode-telephony.md#8300002-service-connection-error) | Service connection failed. |
| [8300003](../errorcode-telephony.md#8300003-system-internal-error) | System internal error. |
| [8300001](../errorcode-telephony.md#8300001-input-parameter-value-out-of-range) | Invalid parameter value. |

