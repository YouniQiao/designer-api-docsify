# deleteContact

## deleteContact

```TypeScript
function deleteContact(key: string, callback: AsyncCallback<void>): void
```

删除联系人。使用callback异步回调。

**起始版本：** 7

**废弃版本：** 10

**替代接口：** [deleteContact](#deleteContact)(context: Context, key: string, callback: AsyncCallback&lt;void&gt;)

**需要权限：** ohos.permission.WRITE_CONTACTS

<!--Device-contact-function deleteContact(key: string, callback: AsyncCallback<void>): void--><!--Device-contact-function deleteContact(key: string, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | string | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { contact } from '@kit.ContactsKit';

// 通过selectContacts接口选择联系人。
contact.selectContacts().then((data) => {
  // 请在组件内获取context。
  let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
  // 第一个参数传入选择联系人的key
  contact.deleteContact(data[0].key, (err: BusinessError) => {
    if (err) {
      console.error(`Failed to delete Contact. Code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info('Succeeded in deleting Contact.');
  });
});
```


## deleteContact

```TypeScript
function deleteContact(context: Context, key: string, callback: AsyncCallback<void>): void
```

删除联系人。使用callback异步回调。

**起始版本：** 10

**废弃版本：** -1

**需要权限：** ohos.permission.WRITE_CONTACTS

<!--Device-contact-function deleteContact(context: Context, key: string, callback: AsyncCallback<void>): void--><!--Device-contact-function deleteContact(context: Context, key: string, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-arkui/arkts-components/arkts-arkui-context-t.md) | 是 |
| key | string | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../errorcode-contacts.md#401-打开联系人头像文件失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |

## 示例

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在界面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](../../../application-models/uiability-usage.md#获取uiability的上下文信息)。

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
  import { contact } from '@kit.ContactsKit';
  import { common } from '@kit.AbilityKit';

 // 通过selectContacts接口选择联系人。
  contact.selectContacts().then((data) => {
    // 请在组件内获取context。
    let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
    // 第二个参数传入选择联系人的key
    contact.deleteContact(context, data[0].key, (err: BusinessError) => {
      if (err) {
        console.error(`Failed to delete Contact. Code: ${err.code}, message: ${err.message}`);
        return;
      }
      console.info('Succeeded in deleting Contact.');
    });
  });
```


## deleteContact

```TypeScript
function deleteContact(key: string): Promise<void>
```

删除联系人。使用Promise异步回调。

**起始版本：** 7

**废弃版本：** 10

**替代接口：** [deleteContact](#deleteContact)(context: Context, key: string)

**需要权限：** ohos.permission.WRITE_CONTACTS

<!--Device-contact-function deleteContact(key: string): Promise<void>--><!--Device-contact-function deleteContact(key: string): Promise<void>-End-->

**系统能力：** SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| key | string | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

## 示例

```TypeScript
import { contact } from '@kit.ContactsKit';

// 通过selectContacts接口选择联系人。
contact.selectContacts().then((data) => {
  // 第一个参数传入选择联系人的key
  let promise = contact.deleteContact(data[0].key);
  promise.then(() => {
    console.info(`Succeeded in deleting Contact.`);
  });
});
```


## deleteContact

```TypeScript
function deleteContact(context: Context, key: string): Promise<void>
```

删除联系人。使用Promise异步回调。

**起始版本：** 10

**废弃版本：** -1

**需要权限：** ohos.permission.WRITE_CONTACTS

<!--Device-contact-function deleteContact(context: Context, key: string): Promise<void>--><!--Device-contact-function deleteContact(context: Context, key: string): Promise<void>-End-->

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
| [401](../errorcode-contacts.md#401-打开联系人头像文件失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |

## 示例

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在界面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](../../../application-models/uiability-usage.md#获取uiability的上下文信息)。

```TypeScript
import { common } from '@kit.AbilityKit';
import { contact } from '@kit.ContactsKit';

// 通过selectContacts接口选择联系人。
contact.selectContacts().then((data) => {
  // 请在组件内获取context。
  let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
  // 第二个参数传入选择联系人的key
  let promise = contact.deleteContact(context, data[0].key);
  promise.then(() => {
    console.info(`Succeeded in deleting Contact.`);
  });
});
```
