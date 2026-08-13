# on

## on('networkStateChange')

```TypeScript
function on(type: 'networkStateChange', callback: Callback<NetworkState>): void
```

订阅网络状态变化事件，使用callback方式作为异步方法。

**起始版本：** 6

**需要权限：** ohos.permission.GET_NETWORK_INFO

<!--Device-observer-function on(type: 'networkStateChange', callback: Callback<NetworkState>): void--><!--Device-observer-function on(type: 'networkStateChange', callback: Callback<NetworkState>): void-End-->

**系统能力：** SystemCapability.Telephony.StateRegistry

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'networkStateChange' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;NetworkState&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [8300999](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300999-内部错误) |
| [8300002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300002-服务连接失败) |
| [8300003](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300003-系统内部错误) |
| [8300001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300001-输入参数不在处理范围内) |

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

订阅指定卡槽位的网络状态变化事件，使用callback方式作为异步方法。

**起始版本：** 6

**需要权限：** ohos.permission.GET_NETWORK_INFO

<!--Device-observer-function on(type: 'networkStateChange', options: ObserverOptions, callback: Callback<NetworkState>): void--><!--Device-observer-function on(type: 'networkStateChange', options: ObserverOptions, callback: Callback<NetworkState>): void-End-->

**系统能力：** SystemCapability.Telephony.StateRegistry

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'networkStateChange' | 是 |
| options | [ObserverOptions](arkts-telephony-observer-observeroptions-i.md) | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;NetworkState&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [8300999](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300999-内部错误) |
| [8300002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300002-服务连接失败) |
| [8300003](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300003-系统内部错误) |
| [8300001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300001-输入参数不在处理范围内) |

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

订阅信号状态变化事件，使用callback方式作为异步方法。

**起始版本：** 6

<!--Device-observer-function on(type: 'signalInfoChange', callback: Callback<Array<SignalInformation>>): void--><!--Device-observer-function on(type: 'signalInfoChange', callback: Callback<Array<SignalInformation>>): void-End-->

**系统能力：** SystemCapability.Telephony.StateRegistry

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'signalInfoChange' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;[SignalInformation](arkts-telephony-observer-signalinformation-t.md)&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [8300999](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300999-内部错误) |
| [8300002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300002-服务连接失败) |
| [8300003](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300003-系统内部错误) |
| [8300001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300001-输入参数不在处理范围内) |

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

订阅指定卡槽位的信号状态变化事件，使用callback方式作为异步方法。

**起始版本：** 6

<!--Device-observer-function on(type: 'signalInfoChange', options: ObserverOptions, callback: Callback<Array<SignalInformation>>): void--><!--Device-observer-function on(type: 'signalInfoChange', options: ObserverOptions, callback: Callback<Array<SignalInformation>>): void-End-->

**系统能力：** SystemCapability.Telephony.StateRegistry

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'signalInfoChange' | 是 |
| options | [ObserverOptions](arkts-telephony-observer-observeroptions-i.md) | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;[SignalInformation](arkts-telephony-observer-signalinformation-t.md)&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [8300999](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300999-内部错误) |
| [8300002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300002-服务连接失败) |
| [8300003](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300003-系统内部错误) |
| [8300001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300001-输入参数不在处理范围内) |

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

订阅蜂窝数据链路连接状态，使用callback方式作为异步方法。

**起始版本：** 7

<!--Device-observer-function on(type: 'cellularDataConnectionStateChange', callback: Callback<DataConnectionStateInfo>): void--><!--Device-observer-function on(type: 'cellularDataConnectionStateChange', callback: Callback<DataConnectionStateInfo>): void-End-->

**系统能力：** SystemCapability.Telephony.StateRegistry

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'cellularDataConnectionStateChange' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[DataConnectionStateInfo](arkts-telephony-observer-dataconnectionstateinfo-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [8300999](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300999-内部错误) |
| [8300002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300002-服务连接失败) |
| [8300003](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300003-系统内部错误) |
| [8300001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300001-输入参数不在处理范围内) |

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

订阅指定卡槽位的蜂窝数据链路连接状态，使用callback方式作为异步方法。

**起始版本：** 7

<!--Device-observer-function on(type: 'cellularDataConnectionStateChange', options: ObserverOptions,              callback: Callback<DataConnectionStateInfo>): void--><!--Device-observer-function on(type: 'cellularDataConnectionStateChange', options: ObserverOptions,              callback: Callback<DataConnectionStateInfo>): void-End-->

**系统能力：** SystemCapability.Telephony.StateRegistry

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'cellularDataConnectionStateChange' | 是 |
| options | [ObserverOptions](arkts-telephony-observer-observeroptions-i.md) | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[DataConnectionStateInfo](arkts-telephony-observer-dataconnectionstateinfo-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [8300999](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300999-内部错误) |
| [8300002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300002-服务连接失败) |
| [8300003](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300003-系统内部错误) |
| [8300001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300001-输入参数不在处理范围内) |

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

订阅蜂窝数据业务的上下行数据流状态，使用callback方式作为异步方法。

**起始版本：** 7

<!--Device-observer-function on(type: 'cellularDataFlowChange', callback: Callback<DataFlowType>): void--><!--Device-observer-function on(type: 'cellularDataFlowChange', callback: Callback<DataFlowType>): void-End-->

**系统能力：** SystemCapability.Telephony.StateRegistry

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'cellularDataFlowChange' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[DataFlowType](arkts-telephony-observer-dataflowtype-t.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [8300999](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300999-内部错误) |
| [8300002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300002-服务连接失败) |
| [8300003](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300003-系统内部错误) |
| [8300001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300001-输入参数不在处理范围内) |

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

订阅指定卡槽位的蜂窝数据业务的上下行数据流状态，使用callback方式作为异步方法。

**起始版本：** 7

<!--Device-observer-function on(type: 'cellularDataFlowChange', options: ObserverOptions, callback: Callback<DataFlowType>): void--><!--Device-observer-function on(type: 'cellularDataFlowChange', options: ObserverOptions, callback: Callback<DataFlowType>): void-End-->

**系统能力：** SystemCapability.Telephony.StateRegistry

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'cellularDataFlowChange' | 是 |
| options | [ObserverOptions](arkts-telephony-observer-observeroptions-i.md) | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[DataFlowType](arkts-telephony-observer-dataflowtype-t.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [8300999](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300999-内部错误) |
| [8300002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300002-服务连接失败) |
| [8300003](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300003-系统内部错误) |
| [8300001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300001-输入参数不在处理范围内) |

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

订阅通话状态变化事件，使用callback方式作为异步方法。

**起始版本：** 6

<!--Device-observer-function on(type: 'callStateChange', callback: Callback<CallStateInfo>): void--><!--Device-observer-function on(type: 'callStateChange', callback: Callback<CallStateInfo>): void-End-->

**系统能力：** SystemCapability.Telephony.StateRegistry

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'callStateChange' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[CallStateInfo](arkts-telephony-observer-callstateinfo-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [8300999](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300999-内部错误) |
| [8300002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300002-服务连接失败) |
| [8300003](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300003-系统内部错误) |
| [8300001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300001-输入参数不在处理范围内) |

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

订阅通话状态变化事件，使用callback方式作为异步方法。

**起始版本：** 6

<!--Device-observer-function on(type: 'callStateChange', options: ObserverOptions, callback: Callback<CallStateInfo>): void--><!--Device-observer-function on(type: 'callStateChange', options: ObserverOptions, callback: Callback<CallStateInfo>): void-End-->

**系统能力：** SystemCapability.Telephony.StateRegistry

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'callStateChange' | 是 |
| options | [ObserverOptions](arkts-telephony-observer-observeroptions-i.md) | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[CallStateInfo](arkts-telephony-observer-callstateinfo-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [8300999](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300999-内部错误) |
| [8300002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300002-服务连接失败) |
| [8300003](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300003-系统内部错误) |
| [8300001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300001-输入参数不在处理范围内) |

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

订阅通话状态变化拓展事件，使用callback方式作为异步方法。

**起始版本：** 21

<!--Device-observer-function on(type: 'callStateChangeEx', callback: Callback<TelCallState>, options?: ObserverOptions): void--><!--Device-observer-function on(type: 'callStateChangeEx', callback: Callback<TelCallState>, options?: ObserverOptions): void-End-->

**系统能力：** SystemCapability.Telephony.StateRegistry

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'callStateChangeEx' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;TelCallState&gt; | 是 |
| options | [ObserverOptions](arkts-telephony-observer-observeroptions-i.md) | 否 |

**错误码：**

| 错误码ID |
| --- |
| [8800999](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8800999-内部错误) |
| [8800002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8800002-服务连接失败) |
| [8800003](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8800003-系统内部错误) |
| [8800001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8800001-输入参数不在处理范围内) |

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

订阅sim状态更改事件，使用callback方式作为异步方法。

> **说明：**
> 
> 此接口不包含sim卡的激活状态，具体请参见[sim.isSimActive](arkts-telephony-sim-issimactive-f.md#isSimActive)接口。

**起始版本：** 7

<!--Device-observer-function on(type: 'simStateChange', callback: Callback<SimStateData>): void--><!--Device-observer-function on(type: 'simStateChange', callback: Callback<SimStateData>): void-End-->

**系统能力：** SystemCapability.Telephony.StateRegistry

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'simStateChange' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[SimStateData](arkts-telephony-observer-simstatedata-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [8300999](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300999-内部错误) |
| [8300002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300002-服务连接失败) |
| [8300003](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300003-系统内部错误) |
| [8300001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300001-输入参数不在处理范围内) |

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

订阅指定卡槽位的sim状态更改事件，使用callback方式作为异步方法。

**起始版本：** 7

<!--Device-observer-function on(type: 'simStateChange', options: ObserverOptions, callback: Callback<SimStateData>): void--><!--Device-observer-function on(type: 'simStateChange', options: ObserverOptions, callback: Callback<SimStateData>): void-End-->

**系统能力：** SystemCapability.Telephony.StateRegistry

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'simStateChange' | 是 |
| options | [ObserverOptions](arkts-telephony-observer-observeroptions-i.md) | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[SimStateData](arkts-telephony-observer-simstatedata-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [8300999](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300999-内部错误) |
| [8300002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300002-服务连接失败) |
| [8300003](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300003-系统内部错误) |
| [8300001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300001-输入参数不在处理范围内) |

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

订阅卡帐户变化事件，使用callback方式作为异步方法。

**起始版本：** 10

<!--Device-observer-function on(type: 'iccAccountInfoChange', callback: Callback<void>): void--><!--Device-observer-function on(type: 'iccAccountInfoChange', callback: Callback<void>): void-End-->

**系统能力：** SystemCapability.Telephony.StateRegistry

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'iccAccountInfoChange' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#401-打开联系人头像文件失败) |
| [8300999](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300999-内部错误) |
| [8300002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300002-服务连接失败) |
| [8300003](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300003-系统内部错误) |
| [8300001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-telephony-kit/errorcode-telephony.md#8300001-输入参数不在处理范围内) |

## 示例

```TypeScript
observer.on('iccAccountInfoChange', () => {
    console.info("on iccAccountInfoChange success");
});
```
