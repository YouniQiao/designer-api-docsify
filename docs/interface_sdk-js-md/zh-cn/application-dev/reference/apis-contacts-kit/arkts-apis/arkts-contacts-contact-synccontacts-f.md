# syncContacts

## 导入模块

```TypeScript
import { contact } from 'kits/@kit.ContactsKit';
```

## syncContacts

```TypeScript
function syncContacts(context: Context, mode: ContactSyncMode, progress: ContactSyncProgress, contacts: Array<Contact>): Promise<Array<number>>
```

批量同步多个联系人至联系人数据库。每次最多可批量同步400个联系人。调用方必须处于前台。

**起始版本：** 26.0.0

**需要权限：** ohos.permission.WRITE_CONTACTS

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-arkui/arkts-components/arkts-arkui-context-t.md) | 是 |
| mode | [ContactSyncMode](arkts-contacts-contact-contactsyncmode-e.md) | 是 |
| progress | [ContactSyncProgress](arkts-contacts-contact-contactsyncprogress-i.md) | 是 |
| contacts | Array&lt;[Contact](arkts-contacts-contact-contact-c.md)&gt; | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;number & gt; & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [16700001](../errorcode-contacts.md#16700001-系统内部错误) |
| [16700002](../errorcode-contacts.md#16700002-参数检查失败) |
| [16700003](../errorcode-contacts.md#16700003-禁止后台调用) |
| [16700004](../errorcode-contacts.md#16700004-联系人数量超过限制) |
| [16700103](../errorcode-contacts.md#16700103-用户取消) |
