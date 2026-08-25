# queryContactsByPhoneNumber

## 导入模块

```TypeScript
import { contact } from 'kits/@kit.ContactsKit';
```

## queryContactsByPhoneNumber

```TypeScript
function queryContactsByPhoneNumber(phoneNumber: string, callback: AsyncCallback<Array<Contact>>): void
```

根据电话号码查询联系人。使用callback异步回调。该接口仅返回联系人信息中的id、key、phoneNumbers属性。如果要查询联系人的所有信息，建议使用 [queryContact](arkts-contacts-contact-querycontact-f.md) 接口，根据该接口返回的属性key查询。应用在后台调用此接口获取联系人信息必须要申请对应的长时任务。

**起始版本：** 7

**废弃版本：** 10

**替代接口：** [queryContactsByPhoneNumber](#querycontactsbyphonenumber)(context: Context, phoneNumber: string, callback: AsyncCallback&lt;Array&lt;Contact&gt;&gt;)

**需要权限：** ohos.permission.READ_CONTACTS

**系统能力：** SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| phoneNumber | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[Contact](arkts-contacts-contact-contact-c.md)&gt;&gt; | 是 |


## queryContactsByPhoneNumber

```TypeScript
function queryContactsByPhoneNumber(context: Context, phoneNumber: string, callback: AsyncCallback<Array<Contact>>): void
```

根据电话号码查询联系人。使用callback异步回调。该接口仅返回联系人信息中的id、key、phoneNumbers属性。如果要查询联系人的所有信息，建议使用 [queryContact](arkts-contacts-contact-querycontact-f.md) 接口，根据该接口返回的属性key查询。应用在后台调用此接口获取联系人信息必须要申请对应的长时任务。

**起始版本：** 10

**需要权限：** ohos.permission.READ_CONTACTS

**系统能力：** SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-arkui/arkts-components/arkts-arkui-context-t.md) | 是 |
| phoneNumber | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[Contact](arkts-contacts-contact-contact-c.md)&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../errorcode-contacts.md#401-打开联系人头像文件失败) |


## queryContactsByPhoneNumber

```TypeScript
function queryContactsByPhoneNumber(phoneNumber: string, holder: Holder, callback: AsyncCallback<Array<Contact>>): void
```

根据电话号码和holder查询联系人，使用callback异步回调。该接口返回的列表仅包含联系人信息中的id、key、phoneNumbers属性。如果要查询联系人的所有信息，建议使用 [queryContact](arkts-contacts-contact-querycontact-f.md) 接口，根据该接口返回的属性key查询。应用在后台调用此接口获取联系人信息必须要申请对应的长时任务。

**起始版本：** 7

**废弃版本：** 10

**替代接口：** [queryContactsByPhoneNumber](#querycontactsbyphonenumber)(context: Context, phoneNumber: string, holder: Holder, callback: AsyncCallback&lt;Array&lt;Contact&gt;&gt;)

**需要权限：** ohos.permission.READ_CONTACTS

**系统能力：** SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| phoneNumber | string | 是 |
| holder | [Holder](arkts-contacts-contact-holder-c.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[Contact](arkts-contacts-contact-contact-c.md)&gt;&gt; | 是 |


## queryContactsByPhoneNumber

```TypeScript
function queryContactsByPhoneNumber(context: Context, phoneNumber: string, holder: Holder, callback: AsyncCallback<Array<Contact>>): void
```

根据电话号码和holder查询联系人。使用callback异步回调。该接口返回的列表仅包含联系人信息中的id、key、phoneNumbers属性。如果要查询联系人的所有信息，建议使用 [queryContact](arkts-contacts-contact-querycontact-f.md) 接口，根据该接口返回的属性key查询。应用在后台调用此接口获取联系人信息必须要申请对应的长时任务。

**起始版本：** 10

**需要权限：** ohos.permission.READ_CONTACTS

**系统能力：** SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-arkui/arkts-components/arkts-arkui-context-t.md) | 是 |
| phoneNumber | string | 是 |
| holder | [Holder](arkts-contacts-contact-holder-c.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[Contact](arkts-contacts-contact-contact-c.md)&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../errorcode-contacts.md#401-打开联系人头像文件失败) |


## queryContactsByPhoneNumber

```TypeScript
function queryContactsByPhoneNumber(phoneNumber: string, attrs: ContactAttributes, callback: AsyncCallback<Array<Contact>>): void
```

根据电话号码和attrs查询联系人。使用callback异步回调。该接口返回的列表仅包含联系人信息中的id、key、phoneNumbers属性。如果要查询联系人的所有信息，建议使用 [queryContact](arkts-contacts-contact-querycontact-f.md) 接口，根据该接口返回的属性key查询。应用在后台调用此接口获取联系人信息必须要申请对应的长时任务。

**起始版本：** 7

**废弃版本：** 10

**替代接口：** [queryContactsByPhoneNumber](#querycontactsbyphonenumber)(context: Context, phoneNumber: string, attrs: ContactAttributes, callback: AsyncCallback&lt;Array&lt;Contact&gt;&gt;)

**需要权限：** ohos.permission.READ_CONTACTS

**系统能力：** SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| phoneNumber | string | 是 |
| attrs | [ContactAttributes](arkts-contacts-contact-contactattributes-c.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[Contact](arkts-contacts-contact-contact-c.md)&gt;&gt; | 是 |


## queryContactsByPhoneNumber

```TypeScript
function queryContactsByPhoneNumber(context: Context, phoneNumber: string, attrs: ContactAttributes, callback: AsyncCallback<Array<Contact>>): void
```

根据电话号码和attrs查询联系人。使用callback异步回调。该接口返回的列表仅包含联系人信息中的id、key、phoneNumbers属性。如果要查询联系人的所有信息，建议使用 [queryContact](arkts-contacts-contact-querycontact-f.md) 接口，根据该接口返回的属性key查询。应用在后台调用此接口获取联系人信息必须要申请对应的长时任务。

**起始版本：** 10

**需要权限：** ohos.permission.READ_CONTACTS

**系统能力：** SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-arkui/arkts-components/arkts-arkui-context-t.md) | 是 |
| phoneNumber | string | 是 |
| attrs | [ContactAttributes](arkts-contacts-contact-contactattributes-c.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[Contact](arkts-contacts-contact-contact-c.md)&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../errorcode-contacts.md#401-打开联系人头像文件失败) |


## queryContactsByPhoneNumber

```TypeScript
function queryContactsByPhoneNumber(phoneNumber: string, holder: Holder, attrs: ContactAttributes, callback: AsyncCallback<Array<Contact>>): void
```

根据电话号码、holder和attrs查询联系人。使用callback异步回调。该接口返回的列表仅包含联系人信息中的id、key、phoneNumbers属性。如果要查询联系人的所有信息，建议使用 [queryContact](arkts-contacts-contact-querycontact-f.md) 接口，根据该接口返回的属性key查询。应用在后台调用此接口获取联系人信息必须要申请对应的长时任务。

**起始版本：** 7

**废弃版本：** 10

**替代接口：** [queryContactsByPhoneNumber](#querycontactsbyphonenumber)(context: Context, phoneNumber: string, holder: Holder, attrs: ContactAttributes, callback: AsyncCallback&lt;Array&lt;Contact&gt;&gt;)

**需要权限：** ohos.permission.READ_CONTACTS

**系统能力：** SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| phoneNumber | string | 是 |
| holder | [Holder](arkts-contacts-contact-holder-c.md) | 是 |
| attrs | [ContactAttributes](arkts-contacts-contact-contactattributes-c.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[Contact](arkts-contacts-contact-contact-c.md)&gt;&gt; | 是 |


## queryContactsByPhoneNumber

```TypeScript
function queryContactsByPhoneNumber(context: Context, phoneNumber: string, holder: Holder, attrs: ContactAttributes,
    callback: AsyncCallback<Array<Contact>>): void
```

根据电话号码、holder和attrs查询联系人。使用callback异步回调。该接口返回的列表仅包含联系人信息中的id、key、phoneNumbers属性。如果要查询联系人的所有信息，建议使用 [queryContact](arkts-contacts-contact-querycontact-f.md) 接口，根据该接口返回的属性key查询。应用在后台调用此接口获取联系人信息必须要申请对应的长时任务。

**起始版本：** 10

**需要权限：** ohos.permission.READ_CONTACTS

**系统能力：** SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-arkui/arkts-components/arkts-arkui-context-t.md) | 是 |
| phoneNumber | string | 是 |
| holder | [Holder](arkts-contacts-contact-holder-c.md) | 是 |
| attrs | [ContactAttributes](arkts-contacts-contact-contactattributes-c.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[Contact](arkts-contacts-contact-contact-c.md)&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../errorcode-contacts.md#401-打开联系人头像文件失败) |


## queryContactsByPhoneNumber

```TypeScript
function queryContactsByPhoneNumber(phoneNumber: string, holder?: Holder, attrs?: ContactAttributes): Promise<Array<Contact>>
```

根据电话号码、holder和attrs查询联系人。使用Promise异步回调。该接口返回的列表仅包含联系人信息中的id、key、phoneNumbers属性。如果要查询联系人的所有信息，建议使用 [queryContact](arkts-contacts-contact-querycontact-f.md) 接口，根据该接口返回的属性key查询。应用在后台调用此接口获取联系人信息必须要申请对应的长时任务。

**起始版本：** 7

**废弃版本：** 10

**替代接口：** [queryContactsByPhoneNumber](#querycontactsbyphonenumber)(context: Context, phoneNumber: string, holder?: Holder, attrs?: ContactAttributes)

**需要权限：** ohos.permission.READ_CONTACTS

**系统能力：** SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| phoneNumber | string | 是 |
| holder | [Holder](arkts-contacts-contact-holder-c.md) | 否 |
| attrs | [ContactAttributes](arkts-contacts-contact-contactattributes-c.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;[Contact](arkts-contacts-contact-contact-c.md)&gt;&gt; |


## queryContactsByPhoneNumber

```TypeScript
function queryContactsByPhoneNumber(context: Context, phoneNumber: string, holder?: Holder, attrs?: ContactAttributes): Promise<Array<Contact>>
```

根据电话号码、holder和attrs查询联系人。使用Promise异步回调。该接口返回的列表仅包含联系人信息中的id、key、phoneNumbers属性。如果要查询联系人的所有信息，建议使用 [queryContact](arkts-contacts-contact-querycontact-f.md) 接口，根据该接口返回的属性key查询。应用在后台调用此接口获取联系人信息必须要申请对应的长时任务。

**起始版本：** 10

**需要权限：** ohos.permission.READ_CONTACTS

**系统能力：** SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-arkui/arkts-components/arkts-arkui-context-t.md) | 是 |
| phoneNumber | string | 是 |
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
