# queryApnIds

## 导入模块

```TypeScript
import { data } from 'kits/@kit.TelephonyKit';
```

## queryApnIds

```TypeScript
function queryApnIds(apnInfo: ApnInfo): Promise<Array<number>>
```

异步获取传入的ApnInfo对应的ApnId信息。

**起始版本：** 16

**需要权限：** ohos.permission.MANAGE_APN_SETTING

**系统能力：** SystemCapability.Telephony.CellularData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| apnInfo | [ApnInfo](arkts-telephony-data-apninfo-i.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;number & gt; & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
