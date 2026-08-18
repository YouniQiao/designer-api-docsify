# queryHolders

## Modules to Import

```TypeScript
import { contact } from '@kit.ContactsKit';
```

## queryHolders

```TypeScript
function queryHolders(callback: AsyncCallback<Array<Holder>>): void
```

Queries all applications that have created contacts. This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 10

**Substitutes:** [queryHolders](#queryholders)(context: Context, callback: AsyncCallback&lt;Array&lt;Holder&gt;&gt;)

**Required permissions:** ohos.permission.READ_CONTACTS

<!--Device-contact-function queryHolders(callback: AsyncCallback<Array<Holder>>): void--><!--Device-contact-function queryHolders(callback: AsyncCallback<Array<Holder>>): void-End-->

**System capability:** SystemCapability.Applications.ContactsData

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;Array&lt;[Holder](arkts-contacts-contact-holder-c.md)&gt;&gt; | Yes | Indicates the callback for getting the result of the call. If the operation is successful, an array of the queried applications is returned. If the operation fails, an error code is returned. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

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

Queries all applications that have created contacts. This API uses an asynchronous callback to return the result.

**Since:** 10

**Required permissions:** ohos.permission.READ_CONTACTS

<!--Device-contact-function queryHolders(context: Context, callback: AsyncCallback<Array<Holder>>): void--><!--Device-contact-function queryHolders(context: Context, callback: AsyncCallback<Array<Holder>>): void-End-->

**System capability:** SystemCapability.Applications.ContactsData

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | Context | Yes | Indicates the context of application or capability. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;Array&lt;[Holder](arkts-contacts-contact-holder-c.md)&gt;&gt; | Yes | Indicates the callback for getting the result of the call. If the operation is successful, an array of the queried applications is returned. If the operation fails, an error code is returned. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../errorcode-contacts.md#401-failed-to-open-the-contact-portrait-file) | Parameter error. Possible causes: Mandatory parameters are left unspecified. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |

**Examples**

In the sample code provided in this topic, this.context is used to obtain UIAbilityContext, where this indicates a UIAbility instance inherited from UIAbility. To use UIAbilityContext APIs on pages, see [Obtaining the Context of UIAbility](../../../application-models/uiability-usage.md#obtaining-the-context-of-uiability).

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context within the component.
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

Queries all applications that have created contacts. This API uses a promise to return the result.

**Since:** 7

**Deprecated since:** 10

**Substitutes:** [queryHolders](#queryholders)(context: Context)

**Required permissions:** ohos.permission.READ_CONTACTS

<!--Device-contact-function queryHolders(): Promise<Array<Holder>>--><!--Device-contact-function queryHolders(): Promise<Array<Holder>>-End-->

**System capability:** SystemCapability.Applications.ContactsData

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;[Holder](arkts-contacts-contact-holder-c.md)&gt;&gt; | Promise used to return the result, which is an array of queried applications. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let promise = contact.queryHolders();
promise.then((data) => {
  console.info(`Succeeded in querying Holders. data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to query Holders. Code: ${err.code}, message: ${err.message}`);
});
```


## queryHolders

```TypeScript
function queryHolders(context: Context): Promise<Array<Holder>>
```

Queries all applications that have created contacts. This API uses a promise to return the result.

**Since:** 10

**Required permissions:** ohos.permission.READ_CONTACTS

<!--Device-contact-function queryHolders(context: Context): Promise<Array<Holder>>--><!--Device-contact-function queryHolders(context: Context): Promise<Array<Holder>>-End-->

**System capability:** SystemCapability.Applications.ContactsData

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | Context | Yes | Indicates the context of application or capability. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;[Holder](arkts-contacts-contact-holder-c.md)&gt;&gt; | Promise used to return the result, which is an array of queried applications. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../errorcode-contacts.md#401-failed-to-open-the-contact-portrait-file) | Parameter error. Possible causes: Mandatory parameters are left unspecified. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |

**Examples**

In the sample code provided in this topic, this.context is used to obtain UIAbilityContext, where this indicates a UIAbility instance inherited from UIAbility. To use UIAbilityContext APIs on pages, see [Obtaining the Context of UIAbility](../../../application-models/uiability-usage.md#obtaining-the-context-of-uiability).

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context within the component.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let promise = contact.queryHolders(context);
promise.then((data) => {
  console.info(`Succeeded in querying Holders. data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to query Holders. Code: ${err.code}, message: ${err.message}`);
});
```

