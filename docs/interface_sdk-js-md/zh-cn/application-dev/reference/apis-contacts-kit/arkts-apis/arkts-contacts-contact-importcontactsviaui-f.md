# importContactsViaUI

## 导入模块

```TypeScript
import { contact } from 'kits/@kit.ContactsKit';
```

## importContactsViaUI

```TypeScript
function importContactsViaUI(context: Context, contacts: Array<Contact>): Promise<Array<number>>
```

通过UI交互批量导入多个联系人。每次最多可导入100个联系人。不支持导入联系人的头像。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Applications.Contacts

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
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [16700001](../errorcode-contacts.md#16700001-系统内部错误) |
| [16700002](../errorcode-contacts.md#16700002-参数检查失败) |
| [16700004](../errorcode-contacts.md#16700004-联系人数量超过限制) |
| [16700103](../errorcode-contacts.md#16700103-用户取消) |
