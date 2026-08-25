# queryGroups

## 导入模块

```TypeScript
import { contact } from 'kits/@kit.ContactsKit';
```

## queryGroups

```TypeScript
function queryGroups(callback: AsyncCallback<Array<Group>>): void
```

查询联系人的所有群组。使用callback异步回调。

**起始版本：** 7

**废弃版本：** 10

**替代接口：** [queryGroups](#querygroups)(context: Context, callback: AsyncCallback&lt;Array&lt;Group&gt;&gt;)

**需要权限：** ohos.permission.READ_CONTACTS

**系统能力：** SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[Group](arkts-contacts-contact-group-c.md)&gt;&gt; | 是 |


## queryGroups

```TypeScript
function queryGroups(context: Context, callback: AsyncCallback<Array<Group>>): void
```

查询联系人的所有群组。使用callback异步回调。

**起始版本：** 10

**需要权限：** ohos.permission.READ_CONTACTS

**系统能力：** SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-arkui/arkts-components/arkts-arkui-context-t.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[Group](arkts-contacts-contact-group-c.md)&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../errorcode-contacts.md#401-打开联系人头像文件失败) |


## queryGroups

```TypeScript
function queryGroups(holder: Holder, callback: AsyncCallback<Array<Group>>): void
```

根据holder查询联系人的所有群组。使用callback异步回调。

**起始版本：** 7

**废弃版本：** 10

**替代接口：** [queryGroups](#querygroups)(context: Context, holder: Holder, callback: AsyncCallback&lt;Array&lt;Group&gt;&gt;)

**需要权限：** ohos.permission.READ_CONTACTS

**系统能力：** SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| holder | [Holder](arkts-contacts-contact-holder-c.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[Group](arkts-contacts-contact-group-c.md)&gt;&gt; | 是 |


## queryGroups

```TypeScript
function queryGroups(context: Context, holder: Holder, callback: AsyncCallback<Array<Group>>): void
```

根据holder查询联系人的所有群组。使用callback异步回调。

**起始版本：** 10

**需要权限：** ohos.permission.READ_CONTACTS

**系统能力：** SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-arkui/arkts-components/arkts-arkui-context-t.md) | 是 |
| holder | [Holder](arkts-contacts-contact-holder-c.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[Group](arkts-contacts-contact-group-c.md)&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../errorcode-contacts.md#401-打开联系人头像文件失败) |


## queryGroups

```TypeScript
function queryGroups(holder?: Holder): Promise<Array<Group>>
```

根据holder查询联系人的所有群组。使用Promise异步回调。

**起始版本：** 7

**废弃版本：** 10

**替代接口：** [queryGroups](#querygroups)(context: Context, holder?: Holder)

**需要权限：** ohos.permission.READ_CONTACTS

**系统能力：** SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| holder | [Holder](arkts-contacts-contact-holder-c.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;[Group](arkts-contacts-contact-group-c.md)&gt;&gt; |


## queryGroups

```TypeScript
function queryGroups(context: Context, holder?: Holder): Promise<Array<Group>>
```

根据holder查询联系人的所有群组。使用Promise异步回调。

**起始版本：** 10

**需要权限：** ohos.permission.READ_CONTACTS

**系统能力：** SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-arkui/arkts-components/arkts-arkui-context-t.md) | 是 |
| holder | [Holder](arkts-contacts-contact-holder-c.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;[Group](arkts-contacts-contact-group-c.md)&gt;&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../errorcode-contacts.md#401-打开联系人头像文件失败) |
