# deleteContact

## 导入模块

```TypeScript
import { contact } from 'kits/@kit.ContactsKit';
```

## deleteContact

```TypeScript
function deleteContact(key: string, callback: AsyncCallback<void>): void
```

删除联系人。使用callback异步回调。

**起始版本：** 7

**废弃版本：** 10

**替代接口：** [deleteContact](#deletecontact)(context: Context, key: string, callback: AsyncCallback&lt;void&gt;)

**需要权限：** ohos.permission.WRITE_CONTACTS

**系统能力：** SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |


## deleteContact

```TypeScript
function deleteContact(context: Context, key: string, callback: AsyncCallback<void>): void
```

删除联系人。使用callback异步回调。

**起始版本：** 10

**需要权限：** ohos.permission.WRITE_CONTACTS

**系统能力：** SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-arkui/arkts-components/arkts-arkui-context-t.md) | 是 |
| key | string | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../errorcode-contacts.md#401-打开联系人头像文件失败) |


## deleteContact

```TypeScript
function deleteContact(key: string): Promise<void>
```

删除联系人。使用Promise异步回调。

**起始版本：** 7

**废弃版本：** 10

**替代接口：** [deleteContact](#deletecontact)(context: Context, key: string)

**需要权限：** ohos.permission.WRITE_CONTACTS

**系统能力：** SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |


## deleteContact

```TypeScript
function deleteContact(context: Context, key: string): Promise<void>
```

删除联系人。使用Promise异步回调。

**起始版本：** 10

**需要权限：** ohos.permission.WRITE_CONTACTS

**系统能力：** SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-arkui/arkts-components/arkts-arkui-context-t.md) | 是 |
| key | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../errorcode-contacts.md#401-打开联系人头像文件失败) |
