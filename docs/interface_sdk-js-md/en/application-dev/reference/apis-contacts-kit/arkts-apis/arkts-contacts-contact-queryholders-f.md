# queryHolders

## Modules to Import

```TypeScript
import { contact } from 'kits/@kit.ContactsKit';
```

## queryHolders

```TypeScript
function queryHolders(callback: AsyncCallback<Array<Holder>>): void
```

查询所有创建联系人的应用信息类。使用callback异步回调。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 10

**Substitutes:** [contact.queryHolders](arkts-contacts-contact-queryholders-f.md#queryholders)(context:

**Required permissions:** ohos.permission.READ_CONTACTS

<!--Device-contact-function queryHolders(callback: AsyncCallback<Array<Holder>>): void--><!--Device-contact-function queryHolders(callback: AsyncCallback<Array<Holder>>): void-End-->

**System capability:** SystemCapability.Applications.ContactsData

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;Holder&gt;&gt; | Yes | 回调函数。成功返回查询到的创建联系人应用信息的对象数组；失败返回具体的错误码信息。 |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { contact } from '@kit.ContactsKit';

contact.queryHolders((err: BusinessError, data) => {
  if (err) {
    console.error(`Failed to query Holders. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in querying Holders. data->${JSON.stringify(data)}`);
});
```


## queryHolders

```TypeScript
function queryHolders(context: Context, callback: AsyncCallback<Array<Holder>>): void
```

查询所有创建联系人的应用信息类。使用callback异步回调。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Required permissions:** ohos.permission.READ_CONTACTS

<!--Device-contact-function queryHolders(context: Context, callback: AsyncCallback<Array<Holder>>): void--><!--Device-contact-function queryHolders(context: Context, callback: AsyncCallback<Array<Holder>>): void-End-->

**System capability:** SystemCapability.Applications.ContactsData

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [Context](../../apis-arkui/arkts-components/arkts-arkui-context-t.md) | Yes | 应用上下文Context。 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;Holder&gt;&gt; | Yes | 回调函数。成功返回查询到的创建联系人应用信息的对象数组；失败返回具体的错误码信息。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: Mandatory parameters are left unspecified. |
| 201 | Permission denied. |

## Examples

In the examples in this document, this.context is used to obtain the UIAbilityContext, where this represents a UIAbility instance inherited from UIAbility. To use the capabilities provided by UIAbilityContext in a page, see [Obtaining the Context of UIAbility](../../application-models/uiability-usage.md#obtaining-the-context-of-uiability).

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { contact } from '@kit.ContactsKit';
import { common } from '@kit.AbilityKit';

// Obtain the context in the component.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
contact.queryHolders(context, (err: BusinessError, data) => {
  if (err) {
    console.error(`Failed to query Holders. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in querying Holders. data->${JSON.stringify(data)}`);
});
```


## queryHolders

```TypeScript
function queryHolders(): Promise<Array<Holder>>
```

查询所有创建联系人的应用信息类。使用Promise异步回调。

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 10

**Substitutes:** [contact.queryHolders](arkts-contacts-contact-queryholders-f.md#queryholders)(context:

**Required permissions:** ohos.permission.READ_CONTACTS

<!--Device-contact-function queryHolders(): Promise<Array<Holder>>--><!--Device-contact-function queryHolders(): Promise<Array<Holder>>-End-->

**System capability:** SystemCapability.Applications.ContactsData

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;Holder&gt;&gt; | Promise对象。返回查询到的创建联系人应用信息的对象数组。 |

## Examples

```TypeScript
import { contact } from '@kit.ContactsKit';

let promise = contact.queryHolders();
promise.then((data) => {
  console.info(`Succeeded in querying Holders. data->${JSON.stringify(data)}`);
});
```


## queryHolders

```TypeScript
function queryHolders(context: Context): Promise<Array<Holder>>
```

查询所有创建联系人的应用信息类。使用Promise异步回调。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Required permissions:** ohos.permission.READ_CONTACTS

<!--Device-contact-function queryHolders(context: Context): Promise<Array<Holder>>--><!--Device-contact-function queryHolders(context: Context): Promise<Array<Holder>>-End-->

**System capability:** SystemCapability.Applications.ContactsData

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [Context](../../apis-arkui/arkts-components/arkts-arkui-context-t.md) | Yes | 应用上下文Context。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;Holder&gt;&gt; | Promise对象。返回查询到的创建联系人应用信息的对象数组。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 401 | Parameter error. Possible causes: Mandatory parameters are left unspecified. |
| 201 | Permission denied. |

## Examples

In the examples in this document, this.context is used to obtain the UIAbilityContext, where this represents a UIAbility instance inherited from UIAbility. If you need to use the capabilities provided by UIAbilityContext in a page, see [Obtaining the Context of UIAbility](../../application-models/uiability-usage.md#obtaining-the-context-of-uiability).

```TypeScript
import { common } from '@kit.AbilityKit';
import { contact } from '@kit.ContactsKit';

// Obtain the context in the component.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let promise = contact.queryHolders(context);
promise.then((data) => {
  console.info(`Succeeded in querying Holders. data->${JSON.stringify(data)}`);
});
```

