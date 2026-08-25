# off

## 导入模块

```TypeScript
import { observer } from 'kits/@kit.TelephonyKit';
```

## off('networkStateChange')

```TypeScript
function off(type: 'networkStateChange', callback?: Callback<NetworkState>): void
```

取消订阅网络状态变化事件，使用callback方式作为异步方法。

> **说明：**&gt;
> 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。

**起始版本：** 6

**系统能力：** SystemCapability.Telephony.StateRegistry

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'networkStateChange' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;NetworkState&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [8300001](../errorcode-telephony.md#8300001-输入参数不在处理范围内) |
| [8300002](../errorcode-telephony.md#8300002-服务连接失败) |
| [8300003](../errorcode-telephony.md#8300003-系统内部错误) |
| [8300999](../errorcode-telephony.md#8300999-内部错误) |


## off('signalInfoChange')

```TypeScript
function off(type: 'signalInfoChange', callback?: Callback<Array<SignalInformation>>): void
```

取消订阅信号状态变化事件，使用callback方式作为异步方法。

> **说明：**&gt;
> 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。

**起始版本：** 6

**系统能力：** SystemCapability.Telephony.StateRegistry

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'signalInfoChange' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;SignalInformation&gt;&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [8300001](../errorcode-telephony.md#8300001-输入参数不在处理范围内) |
| [8300002](../errorcode-telephony.md#8300002-服务连接失败) |
| [8300003](../errorcode-telephony.md#8300003-系统内部错误) |
| [8300999](../errorcode-telephony.md#8300999-内部错误) |


## off('cellularDataConnectionStateChange')

```TypeScript
function off(type: 'cellularDataConnectionStateChange', callback?: Callback<DataConnectionStateInfo>): void
```

移除订阅蜂窝数据链路连接状态，使用callback方式作为异步方法。

> **说明：**&gt;
> 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。

**起始版本：** 7

**系统能力：** SystemCapability.Telephony.StateRegistry

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'cellularDataConnectionStateChange' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[DataConnectionStateInfo](arkts-telephony-observer-dataconnectionstateinfo-i.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [8300001](../errorcode-telephony.md#8300001-输入参数不在处理范围内) |
| [8300002](../errorcode-telephony.md#8300002-服务连接失败) |
| [8300003](../errorcode-telephony.md#8300003-系统内部错误) |
| [8300999](../errorcode-telephony.md#8300999-内部错误) |


## off('cellularDataFlowChange')

```TypeScript
function off(type: 'cellularDataFlowChange', callback?: Callback<DataFlowType>): void
```

移除订阅蜂窝数据业务的上下行数据流状态，使用callback方式作为异步方法。

> **说明：**&gt;
> 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。

**起始版本：** 7

**系统能力：** SystemCapability.Telephony.StateRegistry

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'cellularDataFlowChange' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;DataFlowType&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [8300001](../errorcode-telephony.md#8300001-输入参数不在处理范围内) |
| [8300002](../errorcode-telephony.md#8300002-服务连接失败) |
| [8300003](../errorcode-telephony.md#8300003-系统内部错误) |
| [8300999](../errorcode-telephony.md#8300999-内部错误) |


## off('callStateChange')

```TypeScript
function off(type: 'callStateChange', callback?: Callback<CallStateInfo>): void
```

取消订阅通话状态变化事件，使用callback方式作为异步方法。

> **说明：**&gt;
> 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。

**起始版本：** 6

**系统能力：** SystemCapability.Telephony.StateRegistry

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'callStateChange' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[CallStateInfo](arkts-telephony-observer-callstateinfo-i.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [8300001](../errorcode-telephony.md#8300001-输入参数不在处理范围内) |
| [8300002](../errorcode-telephony.md#8300002-服务连接失败) |
| [8300003](../errorcode-telephony.md#8300003-系统内部错误) |
| [8300999](../errorcode-telephony.md#8300999-内部错误) |


## off('callStateChangeEx')

```TypeScript
function off(type: 'callStateChangeEx', callback?: Callback<TelCallState>): void
```

取消订阅通话状态变化拓展事件，使用callback方式作为异步方法。

> **说明：**&gt;
> 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。

**起始版本：** 21

**系统能力：** SystemCapability.Telephony.StateRegistry

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'callStateChangeEx' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;TelCallState&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [8800001](../errorcode-telephony.md#8800001-输入参数不在处理范围内) |
| [8800002](../errorcode-telephony.md#8800002-服务连接失败) |
| [8800003](../errorcode-telephony.md#8800003-系统内部错误) |
| [8800999](../errorcode-telephony.md#8800999-内部错误) |


## off('simStateChange')

```TypeScript
function off(type: 'simStateChange', callback?: Callback<SimStateData>): void
```

移除订阅sim状态更改事件，使用callback方式作为异步方法。

> **说明：**&gt;
> 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。

**起始版本：** 7

**系统能力：** SystemCapability.Telephony.StateRegistry

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'simStateChange' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[SimStateData](arkts-telephony-observer-simstatedata-i.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [8300001](../errorcode-telephony.md#8300001-输入参数不在处理范围内) |
| [8300002](../errorcode-telephony.md#8300002-服务连接失败) |
| [8300003](../errorcode-telephony.md#8300003-系统内部错误) |
| [8300999](../errorcode-telephony.md#8300999-内部错误) |


## off('iccAccountInfoChange')

```TypeScript
function off(type: 'iccAccountInfoChange', callback?: Callback<void>): void
```

移除订阅卡帐户变化事件，使用callback方式作为异步方法。

> **说明：**&gt;
> 可以指定传入on中的callback取消一个订阅，也可以不指定callback清空所有订阅。

**起始版本：** 10

**系统能力：** SystemCapability.Telephony.StateRegistry

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'iccAccountInfoChange' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;void&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [8300001](../errorcode-telephony.md#8300001-输入参数不在处理范围内) |
| [8300002](../errorcode-telephony.md#8300002-服务连接失败) |
| [8300003](../errorcode-telephony.md#8300003-系统内部错误) |
| [8300999](../errorcode-telephony.md#8300999-内部错误) |
