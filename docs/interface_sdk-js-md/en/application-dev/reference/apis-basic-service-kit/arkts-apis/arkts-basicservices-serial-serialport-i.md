# SerialPort

串口对象，提供串口设备信息和通信相关能力

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-serial-interface SerialPort--><!--Device-serial-interface SerialPort-End-->

**System capability:** SystemCapability.BusManager.Serial

## Modules to Import

```TypeScript
import { serial } from 'kits/@kit.BasicServicesKit';
```

## close

```TypeScript
close(): Promise<void>
```

关闭串口。使用Promise异步回调。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SerialPort-close(): Promise<void>--><!--Device-SerialPort-close(): Promise<void>-End-->

**System capability:** SystemCapability.BusManager.Serial

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 35700001 | Service error. |
| 35700005 | Port not open. |

## drain

```TypeScript
drain(): Promise<void>
```

等待所有写入请求完成。使用Promise异步回调。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SerialPort-drain(): Promise<void>--><!--Device-SerialPort-drain(): Promise<void>-End-->

**System capability:** SystemCapability.BusManager.Serial

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 35700001 | Service error. |
| 35700003 | Virtual serial port disconnected. |
| 35700005 | Port not open. |

## flush

```TypeScript
flush(): Promise<void>
```

flush串口缓冲区。使用Promise异步回调。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SerialPort-flush(): Promise<void>--><!--Device-SerialPort-flush(): Promise<void>-End-->

**System capability:** SystemCapability.BusManager.Serial

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 35700001 | Service error. |
| 35700003 | Virtual serial port disconnected. |
| 35700005 | Port not open. |

## getCts

```TypeScript
getCts(): Promise<boolean>
```

获取cts信号状态。使用Promise异步回调。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SerialPort-getCts(): Promise<boolean>--><!--Device-SerialPort-getCts(): Promise<boolean>-End-->

**System capability:** SystemCapability.BusManager.Serial

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | Promise对象，返回CTS信号状态，表示是否允许发送数据 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 35700001 | Service error. |
| 35700003 | Virtual serial port disconnected. |
| 35700005 | Port not open. |

## getDsr

```TypeScript
getDsr(): Promise<boolean>
```

获取DSR信号状态，使用Promise异步返回

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SerialPort-getDsr(): Promise<boolean>--><!--Device-SerialPort-getDsr(): Promise<boolean>-End-->

**System capability:** SystemCapability.BusManager.Serial

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | DSR信号状态，true表示对端已就绪，false表示对端未就绪 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 35700001 | Service error. |
| 35700003 | Virtual serial port disconnected. |
| 35700005 | Port not open. |

## offDataRead

```TypeScript
offDataRead(callback?: Callback<Uint8Array>): void
```

取消监听串口端口接收数据事件。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SerialPort-offDataRead(callback?: Callback<Uint8Array>): void--><!--Device-SerialPort-offDataRead(callback?: Callback<Uint8Array>): void-End-->

**System capability:** SystemCapability.BusManager.Serial

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;Uint8Array&gt; | No | 回调函数，返回串口端口接收到的数据 &lt;br&gt;默认值:缺省行为：清除串口端口接收数据事件的所有监听。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 35700001 | Service error. |
| 35700005 | Port not open. |

## offDisconnect

```TypeScript
offDisconnect(callback?: Callback<void>): void
```

取消监听USB虚拟串口断开事件。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SerialPort-offDisconnect(callback?: Callback<void>): void--><!--Device-SerialPort-offDisconnect(callback?: Callback<void>): void-End-->

**System capability:** SystemCapability.BusManager.Serial

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;void&gt; | No | USB虚拟串口断开的回调函数。 &lt;br&gt;默认值：清除所有USB虚拟串口断开事件的回调函数。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 35700001 | Service error. |
| 35700005 | Port not open. |

## onDataRead

```TypeScript
onDataRead(callback: Callback<Uint8Array>): void
```

监听串口端口接收到的数据。使用Callback异步回调。调用{@link close}接口时，会清理全部回调

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SerialPort-onDataRead(callback: Callback<Uint8Array>): void--><!--Device-SerialPort-onDataRead(callback: Callback<Uint8Array>): void-End-->

**System capability:** SystemCapability.BusManager.Serial

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;Uint8Array&gt; | Yes | 回调函数，返回串口端口接收到的数据 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 35700001 | Service error. |
| 35700003 | Virtual serial port disconnected. |
| 35700005 | Port not open. |

## onDisconnect

```TypeScript
onDisconnect(callback: Callback<void>): void
```

监听USB虚拟串口断开事件。使用Callback异步回调。调用{@link close}接口时，会清理全部回调

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SerialPort-onDisconnect(callback: Callback<void>): void--><!--Device-SerialPort-onDisconnect(callback: Callback<void>): void-End-->

**System capability:** SystemCapability.BusManager.Serial

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [Callback](arkts-basicservices-base-callback-i.md)&lt;void&gt; | Yes | USB虚拟串口断开事件的回调函数。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 35700001 | Service error. |
| 35700005 | Port not open. |

## open

```TypeScript
open(config?: SerialConfigs): Promise<void>
```

打开端口。使用Promise异步回调。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SerialPort-open(config?: SerialConfigs): Promise<void>--><!--Device-SerialPort-open(config?: SerialConfigs): Promise<void>-End-->

**System capability:** SystemCapability.BusManager.Serial

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| config | [SerialConfigs](arkts-basicservices-serial-serialconfigs-i.md) | No | 串口通信参数 &lt;br&gt;默认值:默认值：参考SerialConfigs的默认值。 &lt;br&gt;Default value: Refer to the default value of SerialConfigs.. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 35700001 | Service error. |
| 35700002 | Invalid parameter. |
| 35700003 | Virtual serial port disconnected. |
| 35700004 | Port already in use. |
| 35700007 | User authorization required. |

## sendBrk

```TypeScript
sendBrk(): Promise<void>
```

发送brk信号。使用Promise异步回调。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SerialPort-sendBrk(): Promise<void>--><!--Device-SerialPort-sendBrk(): Promise<void>-End-->

**System capability:** SystemCapability.BusManager.Serial

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 35700001 | Service error. |
| 35700003 | Virtual serial port disconnected. |
| 35700005 | Port not open. |

## setDtr

```TypeScript
setDtr(enable: boolean): Promise<void>
```

设置DTR信号状态，使用Promise异步返回

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SerialPort-setDtr(enable: boolean): Promise<void>--><!--Device-SerialPort-setDtr(enable: boolean): Promise<void>-End-->

**System capability:** SystemCapability.BusManager.Serial

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enable | boolean | Yes | DTR信号状态，表示本端是否就绪。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | 不返回任何值的Promise。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 35700001 | Service error. |
| 35700003 | Virtual serial port disconnected. |
| 35700005 | Port not open. |

## setRts

```TypeScript
setRts(enable: boolean): Promise<void>
```

设置rts信号。使用Promise异步回调。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SerialPort-setRts(enable: boolean): Promise<void>--><!--Device-SerialPort-setRts(enable: boolean): Promise<void>-End-->

**System capability:** SystemCapability.BusManager.Serial

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enable | boolean | Yes | RTS信号状态，表示是否请求发送。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise对象，无返回结果 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 35700001 | Service error. |
| 35700003 | Virtual serial port disconnected. |
| 35700005 | Port not open. |

## write

ArkTS-Dyn:
```TypeScript
write(data: Uint8Array, timeout?: number): Promise<number>
```

ArkTS-Sta:
```TypeScript
write(data: Uint8Array, timeout?: int): Promise<int>
```

发送数据。使用Promise异步回调。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SerialPort-write(data: Uint8Array, timeout?: int): Promise<int>--><!--Device-SerialPort-write(data: Uint8Array, timeout?: int): Promise<int>-End-->

**System capability:** SystemCapability.BusManager.Serial

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | Uint8Array | Yes | 要发送的数据 &lt;br&gt;长度范围:(0,4096]。 |
| timeout | ArkTS-Dyn: number  <br>ArkTS-Sta：int | No | 超时时间 &lt;br&gt;长度范围:[0,300000]。取值限定为整数。单位:毫秒。默认值:0。 &lt;br&gt;表示端口无法写入数据时不等待，直接返回。 |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: Promise&lt;number&gt;  <br>ArkTS-Sta：Promise&lt;int&gt; | Promise对象，返回成功写入的长度 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 35700001 | Service error. |
| 35700002 | Invalid parameter. |
| 35700003 | Virtual serial port disconnected. |
| 35700005 | Port not open. |
| 35700006 | Transmission timeout. |

## portInfo

```TypeScript
readonly portInfo: SerialPortInfo
```

串口端口信息

**Type:** [SerialPortInfo](arkts-basicservices-serial-serialportinfo-i.md)

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-SerialPort-readonly portInfo: SerialPortInfo--><!--Device-SerialPort-readonly portInfo: SerialPortInfo-End-->

**System capability:** SystemCapability.BusManager.Serial

