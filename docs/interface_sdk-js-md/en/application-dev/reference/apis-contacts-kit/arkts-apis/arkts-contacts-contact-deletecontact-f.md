# deleteContact

## Modules to Import

```TypeScript
import { contact } from '@kit.ContactsKit';
```

## deleteContact

```TypeScript
function deleteContact(key: string, callback: AsyncCallback<void>): void
```

Deletes a contact. This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 10

**Substitutes:** [deleteContact](#deletecontact)(context: Context, key: string, callback: AsyncCallback&lt;void&gt;)

**Required permissions:** ohos.permission.WRITE_CONTACTS

<!--Device-contact-function deleteContact(key: string, callback: AsyncCallback<void>): void--><!--Device-contact-function deleteContact(key: string, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Applications.ContactsData

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | string | Yes | Unique query key of a contact. One contact corresponds to one key, which can be obtained through [queryKey](arkts-contacts-contact-querykey-f.md). |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Indicates the callback for getting the result of the call. If the operation is successful, the ID of the deleted contact is returned. If the operation fails, an error code is returned. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// Select a contact via selectContacts.
contact.selectContacts().then((data) => {
  // Obtain the context within the component.
  let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
  // Pass the key of the selected contact as the first parameter.
  contact.deleteContact(data[0].key, (err: BusinessError) => {
    if (err) {
      console.error(`Failed to delete Contact. Code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info('Succeeded in deleting Contact.');
  });
}).catch((err: BusinessError) => {
  console.error(`Failed to select Contacts. Code: ${err.code}, message: ${err.message}`);
});
```


## deleteContact

```TypeScript
function deleteContact(context: Context, key: string, callback: AsyncCallback<void>): void
```

Deletes a contact. This API uses an asynchronous callback to return the result.

**Since:** 10

**Required permissions:** ohos.permission.WRITE_CONTACTS

<!--Device-contact-function deleteContact(context: Context, key: string, callback: AsyncCallback<void>): void--><!--Device-contact-function deleteContact(context: Context, key: string, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Applications.ContactsData

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | Context | Yes | Indicates the context of application or capability. |
| key | string | Yes | Unique query key of a contact. One contact corresponds to one key, which can be obtained through [queryKey](arkts-contacts-contact-querykey-f.md). |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Indicates the callback for getting the result of the call. If the operation is successful, the ID of the deleted contact is returned. If the operation fails, an error code is returned. |

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

 // Select a contact via selectContacts.
  contact.selectContacts().then((data) => {
    // Obtain the context within the component.
    let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
    // Pass the key of the selected contact as the second parameter.
    contact.deleteContact(context, data[0].key, (err: BusinessError) => {
      if (err) {
        console.error(`Failed to delete Contact. Code: ${err.code}, message: ${err.message}`);
        return;
      }
      console.info('Succeeded in deleting Contact.');
    });
  }).catch((err: BusinessError) => {
    console.error(`Failed to select Contacts. Code: ${err.code}, message: ${err.message}`);
  });
```


## deleteContact

```TypeScript
function deleteContact(key: string): Promise<void>
```

Deletes a contact. This API uses a promise to return the result.

**Since:** 7

**Deprecated since:** 10

**Substitutes:** [deleteContact](#deletecontact)(context: Context, key: string)

**Required permissions:** ohos.permission.WRITE_CONTACTS

<!--Device-contact-function deleteContact(key: string): Promise<void>--><!--Device-contact-function deleteContact(key: string): Promise<void>-End-->

**System capability:** SystemCapability.Applications.ContactsData

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| key | string | Yes | Unique query key of a contact. One contact corresponds to one key, which can be obtained through [queryKey](arkts-contacts-contact-querykey-f.md). |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// Select a contact via selectContacts.
contact.selectContacts().then((data) => {
  // Pass the key of the selected contact as the first parameter.
  let promise = contact.deleteContact(data[0].key);
  promise.then(() => {
    console.info(`Succeeded in deleting Contact.`);
  }).catch((err: BusinessError) => {
    console.error(`Failed to delete Contact. Code: ${err.code}, message: ${err.message}`);
  });
}).catch((err: BusinessError) => {
  console.error(`Failed to select Contacts. Code: ${err.code}, message: ${err.message}`);
});
```


## deleteContact

```TypeScript
function deleteContact(context: Context, key: string): Promise<void>
```

Deletes a contact. This API uses a promise to return the result.

**Since:** 10

**Required permissions:** ohos.permission.WRITE_CONTACTS

<!--Device-contact-function deleteContact(context: Context, key: string): Promise<void>--><!--Device-contact-function deleteContact(context: Context, key: string): Promise<void>-End-->

**System capability:** SystemCapability.Applications.ContactsData

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | Context | Yes | Indicates the context of application or capability. |
| key | string | Yes | Unique query key of a contact. One contact corresponds to one key, which can be obtained through [queryKey](arkts-contacts-contact-querykey-f.md). |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

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

// Select a contact via selectContacts.
contact.selectContacts().then((data) => {
  // Obtain the context within the component.
  let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
  // Pass the key of the selected contact as the second parameter.
  let promise = contact.deleteContact(context, data[0].key);
  promise.then(() => {
    console.info(`Succeeded in deleting Contact.`);
  }).catch((err: BusinessError) => {
    console.error(`Failed to delete Contact. Code: ${err.code}, message: ${err.message}`);
  });
}).catch((err: BusinessError) => {
  console.error(`Failed to select Contacts. Code: ${err.code}, message: ${err.message}`);
});
```

