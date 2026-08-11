# SerialPort

串口对象，提供串口设备信息和通信相关能力

**起始版本：** 26.0.0

<!--Device-serial-interface SerialPort--><!--Device-serial-interface SerialPort-End-->

**系统能力：** SystemCapability.BusManager.Serial

## close

```TypeScript
close(): Promise<void>
```

关闭串口。使用Promise异步回调。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SerialPort-close(): Promise<void>--><!--Device-SerialPort-close(): Promise<void>-End-->

**系统能力：** SystemCapability.BusManager.Serial

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [35700001](../../apis-basic-services-kit/errorcode-busmanager-serial.md#35700001-服务异常) |
| [35700005](../../apis-basic-services-kit/errorcode-busmanager-serial.md#35700005-端口未打开) |

## drain

```TypeScript
drain(): Promise<void>
```

等待所有写入请求完成。使用Promise异步回调。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SerialPort-drain(): Promise<void>--><!--Device-SerialPort-drain(): Promise<void>-End-->

**系统能力：** SystemCapability.BusManager.Serial

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [35700001](../../apis-basic-services-kit/errorcode-busmanager-serial.md#35700001-服务异常) |
| [35700003](../../apis-basic-services-kit/errorcode-busmanager-serial.md#35700003-虚拟串口断开) |
| [35700005](../../apis-basic-services-kit/errorcode-busmanager-serial.md#35700005-端口未打开) |

## flush

```TypeScript
flush(): Promise<void>
```

flush串口缓冲区。使用Promise异步回调。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SerialPort-flush(): Promise<void>--><!--Device-SerialPort-flush(): Promise<void>-End-->

**系统能力：** SystemCapability.BusManager.Serial

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [35700001](../../apis-basic-services-kit/errorcode-busmanager-serial.md#35700001-服务异常) |
| [35700003](../../apis-basic-services-kit/errorcode-busmanager-serial.md#35700003-虚拟串口断开) |
| [35700005](../../apis-basic-services-kit/errorcode-busmanager-serial.md#35700005-端口未打开) |

## getCts

```TypeScript
getCts(): Promise<boolean>
```

获取cts信号状态。使用Promise异步回调。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SerialPort-getCts(): Promise<boolean>--><!--Device-SerialPort-getCts(): Promise<boolean>-End-->

**系统能力：** SystemCapability.BusManager.Serial

**返回值：**

| 类型 |
| --- |
| Promise&lt;boolean&gt; |

**错误码：**

| 错误码ID |
| --- |
| [35700001](../../apis-basic-services-kit/errorcode-busmanager-serial.md#35700001-服务异常) |
| [35700003](../../apis-basic-services-kit/errorcode-busmanager-serial.md#35700003-虚拟串口断开) |
| [35700005](../../apis-basic-services-kit/errorcode-busmanager-serial.md#35700005-端口未打开) |

## getDsr

```TypeScript
getDsr(): Promise<boolean>
```

获取DSR信号状态，使用Promise异步返回

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SerialPort-getDsr(): Promise<boolean>--><!--Device-SerialPort-getDsr(): Promise<boolean>-End-->

**系统能力：** SystemCapability.BusManager.Serial

**返回值：**

| 类型 |
| --- |
| Promise&lt;boolean&gt; |

**错误码：**

| 错误码ID |
| --- |
| [35700001](../../apis-basic-services-kit/errorcode-busmanager-serial.md#35700001-服务异常) |
| [35700003](../../apis-basic-services-kit/errorcode-busmanager-serial.md#35700003-虚拟串口断开) |
| [35700005](../../apis-basic-services-kit/errorcode-busmanager-serial.md#35700005-端口未打开) |

## offDataRead

```TypeScript
offDataRead(callback?: Callback<Uint8Array>): void
```

取消监听串口端口接收数据事件。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SerialPort-offDataRead(callback?: Callback<Uint8Array>): void--><!--Device-SerialPort-offDataRead(callback?: Callback<Uint8Array>): void-End-->

**系统能力：** SystemCapability.BusManager.Serial

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;Uint8Array&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [35700001](../../apis-basic-services-kit/errorcode-busmanager-serial.md#35700001-服务异常) |
| [35700005](../../apis-basic-services-kit/errorcode-busmanager-serial.md#35700005-端口未打开) |

## offDisconnect

```TypeScript
offDisconnect(callback?: Callback<void>): void
```

取消监听USB虚拟串口断开事件。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SerialPort-offDisconnect(callback?: Callback<void>): void--><!--Device-SerialPort-offDisconnect(callback?: Callback<void>): void-End-->

**系统能力：** SystemCapability.BusManager.Serial

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;void&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [35700001](../../apis-basic-services-kit/errorcode-busmanager-serial.md#35700001-服务异常) |
| [35700005](../../apis-basic-services-kit/errorcode-busmanager-serial.md#35700005-端口未打开) |

## onDataRead

```TypeScript
onDataRead(callback: Callback<Uint8Array>): void
```

监听串口端口接收到的数据。使用Callback异步回调。调用{@link close}接口时，会清理全部回调

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SerialPort-onDataRead(callback: Callback<Uint8Array>): void--><!--Device-SerialPort-onDataRead(callback: Callback<Uint8Array>): void-End-->

**系统能力：** SystemCapability.BusManager.Serial

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;Uint8Array&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [35700001](../../apis-basic-services-kit/errorcode-busmanager-serial.md#35700001-服务异常) |
| [35700003](../../apis-basic-services-kit/errorcode-busmanager-serial.md#35700003-虚拟串口断开) |
| [35700005](../../apis-basic-services-kit/errorcode-busmanager-serial.md#35700005-端口未打开) |

## onDisconnect

```TypeScript
onDisconnect(callback: Callback<void>): void
```

监听USB虚拟串口断开事件。使用Callback异步回调。调用{@link close}接口时，会清理全部回调

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SerialPort-onDisconnect(callback: Callback<void>): void--><!--Device-SerialPort-onDisconnect(callback: Callback<void>): void-End-->

**系统能力：** SystemCapability.BusManager.Serial

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [35700001](../../apis-basic-services-kit/errorcode-busmanager-serial.md#35700001-服务异常) |
| [35700005](../../apis-basic-services-kit/errorcode-busmanager-serial.md#35700005-端口未打开) |

## open

```TypeScript
open(config?: SerialConfigs): Promise<void>
```

打开端口。使用Promise异步回调。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SerialPort-open(config?: SerialConfigs): Promise<void>--><!--Device-SerialPort-open(config?: SerialConfigs): Promise<void>-End-->

**系统能力：** SystemCapability.BusManager.Serial

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| config | [SerialConfigs](arkts-basicservices-serial-serialconfigs-i.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [35700001](../../apis-basic-services-kit/errorcode-busmanager-serial.md#35700001-服务异常) |
| [35700002](../../apis-basic-services-kit/errorcode-busmanager-serial.md#35700002-参数错误) |
| [35700003](../../apis-basic-services-kit/errorcode-busmanager-serial.md#35700003-虚拟串口断开) |
| [35700004](../../apis-basic-services-kit/errorcode-busmanager-serial.md#35700004-端口已被占用) |
| [35700007](../../apis-basic-services-kit/errorcode-busmanager-serial.md#35700007-需要用户授权) |

## sendBrk

```TypeScript
sendBrk(): Promise<void>
```

发送brk信号。使用Promise异步回调。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SerialPort-sendBrk(): Promise<void>--><!--Device-SerialPort-sendBrk(): Promise<void>-End-->

**系统能力：** SystemCapability.BusManager.Serial

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [35700001](../../apis-basic-services-kit/errorcode-busmanager-serial.md#35700001-服务异常) |
| [35700003](../../apis-basic-services-kit/errorcode-busmanager-serial.md#35700003-虚拟串口断开) |
| [35700005](../../apis-basic-services-kit/errorcode-busmanager-serial.md#35700005-端口未打开) |

## setDtr

```TypeScript
setDtr(enable: boolean): Promise<void>
```

设置DTR信号状态，使用Promise异步返回

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SerialPort-setDtr(enable: boolean): Promise<void>--><!--Device-SerialPort-setDtr(enable: boolean): Promise<void>-End-->

**系统能力：** SystemCapability.BusManager.Serial

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enable | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [35700001](../../apis-basic-services-kit/errorcode-busmanager-serial.md#35700001-服务异常) |
| [35700003](../../apis-basic-services-kit/errorcode-busmanager-serial.md#35700003-虚拟串口断开) |
| [35700005](../../apis-basic-services-kit/errorcode-busmanager-serial.md#35700005-端口未打开) |

## setRts

```TypeScript
setRts(enable: boolean): Promise<void>
```

设置rts信号。使用Promise异步回调。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SerialPort-setRts(enable: boolean): Promise<void>--><!--Device-SerialPort-setRts(enable: boolean): Promise<void>-End-->

**系统能力：** SystemCapability.BusManager.Serial

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enable | boolean | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;void&gt; |

**错误码：**

| 错误码ID |
| --- |
| [35700001](../../apis-basic-services-kit/errorcode-busmanager-serial.md#35700001-服务异常) |
| [35700003](../../apis-basic-services-kit/errorcode-busmanager-serial.md#35700003-虚拟串口断开) |
| [35700005](../../apis-basic-services-kit/errorcode-busmanager-serial.md#35700005-端口未打开) |

## write

```TypeScript
write(data: Uint8Array, timeout?: number): Promise<number>
```

发送数据。使用Promise异步回调。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SerialPort-write(data: Uint8Array, timeout?: int): Promise<int>--><!--Device-SerialPort-write(data: Uint8Array, timeout?: int): Promise<int>-End-->

**系统能力：** SystemCapability.BusManager.Serial

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| data | Uint8Array | 是 |
| timeout | number | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;number&gt; |

**错误码：**

| 错误码ID |
| --- |
| [35700001](../../apis-basic-services-kit/errorcode-busmanager-serial.md#35700001-服务异常) |
| [35700002](../../apis-basic-services-kit/errorcode-busmanager-serial.md#35700002-参数错误) |
| [35700003](../../apis-basic-services-kit/errorcode-busmanager-serial.md#35700003-虚拟串口断开) |
| [35700005](../../apis-basic-services-kit/errorcode-busmanager-serial.md#35700005-端口未打开) |
| [35700006](../../apis-basic-services-kit/errorcode-busmanager-serial.md#35700006-传输超时) |

## portInfo

```TypeScript
readonly portInfo: SerialPortInfo
```

串口端口信息

**类型：** [SerialPortInfo](arkts-basicservices-serial-serialportinfo-i.md)

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-SerialPort-readonly portInfo: SerialPortInfo--><!--Device-SerialPort-readonly portInfo: SerialPortInfo-End-->

**系统能力：** SystemCapability.BusManager.Serial
