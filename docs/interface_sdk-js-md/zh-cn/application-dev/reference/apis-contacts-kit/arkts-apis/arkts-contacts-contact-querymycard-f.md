# queryMyCard

## 导入模块

```TypeScript
import { contact } from 'kits/@kit.ContactsKit';
```

## queryMyCard

```TypeScript
function queryMyCard(callback: AsyncCallback<Contact>): void
```

查询“我的名片”。使用callback异步回调。

**起始版本：** 7

**废弃版本：** 10

**替代接口：** [queryMyCard](#querymycard)(context: Context, callback: AsyncCallback&lt;Contact&gt;)

**需要权限：** ohos.permission.READ_CONTACTS

**系统能力：** SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[Contact](arkts-contacts-contact-contact-c.md)&gt; | 是 |


## queryMyCard

```TypeScript
function queryMyCard(context: Context, callback: AsyncCallback<Contact>): void
```

查询“我的名片”。使用callback异步回调。

**起始版本：** 10

**需要权限：** ohos.permission.READ_CONTACTS

**系统能力：** SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-arkui/arkts-components/arkts-arkui-context-t.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[Contact](arkts-contacts-contact-contact-c.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../errorcode-contacts.md#401-打开联系人头像文件失败) |


## queryMyCard

```TypeScript
function queryMyCard(attrs: ContactAttributes, callback: AsyncCallback<Contact>): void
```

查询“我的名片”（支持传入联系人的属性列表）。使用callback异步回调。

**起始版本：** 7

**废弃版本：** 10

**替代接口：** [queryMyCard](#querymycard)(context: Context, attrs: ContactAttributes, callback: AsyncCallback&lt;Contact&gt;)

**需要权限：** ohos.permission.READ_CONTACTS

**系统能力：** SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| attrs | [ContactAttributes](arkts-contacts-contact-contactattributes-c.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[Contact](arkts-contacts-contact-contact-c.md)&gt; | 是 |


## queryMyCard

```TypeScript
function queryMyCard(context: Context, attrs: ContactAttributes, callback: AsyncCallback<Contact>): void
```

查询“我的名片”（支持传入联系人的属性列表）。使用callback异步回调。

**起始版本：** 10

**需要权限：** ohos.permission.READ_CONTACTS

**系统能力：** SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-arkui/arkts-components/arkts-arkui-context-t.md) | 是 |
| attrs | [ContactAttributes](arkts-contacts-contact-contactattributes-c.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[Contact](arkts-contacts-contact-contact-c.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../errorcode-contacts.md#401-打开联系人头像文件失败) |


## queryMyCard

```TypeScript
function queryMyCard(attrs?: ContactAttributes): Promise<Contact>
```

查询“我的名片”（支持传入联系人的属性列表）。使用Promise异步回调。

**起始版本：** 7

**废弃版本：** 10

**替代接口：** [queryMyCard](#querymycard)(context: Context, attrs?: ContactAttributes)

**需要权限：** ohos.permission.READ_CONTACTS

**系统能力：** SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| attrs | [ContactAttributes](arkts-contacts-contact-contactattributes-c.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[Contact](arkts-contacts-contact-contact-c.md)&gt; |


## queryMyCard

```TypeScript
function queryMyCard(context: Context, attrs?: ContactAttributes): Promise<Contact>
```

查询"我的名片"（支持传入联系人的属性列表）。使用Promise异步回调。

**起始版本：** 10

**需要权限：** ohos.permission.READ_CONTACTS

**系统能力：** SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-arkui/arkts-components/arkts-arkui-context-t.md) | 是 |
| attrs | [ContactAttributes](arkts-contacts-contact-contactattributes-c.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;[Contact](arkts-contacts-contact-contact-c.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../errorcode-contacts.md#401-打开联系人头像文件失败) |
