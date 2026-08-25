# queryHolders

## 导入模块

```TypeScript
import { contact } from 'kits/@kit.ContactsKit';
```

## queryHolders

```TypeScript
function queryHolders(callback: AsyncCallback<Array<Holder>>): void
```

查询所有创建联系人的应用信息类。使用callback异步回调。

**起始版本：** 7

**废弃版本：** 10

**替代接口：** [queryHolders](#queryholders)(context: Context, callback: AsyncCallback&lt;Array&lt;Holder&gt;&gt;)

**需要权限：** ohos.permission.READ_CONTACTS

**系统能力：** SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[Holder](arkts-contacts-contact-holder-c.md)&gt;&gt; | 是 |


## queryHolders

```TypeScript
function queryHolders(context: Context, callback: AsyncCallback<Array<Holder>>): void
```

查询所有创建联系人的应用信息类。使用callback异步回调。

**起始版本：** 10

**需要权限：** ohos.permission.READ_CONTACTS

**系统能力：** SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-arkui/arkts-components/arkts-arkui-context-t.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[Holder](arkts-contacts-contact-holder-c.md)&gt;&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../errorcode-contacts.md#401-打开联系人头像文件失败) |


## queryHolders

```TypeScript
function queryHolders(): Promise<Array<Holder>>
```

查询所有创建联系人的应用信息类。使用Promise异步回调。

**起始版本：** 7

**废弃版本：** 10

**替代接口：** [queryHolders](#queryholders)(context: Context)

**需要权限：** ohos.permission.READ_CONTACTS

**系统能力：** SystemCapability.Applications.ContactsData

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;[Holder](arkts-contacts-contact-holder-c.md)&gt;&gt; |


## queryHolders

```TypeScript
function queryHolders(context: Context): Promise<Array<Holder>>
```

查询所有创建联系人的应用信息类。使用Promise异步回调。

**起始版本：** 10

**需要权限：** ohos.permission.READ_CONTACTS

**系统能力：** SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-arkui/arkts-components/arkts-arkui-context-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;[Holder](arkts-contacts-contact-holder-c.md)&gt;&gt; |

**错误码：**

| 错误码ID |
| --- |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| [401](../errorcode-contacts.md#401-打开联系人头像文件失败) |
