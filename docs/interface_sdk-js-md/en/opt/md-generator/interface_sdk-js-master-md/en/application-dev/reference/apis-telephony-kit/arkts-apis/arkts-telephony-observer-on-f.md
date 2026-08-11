# on

## Modules to Import

```TypeScript
import { observer } from 'kits/@kit.TelephonyKit';
```

## on('networkStateChange')

```TypeScript
function on(type: 'networkStateChange', callback: Callback<NetworkState>): void
```

Callback when the network state corresponding to the default sim card is updated.

**Since:** 6

**Required permissions:** ohos.permission.GET_NETWORK_INFO

<!--Device-observer-function on(type: 'networkStateChange', callback: Callback<NetworkState>): void--><!--Device-observer-function on(type: 'networkStateChange', callback: Callback<NetworkState>): void-End-->

**System capability:** SystemCapability.Telephony.StateRegistry

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'networkStateChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;NetworkState&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [8300999](../errorcode-telephony.md#8300999-internal-error) |
| [8300002](../errorcode-telephony.md#8300002-service-connection-error) |
| [8300003](../errorcode-telephony.md#8300003-system-internal-error) |
| [8300001](../errorcode-telephony.md#8300001-input-parameter-value-out-of-range) |

## Examples

```TypeScript
observer.on('networkStateChange', (data: observer.NetworkState) => {
    console.info("on networkStateChange, data:" + JSON.stringify(data));
});
```


## on('networkStateChange')

```TypeScript
function on(type: 'networkStateChange', options: ObserverOptions, callback: Callback<NetworkState>): void
```

Callback when the network state corresponding to the monitored {@code slotId} is updated.

**Since:** 11

**Required permissions:** ohos.permission.GET_NETWORK_INFO

<!--Device-observer-function on(type: 'networkStateChange', options: ObserverOptions, callback: Callback<NetworkState>): void--><!--Device-observer-function on(type: 'networkStateChange', options: ObserverOptions, callback: Callback<NetworkState>): void-End-->

**System capability:** SystemCapability.Telephony.StateRegistry

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'networkStateChange' | Yes |
| options | [ObserverOptions](arkts-telephony-observer-observeroptions-i.md) | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;NetworkState&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [8300999](../errorcode-telephony.md#8300999-internal-error) |
| [8300002](../errorcode-telephony.md#8300002-service-connection-error) |
| [8300003](../errorcode-telephony.md#8300003-system-internal-error) |
| [8300001](../errorcode-telephony.md#8300001-input-parameter-value-out-of-range) |

## Examples

```TypeScript
let options: observer.ObserverOptions = {
    slotId: 0
}
observer.on('networkStateChange', options, (data: observer.NetworkState) => {
    console.info("on networkStateChange, data:" + JSON.stringify(data));
});
```


## on('signalInfoChange')

```TypeScript
function on(type: 'signalInfoChange', callback: Callback<Array<SignalInformation>>): void
```

Callback when the signal strength corresponding to the default sim card is updated.

**Since:** 6

<!--Device-observer-function on(type: 'signalInfoChange', callback: Callback<Array<SignalInformation>>): void--><!--Device-observer-function on(type: 'signalInfoChange', callback: Callback<Array<SignalInformation>>): void-End-->

**System capability:** SystemCapability.Telephony.StateRegistry

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'signalInfoChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;SignalInformation&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [8300999](../errorcode-telephony.md#8300999-internal-error) |
| [8300002](../errorcode-telephony.md#8300002-service-connection-error) |
| [8300003](../errorcode-telephony.md#8300003-system-internal-error) |
| [8300001](../errorcode-telephony.md#8300001-input-parameter-value-out-of-range) |

## Examples

```TypeScript
import { radio } from '@kit.TelephonyKit';

observer.on('signalInfoChange', (data: Array<radio.SignalInformation>) => {
    console.info("on signalInfoChange, data:" + JSON.stringify(data));
});
```


## on('signalInfoChange')

```TypeScript
function on(type: 'signalInfoChange', options: ObserverOptions, callback: Callback<Array<SignalInformation>>): void
```

Callback when the signal strength corresponding to a monitored {@code slotId} is updated.

**Since:** 11

<!--Device-observer-function on(type: 'signalInfoChange', options: ObserverOptions, callback: Callback<Array<SignalInformation>>): void--><!--Device-observer-function on(type: 'signalInfoChange', options: ObserverOptions, callback: Callback<Array<SignalInformation>>): void-End-->

**System capability:** SystemCapability.Telephony.StateRegistry

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'signalInfoChange' | Yes |
| options | [ObserverOptions](arkts-telephony-observer-observeroptions-i.md) | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;SignalInformation&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [8300999](../errorcode-telephony.md#8300999-internal-error) |
| [8300002](../errorcode-telephony.md#8300002-service-connection-error) |
| [8300003](../errorcode-telephony.md#8300003-system-internal-error) |
| [8300001](../errorcode-telephony.md#8300001-input-parameter-value-out-of-range) |

## Examples

```TypeScript
import { radio } from '@kit.TelephonyKit';

let options: observer.ObserverOptions = {
    slotId: 0
}
observer.on('signalInfoChange', options, (data: Array<radio.SignalInformation>) => {
    console.info("on signalInfoChange, data:" + JSON.stringify(data));
});
```


## on('cellularDataConnectionStateChange')

```TypeScript
function on(type: 'cellularDataConnectionStateChange', callback: Callback<DataConnectionStateInfo>): void
```

Callback when the cellular data link connection state corresponding to the default sim card is updated.

**Since:** 11

<!--Device-observer-function on(type: 'cellularDataConnectionStateChange', callback: Callback<DataConnectionStateInfo>): void--><!--Device-observer-function on(type: 'cellularDataConnectionStateChange', callback: Callback<DataConnectionStateInfo>): void-End-->

**System capability:** SystemCapability.Telephony.StateRegistry

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'cellularDataConnectionStateChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;DataConnectionStateInfo&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [8300999](../errorcode-telephony.md#8300999-internal-error) |
| [8300002](../errorcode-telephony.md#8300002-service-connection-error) |
| [8300003](../errorcode-telephony.md#8300003-system-internal-error) |
| [8300001](../errorcode-telephony.md#8300001-input-parameter-value-out-of-range) |

## Examples

```TypeScript
observer.on('cellularDataConnectionStateChange', (data: observer.DataConnectionStateInfo) => {
    console.info("on cellularDataConnectionStateChange, data:" + JSON.stringify(data));
});
```


## on('cellularDataConnectionStateChange')

```TypeScript
function on(type: 'cellularDataConnectionStateChange', options: ObserverOptions,
              callback: Callback<DataConnectionStateInfo>): void
```

Callback when the cellular data link connection state corresponding to the monitored {@code slotId} is updated.

**Since:** 11

<!--Device-observer-function on(type: 'cellularDataConnectionStateChange', options: ObserverOptions,              callback: Callback<DataConnectionStateInfo>): void--><!--Device-observer-function on(type: 'cellularDataConnectionStateChange', options: ObserverOptions,              callback: Callback<DataConnectionStateInfo>): void-End-->

**System capability:** SystemCapability.Telephony.StateRegistry

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'cellularDataConnectionStateChange' | Yes |
| options | [ObserverOptions](arkts-telephony-observer-observeroptions-i.md) | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;DataConnectionStateInfo&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [8300999](../errorcode-telephony.md#8300999-internal-error) |
| [8300002](../errorcode-telephony.md#8300002-service-connection-error) |
| [8300003](../errorcode-telephony.md#8300003-system-internal-error) |
| [8300001](../errorcode-telephony.md#8300001-input-parameter-value-out-of-range) |

## Examples

```TypeScript
let options: observer.ObserverOptions = {
    slotId: 0
}
observer.on('cellularDataConnectionStateChange', options, (data: observer.DataConnectionStateInfo) => {
    console.info("on cellularDataConnectionStateChange, data:" + JSON.stringify(data));
});
```


## on('cellularDataFlowChange')

```TypeScript
function on(type: 'cellularDataFlowChange', callback: Callback<DataFlowType>): void
```

Callback when the uplink and downlink data flow state of cellular data services corresponding to the default sim card is updated.

**Since:** 7

<!--Device-observer-function on(type: 'cellularDataFlowChange', callback: Callback<DataFlowType>): void--><!--Device-observer-function on(type: 'cellularDataFlowChange', callback: Callback<DataFlowType>): void-End-->

**System capability:** SystemCapability.Telephony.StateRegistry

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'cellularDataFlowChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;DataFlowType&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [8300999](../errorcode-telephony.md#8300999-internal-error) |
| [8300002](../errorcode-telephony.md#8300002-service-connection-error) |
| [8300003](../errorcode-telephony.md#8300003-system-internal-error) |
| [8300001](../errorcode-telephony.md#8300001-input-parameter-value-out-of-range) |

## Examples

```TypeScript
import { data } from '@kit.TelephonyKit';

observer.on('cellularDataFlowChange', (data: data.DataFlowType) => {
    console.info("on cellularDataFlowChange, data:" + JSON.stringify(data));
});
```


## on('cellularDataFlowChange')

```TypeScript
function on(type: 'cellularDataFlowChange', options: ObserverOptions, callback: Callback<DataFlowType>): void
```

Callback when the uplink and downlink data flow state of cellular data services corresponding to the monitored {@code slotId} is updated.

**Since:** 11

<!--Device-observer-function on(type: 'cellularDataFlowChange', options: ObserverOptions, callback: Callback<DataFlowType>): void--><!--Device-observer-function on(type: 'cellularDataFlowChange', options: ObserverOptions, callback: Callback<DataFlowType>): void-End-->

**System capability:** SystemCapability.Telephony.StateRegistry

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'cellularDataFlowChange' | Yes |
| options | [ObserverOptions](arkts-telephony-observer-observeroptions-i.md) | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;DataFlowType&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [8300999](../errorcode-telephony.md#8300999-internal-error) |
| [8300002](../errorcode-telephony.md#8300002-service-connection-error) |
| [8300003](../errorcode-telephony.md#8300003-system-internal-error) |
| [8300001](../errorcode-telephony.md#8300001-input-parameter-value-out-of-range) |

## Examples

```TypeScript
import { data } from '@kit.TelephonyKit';

let options: observer.ObserverOptions = {
    slotId: 0
}
observer.on('cellularDataFlowChange', options, (data: data.DataFlowType) => {
    console.info("on cellularDataFlowChange, data:" + JSON.stringify(data));
});
```


## on('callStateChange')

```TypeScript
function on(type: 'callStateChange', callback: Callback<CallStateInfo>): void
```

Callback when the call state corresponding to the default sim card is updated.

**Since:** 11

<!--Device-observer-function on(type: 'callStateChange', callback: Callback<CallStateInfo>): void--><!--Device-observer-function on(type: 'callStateChange', callback: Callback<CallStateInfo>): void-End-->

**System capability:** SystemCapability.Telephony.StateRegistry

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'callStateChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;CallStateInfo&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [8300999](../errorcode-telephony.md#8300999-internal-error) |
| [8300002](../errorcode-telephony.md#8300002-service-connection-error) |
| [8300003](../errorcode-telephony.md#8300003-system-internal-error) |
| [8300001](../errorcode-telephony.md#8300001-input-parameter-value-out-of-range) |

## Examples

```TypeScript
observer.on('callStateChange', (data: observer.CallStateInfo) => {
    console.info("on callStateChange, data:" + JSON.stringify(data));
});
```


## on('callStateChange')

```TypeScript
function on(type: 'callStateChange', options: ObserverOptions, callback: Callback<CallStateInfo>): void
```

Callback when the call state corresponding to the monitored {@code slotId} is updated.

**Since:** 11

<!--Device-observer-function on(type: 'callStateChange', options: ObserverOptions, callback: Callback<CallStateInfo>): void--><!--Device-observer-function on(type: 'callStateChange', options: ObserverOptions, callback: Callback<CallStateInfo>): void-End-->

**System capability:** SystemCapability.Telephony.StateRegistry

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'callStateChange' | Yes |
| options | [ObserverOptions](arkts-telephony-observer-observeroptions-i.md) | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;CallStateInfo&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [8300999](../errorcode-telephony.md#8300999-internal-error) |
| [8300002](../errorcode-telephony.md#8300002-service-connection-error) |
| [8300003](../errorcode-telephony.md#8300003-system-internal-error) |
| [8300001](../errorcode-telephony.md#8300001-input-parameter-value-out-of-range) |

## Examples

```TypeScript
let options: observer.ObserverOptions = {
    slotId: 0
}
observer.on('callStateChange', options, (data: observer.CallStateInfo) => {
    console.info("on callStateChange, data:" + JSON.stringify(data));
});
```


## on('callStateChangeEx')

```TypeScript
function on(type: 'callStateChangeEx', callback: Callback<TelCallState>, options?: ObserverOptions): void
```

Callback when the telCall state corresponding to the monitored {@code slotId} is updated.

**Since:** 21

<!--Device-observer-function on(type: 'callStateChangeEx', callback: Callback<TelCallState>, options?: ObserverOptions): void--><!--Device-observer-function on(type: 'callStateChangeEx', callback: Callback<TelCallState>, options?: ObserverOptions): void-End-->

**System capability:** SystemCapability.Telephony.StateRegistry

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'callStateChangeEx' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;TelCallState&gt; | Yes |
| options | [ObserverOptions](arkts-telephony-observer-observeroptions-i.md) | No |

**Error codes:**

| Error Code ID |
| --- |
| [8800999](../errorcode-telephony.md#8800999-internal-error) |
| [8800002](../errorcode-telephony.md#8800002-service-connection-error) |
| [8800003](../errorcode-telephony.md#8800003-system-internal-error) |
| [8800001](../errorcode-telephony.md#8800001-input-parameter-value-out-of-range) |

## Examples

```TypeScript
import { call } from '@kit.TelephonyKit';

let callback: (data: call.TelCallState) => void = (data: call.TelCallState) => {
    console.info("on callStateChangeEx, data:" + JSON.stringify(data));
}
let options: observer.ObserverOptions = {
    slotId: 0
}

observer.on('callStateChangeEx', callback, options);
observer.on('callStateChangeEx', callback);
```


## on('simStateChange')

```TypeScript
function on(type: 'simStateChange', callback: Callback<SimStateData>): void
```

Callback when the sim state corresponding to the default sim card is updated.

**Since:** 7

<!--Device-observer-function on(type: 'simStateChange', callback: Callback<SimStateData>): void--><!--Device-observer-function on(type: 'simStateChange', callback: Callback<SimStateData>): void-End-->

**System capability:** SystemCapability.Telephony.StateRegistry

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'simStateChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;SimStateData&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [8300999](../errorcode-telephony.md#8300999-internal-error) |
| [8300002](../errorcode-telephony.md#8300002-service-connection-error) |
| [8300003](../errorcode-telephony.md#8300003-system-internal-error) |
| [8300001](../errorcode-telephony.md#8300001-input-parameter-value-out-of-range) |

## Examples

```TypeScript
observer.on('simStateChange', (data: observer.SimStateData) => {
    console.info("on simStateChange, data:" + JSON.stringify(data));
});
```


## on('simStateChange')

```TypeScript
function on(type: 'simStateChange', options: ObserverOptions, callback: Callback<SimStateData>): void
```

Callback when the sim state corresponding to the monitored {@code slotId} is updated.

**Since:** 11

<!--Device-observer-function on(type: 'simStateChange', options: ObserverOptions, callback: Callback<SimStateData>): void--><!--Device-observer-function on(type: 'simStateChange', options: ObserverOptions, callback: Callback<SimStateData>): void-End-->

**System capability:** SystemCapability.Telephony.StateRegistry

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'simStateChange' | Yes |
| options | [ObserverOptions](arkts-telephony-observer-observeroptions-i.md) | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;SimStateData&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [8300999](../errorcode-telephony.md#8300999-internal-error) |
| [8300002](../errorcode-telephony.md#8300002-service-connection-error) |
| [8300003](../errorcode-telephony.md#8300003-system-internal-error) |
| [8300001](../errorcode-telephony.md#8300001-input-parameter-value-out-of-range) |

## Examples

```TypeScript
let options: observer.ObserverOptions = {
    slotId: 0
}
observer.on('simStateChange', options, (data: observer.SimStateData) => {
    console.info("on simStateChange, data:" + JSON.stringify(data));
});
```


## on('iccAccountInfoChange')

```TypeScript
function on(type: 'iccAccountInfoChange', callback: Callback<void>): void
```

Receives an ICC account change. This callback is invoked when the ICC account updates and the observer is added to monitor the updates.

**Since:** 10

<!--Device-observer-function on(type: 'iccAccountInfoChange', callback: Callback<void>): void--><!--Device-observer-function on(type: 'iccAccountInfoChange', callback: Callback<void>): void-End-->

**System capability:** SystemCapability.Telephony.StateRegistry

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'iccAccountInfoChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [8300999](../errorcode-telephony.md#8300999-internal-error) |
| [8300002](../errorcode-telephony.md#8300002-service-connection-error) |
| [8300003](../errorcode-telephony.md#8300003-system-internal-error) |
| [8300001](../errorcode-telephony.md#8300001-input-parameter-value-out-of-range) |

## Examples

```TypeScript
observer.on('iccAccountInfoChange', () => {
    console.info("on iccAccountInfoChange success");
});
```
