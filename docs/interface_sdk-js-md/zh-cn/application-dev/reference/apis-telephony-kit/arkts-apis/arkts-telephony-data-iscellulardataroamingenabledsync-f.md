# isCellularDataRoamingEnabledSync

## 导入模块

```TypeScript
import { data } from 'kits/@kit.TelephonyKit';
```

## isCellularDataRoamingEnabledSync

```TypeScript
function isCellularDataRoamingEnabledSync(slotId: number): boolean
```

检查蜂窝数据业务是否启用漫游，调用此API返回结果。

**起始版本：** 12

**需要权限：** ohos.permission.GET_NETWORK_INFO

**系统能力：** SystemCapability.Telephony.CellularData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| slotId | number | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [8300001](../errorcode-telephony.md#8300001-输入参数不在处理范围内) |
| [8300002](../errorcode-telephony.md#8300002-服务连接失败) |
| [8300003](../errorcode-telephony.md#8300003-系统内部错误) |
| [8300999](../errorcode-telephony.md#8300999-内部错误) |
