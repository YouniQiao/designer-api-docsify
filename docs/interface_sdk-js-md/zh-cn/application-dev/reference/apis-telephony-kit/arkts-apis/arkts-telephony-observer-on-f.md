# on

## 导入模块

```TypeScript
import { observer } from 'kits/@kit.TelephonyKit';
```

## on('networkStateChange')

```TypeScript
function on(type: 'networkStateChange', callback: Callback<NetworkState>): void
```

订阅网络状态变化事件，使用callback方式作为异步方法。

**起始版本：** 6

**需要权限：** ohos.permission.GET_NETWORK_INFO

**系统能力：** SystemCapability.Telephony.StateRegistry

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'networkStateChange' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;NetworkState&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [8300001](../errorcode-telephony.md#8300001-输入参数不在处理范围内) |
| [8300002](../errorcode-telephony.md#8300002-服务连接失败) |
| [8300003](../errorcode-telephony.md#8300003-系统内部错误) |
| [8300999](../errorcode-telephony.md#8300999-内部错误) |


## on('networkStateChange')

```TypeScript
function on(type: 'networkStateChange', options: ObserverOptions, callback: Callback<NetworkState>): void
```

订阅指定卡槽位的网络状态变化事件，使用callback方式作为异步方法。

**起始版本：** 6

**需要权限：** ohos.permission.GET_NETWORK_INFO

**系统能力：** SystemCapability.Telephony.StateRegistry

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'networkStateChange' | 是 |
| options | [ObserverOptions](arkts-telephony-observer-observeroptions-i.md) | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;NetworkState&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [8300001](../errorcode-telephony.md#8300001-输入参数不在处理范围内) |
| [8300002](../errorcode-telephony.md#8300002-服务连接失败) |
| [8300003](../errorcode-telephony.md#8300003-系统内部错误) |
| [8300999](../errorcode-telephony.md#8300999-内部错误) |


## on('signalInfoChange')

```TypeScript
function on(type: 'signalInfoChange', callback: Callback<Array<SignalInformation>>): void
```

订阅信号状态变化事件，使用callback方式作为异步方法。

**起始版本：** 6

**系统能力：** SystemCapability.Telephony.StateRegistry

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'signalInfoChange' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;SignalInformation&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [8300001](../errorcode-telephony.md#8300001-输入参数不在处理范围内) |
| [8300002](../errorcode-telephony.md#8300002-服务连接失败) |
| [8300003](../errorcode-telephony.md#8300003-系统内部错误) |
| [8300999](../errorcode-telephony.md#8300999-内部错误) |


## on('signalInfoChange')

```TypeScript
function on(type: 'signalInfoChange', options: ObserverOptions, callback: Callback<Array<SignalInformation>>): void
```

订阅指定卡槽位的信号状态变化事件，使用callback方式作为异步方法。

**起始版本：** 6

**系统能力：** SystemCapability.Telephony.StateRegistry

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'signalInfoChange' | 是 |
| options | [ObserverOptions](arkts-telephony-observer-observeroptions-i.md) | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;SignalInformation&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [8300001](../errorcode-telephony.md#8300001-输入参数不在处理范围内) |
| [8300002](../errorcode-telephony.md#8300002-服务连接失败) |
| [8300003](../errorcode-telephony.md#8300003-系统内部错误) |
| [8300999](../errorcode-telephony.md#8300999-内部错误) |


## on('cellularDataConnectionStateChange')

```TypeScript
function on(type: 'cellularDataConnectionStateChange', callback: Callback<DataConnectionStateInfo>): void
```

订阅蜂窝数据链路连接状态，使用callback方式作为异步方法。

**起始版本：** 7

**系统能力：** SystemCapability.Telephony.StateRegistry

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'cellularDataConnectionStateChange' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[DataConnectionStateInfo](arkts-telephony-observer-dataconnectionstateinfo-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [8300001](../errorcode-telephony.md#8300001-输入参数不在处理范围内) |
| [8300002](../errorcode-telephony.md#8300002-服务连接失败) |
| [8300003](../errorcode-telephony.md#8300003-系统内部错误) |
| [8300999](../errorcode-telephony.md#8300999-内部错误) |


## on('cellularDataConnectionStateChange')

```TypeScript
function on(type: 'cellularDataConnectionStateChange', options: ObserverOptions,
              callback: Callback<DataConnectionStateInfo>): void
```

订阅指定卡槽位的蜂窝数据链路连接状态，使用callback方式作为异步方法。

**起始版本：** 7

**系统能力：** SystemCapability.Telephony.StateRegistry

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'cellularDataConnectionStateChange' | 是 |
| options | [ObserverOptions](arkts-telephony-observer-observeroptions-i.md) | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[DataConnectionStateInfo](arkts-telephony-observer-dataconnectionstateinfo-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [8300001](../errorcode-telephony.md#8300001-输入参数不在处理范围内) |
| [8300002](../errorcode-telephony.md#8300002-服务连接失败) |
| [8300003](../errorcode-telephony.md#8300003-系统内部错误) |
| [8300999](../errorcode-telephony.md#8300999-内部错误) |


## on('cellularDataFlowChange')

```TypeScript
function on(type: 'cellularDataFlowChange', callback: Callback<DataFlowType>): void
```

订阅蜂窝数据业务的上下行数据流状态，使用callback方式作为异步方法。

**起始版本：** 7

**系统能力：** SystemCapability.Telephony.StateRegistry

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'cellularDataFlowChange' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;DataFlowType&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [8300001](../errorcode-telephony.md#8300001-输入参数不在处理范围内) |
| [8300002](../errorcode-telephony.md#8300002-服务连接失败) |
| [8300003](../errorcode-telephony.md#8300003-系统内部错误) |
| [8300999](../errorcode-telephony.md#8300999-内部错误) |


## on('cellularDataFlowChange')

```TypeScript
function on(type: 'cellularDataFlowChange', options: ObserverOptions, callback: Callback<DataFlowType>): void
```

订阅指定卡槽位的蜂窝数据业务的上下行数据流状态，使用callback方式作为异步方法。

**起始版本：** 7

**系统能力：** SystemCapability.Telephony.StateRegistry

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'cellularDataFlowChange' | 是 |
| options | [ObserverOptions](arkts-telephony-observer-observeroptions-i.md) | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;DataFlowType&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [8300001](../errorcode-telephony.md#8300001-输入参数不在处理范围内) |
| [8300002](../errorcode-telephony.md#8300002-服务连接失败) |
| [8300003](../errorcode-telephony.md#8300003-系统内部错误) |
| [8300999](../errorcode-telephony.md#8300999-内部错误) |


## on('callStateChange')

```TypeScript
function on(type: 'callStateChange', callback: Callback<CallStateInfo>): void
```

订阅通话状态变化事件，使用callback方式作为异步方法。

**起始版本：** 6

**系统能力：** SystemCapability.Telephony.StateRegistry

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'callStateChange' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[CallStateInfo](arkts-telephony-observer-callstateinfo-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [8300001](../errorcode-telephony.md#8300001-输入参数不在处理范围内) |
| [8300002](../errorcode-telephony.md#8300002-服务连接失败) |
| [8300003](../errorcode-telephony.md#8300003-系统内部错误) |
| [8300999](../errorcode-telephony.md#8300999-内部错误) |


## on('callStateChange')

```TypeScript
function on(type: 'callStateChange', options: ObserverOptions, callback: Callback<CallStateInfo>): void
```

订阅通话状态变化事件，使用callback方式作为异步方法。

**起始版本：** 6

**系统能力：** SystemCapability.Telephony.StateRegistry

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'callStateChange' | 是 |
| options | [ObserverOptions](arkts-telephony-observer-observeroptions-i.md) | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[CallStateInfo](arkts-telephony-observer-callstateinfo-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [8300001](../errorcode-telephony.md#8300001-输入参数不在处理范围内) |
| [8300002](../errorcode-telephony.md#8300002-服务连接失败) |
| [8300003](../errorcode-telephony.md#8300003-系统内部错误) |
| [8300999](../errorcode-telephony.md#8300999-内部错误) |


## on('callStateChangeEx')

```TypeScript
function on(type: 'callStateChangeEx', callback: Callback<TelCallState>, options?: ObserverOptions): void
```

订阅通话状态变化拓展事件，使用callback方式作为异步方法。

**起始版本：** 21

**系统能力：** SystemCapability.Telephony.StateRegistry

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'callStateChangeEx' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;TelCallState&gt; | 是 |
| options | [ObserverOptions](arkts-telephony-observer-observeroptions-i.md) | 否 |

**错误码：**

| 错误码ID |
| --- |
| [8800001](../errorcode-telephony.md#8800001-输入参数不在处理范围内) |
| [8800002](../errorcode-telephony.md#8800002-服务连接失败) |
| [8800003](../errorcode-telephony.md#8800003-系统内部错误) |
| [8800999](../errorcode-telephony.md#8800999-内部错误) |


## on('simStateChange')

```TypeScript
function on(type: 'simStateChange', callback: Callback<SimStateData>): void
```

订阅sim状态更改事件，使用callback方式作为异步方法。

> **说明：**&gt;
> 此接口不包含sim卡的激活状态，具体请参见[sim.isSimActive](arkts-telephony-sim-issimactive-f.md)接口。

**起始版本：** 7

**系统能力：** SystemCapability.Telephony.StateRegistry

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'simStateChange' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[SimStateData](arkts-telephony-observer-simstatedata-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [8300001](../errorcode-telephony.md#8300001-输入参数不在处理范围内) |
| [8300002](../errorcode-telephony.md#8300002-服务连接失败) |
| [8300003](../errorcode-telephony.md#8300003-系统内部错误) |
| [8300999](../errorcode-telephony.md#8300999-内部错误) |


## on('simStateChange')

```TypeScript
function on(type: 'simStateChange', options: ObserverOptions, callback: Callback<SimStateData>): void
```

订阅指定卡槽位的sim状态更改事件，使用callback方式作为异步方法。

**起始版本：** 7

**系统能力：** SystemCapability.Telephony.StateRegistry

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'simStateChange' | 是 |
| options | [ObserverOptions](arkts-telephony-observer-observeroptions-i.md) | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[SimStateData](arkts-telephony-observer-simstatedata-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [8300001](../errorcode-telephony.md#8300001-输入参数不在处理范围内) |
| [8300002](../errorcode-telephony.md#8300002-服务连接失败) |
| [8300003](../errorcode-telephony.md#8300003-系统内部错误) |
| [8300999](../errorcode-telephony.md#8300999-内部错误) |


## on('iccAccountInfoChange')

```TypeScript
function on(type: 'iccAccountInfoChange', callback: Callback<void>): void
```

订阅卡帐户变化事件，使用callback方式作为异步方法。

**起始版本：** 10

**系统能力：** SystemCapability.Telephony.StateRegistry

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'iccAccountInfoChange' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [8300001](../errorcode-telephony.md#8300001-输入参数不在处理范围内) |
| [8300002](../errorcode-telephony.md#8300002-服务连接失败) |
| [8300003](../errorcode-telephony.md#8300003-系统内部错误) |
| [8300999](../errorcode-telephony.md#8300999-内部错误) |
