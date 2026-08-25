# queryKey

## 导入模块

```TypeScript
import { contact } from 'kits/@kit.ContactsKit';
```

## queryKey

```TypeScript
function queryKey(id: number, callback: AsyncCallback<string>): void
```

根据联系人的id查询联系人的唯一查询键key。使用callback异步回调。

**起始版本：** 7

**废弃版本：** 10

**替代接口：** [queryKey](#querykey)(context: Context, id: number, callback: AsyncCallback&lt;string&gt;)

**需要权限：** ohos.permission.READ_CONTACTS

**系统能力：** SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| id | number | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 |


## queryKey

```TypeScript
function queryKey(context: Context, id: number, callback: AsyncCallback<string>): void
```

根据联系人的id查询联系人的唯一查询键key。使用callback异步回调。

**起始版本：** 10

**需要权限：** ohos.permission.READ_CONTACTS

**系统能力：** SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-arkui/arkts-components/arkts-arkui-context-t.md) | 是 |
| id | number | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../errorcode-contacts.md#401-打开联系人头像文件失败) |


## queryKey

```TypeScript
function queryKey(id: number, holder: Holder, callback: AsyncCallback<string>): void
```

根据联系人的id和holder查询联系人的唯一查询键key。使用callback异步回调。

**起始版本：** 7

**废弃版本：** 10

**替代接口：** [queryKey](#querykey)(context: Context, id: number, holder: Holder, callback: AsyncCallback&lt;string&gt;)

**需要权限：** ohos.permission.READ_CONTACTS

**系统能力：** SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| id | number | 是 |
| holder | [Holder](arkts-contacts-contact-holder-c.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 |


## queryKey

```TypeScript
function queryKey(context: Context, id: number, holder: Holder, callback: AsyncCallback<string>): void
```

根据联系人的id和holder查询联系人的唯一查询键key。使用callback异步回调。

**起始版本：** 10

**需要权限：** ohos.permission.READ_CONTACTS

**系统能力：** SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-arkui/arkts-components/arkts-arkui-context-t.md) | 是 |
| id | number | 是 |
| holder | [Holder](arkts-contacts-contact-holder-c.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../errorcode-contacts.md#401-打开联系人头像文件失败) |


## queryKey

```TypeScript
function queryKey(id: number, holder?: Holder): Promise<string>
```

根据联系人的id和holder查询联系人的唯一查询键key。使用Promise异步回调。

**起始版本：** 7

**废弃版本：** 10

**替代接口：** [queryKey](#querykey)(context: Context, id: number, holder?: Holder)

**需要权限：** ohos.permission.READ_CONTACTS

**系统能力：** SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| id | number | 是 |
| holder | [Holder](arkts-contacts-contact-holder-c.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |


## queryKey

```TypeScript
function queryKey(context: Context, id: number, holder?: Holder): Promise<string>
```

根据联系人的id和holder查询联系人的唯一查询键key。使用Promise异步回调。

**起始版本：** 10

**需要权限：** ohos.permission.READ_CONTACTS

**系统能力：** SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-arkui/arkts-components/arkts-arkui-context-t.md) | 是 |
| id | number | 是 |
| holder | [Holder](arkts-contacts-contact-holder-c.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;string & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../errorcode-contacts.md#401-打开联系人头像文件失败) |
