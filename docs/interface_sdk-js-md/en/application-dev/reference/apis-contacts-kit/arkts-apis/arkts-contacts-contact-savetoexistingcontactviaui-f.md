# saveToExistingContactViaUI

## Modules to Import

```TypeScript
import { contact } from 'kits/@kit.ContactsKit';
```

## saveToExistingContactViaUI

```TypeScript
function saveToExistingContactViaUI(context: Context, contact: Contact): Promise<number>
```

Saves the information to an existing contact through UI interaction.. This API uses a promise to return the result.

**Since:** 15

**Atomic service API:** This API can be used in atomic services since API version 15.

**System capability:** SystemCapability.Applications.Contacts

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
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [16700001](../errorcode-contacts.md#16700001-system-internal-error) |
| [16700101](../errorcode-contacts.md#16700101-database-query-failed) |
| [16700102](../errorcode-contacts.md#16700102-database-data-addition-deletion-or-modification-failed) |
| [16700103](../errorcode-contacts.md#16700103-operation-canceled) |
