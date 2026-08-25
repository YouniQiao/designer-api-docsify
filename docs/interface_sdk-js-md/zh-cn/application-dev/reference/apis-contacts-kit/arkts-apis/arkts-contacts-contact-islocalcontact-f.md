# isLocalContact

## 导入模块

```TypeScript
import { contact } from 'kits/@kit.ContactsKit';
```

## isLocalContact

```TypeScript
function isLocalContact(id: number, callback: AsyncCallback<boolean>): void
```

判断当前联系人id是否在电话簿中。使用callback异步回调。

**起始版本：** 7

**废弃版本：** 10

**替代接口：** [isLocalContact](#islocalcontact)(context: Context, id: number, callback: AsyncCallback&lt;boolean&gt;)

**需要权限：** ohos.permission.READ_CONTACTS

**系统能力：** SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| id | number | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |


## isLocalContact

```TypeScript
function isLocalContact(context: Context, id: number, callback: AsyncCallback<boolean>): void
```

判断当前联系人id是否在电话簿中。使用callback异步回调。

**起始版本：** 10

**需要权限：** ohos.permission.READ_CONTACTS

**系统能力：** SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-arkui/arkts-components/arkts-arkui-context-t.md) | 是 |
| id | number | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../errorcode-contacts.md#401-打开联系人头像文件失败) |


## isLocalContact

```TypeScript
function isLocalContact(id: number): Promise<boolean>
```

判断当前联系人id是否在电话簿中。使用Promise异步回调。

**起始版本：** 7

**废弃版本：** 10

**替代接口：** [isLocalContact](#islocalcontact)(context: Context, id: number)

**需要权限：** ohos.permission.READ_CONTACTS

**系统能力：** SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| id | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |


## isLocalContact

```TypeScript
function isLocalContact(context: Context, id: number): Promise<boolean>
```

判断当前联系人id是否在电话簿中。使用Promise异步回调。

**起始版本：** 10

**需要权限：** ohos.permission.READ_CONTACTS

**系统能力：** SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-arkui/arkts-components/arkts-arkui-context-t.md) | 是 |
| id | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../errorcode-contacts.md#401-打开联系人头像文件失败) |
