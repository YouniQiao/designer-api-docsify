# selectContact

## Modules to Import

```TypeScript
```

## selectContact

```TypeScript
function selectContact(callback: AsyncCallback<Array<Contact>>): void
```

Selects a contact. This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 10

**Substitutes:** [selectContacts](arkts-contacts-contact-selectcontacts-f.md#selectcontacts)(callback: AsyncCallback&lt;Array&lt;Contact&gt;&gt;)

<!--Device-contact-function selectContact(callback: AsyncCallback<Array<Contact>>): void--><!--Device-contact-function selectContact(callback: AsyncCallback<Array<Contact>>): void-End-->

**System capability:** SystemCapability.Applications.Contacts

**Parameters:**

| [Name](arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[Contact](arkts-contacts-contact-contact-c.md)&gt;&gt; | Yes |

**Examples**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { contact } from '@kit.ContactsKit';

// Open the contact selection UI.
contact.selectContact((err: BusinessError, data) => {
  if (err) {
    console.error(`Failed to select Contact. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in selecting Contact. data->${JSON.stringify(data)}`);
});
```


## selectContact

```TypeScript
function selectContact(): Promise<Array<Contact>>
```

Selects a contact. This API uses a promise to return the result.

**Since:** 7

**Deprecated since:** 10

**Substitutes:** [selectContacts](arkts-contacts-contact-selectcontacts-f.md#selectcontacts)()

<!--Device-contact-function selectContact(): Promise<Array<Contact>>--><!--Device-contact-function selectContact(): Promise<Array<Contact>>-End-->

**System capability:** SystemCapability.Applications.Contacts

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[Contact](arkts-contacts-contact-contact-c.md)&gt;&gt; |

**Examples**

```TypeScript
import { contact } from '@kit.ContactsKit';

// Open the contact selection UI.
let promise = contact.selectContact();
promise.then((data) => {
  console.info(`Succeeded in selecting Contact. data->${JSON.stringify(data)}`);
});
```
