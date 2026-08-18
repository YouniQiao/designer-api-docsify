# onNetworkStateChange

## 导入模块

```TypeScript
```

## onNetworkStateChange

```TypeScript
function onNetworkStateChange(callback: Callback<NetworkState>): void
```

Callback when the network state corresponding to the default sim card is updated.

**起始版本：** 23

**需要权限：** ohos.permission.GET_NETWORK_INFO

<!--Device-observer-function onNetworkStateChange(callback: Callback<NetworkState>): void--><!--Device-observer-function onNetworkStateChange(callback: Callback<NetworkState>): void-End-->

**系统能力：** SystemCapability.Telephony.StateRegistry

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;NetworkState&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [8300999](../errorcode-telephony.md#8300999-内部错误) |
| [8300002](../errorcode-telephony.md#8300002-服务连接失败) |
| [8300003](../errorcode-telephony.md#8300003-系统内部错误) |
| [8300001](../errorcode-telephony.md#8300001-输入参数不在处理范围内) |


## onNetworkStateChange

```TypeScript
function onNetworkStateChange(options: ObserverOptions, callback: Callback<NetworkState>): void
```

Callback when the network state corresponding to the monitored {@code slotId} is updated.

**起始版本：** 23

**需要权限：** ohos.permission.GET_NETWORK_INFO

<!--Device-observer-function onNetworkStateChange(options: ObserverOptions, callback: Callback<NetworkState>): void--><!--Device-observer-function onNetworkStateChange(options: ObserverOptions, callback: Callback<NetworkState>): void-End-->

**系统能力：** SystemCapability.Telephony.StateRegistry

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| options | [ObserverOptions](arkts-telephony-observer-observeroptions-i.md) | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;NetworkState&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [8300999](../errorcode-telephony.md#8300999-内部错误) |
| [8300002](../errorcode-telephony.md#8300002-服务连接失败) |
| [8300003](../errorcode-telephony.md#8300003-系统内部错误) |
| [8300001](../errorcode-telephony.md#8300001-输入参数不在处理范围内) |
