# isMyCard

## Modules to Import

```TypeScript
import { contact } from '@kit.ContactsKit';
```

## isMyCard

```TypeScript
function isMyCard(id: number, callback: AsyncCallback<boolean>): void
```

Checks whether a contact is included in my card. This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 10

**Substitutes:** [isMyCard](#ismycard)(context: Context, id: number, callback: AsyncCallback&lt;boolean&gt;)

**Required permissions:** ohos.permission.READ_CONTACTS

<!--Device-contact-function isMyCard(id: number, callback: AsyncCallback<boolean>): void--><!--Device-contact-function isMyCard(id: number, callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.Applications.ContactsData

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| id | number | Yes | Contact ID. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;boolean&gt; | Yes | Indicates the callback for getting the result of the call. If the operation is successful, a Boolean value is returned. The value **true** indicates that the contact is included in my card, and the value **false** indicates the opposite. If the operation fails, an error code is returned. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

contact.isMyCard(1, (err: BusinessError, data) => {
  if (err) {
    console.error(`Failed to isMyCard. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in isMyCard. data->${JSON.stringify(data)}`);
});
```


## isMyCard

```TypeScript
function isMyCard(context: Context, id: number, callback: AsyncCallback<boolean>): void
```

Checks whether a contact is included in my card. This API uses an asynchronous callback to return the result.

**Since:** 10

**Required permissions:** ohos.permission.READ_CONTACTS

<!--Device-contact-function isMyCard(context: Context, id: number, callback: AsyncCallback<boolean>): void--><!--Device-contact-function isMyCard(context: Context, id: number, callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.Applications.ContactsData

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | Context | Yes | Indicates the context of application or capability. |
| id | number | Yes | Contact ID. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-asynccallback-t.md)&lt;boolean&gt; | Yes | Indicates the callback for getting the result of the call. If the operation is successful, a Boolean value is returned. The value **true** indicates that the contact is included in my card, and the value **false** indicates the opposite. If the operation fails, an error code is returned. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../errorcode-contacts.md#401-failed-to-open-the-contact-portrait-file) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |

**Examples**

In the sample code provided in this topic, this.context is used to obtain UIAbilityContext, where this indicates a UIAbility instance inherited from UIAbility. To use UIAbilityContext APIs on pages, see [Obtaining the Context of UIAbility](../../../application-models/uiability-usage.md#obtaining-the-context-of-uiability).

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
  import { common } from '@kit.AbilityKit';

  // Obtain the context within the component.
  let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
  contact.isMyCard(context, 1, (err: BusinessError, data) => {
    if (err) {
      console.error(`Failed to isMyCard. Code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info(`Succeeded in isMyCard. data->${JSON.stringify(data)}`);
  });
```


## isMyCard

```TypeScript
function isMyCard(id: number): Promise<boolean>
```

Checks whether a contact is included in my card. This API uses a promise to return the result.

**Since:** 7

**Deprecated since:** 10

**Substitutes:** [isMyCard](#ismycard)(context: Context, id: number)

**Required permissions:** ohos.permission.READ_CONTACTS

<!--Device-contact-function isMyCard(id: number): Promise<boolean>--><!--Device-contact-function isMyCard(id: number): Promise<boolean>-End-->

**System capability:** SystemCapability.Applications.ContactsData

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| id | number | Yes | Contact ID. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | Promise used to return the result. The value **true** indicates that the contact is included in my card, and the value **false** indicates the opposite. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let promise = contact.isMyCard(1);
promise.then((data) => {
  console.info(`Succeeded in isMyCard. data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to isMyCard. Code: ${err.code}, message: ${err.message}`);
});
```


## isMyCard

```TypeScript
function isMyCard(context: Context, id: number): Promise<boolean>
```

Checks whether a contact is included in my card. This API uses a promise to return the result.

**Since:** 10

**Required permissions:** ohos.permission.READ_CONTACTS

<!--Device-contact-function isMyCard(context: Context, id: number): Promise<boolean>--><!--Device-contact-function isMyCard(context: Context, id: number): Promise<boolean>-End-->

**System capability:** SystemCapability.Applications.ContactsData

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | Context | Yes | Indicates the context of application or capability. |
| id | number | Yes | Contact ID. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;boolean&gt; | Promise used to return the result. The value **true** indicates that the contact is included in my card, and the value **false** indicates the opposite. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../errorcode-contacts.md#401-failed-to-open-the-contact-portrait-file) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |

**Examples**

In the sample code provided in this topic, this.context is used to obtain UIAbilityContext, where this indicates a UIAbility instance inherited from UIAbility. To use UIAbilityContext APIs on pages, see [Obtaining the Context of UIAbility](../../../application-models/uiability-usage.md#obtaining-the-context-of-uiability).

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
  import { common } from '@kit.AbilityKit';

  // Obtain the context within the component.
  let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
  let promise = contact.isMyCard(context, 1);
  promise.then((data) => {
    console.info(`Succeeded in isMyCard. data->${JSON.stringify(data)}`);
  }).catch((err: BusinessError) => {
    console.error(`Failed to isMyCard. Code: ${err.code}, message: ${err.message}`);
  });
```

