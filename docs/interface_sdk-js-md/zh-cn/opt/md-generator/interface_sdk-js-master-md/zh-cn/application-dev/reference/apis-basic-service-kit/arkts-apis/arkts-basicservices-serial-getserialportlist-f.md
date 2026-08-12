# getSerialPortList

## getSerialPortList

```TypeScript
function getSerialPortList(): Promise<SerialPort[]>
```

获取串口列表。使用Promise异步回调。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-serial-function getSerialPortList(): Promise<SerialPort[]>--><!--Device-serial-function getSerialPortList(): Promise<SerialPort[]>-End-->

**系统能力：** SystemCapability.BusManager.Serial

**返回值：**

| 类型 |
| --- |
| Promise & lt;SerialPort[] & gt; |

**错误码：**

| 错误码ID |
| --- |
| [35700001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-basic-services-kit/errorcode-busmanager-serial.md#35700001-服务异常) |
| [203](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#203-企业管理策略禁止使用此系统功能) |
