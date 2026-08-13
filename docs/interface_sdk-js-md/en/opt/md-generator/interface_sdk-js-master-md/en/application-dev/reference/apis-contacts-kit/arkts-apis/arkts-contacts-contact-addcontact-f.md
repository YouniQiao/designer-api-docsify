# addContact

## Modules to Import

```TypeScript
import { contact } from '@kit.ContactsKit';
```

## addContact

```TypeScript
function addContact(contact: Contact, callback: AsyncCallback<number>): void
```

Adds a contact. This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 10

**Substitutes:** [addContact](#addContact)(context: Context, contact: Contact, callback: AsyncCallback&lt;number&gt;)

**Required permissions:** ohos.permission.WRITE_CONTACTS

<!--Device-contact-function addContact(contact: Contact, callback: AsyncCallback<number>): void--><!--Device-contact-function addContact(contact: Contact, callback: AsyncCallback<number>): void-End-->

**System capability:** SystemCapability.Applications.ContactsData

**Parameters:**

| [Name](arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [contact](arkts-contact.md) | [Contact](arkts-contacts-contact-contact-c.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';
import { contact } from '@kit.ContactsKit';

// Obtain the context in the component.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
contact.addContact(context, {
  name: {
    fullName: 'xxx'
  },
  phoneNumbers: [{
    phoneNumber: '138xxxxxxxx'
  }]
}, (err: BusinessError, data) => {
  if (err) {
    console.error(`Failed to add Contact. Code:${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in adding Contact. data: ${JSON.stringify(data)}`);
});
```


## addContact

```TypeScript
function addContact(context: Context, contact: Contact, callback: AsyncCallback<number>): void
```

Adds a contact. This API uses an asynchronous callback to return the result.

**Since:** 10

**Deprecated since:** -1

**Required permissions:** ohos.permission.WRITE_CONTACTS

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-contact-function addContact(context: Context, contact: Contact, callback: AsyncCallback<number>): void--><!--Device-contact-function addContact(context: Context, contact: Contact, callback: AsyncCallback<number>): void-End-->

**System capability:** SystemCapability.Applications.ContactsData

**Parameters:**

| [Name](arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [Context](../../apis-mind-spore-lite-kit/arkts-apis/arkts-mindsporelite-mindsporelite-context-i.md) | Yes |
| [contact](arkts-contact.md) | [Contact](arkts-contacts-contact-contact-c.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../errorcode-contacts.md#401-failed-to-open-the-contact-portrait-file) |
| [201](../../errorcode-universal.md#201-permission-denied) |

## Examples

In the examples in this document, this.context is used to obtain the UIAbilityContext, where this represents the UIAbility instance that inherits from UIAbility. To use the capabilities provided by UIAbilityContext in the UI, see [Obtaining the Context of UIAbility](../../../application-models/uiability-usage.md#obtaining-the-context-of-uiability).

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
  import { common } from '@kit.AbilityKit';
  import { contact } from '@kit.ContactsKit';

  // Obtain the context within the component.
  let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
  contact.addContact(context, {
    name: {
      fullName: 'xxx'
    },
    phoneNumbers: [{
      phoneNumber: '138xxxxxxxx'
    }]
  }, (err: BusinessError, data) => {
    if (err) {
      console.error(`Failed to add Contact. Code:${err.code}, message: ${err.message}`);
      return;
    }
    console.info(`Succeeded in adding Contact. data: ${JSON.stringify(data)}`);
  });
```


## addContact

```TypeScript
function addContact(contact: Contact): Promise<number>
```

Adds a contact. This API uses a promise to return the result.

**Since:** 7

**Deprecated since:** 10

**Substitutes:** [addContact](#addContact)(context: Context, contact: Contact)

**Required permissions:** ohos.permission.WRITE_CONTACTS

<!--Device-contact-function addContact(contact: Contact): Promise<number>--><!--Device-contact-function addContact(contact: Contact): Promise<number>-End-->

**System capability:** SystemCapability.Applications.ContactsData

**Parameters:**

| [Name](arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [contact](arkts-contact.md) | [Contact](arkts-contacts-contact-contact-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

## Examples

```TypeScript
import { contact } from '@kit.ContactsKit';

// Returns the data after the contact is added successfully.
let promise = contact.addContact({
  name: {
    fullName: 'xxx'
  },
  phoneNumbers: [{
    phoneNumber: '138xxxxxxxx'
  }]
});
// Callback invoked when the promise is resolved.
promise.then((data) => {
  console.info(`Succeeded in adding Contact. data: ${JSON.stringify(data)}`);
});
```


## addContact

```TypeScript
function addContact(context: Context, contact: Contact): Promise<number>
```

Adds a contact. This API uses a promise to return the result.

**Since:** 10

**Deprecated since:** -1

**Required permissions:** ohos.permission.WRITE_CONTACTS

**Atomic service API:** This API can be used in atomic services since API version 12.

<!--Device-contact-function addContact(context: Context, contact: Contact): Promise<number>--><!--Device-contact-function addContact(context: Context, contact: Contact): Promise<number>-End-->

**System capability:** SystemCapability.Applications.ContactsData

**Parameters:**

| [Name](arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [Context](../../apis-mind-spore-lite-kit/arkts-apis/arkts-mindsporelite-mindsporelite-context-i.md) | Yes |
| [contact](arkts-contact.md) | [Contact](arkts-contacts-contact-contact-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../errorcode-contacts.md#401-failed-to-open-the-contact-portrait-file) |
| [201](../../errorcode-universal.md#201-permission-denied) |

## Examples

In the examples in this document, this.context is used to obtain the UIAbilityContext, where this represents a UIAbility instance inherited from UIAbility. If you need to use the capabilities provided by UIAbilityContext in a UI page, see [Obtaining the Context of UIAbility](../../../application-models/uiability-usage.md#obtaining-the-context-of-uiability).

```TypeScript
import { contact } from '@kit.ContactsKit';
  import { common } from '@kit.AbilityKit';

  // Obtain the context within the component.
  let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
  let promise = contact.addContact(context, {
    name: {
      fullName: 'xxx'
    },
    phoneNumbers: [{
      phoneNumber: '138xxxxxxxx'
    }]
  });
  promise.then((data) => {
    console.info(`Succeeded in adding Contact. data: ${JSON.stringify(data)}`);
  });
```
