# queryContacts

## 导入模块

```TypeScript
import { contact } from 'kits/@kit.ContactsKit';
```

## queryContacts

```TypeScript
function queryContacts(callback: AsyncCallback<Array<Contact>>): void
```

查询所有联系人。使用callback异步回调。

**起始版本：** 7

**废弃版本：** 10

**替代接口：** [queryContacts](#querycontacts)(context: Context, callback: AsyncCallback&lt;Array&lt;Contact&gt;&gt;)

**需要权限：** ohos.permission.READ_CONTACTS

**系统能力：** SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[Contact](arkts-contacts-contact-contact-c.md)&gt;&gt; | 是 |


## queryContacts

```TypeScript
function queryContacts(context: Context, callback: AsyncCallback<Array<Contact>>): void
```

查询所有联系人。使用callback异步回调。

**起始版本：** 10

**需要权限：** ohos.permission.READ_CONTACTS

**系统能力：** SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-arkui/arkts-components/arkts-arkui-context-t.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[Contact](arkts-contacts-contact-contact-c.md)&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../errorcode-contacts.md#401-打开联系人头像文件失败) |


## queryContacts

```TypeScript
function queryContacts(holder: Holder, callback: AsyncCallback<Array<Contact>>): void
```

根据holder查询所有联系人。使用callback异步回调。

**起始版本：** 7

**废弃版本：** 10

**替代接口：** [queryContacts](#querycontacts)(context: Context, holder: Holder, callback: AsyncCallback&lt;Array&lt;Contact&gt;&gt;)

**需要权限：** ohos.permission.READ_CONTACTS

**系统能力：** SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| holder | [Holder](arkts-contacts-contact-holder-c.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[Contact](arkts-contacts-contact-contact-c.md)&gt;&gt; | 是 |


## queryContacts

```TypeScript
function queryContacts(context: Context, holder: Holder, callback: AsyncCallback<Array<Contact>>): void
```

根据holder查询所有联系人。使用callback异步回调。

**起始版本：** 10

**需要权限：** ohos.permission.READ_CONTACTS

**系统能力：** SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-arkui/arkts-components/arkts-arkui-context-t.md) | 是 |
| holder | [Holder](arkts-contacts-contact-holder-c.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[Contact](arkts-contacts-contact-contact-c.md)&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../errorcode-contacts.md#401-打开联系人头像文件失败) |


## queryContacts

```TypeScript
function queryContacts(attrs: ContactAttributes, callback: AsyncCallback<Array<Contact>>): void
```

根据attrs查询所有联系人。使用callback异步回调。

**起始版本：** 7

**废弃版本：** 10

**替代接口：** [queryContacts](#querycontacts)(context: Context, attrs: ContactAttributes, callback: AsyncCallback&lt;Array&lt;Contact&gt;&gt;)

**需要权限：** ohos.permission.READ_CONTACTS

**系统能力：** SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| attrs | [ContactAttributes](arkts-contacts-contact-contactattributes-c.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[Contact](arkts-contacts-contact-contact-c.md)&gt;&gt; | 是 |


## queryContacts

```TypeScript
function queryContacts(context: Context, attrs: ContactAttributes, callback: AsyncCallback<Array<Contact>>): void
```

根据attrs查询所有联系人。使用callback异步回调。

**起始版本：** 10

**需要权限：** ohos.permission.READ_CONTACTS

**系统能力：** SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-arkui/arkts-components/arkts-arkui-context-t.md) | 是 |
| attrs | [ContactAttributes](arkts-contacts-contact-contactattributes-c.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[Contact](arkts-contacts-contact-contact-c.md)&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../errorcode-contacts.md#401-打开联系人头像文件失败) |


## queryContacts

```TypeScript
function queryContacts(holder: Holder, attrs: ContactAttributes, callback: AsyncCallback<Array<Contact>>): void
```

根据holder和attrs查询所有联系人。使用callback异步回调。

**起始版本：** 7

**废弃版本：** 10

**替代接口：** [queryContacts](#querycontacts)(context: Context, holder: Holder, attrs: ContactAttributes, callback: AsyncCallback&lt;Array&lt;Contact&gt;&gt;)

**需要权限：** ohos.permission.READ_CONTACTS

**系统能力：** SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| holder | [Holder](arkts-contacts-contact-holder-c.md) | 是 |
| attrs | [ContactAttributes](arkts-contacts-contact-contactattributes-c.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[Contact](arkts-contacts-contact-contact-c.md)&gt;&gt; | 是 |


## queryContacts

```TypeScript
function queryContacts(context: Context, holder: Holder, attrs: ContactAttributes, callback: AsyncCallback<Array<Contact>>): void
```

根据holder和attrs查询所有联系人。使用callback异步回调。

**起始版本：** 10

**需要权限：** ohos.permission.READ_CONTACTS

**系统能力：** SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-arkui/arkts-components/arkts-arkui-context-t.md) | 是 |
| holder | [Holder](arkts-contacts-contact-holder-c.md) | 是 |
| attrs | [ContactAttributes](arkts-contacts-contact-contactattributes-c.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[Contact](arkts-contacts-contact-contact-c.md)&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../errorcode-contacts.md#401-打开联系人头像文件失败) |


## queryContacts

```TypeScript
function queryContacts(holder?: Holder, attrs?: ContactAttributes): Promise<Array<Contact>>
```

根据holder和attrs查询所有联系人。使用Promise异步回调。

**起始版本：** 7

**废弃版本：** 10

**替代接口：** [queryContacts](#querycontacts)(context: Context, holder?: Holder, attrs?: ContactAttributes)

**需要权限：** ohos.permission.READ_CONTACTS

**系统能力：** SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| holder | [Holder](arkts-contacts-contact-holder-c.md) | 否 |
| attrs | [ContactAttributes](arkts-contacts-contact-contactattributes-c.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;[Contact](arkts-contacts-contact-contact-c.md)&gt;&gt; |


## queryContacts

```TypeScript
function queryContacts(context: Context, holder?: Holder, attrs?: ContactAttributes): Promise<Array<Contact>>
```

根据holder和attrs查询所有联系人。使用Promise异步回调。

**起始版本：** 10

**需要权限：** ohos.permission.READ_CONTACTS

**系统能力：** SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-arkui/arkts-components/arkts-arkui-context-t.md) | 是 |
| holder | [Holder](arkts-contacts-contact-holder-c.md) | 否 |
| attrs | [ContactAttributes](arkts-contacts-contact-contactattributes-c.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;[Contact](arkts-contacts-contact-contact-c.md)&gt;&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../errorcode-contacts.md#401-打开联系人头像文件失败) |
