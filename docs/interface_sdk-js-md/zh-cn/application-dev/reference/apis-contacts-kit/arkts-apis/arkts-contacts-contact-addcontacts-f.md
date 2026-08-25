# addContacts

## 导入模块

```TypeScript
import { contact } from 'kits/@kit.ContactsKit';
```

## addContacts

```TypeScript
function addContacts(context: Context, contacts: Array<Contact>): Promise<Array<number>>
```

批量添加联系人。使用Promise异步回调。

**起始版本：** 23

**需要权限：** ohos.permission.WRITE_CONTACTS

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-arkui/arkts-components/arkts-arkui-context-t.md) | 是 |
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
