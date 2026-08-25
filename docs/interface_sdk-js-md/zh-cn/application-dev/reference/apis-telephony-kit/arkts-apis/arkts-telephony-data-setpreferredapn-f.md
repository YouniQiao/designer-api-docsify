# setPreferredApn

## 导入模块

```TypeScript
import { data } from 'kits/@kit.TelephonyKit';
```

## setPreferredApn

```TypeScript
function setPreferredApn(apnId: number): Promise<boolean>
```

异步设置apnId对应的APN为首选APN。

> 注意:&gt;
> 如果传入的apnId为无效的apnId，切回运营商默认配置的优选Apn。

**起始版本：** 16

**需要权限：** ohos.permission.MANAGE_APN_SETTING

**系统能力：** SystemCapability.Telephony.CellularData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| apnId | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
