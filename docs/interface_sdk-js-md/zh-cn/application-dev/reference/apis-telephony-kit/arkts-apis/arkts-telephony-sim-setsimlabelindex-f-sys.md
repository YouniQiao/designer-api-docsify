# setSimLabelIndex（系统接口）

## 导入模块

```TypeScript
import { sim } from 'kits/@kit.TelephonyKit';
```

## setSimLabelIndex

```TypeScript
function setSimLabelIndex(simId: number, simLabelIndex: number): Promise<void>
```

设置SIM卡标签索引。

**起始版本：** 23

**需要权限：** ohos.permission.SET_TELEPHONY_STATE

**系统能力：** SystemCapability.Telephony.CoreService

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| simId | number | 是 |
| [simLabelIndex](arkts-telephony-sim-iccaccountinfo-i-sys.md) | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [8300001](../errorcode-telephony.md#8300001-输入参数不在处理范围内) |
| [8300002](../errorcode-telephony.md#8300002-服务连接失败) |
| [8300003](../errorcode-telephony.md#8300003-系统内部错误) |
| [8300999](../errorcode-telephony.md#8300999-内部错误) |
