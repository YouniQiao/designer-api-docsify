# queryContactSyncInfo

## 导入模块

```TypeScript
import { contact } from 'kits/@kit.ContactsKit';
```

## queryContactSyncInfo

```TypeScript
function queryContactSyncInfo(context: Context): Promise<Array<ContactSyncInfo>>
```

查询调用应用程序正在进行的联系人同步信息。如果返回的联系人同步信息为空，则调用方不进行联系人同步或联系人同步已完成。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.READ_CONTACTS

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-arkui/arkts-components/arkts-arkui-context-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;[ContactSyncInfo](arkts-contacts-contact-contactsyncinfo-i.md)&gt;&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [16700001](../errorcode-contacts.md#16700001-系统内部错误) |
