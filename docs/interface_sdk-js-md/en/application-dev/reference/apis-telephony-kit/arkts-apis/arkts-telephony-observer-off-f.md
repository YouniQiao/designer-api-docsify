# off

## Modules to Import

```TypeScript
import { observer } from 'kits/@kit.TelephonyKit';
```

## off('networkStateChange')

```TypeScript
function off(type: 'networkStateChange', callback?: Callback<NetworkState>): void
```

Unregisters the observer for network status change events. This API uses an asynchronous callback to return the execution result.

> **NOTE：**&gt;
> You can pass the callback of the **on** function if you want to cancel listening for a certain type of event. If
> you do not pass the callback, you will cancel listening for all events.

**Since:** 6

**System capability:** SystemCapability.Telephony.StateRegistry

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'networkStateChange' | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;NetworkState&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [8300001](../errorcode-telephony.md#8300001-input-parameter-value-out-of-range) |
| [8300002](../errorcode-telephony.md#8300002-service-connection-error) |
| [8300003](../errorcode-telephony.md#8300003-system-internal-error) |
| [8300999](../errorcode-telephony.md#8300999-internal-error) |


## off('signalInfoChange')

```TypeScript
function off(type: 'signalInfoChange', callback?: Callback<Array<SignalInformation>>): void
```

Unregisters the observer for signal status change events. This API uses an asynchronous callback to return the execution result.

> **NOTE：**&gt;
> You can pass the callback of the **on** function if you want to cancel listening for a certain type of event. If
> you do not pass the callback, you will cancel listening for all events.

**Since:** 6

**System capability:** SystemCapability.Telephony.StateRegistry

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'signalInfoChange' | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;SignalInformation&gt;&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [8300001](../errorcode-telephony.md#8300001-input-parameter-value-out-of-range) |
| [8300002](../errorcode-telephony.md#8300002-service-connection-error) |
| [8300003](../errorcode-telephony.md#8300003-system-internal-error) |
| [8300999](../errorcode-telephony.md#8300999-internal-error) |


## off('cellularDataConnectionStateChange')

```TypeScript
function off(type: 'cellularDataConnectionStateChange', callback?: Callback<DataConnectionStateInfo>): void
```

Unregisters the observer for connection status change events of the cellular data link. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> You can pass the callback of the **on** function if you want to cancel listening for a certain type of event. If
> you do not pass the callback, you will cancel listening for all events.

**Since:** 7

**System capability:** SystemCapability.Telephony.StateRegistry

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'cellularDataConnectionStateChange' | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[DataConnectionStateInfo](arkts-telephony-observer-dataconnectionstateinfo-i.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [8300001](../errorcode-telephony.md#8300001-input-parameter-value-out-of-range) |
| [8300002](../errorcode-telephony.md#8300002-service-connection-error) |
| [8300003](../errorcode-telephony.md#8300003-system-internal-error) |
| [8300999](../errorcode-telephony.md#8300999-internal-error) |


## off('cellularDataFlowChange')

```TypeScript
function off(type: 'cellularDataFlowChange', callback?: Callback<DataFlowType>): void
```

Unregisters the observer for the uplink and downlink data flow status change events of the cellular data service. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> You can pass the callback of the **on** function if you want to cancel listening for a certain type of event. If
> you do not pass the callback, you will cancel listening for all events.

**Since:** 7

**System capability:** SystemCapability.Telephony.StateRegistry

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'cellularDataFlowChange' | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;DataFlowType&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [8300001](../errorcode-telephony.md#8300001-input-parameter-value-out-of-range) |
| [8300002](../errorcode-telephony.md#8300002-service-connection-error) |
| [8300003](../errorcode-telephony.md#8300003-system-internal-error) |
| [8300999](../errorcode-telephony.md#8300999-internal-error) |


## off('callStateChange')

```TypeScript
function off(type: 'callStateChange', callback?: Callback<CallStateInfo>): void
```

Unregisters the observer for call status change events. This API uses an asynchronous callback to return the execution result.

> **NOTE：**&gt;
> You can pass the callback of the **on** function if you want to cancel listening for a certain type of event. If
> you do not pass the callback, you will cancel listening for all events.

**Since:** 6

**System capability:** SystemCapability.Telephony.StateRegistry

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'callStateChange' | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[CallStateInfo](arkts-telephony-observer-callstateinfo-i.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [8300001](../errorcode-telephony.md#8300001-input-parameter-value-out-of-range) |
| [8300002](../errorcode-telephony.md#8300002-service-connection-error) |
| [8300003](../errorcode-telephony.md#8300003-system-internal-error) |
| [8300999](../errorcode-telephony.md#8300999-internal-error) |


## off('callStateChangeEx')

```TypeScript
function off(type: 'callStateChangeEx', callback?: Callback<TelCallState>): void
```

Unregisters the observer for extended call status change events. This API uses an asynchronous callback to return the execution result.

> **NOTE：**&gt;
> You can pass the callback of the **on** function if you want to cancel listening for a certain type of event. If
> you do not pass the callback, you will cancel listening for all events.

**Since:** 21

**System capability:** SystemCapability.Telephony.StateRegistry

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'callStateChangeEx' | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;TelCallState&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [8800001](../errorcode-telephony.md#8800001-input-parameter-value-out-of-range) |
| [8800002](../errorcode-telephony.md#8800002-service-connection-error) |
| [8800003](../errorcode-telephony.md#8800003-system-internal-error) |
| [8800999](../errorcode-telephony.md#8800999-internal-error) |


## off('simStateChange')

```TypeScript
function off(type: 'simStateChange', callback?: Callback<SimStateData>): void
```

Unregisters the observer for SIM card status change events. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> You can pass the callback of the **on** function if you want to cancel listening for a certain type of event. If
> you do not pass the callback, you will cancel listening for all events.

**Since:** 7

**System capability:** SystemCapability.Telephony.StateRegistry

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'simStateChange' | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[SimStateData](arkts-telephony-observer-simstatedata-i.md)&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [8300001](../errorcode-telephony.md#8300001-input-parameter-value-out-of-range) |
| [8300002](../errorcode-telephony.md#8300002-service-connection-error) |
| [8300003](../errorcode-telephony.md#8300003-system-internal-error) |
| [8300999](../errorcode-telephony.md#8300999-internal-error) |


## off('iccAccountInfoChange')

```TypeScript
function off(type: 'iccAccountInfoChange', callback?: Callback<void>): void
```

Unregisters the observer for account information change events of the SIM card. This API uses an asynchronous callback to return the result.

> **NOTE：**&gt;
> You can pass the callback of the **on** function if you want to cancel listening for a certain type of event. If
> you do not pass the callback, you will cancel listening for all events.

**Since:** 10

**System capability:** SystemCapability.Telephony.StateRegistry

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'iccAccountInfoChange' | Yes |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | No |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [8300001](../errorcode-telephony.md#8300001-input-parameter-value-out-of-range) |
| [8300002](../errorcode-telephony.md#8300002-service-connection-error) |
| [8300003](../errorcode-telephony.md#8300003-system-internal-error) |
| [8300999](../errorcode-telephony.md#8300999-internal-error) |
