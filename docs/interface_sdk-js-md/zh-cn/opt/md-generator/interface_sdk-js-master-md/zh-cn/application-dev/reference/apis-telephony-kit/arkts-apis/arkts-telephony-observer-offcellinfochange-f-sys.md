# offCellInfoChange（系统接口）

## 导入模块

```TypeScript
```

## offCellInfoChange

```TypeScript
function offCellInfoChange(callback?: Callback<Array<CellInformation>>): void
```

Cancel callback when the cell information is updated.

**起始版本：** 23

<!--Device-observer-function offCellInfoChange(callback?: Callback<Array<CellInformation>>): void--><!--Device-observer-function offCellInfoChange(callback?: Callback<Array<CellInformation>>): void-End-->

**系统能力：** SystemCapability.Telephony.StateRegistry

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;Array&lt;[CellInformation](arkts-telephony-observer-cellinformation-t-sys.md)&gt;&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [8300999](../errorcode-telephony.md#8300999-内部错误) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [8300002](../errorcode-telephony.md#8300002-服务连接失败) |
| [8300003](../errorcode-telephony.md#8300003-系统内部错误) |
| [8300001](../errorcode-telephony.md#8300001-输入参数不在处理范围内) |
