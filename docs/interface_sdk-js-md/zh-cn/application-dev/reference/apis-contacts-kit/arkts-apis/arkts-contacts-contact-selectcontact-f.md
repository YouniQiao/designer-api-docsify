# selectContact

## 导入模块

```TypeScript
import { contact } from 'kits/@kit.ContactsKit';
```

## selectContact

```TypeScript
function selectContact(callback: AsyncCallback<Array<Contact>>): void
```

调用选择联系人接口，打开选择联系人UI界面。使用callback异步回调。

**起始版本：** 7

**废弃版本：** 10

**替代接口：** [selectContacts](arkts-contacts-contact-selectcontacts-f.md)(callback: AsyncCallback&lt;Array&lt;Contact&gt;&gt;)

**系统能力：** SystemCapability.Applications.Contacts

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[Contact](arkts-contacts-contact-contact-c.md)&gt;&gt; | 是 |


## selectContact

```TypeScript
function selectContact(): Promise<Array<Contact>>
```

调用选择联系人接口，打开选择联系人UI界面。使用Promise异步回调。

**起始版本：** 7

**废弃版本：** 10

**替代接口：** [selectContacts](arkts-contacts-contact-selectcontacts-f.md)()

**系统能力：** SystemCapability.Applications.Contacts

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;[Contact](arkts-contacts-contact-contact-c.md)&gt;&gt; |
