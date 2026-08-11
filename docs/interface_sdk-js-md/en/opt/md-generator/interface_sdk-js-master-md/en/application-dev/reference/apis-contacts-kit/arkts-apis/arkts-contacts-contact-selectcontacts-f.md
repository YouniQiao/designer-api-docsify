# selectContacts

## Modules to Import

```TypeScript
import { contact } from 'kits/@kit.ContactsKit';
```

## selectContacts

```TypeScript
function selectContacts(callback: AsyncCallback<Array<Contact>>): void
```

Selects a contact. This API uses an asynchronous callback to return the result.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-contact-function selectContacts(callback: AsyncCallback<Array<Contact>>): void--><!--Device-contact-function selectContacts(callback: AsyncCallback<Array<Contact>>): void-End-->

**System capability:** SystemCapability.Applications.Contacts

**Parameters:**

| [Name](arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;Contact&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { contact } from '@kit.ContactsKit';

// Open the contact selection UI.
contact.selectContacts((err: BusinessError, data) => {
  if (err) {
    console.error(`Failed to select Contacts. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in selecting Contacts. data->${JSON.stringify(data)}`);
});
```


## selectContacts

```TypeScript
function selectContacts(): Promise<Array<Contact>>
```

Selects a contact. This API uses a promise to return the result.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-contact-function selectContacts(): Promise<Array<Contact>>--><!--Device-contact-function selectContacts(): Promise<Array<Contact>>-End-->

**System capability:** SystemCapability.Applications.Contacts

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;Contact&gt;&gt; |

## Examples

```TypeScript
import { contact } from '@kit.ContactsKit';

// Open the contact selection UI.
let promise = contact.selectContacts();
promise.then((data) => {
  console.info(`Succeeded in selecting Contacts. data->${JSON.stringify(data)}`);
});
```


## selectContacts

```TypeScript
function selectContacts(options: ContactSelectionOptions, callback: AsyncCallback<Array<Contact>>): void
```

Selects a contact. (Filter criteria can be transferred during contact selection.) This API uses an asynchronous callback to return the result.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-contact-function selectContacts(options: ContactSelectionOptions, callback: AsyncCallback<Array<Contact>>): void--><!--Device-contact-function selectContacts(options: ContactSelectionOptions, callback: AsyncCallback<Array<Contact>>): void-End-->

**System capability:** SystemCapability.Applications.Contacts

**Parameters:**

| [Name](arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [ContactSelectionOptions](arkts-contacts-contact-contactselectionoptions-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;Contact&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { contact } from '@kit.ContactsKit';

// Open the contact selection UI and select a contact.
contact.selectContacts({
  isMultiSelect:false
}, (err: BusinessError, data) => {
  if (err) {
    console.error(`Failed to select Contacts. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in selecting Contacts. data->${JSON.stringify(data)}`);
});
```


## selectContacts

```TypeScript
function selectContacts(options: ContactSelectionOptions): Promise<Array<Contact>>
```

Selects a contact. (Filter criteria can be transferred during contact selection.) This API uses a promise to return the result.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-contact-function selectContacts(options: ContactSelectionOptions): Promise<Array<Contact>>--><!--Device-contact-function selectContacts(options: ContactSelectionOptions): Promise<Array<Contact>>-End-->

**System capability:** SystemCapability.Applications.Contacts

**Parameters:**

| [Name](arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [ContactSelectionOptions](arkts-contacts-contact-contactselectionoptions-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;Contact&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## Examples

```TypeScript
import { contact } from '@kit.ContactsKit';

// Open the contact selection UI to select a contact.
let promise = contact.selectContacts({isMultiSelect:false});
promise.then((data) => {
  console.info(`Succeeded in selecting Contacts. data->${JSON.stringify(data)}`);
});
```
