# queryContacts

## queryContacts

```TypeScript
function queryContacts(callback: AsyncCallback<Array<Contact>>): void
```

查询所有联系人。使用callback异步回调。

**起始版本：** 7

**废弃版本：** 10

**替代接口：** [contact.queryContacts](arkts-contacts-contact-querycontacts-f.md#querycontacts)(context:

**需要权限：** ohos.permission.READ_CONTACTS

<!--Device-contact-function queryContacts(callback: AsyncCallback<Array<Contact>>): void--><!--Device-contact-function queryContacts(callback: AsyncCallback<Array<Contact>>): void-End-->

**系统能力：** SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;Contact&gt;&gt; | 是 |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { contact } from '@kit.ContactsKit';

// 异步回调查询联系人
contact.queryContacts((err: BusinessError, data) => {
  if (err) {
    console.error(`Failed to query Contacts. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in querying Contacts. data->${JSON.stringify(data)}`);
});
```


## queryContacts

```TypeScript
function queryContacts(context: Context, callback: AsyncCallback<Array<Contact>>): void
```

查询所有联系人。使用callback异步回调。

**起始版本：** 10

**需要权限：** ohos.permission.READ_CONTACTS

<!--Device-contact-function queryContacts(context: Context, callback: AsyncCallback<Array<Contact>>): void--><!--Device-contact-function queryContacts(context: Context, callback: AsyncCallback<Array<Contact>>): void-End-->

**系统能力：** SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-arkui/arkts-components/arkts-arkui-context-t.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;Contact&gt;&gt; | 是 |

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
contact.queryContacts(context, (err: BusinessError, data) => {
  if (err) {
    console.error(`Failed to query Contacts. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in querying Contacts. data->${JSON.stringify(data)}`);
});
```


## queryContacts

```TypeScript
function queryContacts(holder: Holder, callback: AsyncCallback<Array<Contact>>): void
```

根据holder查询所有联系人。使用callback异步回调。

**起始版本：** 7

**废弃版本：** 10

**替代接口：** [contact.queryContacts](arkts-contacts-contact-querycontacts-f.md#querycontacts)(context:

**需要权限：** ohos.permission.READ_CONTACTS

<!--Device-contact-function queryContacts(holder: Holder, callback: AsyncCallback<Array<Contact>>): void--><!--Device-contact-function queryContacts(holder: Holder, callback: AsyncCallback<Array<Contact>>): void-End-->

**系统能力：** SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| holder | [Holder](arkts-contacts-contact-holder-c.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;Contact&gt;&gt; | 是 |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { contact } from '@kit.ContactsKit';

// 异步回调查询联系人
contact.queryContacts({
  holderId: 1,
  bundleName: '',
  displayName: ''
}, (err: BusinessError, data) => {
  if (err) {
    console.error(`Failed to query Contacts. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in querying Contacts. data->${JSON.stringify(data)}`);
});
```


## queryContacts

```TypeScript
function queryContacts(context: Context, holder: Holder, callback: AsyncCallback<Array<Contact>>): void
```

根据holder查询所有联系人。使用callback异步回调。

**起始版本：** 10

**需要权限：** ohos.permission.READ_CONTACTS

<!--Device-contact-function queryContacts(context: Context, holder: Holder, callback: AsyncCallback<Array<Contact>>): void--><!--Device-contact-function queryContacts(context: Context, holder: Holder, callback: AsyncCallback<Array<Contact>>): void-End-->

**系统能力：** SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-arkui/arkts-components/arkts-arkui-context-t.md) | 是 |
| holder | [Holder](arkts-contacts-contact-holder-c.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;Contact&gt;&gt; | 是 |

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
contact.queryContacts(context, {
  holderId: 1,
  bundleName: '',
  displayName: ''
}, (err: BusinessError, data) => {
  if (err) {
    console.error(`Failed to query Contacts. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in querying Contacts. data->${JSON.stringify(data)}`);
});
```


## queryContacts

```TypeScript
function queryContacts(attrs: ContactAttributes, callback: AsyncCallback<Array<Contact>>): void
```

根据attrs查询所有联系人。使用callback异步回调。

**起始版本：** 7

**废弃版本：** 10

**替代接口：** [contact.queryContacts](arkts-contacts-contact-querycontacts-f.md#querycontacts)(context:

**需要权限：** ohos.permission.READ_CONTACTS

<!--Device-contact-function queryContacts(attrs: ContactAttributes, callback: AsyncCallback<Array<Contact>>): void--><!--Device-contact-function queryContacts(attrs: ContactAttributes, callback: AsyncCallback<Array<Contact>>): void-End-->

**系统能力：** SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| attrs | [ContactAttributes](arkts-contacts-contact-contactattributes-c.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;Contact&gt;&gt; | 是 |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { contact } from '@kit.ContactsKit';

// 异步回调查询联系人
contact.queryContacts({
  attributes: [contact.Attribute.ATTR_NAME, contact.Attribute.ATTR_PHONE]
}, (err: BusinessError, data) => {
  if (err) {
    console.error(`Failed to query Contacts. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in querying Contacts. data->${JSON.stringify(data)}`);
});
```


## queryContacts

```TypeScript
function queryContacts(context: Context, attrs: ContactAttributes, callback: AsyncCallback<Array<Contact>>): void
```

根据attrs查询所有联系人。使用callback异步回调。

**起始版本：** 10

**需要权限：** ohos.permission.READ_CONTACTS

<!--Device-contact-function queryContacts(context: Context, attrs: ContactAttributes, callback: AsyncCallback<Array<Contact>>): void--><!--Device-contact-function queryContacts(context: Context, attrs: ContactAttributes, callback: AsyncCallback<Array<Contact>>): void-End-->

**系统能力：** SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-arkui/arkts-components/arkts-arkui-context-t.md) | 是 |
| attrs | [ContactAttributes](arkts-contacts-contact-contactattributes-c.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;Contact&gt;&gt; | 是 |

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
contact.queryContacts(context, {
  attributes: [contact.Attribute.ATTR_NAME, contact.Attribute.ATTR_PHONE]
}, (err: BusinessError, data) => {
  if (err) {
    console.error(`Failed to query Contacts. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in querying Contacts. data->${JSON.stringify(data)}`);
});
```


## queryContacts

```TypeScript
function queryContacts(holder: Holder, attrs: ContactAttributes, callback: AsyncCallback<Array<Contact>>): void
```

根据holder和attrs查询所有联系人。使用callback异步回调。

**起始版本：** 7

**废弃版本：** 10

**替代接口：** [contact.queryContacts](arkts-contacts-contact-querycontacts-f.md#querycontacts)(context:

**需要权限：** ohos.permission.READ_CONTACTS

<!--Device-contact-function queryContacts(holder: Holder, attrs: ContactAttributes, callback: AsyncCallback<Array<Contact>>): void--><!--Device-contact-function queryContacts(holder: Holder, attrs: ContactAttributes, callback: AsyncCallback<Array<Contact>>): void-End-->

**系统能力：** SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| holder | [Holder](arkts-contacts-contact-holder-c.md) | 是 |
| attrs | [ContactAttributes](arkts-contacts-contact-contactattributes-c.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;Contact&gt;&gt; | 是 |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { contact } from '@kit.ContactsKit';

// 异步回调查询联系人
contact.queryContacts({
  holderId: 1,
  bundleName: '',
  displayName: ''
}, {
  attributes: [contact.Attribute.ATTR_NAME, contact.Attribute.ATTR_PHONE]
}, (err: BusinessError, data) => {
  if (err) {
    console.error(`Failed to query Contacts. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in querying Contacts. data->${JSON.stringify(data)}`);
});
```


## queryContacts

```TypeScript
function queryContacts(context: Context, holder: Holder, attrs: ContactAttributes, callback: AsyncCallback<Array<Contact>>): void
```

根据holder和attrs查询所有联系人。使用callback异步回调。

**起始版本：** 10

**需要权限：** ohos.permission.READ_CONTACTS

<!--Device-contact-function queryContacts(context: Context, holder: Holder, attrs: ContactAttributes, callback: AsyncCallback<Array<Contact>>): void--><!--Device-contact-function queryContacts(context: Context, holder: Holder, attrs: ContactAttributes, callback: AsyncCallback<Array<Contact>>): void-End-->

**系统能力：** SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-arkui/arkts-components/arkts-arkui-context-t.md) | 是 |
| holder | [Holder](arkts-contacts-contact-holder-c.md) | 是 |
| attrs | [ContactAttributes](arkts-contacts-contact-contactattributes-c.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;Contact&gt;&gt; | 是 |

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
contact.queryContacts(context, {
  holderId: 1,
  bundleName: '',
  displayName: ''
}, {
  attributes: [contact.Attribute.ATTR_NAME, contact.Attribute.ATTR_PHONE]
}, (err: BusinessError, data) => {
  if (err) {
    console.error(`Failed to query Contacts. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in querying Contacts. data->${JSON.stringify(data)}`);
});
```


## queryContacts

```TypeScript
function queryContacts(holder?: Holder, attrs?: ContactAttributes): Promise<Array<Contact>>
```

根据holder和attrs查询所有联系人。使用Promise异步回调。

**起始版本：** 7

**废弃版本：** 10

**替代接口：** [contact.queryContacts](arkts-contacts-contact-querycontacts-f.md#querycontacts)(context:

**需要权限：** ohos.permission.READ_CONTACTS

<!--Device-contact-function queryContacts(holder?: Holder, attrs?: ContactAttributes): Promise<Array<Contact>>--><!--Device-contact-function queryContacts(holder?: Holder, attrs?: ContactAttributes): Promise<Array<Contact>>-End-->

**系统能力：** SystemCapability.Applications.ContactsData

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| holder | [Holder](arkts-contacts-contact-holder-c.md) | 否 |
| attrs | [ContactAttributes](arkts-contacts-contact-contactattributes-c.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise&lt;Array&lt;Contact&gt;&gt; |

## 示例

```TypeScript
import { contact } from '@kit.ContactsKit';

  // 根据holder和attrs查询所有联系人
  let promise = contact.queryContacts({
    holderId: 1,
    bundleName: '',
    displayName: ''
  }, {
    attributes: [contact.Attribute.ATTR_NAME, contact.Attribute.ATTR_PHONE]
  });
  promise.then((data) => {
    console.info(`Succeeded in querying Contacts. data->${JSON.stringify(data)}`);
  });
```


## queryContacts

```TypeScript
function queryContacts(context: Context, holder?: Holder, attrs?: ContactAttributes): Promise<Array<Contact>>
```

根据holder和attrs查询所有联系人。使用Promise异步回调。

**起始版本：** 10

**需要权限：** ohos.permission.READ_CONTACTS

<!--Device-contact-function queryContacts(context: Context, holder?: Holder, attrs?: ContactAttributes): Promise<Array<Contact>>--><!--Device-contact-function queryContacts(context: Context, holder?: Holder, attrs?: ContactAttributes): Promise<Array<Contact>>-End-->

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
| Promise&lt;Array&lt;Contact&gt;&gt; |

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
let promise = contact.queryContacts(context, {
  holderId: 1,
  bundleName: '',
  displayName: ''
}, {
  attributes: [contact.Attribute.ATTR_NAME, contact.Attribute.ATTR_PHONE]
});
promise.then((data) => {
  console.info(`Succeeded in querying Contacts. data: ${JSON.stringify(data)}`);
});
```
