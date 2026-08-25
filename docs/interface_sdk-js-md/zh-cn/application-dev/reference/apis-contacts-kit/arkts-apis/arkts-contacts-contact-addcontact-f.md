# addContact

## 导入模块

```TypeScript
import { contact } from 'kits/@kit.ContactsKit';
```

## addContact

```TypeScript
function addContact(contact: Contact, callback: AsyncCallback<number>): void
```

添加联系人。使用callback异步回调。

**起始版本：** 7

**废弃版本：** 10

**替代接口：** [addContact](#addcontact)(context: Context, contact: Contact, callback: AsyncCallback&lt;number&gt;)

**需要权限：** ohos.permission.WRITE_CONTACTS

**系统能力：** SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [contact](arkts-contact.md) | [Contact](arkts-contacts-contact-contact-c.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |


## addContact

```TypeScript
function addContact(context: Context, contact: Contact, callback: AsyncCallback<number>): void
```

添加联系人。使用callback异步回调。

**起始版本：** 10

**需要权限：** ohos.permission.WRITE_CONTACTS

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-arkui/arkts-components/arkts-arkui-context-t.md) | 是 |
| [contact](arkts-contact.md) | [Contact](arkts-contacts-contact-contact-c.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../errorcode-contacts.md#401-打开联系人头像文件失败) |


## addContact

```TypeScript
function addContact(contact: Contact): Promise<number>
```

添加联系人。使用Promise异步回调。

**起始版本：** 7

**废弃版本：** 10

**替代接口：** [addContact](#addcontact)(context: Context, contact: Contact)

**需要权限：** ohos.permission.WRITE_CONTACTS

**系统能力：** SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| [contact](arkts-contact.md) | [Contact](arkts-contacts-contact-contact-c.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |


## addContact

```TypeScript
function addContact(context: Context, contact: Contact): Promise<number>
```

添加联系人。使用Promise异步回调。

**起始版本：** 10

**需要权限：** ohos.permission.WRITE_CONTACTS

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.Applications.ContactsData

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
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../errorcode-contacts.md#401-打开联系人头像文件失败) |
