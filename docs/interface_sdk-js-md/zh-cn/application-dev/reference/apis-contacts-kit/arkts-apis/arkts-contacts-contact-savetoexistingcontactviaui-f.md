# saveToExistingContactViaUI

## 导入模块

```TypeScript
import { contact } from 'kits/@kit.ContactsKit';
```

## saveToExistingContactViaUI

```TypeScript
function saveToExistingContactViaUI(context: Context, contact: Contact): Promise<number>
```

调用保存至已有联系人接口，选择联系人UI界面并完成编辑。使用Promise异步回调。

**起始版本：** 15

**原子化服务API：** 从API版本15开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Applications.Contacts

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-arkui/arkts-components/arkts-arkui-context-t.md) | 是 |
| [contact](arkts-contact.md) | [Contact](arkts-contacts-contact-contact-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../errorcode-contacts.md#401-打开联系人头像文件失败) |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [16700001](../errorcode-contacts.md#16700001-系统内部错误) |
| [16700101](../errorcode-contacts.md#16700101-查询数据库失败) |
| [16700102](../errorcode-contacts.md#16700102-增删改数据库失败) |
| [16700103](../errorcode-contacts.md#16700103-用户取消) |
