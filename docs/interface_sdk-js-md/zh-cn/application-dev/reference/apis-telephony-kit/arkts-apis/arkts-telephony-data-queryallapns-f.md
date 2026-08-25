# queryAllApns

## 导入模块

```TypeScript
import { data } from 'kits/@kit.TelephonyKit';
```

## queryAllApns

```TypeScript
function queryAllApns(): Promise<Array<ApnInfo>>
```

异步获取默认移动数据的SIM卡的APN（access point name，接入点名称）信息。

**起始版本：** 16

**需要权限：** ohos.permission.MANAGE_APN_SETTING

**系统能力：** SystemCapability.Telephony.CellularData

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;[ApnInfo](arkts-telephony-data-apninfo-i.md)&gt;&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
