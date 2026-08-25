# selectContact

## Modules to Import

```TypeScript
import { contact } from 'kits/@kit.ContactsKit';
```

## selectContact

```TypeScript
function selectContact(callback: AsyncCallback<Array<Contact>>): void
```

Selects a contact. This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 10

**Substitutes:** [selectContacts](arkts-contacts-contact-selectcontacts-f.md)(callback: AsyncCallback&lt;Array&lt;Contact&gt;&gt;)

**System capability:** SystemCapability.Applications.Contacts

**Parameters:**

| [Name](arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[Contact](arkts-contacts-contact-contact-c.md)&gt;&gt; | Yes |


## selectContact

```TypeScript
function selectContact(): Promise<Array<Contact>>
```

Selects a contact. This API uses a promise to return the result.

**Since:** 7

**Deprecated since:** 10

**Substitutes:** [selectContacts](arkts-contacts-contact-selectcontacts-f.md)()

**System capability:** SystemCapability.Applications.Contacts

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[Contact](arkts-contacts-contact-contact-c.md)&gt;&gt; |
