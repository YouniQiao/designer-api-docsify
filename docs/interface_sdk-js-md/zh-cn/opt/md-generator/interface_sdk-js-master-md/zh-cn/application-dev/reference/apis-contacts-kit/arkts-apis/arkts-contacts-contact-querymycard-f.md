# queryMyCard

## queryMyCard

```TypeScript
function queryMyCard(callback: AsyncCallback<Contact>): void
```

查询“我的名片”。使用callback异步回调。

**起始版本：** 7

**废弃版本：** 10

**替代接口：** [contact.queryMyCard](arkts-contacts-contact-querymycard-f.md#querymycard)(context:

**需要权限：** ohos.permission.READ_CONTACTS

<!--Device-contact-function queryMyCard(callback: AsyncCallback<Contact>): void--><!--Device-contact-function queryMyCard(callback: AsyncCallback<Contact>): void-End-->

**系统能力：** SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Contact&gt; | 是 |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { contact } from '@kit.ContactsKit';

// 回调函数，查询“我的名片”
contact.queryMyCard((err: BusinessError, data) => {
  if (err) {
    console.error(`Failed to query My Card. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in querying My Card. data->${JSON.stringify(data)}`);
});
```


## queryMyCard

```TypeScript
function queryMyCard(context: Context, callback: AsyncCallback<Contact>): void
```

查询“我的名片”。使用callback异步回调。

**起始版本：** 10

**需要权限：** ohos.permission.READ_CONTACTS

<!--Device-contact-function queryMyCard(context: Context, callback: AsyncCallback<Contact>): void--><!--Device-contact-function queryMyCard(context: Context, callback: AsyncCallback<Contact>): void-End-->

**系统能力：** SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-arkui/arkts-components/arkts-arkui-context-t.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Contact&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../errorcode-contacts.md#401-系统内部错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |

## 示例

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在界面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](../../application-models/uiability-usage.md#获取uiability的上下文信息)。

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
  import { contact } from '@kit.ContactsKit';
  import { common } from '@kit.AbilityKit';

  // 请在组件内获取context。
  let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
  contact.queryMyCard(context, (err: BusinessError, data) => {
    if (err) {
      console.error(`Failed to query My Card. Code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info(`Succeeded in querying My Card. data->${JSON.stringify(data)}`);
  });
```


## queryMyCard

```TypeScript
function queryMyCard(attrs: ContactAttributes, callback: AsyncCallback<Contact>): void
```

查询“我的名片”（支持传入联系人的属性列表）。使用callback异步回调。

**起始版本：** 7

**废弃版本：** 10

**替代接口：** [contact.queryMyCard](arkts-contacts-contact-querymycard-f.md#querymycard)(context:

**需要权限：** ohos.permission.READ_CONTACTS

<!--Device-contact-function queryMyCard(attrs: ContactAttributes, callback: AsyncCallback<Contact>): void--><!--Device-contact-function queryMyCard(attrs: ContactAttributes, callback: AsyncCallback<Contact>): void-End-->

**系统能力：** SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| attrs | [ContactAttributes](arkts-contacts-contact-contactattributes-c.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Contact&gt; | 是 |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { contact } from '@kit.ContactsKit';

// 传入联系人的属性列表，查询“我的名片”
contact.queryMyCard({
  attributes: [contact.Attribute.ATTR_NAME, contact.Attribute.ATTR_PHONE]
}, (err: BusinessError, data) => {
  if (err) {
    console.error(`Failed to query My Card. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in querying My Card. data->${JSON.stringify(data)}`);
});
```


## queryMyCard

```TypeScript
function queryMyCard(context: Context, attrs: ContactAttributes, callback: AsyncCallback<Contact>): void
```

查询“我的名片”（支持传入联系人的属性列表）。使用callback异步回调。

**起始版本：** 10

**需要权限：** ohos.permission.READ_CONTACTS

<!--Device-contact-function queryMyCard(context: Context, attrs: ContactAttributes, callback: AsyncCallback<Contact>): void--><!--Device-contact-function queryMyCard(context: Context, attrs: ContactAttributes, callback: AsyncCallback<Contact>): void-End-->

**系统能力：** SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-arkui/arkts-components/arkts-arkui-context-t.md) | 是 |
| attrs | [ContactAttributes](arkts-contacts-contact-contactattributes-c.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Contact&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../errorcode-contacts.md#401-系统内部错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |

## 示例

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在界面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](../../application-models/uiability-usage.md#获取uiability的上下文信息)。

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
  import { contact } from '@kit.ContactsKit';
  import { common } from '@kit.AbilityKit';

  // 请在组件内获取context。
  let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
  contact.queryMyCard(context, {
    attributes: [contact.Attribute.ATTR_NAME, contact.Attribute.ATTR_PHONE]
  }, (err: BusinessError, data) => {
    if (err) {
      console.error(`Failed to query My Card. Code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info(`Succeeded in querying My Card. data->${JSON.stringify(data)}`);
  });
```


## queryMyCard

```TypeScript
function queryMyCard(attrs?: ContactAttributes): Promise<Contact>
```

查询“我的名片”（支持传入联系人的属性列表）。使用Promise异步回调。

**起始版本：** 7

**废弃版本：** 10

**替代接口：** [contact.queryMyCard](arkts-contacts-contact-querymycard-f.md#querymycard)(context:

**需要权限：** ohos.permission.READ_CONTACTS

<!--Device-contact-function queryMyCard(attrs?: ContactAttributes): Promise<Contact>--><!--Device-contact-function queryMyCard(attrs?: ContactAttributes): Promise<Contact>-End-->

**系统能力：** SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| attrs | [ContactAttributes](arkts-contacts-contact-contactattributes-c.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;Contact&gt; |

## 示例

```TypeScript
import { contact } from '@kit.ContactsKit';

// 回调函数，传入联系人的属性列表，查询“我的名片”。
let promise = contact.queryMyCard({
  attributes: [contact.Attribute.ATTR_NAME, contact.Attribute.ATTR_PHONE]
});
promise.then((data) => {
  console.info(`Succeeded in querying My Card. data->${JSON.stringify(data)}`);
});
```


## queryMyCard

```TypeScript
function queryMyCard(context: Context, attrs?: ContactAttributes): Promise<Contact>
```

查询"我的名片"（支持传入联系人的属性列表）。使用Promise异步回调。

**起始版本：** 10

**需要权限：** ohos.permission.READ_CONTACTS

<!--Device-contact-function queryMyCard(context: Context, attrs?: ContactAttributes): Promise<Contact>--><!--Device-contact-function queryMyCard(context: Context, attrs?: ContactAttributes): Promise<Contact>-End-->

**系统能力：** SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-arkui/arkts-components/arkts-arkui-context-t.md) | 是 |
| attrs | [ContactAttributes](arkts-contacts-contact-contactattributes-c.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;Contact&gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../errorcode-contacts.md#401-系统内部错误) |
| [201](../../errorcode-universal.md#201-权限校验失败) |

## 示例

在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的UIAbility实例。如需要在界面中使用UIAbilityContext提供的能力，请参见[获取UIAbility的上下文信息](../../application-models/uiability-usage.md#获取uiability的上下文信息)。

```TypeScript
import { contact } from '@kit.ContactsKit';
  import { common } from '@kit.AbilityKit';

  // 请在组件内获取context。
  let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
  let promise = contact.queryMyCard(context, {
    attributes: [contact.Attribute.ATTR_NAME, contact.Attribute.ATTR_PHONE]
  });
  promise.then((data) => {
    console.info(`Succeeded in querying My Card. data->${JSON.stringify(data)}`);
  });
```
