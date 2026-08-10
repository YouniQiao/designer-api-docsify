# on

## 导入模块

```TypeScript
import { observer } from 'kits/@kit.TelephonyKit';
```

## on('networkStateChange')

```TypeScript
function on(type: 'networkStateChange', callback: Callback<NetworkState>): void
```

Callback when the network state corresponding to the default sim card is updated.

**起始版本：** 6

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为6。

**需要权限：** ohos.permission.GET_NETWORK_INFO

<!--Device-observer-function on(type: 'networkStateChange', callback: Callback<NetworkState>): void--><!--Device-observer-function on(type: 'networkStateChange', callback: Callback<NetworkState>): void-End-->

**系统能力：** SystemCapability.Telephony.StateRegistry

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'networkStateChange' | 是 | Event type. Indicates the networkStateChange event to be subscribed to. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;NetworkState&gt; | 是 | Indicates the callback for getting an instance of the {@code NetworkState} class. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 201 | Permission denied. |
| 8300999 | Unknown error. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300001 | Invalid parameter value. |

## 示例

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

**起始版本：** 11

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为11。

**需要权限：** ohos.permission.GET_NETWORK_INFO

<!--Device-observer-function on(type: 'networkStateChange', options: ObserverOptions, callback: Callback<NetworkState>): void--><!--Device-observer-function on(type: 'networkStateChange', options: ObserverOptions, callback: Callback<NetworkState>): void-End-->

**系统能力：** SystemCapability.Telephony.StateRegistry

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'networkStateChange' | 是 | Event type. Indicates the networkStateChange event to be subscribed to. |
| options | [ObserverOptions](arkts-telephony-observer-observeroptions-i.md) | 是 | Indicates the options for observer. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;NetworkState&gt; | 是 | Indicates the callback for getting an instance of the {@code NetworkState} class. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 201 | Permission denied. |
| 8300999 | Unknown error. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300001 | Invalid parameter value. |

## 示例

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

**起始版本：** 6

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为6。

<!--Device-observer-function on(type: 'signalInfoChange', callback: Callback<Array<SignalInformation>>): void--><!--Device-observer-function on(type: 'signalInfoChange', callback: Callback<Array<SignalInformation>>): void-End-->

**系统能力：** SystemCapability.Telephony.StateRegistry

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'signalInfoChange' | 是 | Event type. Indicates the signalInfoChange event to be subscribed to. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;SignalInformation&gt;&gt; | 是 | Indicates the callback for getting an array of instances of the classes derived from {@link SignalInformation}. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300999 | Unknown error. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300001 | Invalid parameter value. |

## 示例

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

**起始版本：** 11

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为11。

<!--Device-observer-function on(type: 'signalInfoChange', options: ObserverOptions, callback: Callback<Array<SignalInformation>>): void--><!--Device-observer-function on(type: 'signalInfoChange', options: ObserverOptions, callback: Callback<Array<SignalInformation>>): void-End-->

**系统能力：** SystemCapability.Telephony.StateRegistry

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'signalInfoChange' | 是 | Event type. Indicates the signalInfoChange event to be subscribed to. |
| options | [ObserverOptions](arkts-telephony-observer-observeroptions-i.md) | 是 | Indicates the options for observer. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;SignalInformation&gt;&gt; | 是 | Indicates the callback for getting an array of instances of the classes derived from {@link SignalInformation}. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300999 | Unknown error. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300001 | Invalid parameter value. |

## 示例

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

**起始版本：** 11

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为11。

<!--Device-observer-function on(type: 'cellularDataConnectionStateChange', callback: Callback<DataConnectionStateInfo>): void--><!--Device-observer-function on(type: 'cellularDataConnectionStateChange', callback: Callback<DataConnectionStateInfo>): void-End-->

**系统能力：** SystemCapability.Telephony.StateRegistry

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'cellularDataConnectionStateChange' | 是 | Event type. Indicates the cellularDataConnectionStateChange event to be subscribed to. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;DataConnectionStateInfo&gt; | 是 | Indicates the callback for getting the cellular data link connection state, and networkType Indicates the radio access technology for cellular data services. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300999 | Unknown error. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300001 | Invalid parameter value. |

## 示例

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

**起始版本：** 11

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为11。

<!--Device-observer-function on(type: 'cellularDataConnectionStateChange', options: ObserverOptions,              callback: Callback<DataConnectionStateInfo>): void--><!--Device-observer-function on(type: 'cellularDataConnectionStateChange', options: ObserverOptions,              callback: Callback<DataConnectionStateInfo>): void-End-->

**系统能力：** SystemCapability.Telephony.StateRegistry

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'cellularDataConnectionStateChange' | 是 | Event type. Indicates the cellularDataConnectionStateChange event to be subscribed to. |
| options | [ObserverOptions](arkts-telephony-observer-observeroptions-i.md) | 是 | Indicates the options for observer. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;DataConnectionStateInfo&gt; | 是 | Indicates the callback for getting the cellular data link connection state, and networkType Indicates the radio access technology for cellular data services. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300999 | Unknown error. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300001 | Invalid parameter value. |

## 示例

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

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为7。

<!--Device-observer-function on(type: 'cellularDataFlowChange', callback: Callback<DataFlowType>): void--><!--Device-observer-function on(type: 'cellularDataFlowChange', callback: Callback<DataFlowType>): void-End-->

**系统能力：** SystemCapability.Telephony.StateRegistry

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'cellularDataFlowChange' | 是 | Event type. Indicates the cellularDataFlowChange event to be subscribed to. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;DataFlowType&gt; | 是 | Indicates the callback for getting the cellular data flow state. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300999 | Unknown error. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300001 | Invalid parameter value. |

## 示例

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

**起始版本：** 11

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为11。

<!--Device-observer-function on(type: 'cellularDataFlowChange', options: ObserverOptions, callback: Callback<DataFlowType>): void--><!--Device-observer-function on(type: 'cellularDataFlowChange', options: ObserverOptions, callback: Callback<DataFlowType>): void-End-->

**系统能力：** SystemCapability.Telephony.StateRegistry

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'cellularDataFlowChange' | 是 | Event type. Indicates the cellularDataFlowChange event to be subscribed to. |
| options | [ObserverOptions](arkts-telephony-observer-observeroptions-i.md) | 是 | Indicates the options for observer. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;DataFlowType&gt; | 是 | Indicates the callback for getting the cellular data flow state. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300999 | Unknown error. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300001 | Invalid parameter value. |

## 示例

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

**起始版本：** 11

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为11。

<!--Device-observer-function on(type: 'callStateChange', callback: Callback<CallStateInfo>): void--><!--Device-observer-function on(type: 'callStateChange', callback: Callback<CallStateInfo>): void-End-->

**系统能力：** SystemCapability.Telephony.StateRegistry

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'callStateChange' | 是 | Event type. Indicates the callStateChange event to be subscribed to. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;CallStateInfo&gt; | 是 | Indicates the callback for getting the call state and the called number. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300999 | Unknown error. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300001 | Invalid parameter value. |

## 示例

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

**起始版本：** 11

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为11。

<!--Device-observer-function on(type: 'callStateChange', options: ObserverOptions, callback: Callback<CallStateInfo>): void--><!--Device-observer-function on(type: 'callStateChange', options: ObserverOptions, callback: Callback<CallStateInfo>): void-End-->

**系统能力：** SystemCapability.Telephony.StateRegistry

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'callStateChange' | 是 | Event type. Indicates the callStateChange event to be subscribed to. |
| options | [ObserverOptions](arkts-telephony-observer-observeroptions-i.md) | 是 | Indicates the options for observer. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;CallStateInfo&gt; | 是 | Indicates the callback for getting the call state and the called number. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300999 | Unknown error. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300001 | Invalid parameter value. |

## 示例

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

**起始版本：** 21

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为21。

<!--Device-observer-function on(type: 'callStateChangeEx', callback: Callback<TelCallState>, options?: ObserverOptions): void--><!--Device-observer-function on(type: 'callStateChangeEx', callback: Callback<TelCallState>, options?: ObserverOptions): void-End-->

**系统能力：** SystemCapability.Telephony.StateRegistry

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'callStateChangeEx' | 是 | Event type. Indicates the callStateChangeEx event to be subscribed to. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;TelCallState&gt; | 是 | Indicates the callback for getting the telCall state. |
| options | [ObserverOptions](arkts-telephony-observer-observeroptions-i.md) | 否 | Indicates the options for observer. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 8800999 | Unknown error. |
| 8800002 | Service connection failed. |
| 8800003 | System internal error. |
| 8800001 | Invalid parameter value. |

## 示例

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

**起始版本：** 7

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为7。

<!--Device-observer-function on(type: 'simStateChange', callback: Callback<SimStateData>): void--><!--Device-observer-function on(type: 'simStateChange', callback: Callback<SimStateData>): void-End-->

**系统能力：** SystemCapability.Telephony.StateRegistry

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'simStateChange' | 是 | Event type. Indicates the simStateChange event to be subscribed to. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;SimStateData&gt; | 是 | Indicates the callback for getting the SimStateData object. including state Indicates the sim state, and reason Indicates the cause of the change. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300999 | Unknown error. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300001 | Invalid parameter value. |

## 示例

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

**起始版本：** 11

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为11。

<!--Device-observer-function on(type: 'simStateChange', options: ObserverOptions, callback: Callback<SimStateData>): void--><!--Device-observer-function on(type: 'simStateChange', options: ObserverOptions, callback: Callback<SimStateData>): void-End-->

**系统能力：** SystemCapability.Telephony.StateRegistry

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'simStateChange' | 是 | Event type. Indicates the simStateChange event to be subscribed to. |
| options | [ObserverOptions](arkts-telephony-observer-observeroptions-i.md) | 是 | Indicates the options for observer. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;SimStateData&gt; | 是 | Indicates the callback for getting the SimStateData object. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300999 | Unknown error. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300001 | Invalid parameter value. |

## 示例

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

**起始版本：** 10

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为10。

<!--Device-observer-function on(type: 'iccAccountInfoChange', callback: Callback<void>): void--><!--Device-observer-function on(type: 'iccAccountInfoChange', callback: Callback<void>): void-End-->

**系统能力：** SystemCapability.Telephony.StateRegistry

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'iccAccountInfoChange' | 是 | iccAccountInfoChange |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | 是 | including state Indicates the ICC account information, and reason Indicates the cause of the change. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300999 | Unknown error. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300001 | Invalid parameter value. |

## 示例

```TypeScript
observer.on('iccAccountInfoChange', () => {
    console.info("on iccAccountInfoChange success");
});
```

