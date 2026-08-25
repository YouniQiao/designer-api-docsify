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

**System capability:** SystemCapability.Applications.Contacts

**Parameters:**

| [Name](arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[Contact](arkts-contacts-contact-contact-c.md)&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../errorcode-contacts.md#401-failed-to-open-the-contact-portrait-file) |


## selectContacts

```TypeScript
function selectContacts(): Promise<Array<Contact>>
```

Selects a contact. This API uses a promise to return the result.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Applications.Contacts

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[Contact](arkts-contacts-contact-contact-c.md)&gt;&gt; |


## selectContacts

```TypeScript
function selectContacts(options: ContactSelectionOptions, callback: AsyncCallback<Array<Contact>>): void
```

Selects a contact. (Filter criteria can be transferred during contact selection.) This API uses an asynchronous callback to return the result.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Applications.Contacts

**Parameters:**

| [Name](arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [ContactSelectionOptions](arkts-contacts-contact-contactselectionoptions-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[Contact](arkts-contacts-contact-contact-c.md)&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../errorcode-contacts.md#401-failed-to-open-the-contact-portrait-file) |


## selectContacts

```TypeScript
function selectContacts(options: ContactSelectionOptions): Promise<Array<Contact>>
```

Selects a contact. (Filter criteria can be transferred during contact selection.) This API uses a promise to return the result.

**Since:** 10

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.Applications.Contacts

**Parameters:**

| [Name](arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [ContactSelectionOptions](arkts-contacts-contact-contactselectionoptions-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[Contact](arkts-contacts-contact-contact-c.md)&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../errorcode-contacts.md#401-failed-to-open-the-contact-portrait-file) |
