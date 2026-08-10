# queryContact

## Modules to Import

```TypeScript
import { contact } from 'kits/@kit.ContactsKit';
```

## queryContact

```TypeScript
function queryContact(key: string, callback: AsyncCallback<Contact>): void
```

根据联系人唯一标识符key查询联系人。使用callback异步回调。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 10

**Substitutes:** [contact.queryContact](arkts-contacts-contact-querycontact-f.md#querycontact)(context:

**Required permissions:** ohos.permission.READ_CONTACTS

<!--Device-contact-function queryContact(key: string, callback: AsyncCallback<Contact>): void--><!--Device-contact-function queryContact(key: string, callback: AsyncCallback<Contact>): void-End-->

**System capability:** SystemCapability.Applications.ContactsData

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | string | Yes | 联系人的唯一查询键key，是新建联系人时系统自动生成的唯一标识，一个联系人对应一个key,可以通过[queryKey](contact.queryKey(context: Context, id: number, callback: AsyncCallback&lt;string&gt;): void)获取。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Contact&gt; | Yes | 回调函数。成功返回查询的联系人对象；失败返回具体的错误码信息。 |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { contact } from '@kit.ContactsKit';

// Query the contact with key='xxx'.
contact.queryContact('xxx', (err: BusinessError, data) => {
  if (err) {
    console.error(`Failed to query Contact. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in querying Contact. data->${JSON.stringify(data)}`);
});
```


## queryContact

```TypeScript
function queryContact(context: Context, key: string, callback: AsyncCallback<Contact>): void
```

根据key查询联系人。使用callback异步回调。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Required permissions:** ohos.permission.READ_CONTACTS

<!--Device-contact-function queryContact(context: Context, key: string, callback: AsyncCallback<Contact>): void--><!--Device-contact-function queryContact(context: Context, key: string, callback: AsyncCallback<Contact>): void-End-->

**System capability:** SystemCapability.Applications.ContactsData

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [Context](../../apis-arkui/arkts-components/arkts-arkui-context-t.md) | Yes | 应用上下文Context。 |
| key | string | Yes | 联系人的唯一查询键key，是新建联系人时系统自动生成的唯一标识，一个联系人对应一个key,可以通过[queryKey](contact.queryKey(context: Context, id: number, callback: AsyncCallback&lt;string&gt;): void)获取。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Contact&gt; | Yes | 回调函数。成功返回查询的联系人对象；失败返回具体的错误码信息。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: Mandatory parameters are left unspecified. |
| 201 | Permission denied. |

## Examples

In the examples in this document, this.context is used to obtain the UIAbilityContext, where this represents a UIAbility instance inherited from UIAbility. To use the capabilities provided by UIAbilityContext in the UI, see [Obtaining the Context of UIAbility](../../application-models/uiability-usage.md#obtaining-the-context-of-uiability).

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { contact } from '@kit.ContactsKit';
import { common } from '@kit.AbilityKit';

// Obtain the context in the component.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
contact.queryContact(context, 'xxx', (err: BusinessError, data) => {
  if (err) {
    console.error(`Failed to query Contact. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in querying Contact. data->${JSON.stringify(data)}`);
});
```


## queryContact

```TypeScript
function queryContact(key: string, holder: Holder, callback: AsyncCallback<Contact>): void
```

根据key和holder查询联系人。使用callback异步回调。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 10

**Substitutes:** [contact.queryContact](arkts-contacts-contact-querycontact-f.md#querycontact)(context:

**Required permissions:** ohos.permission.READ_CONTACTS

<!--Device-contact-function queryContact(key: string, holder: Holder, callback: AsyncCallback<Contact>): void--><!--Device-contact-function queryContact(key: string, holder: Holder, callback: AsyncCallback<Contact>): void-End-->

**System capability:** SystemCapability.Applications.ContactsData

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | string | Yes | 联系人的唯一查询键key，是新建联系人时系统自动生成的唯一标识，一个联系人对应一个key,可以通过[queryKey](contact.queryKey(context: Context, id: number, callback: AsyncCallback&lt;string&gt;): void)获取。 |
| holder | [Holder](arkts-contacts-contact-holder-c.md) | Yes | 创建联系人的应用信息类，如果传入参数为空则默认使用系统联系人应用查询。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Contact&gt; | Yes | 回调函数。成功返回查询的联系人对象；失败返回具体的错误码信息。 |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { contact } from '@kit.ContactsKit';

// Query the contact with key='xxx' and holderId=1.
contact.queryContact('xxx', {
  holderId: 1,
  bundleName: '',
  displayName: ''
}, (err: BusinessError, data) => {
  if (err) {
    console.error(`Failed to query Contact. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in querying Contact. data->${JSON.stringify(data)}`);
});
```


## queryContact

```TypeScript
function queryContact(context: Context, key: string, holder: Holder, callback: AsyncCallback<Contact>): void
```

根据key和holder查询联系人。使用callback异步回调。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Required permissions:** ohos.permission.READ_CONTACTS

<!--Device-contact-function queryContact(context: Context, key: string, holder: Holder, callback: AsyncCallback<Contact>): void--><!--Device-contact-function queryContact(context: Context, key: string, holder: Holder, callback: AsyncCallback<Contact>): void-End-->

**System capability:** SystemCapability.Applications.ContactsData

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [Context](../../apis-arkui/arkts-components/arkts-arkui-context-t.md) | Yes | 应用上下文Context。 |
| key | string | Yes | 联系人的唯一查询键key，是新建联系人时系统自动生成的唯一标识，一个联系人对应一个key,可以通过[queryKey](contact.queryKey(context: Context, id: number, callback: AsyncCallback&lt;string&gt;): void)获取。 |
| holder | [Holder](arkts-contacts-contact-holder-c.md) | Yes | 创建联系人的应用信息类，如果传入参数为空则默认使用系统联系人应用查询。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Contact&gt; | Yes | 回调函数。成功返回查询的联系人对象；失败返回具体的错误码信息。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: Mandatory parameters are left unspecified. |
| 201 | Permission denied. |

## Examples

In the examples in this document, this.context is used to obtain the UIAbilityContext, where this represents a UIAbility instance inherited from UIAbility. If you need to use the capabilities provided by UIAbilityContext in a page, see [Obtaining the Context of UIAbility](../../application-models/uiability-usage.md#obtaining-the-context-of-uiability).

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { contact } from '@kit.ContactsKit';
import { common } from '@kit.AbilityKit';

// Obtain the context in the component.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
contact.queryContact(context, 'xxx', {
  holderId: 1,
  bundleName: '',
  displayName: ''
}, (err: BusinessError, data) => {
  if (err) {
    console.error(`Failed to query Contact. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in querying Contact. data->${JSON.stringify(data)}`);
});
```


## queryContact

```TypeScript
function queryContact(key: string, attrs: ContactAttributes, callback: AsyncCallback<Contact>): void
```

根据key和指定属性(attrs)查询联系人。使用callback异步回调。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 10

**Substitutes:** [contact.queryContact](arkts-contacts-contact-querycontact-f.md#querycontact)(context:

**Required permissions:** ohos.permission.READ_CONTACTS

<!--Device-contact-function queryContact(key: string, attrs: ContactAttributes, callback: AsyncCallback<Contact>): void--><!--Device-contact-function queryContact(key: string, attrs: ContactAttributes, callback: AsyncCallback<Contact>): void-End-->

**System capability:** SystemCapability.Applications.ContactsData

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | string | Yes | 联系人的唯一查询键key，是新建联系人时系统自动生成的唯一标识，一个联系人对应一个key,可以通过[queryKey](contact.queryKey(context: Context, id: number, callback: AsyncCallback&lt;string&gt;): void)获取。 |
| attrs | [ContactAttributes](arkts-contacts-contact-contactattributes-c.md) | Yes | 联系人的属性列表，如果为空，则查询联系人的所有属性字段（包括姓名、电话、邮箱等）。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Contact&gt; | Yes | 回调函数。成功返回查询的联系人对象；失败返回具体的错误码信息。 |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { contact } from '@kit.ContactsKit';

// Pass in key='xxx' and the contact attribute list for querying.
contact.queryContact('xxx', {
  attributes: [contact.Attribute.ATTR_NAME, contact.Attribute.ATTR_PHONE]
}, (err: BusinessError, data) => {
  if (err) {
    console.error(`Failed to query Contact. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in querying Contact. data->${JSON.stringify(data)}`);
});
```


## queryContact

```TypeScript
function queryContact(context: Context, key: string, attrs: ContactAttributes, callback: AsyncCallback<Contact>): void
```

根据key和attrs查询联系人。使用callback异步回调。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Required permissions:** ohos.permission.READ_CONTACTS

<!--Device-contact-function queryContact(context: Context, key: string, attrs: ContactAttributes, callback: AsyncCallback<Contact>): void--><!--Device-contact-function queryContact(context: Context, key: string, attrs: ContactAttributes, callback: AsyncCallback<Contact>): void-End-->

**System capability:** SystemCapability.Applications.ContactsData

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [Context](../../apis-arkui/arkts-components/arkts-arkui-context-t.md) | Yes | 应用上下文Context。 |
| key | string | Yes | 联系人的唯一查询键key，是新建联系人时系统自动生成的唯一标识，一个联系人对应一个key,可以通过[queryKey](contact.queryKey(context: Context, id: number, callback: AsyncCallback&lt;string&gt;): void)获取。 |
| attrs | [ContactAttributes](arkts-contacts-contact-contactattributes-c.md) | Yes | 联系人的属性列表，如果为空，则查询联系人的所有属性字段（包括姓名、电话、邮箱等）。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Contact&gt; | Yes | 回调函数。成功返回查询的联系人对象；失败返回具体的错误码信息。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: Mandatory parameters are left unspecified. |
| 201 | Permission denied. |

## Examples

In the examples in this document, this.context is used to obtain the UIAbilityContext, where this represents a UIAbility instance inherited from UIAbility. If you need to use the capabilities provided by UIAbilityContext in the UI, see [Obtaining the Context of UIAbility](../../application-models/uiability-usage.md#obtaining-the-context-of-uiability).

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { contact } from '@kit.ContactsKit';
import { common } from '@kit.AbilityKit';

// Obtain the context in the component.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
contact.queryContact(context, 'xxx', {
  attributes: [contact.Attribute.ATTR_NAME, contact.Attribute.ATTR_PHONE]
}, (err: BusinessError, data) => {
  if (err) {
    console.error(`Failed to query Contact. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in querying Contact. data->${JSON.stringify(data)}`);
});
```


## queryContact

```TypeScript
function queryContact(key: string, holder: Holder, attrs: ContactAttributes, callback: AsyncCallback<Contact>): void
```

根据key、holder和attrs查询联系人。使用callback异步回调。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 10

**Substitutes:** [contact.queryContact](arkts-contacts-contact-querycontact-f.md#querycontact)(context:

**Required permissions:** ohos.permission.READ_CONTACTS

<!--Device-contact-function queryContact(key: string, holder: Holder, attrs: ContactAttributes, callback: AsyncCallback<Contact>): void--><!--Device-contact-function queryContact(key: string, holder: Holder, attrs: ContactAttributes, callback: AsyncCallback<Contact>): void-End-->

**System capability:** SystemCapability.Applications.ContactsData

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | string | Yes | 联系人的唯一查询键key，是新建联系人时系统自动生成的唯一标识，一个联系人对应一个key,可以通过[queryKey](contact.queryKey(context: Context, id: number, callback: AsyncCallback&lt;string&gt;): void)获取。 |
| holder | [Holder](arkts-contacts-contact-holder-c.md) | Yes | 创建联系人的应用信息类，为空则默认使用系统联系人应用查询。 |
| attrs | [ContactAttributes](arkts-contacts-contact-contactattributes-c.md) | Yes | 联系人的属性列表，当该参数为空时，则查询联系人的所有属性字段（包括姓名、电话、邮箱等）。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Contact&gt; | Yes | 回调函数。成功返回查询的联系人对象；失败返回具体的错误码信息。 |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { contact } from '@kit.ContactsKit';

// Query contacts that meet the conditions specified by key, holder, and attrs.
contact.queryContact('xxx', {
  holderId: 1,
  bundleName: '',
  displayName: ''
}, {
  attributes: [contact.Attribute.ATTR_NAME, contact.Attribute.ATTR_PHONE]
}, (err: BusinessError, data) => {
  if (err) {
    console.error(`Failed to query Contact. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in querying Contact. data->${JSON.stringify(data)}`);
});
```


## queryContact

```TypeScript
function queryContact(context: Context, key: string, holder: Holder, attrs: ContactAttributes, callback: AsyncCallback<Contact>): void
```

根据key、holder和attrs查询联系人。使用callback异步回调。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Required permissions:** ohos.permission.READ_CONTACTS

<!--Device-contact-function queryContact(context: Context, key: string, holder: Holder, attrs: ContactAttributes, callback: AsyncCallback<Contact>): void--><!--Device-contact-function queryContact(context: Context, key: string, holder: Holder, attrs: ContactAttributes, callback: AsyncCallback<Contact>): void-End-->

**System capability:** SystemCapability.Applications.ContactsData

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [Context](../../apis-arkui/arkts-components/arkts-arkui-context-t.md) | Yes | 应用上下文Context。 |
| key | string | Yes | 联系人的唯一查询键key，是新建联系人时系统自动生成的唯一标识，一个联系人对应一个key,可以通过[queryKey](contact.queryKey(context: Context, id: number, callback: AsyncCallback&lt;string&gt;): void)获取。 |
| holder | [Holder](arkts-contacts-contact-holder-c.md) | Yes | 创建联系人的应用信息类，如果传入参数为空则默认使用系统联系人应用查询。 |
| attrs | [ContactAttributes](arkts-contacts-contact-contactattributes-c.md) | Yes | 联系人的属性列表，如果为空，则查询联系人的所有属性字段（包括姓名、电话、邮箱等）。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Contact&gt; | Yes | 回调函数。成功返回查询的联系人对象；失败返回具体的错误码信息。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: Mandatory parameters are left unspecified. |
| 201 | Permission denied. |

## Examples

In the examples in this document, UIAbilityContext is obtained through this.context, where this represents a UIAbility instance inherited from UIAbility. If you need to use the capabilities provided by UIAbilityContext in the UI, see [Obtaining the Context of UIAbility](../../application-models/uiability-usage.md#obtaining-the-context-of-uiability).

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
  import { contact } from '@kit.ContactsKit';
  import { common } from '@kit.AbilityKit';

  // Obtain the context in the component.
  let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
  contact.queryContact(context, 'xxx', {
    holderId: 1,
    bundleName: '',
    displayName: ''
  }, {
    attributes: [contact.Attribute.ATTR_NAME, contact.Attribute.ATTR_PHONE]
  }, (err: BusinessError, data) => {
    if (err) {
      console.error(`Failed to query Contact. Code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info(`Succeeded in querying Contact. data->${JSON.stringify(data)}`);
  });
```


## queryContact

```TypeScript
function queryContact(key: string, holder?: Holder, attrs?: ContactAttributes): Promise<Contact>
```

根据key、holder和attrs查询联系人。使用Promise异步回调。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 10

**Substitutes:** [contact.queryContact](arkts-contacts-contact-querycontact-f.md#querycontact)(context:

**Required permissions:** ohos.permission.READ_CONTACTS

<!--Device-contact-function queryContact(key: string, holder?: Holder, attrs?: ContactAttributes): Promise<Contact>--><!--Device-contact-function queryContact(key: string, holder?: Holder, attrs?: ContactAttributes): Promise<Contact>-End-->

**System capability:** SystemCapability.Applications.ContactsData

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | string | Yes | 联系人的唯一查询键key，是新建联系人时自动生成的唯一标识，一个联系人对应一个key,可以通过[queryKey](contact.queryKey(context: Context, id: number, callback: AsyncCallback&lt;string&gt;): void)获取。 |
| holder | [Holder](arkts-contacts-contact-holder-c.md) | No | 创建联系人的应用信息类，不传该参数则默认使用系统联系人应用查询。 |
| attrs | [ContactAttributes](arkts-contacts-contact-contactattributes-c.md) | No | 联系人的属性列表，不传默认查询所有联系人属性。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Contact&gt; | Promise对象。返回查询到的联系人对象。 |

## Examples

```TypeScript
import { contact } from '@kit.ContactsKit';

// Query the contact using an asynchronous callback.
let promise = contact.queryContact('xxx', {
  holderId: 1,
  bundleName: '',
  displayName: ''
}, {
  attributes: [contact.Attribute.ATTR_NAME, contact.Attribute.ATTR_PHONE]
});
promise.then((data) => {
  console.info(`Succeeded in querying Contact. data->${JSON.stringify(data)}`);
});
```


## queryContact

```TypeScript
function queryContact(context: Context, key: string, holder?: Holder, attrs?: ContactAttributes): Promise<Contact>
```

根据key、holder和attrs查询联系人。使用Promise异步回调。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Required permissions:** ohos.permission.READ_CONTACTS

<!--Device-contact-function queryContact(context: Context, key: string, holder?: Holder, attrs?: ContactAttributes): Promise<Contact>--><!--Device-contact-function queryContact(context: Context, key: string, holder?: Holder, attrs?: ContactAttributes): Promise<Contact>-End-->

**System capability:** SystemCapability.Applications.ContactsData

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [Context](../../apis-arkui/arkts-components/arkts-arkui-context-t.md) | Yes | 应用上下文Context。 |
| key | string | Yes | 联系人的唯一查询键key，是新建联系人时系统自动生成的唯一标识，一个联系人对应一个key,可以通过[queryKey](contact.queryKey(context: Context, id: number, callback: AsyncCallback&lt;string&gt;): void)获取。 |
| holder | [Holder](arkts-contacts-contact-holder-c.md) | No | 创建联系人的应用信息类，不传该参数，则默认使用系统联系人应用查询。 |
| attrs | [ContactAttributes](arkts-contacts-contact-contactattributes-c.md) | No | 联系人的属性列表，不传该参数，则默认查询所有联系人属性。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Contact&gt; | Promise对象。返回查询到的联系人对象。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: Mandatory parameters are left unspecified. |
| 201 | Permission denied. |

## Examples

In the examples in this document, this.context is used to obtain the UIAbilityContext, where this represents a UIAbility instance inherited from UIAbility. If you need to use the capabilities provided by UIAbilityContext in a page, see [Obtaining the Context of UIAbility](../../application-models/uiability-usage.md#obtaining-the-context-of-uiability).

```TypeScript
import { contact } from '@kit.ContactsKit';
import { common } from '@kit.AbilityKit';

// Obtain the context in the component.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let promise = contact.queryContact(context, 'xxx', {
  holderId: 1,
  bundleName: '',
  displayName: ''
}, {
  attributes: [contact.Attribute.ATTR_NAME, contact.Attribute.ATTR_PHONE]
});
promise.then((data) => {
  console.info(`Succeeded in querying Contact. data->${JSON.stringify(data)}`);
});
```

