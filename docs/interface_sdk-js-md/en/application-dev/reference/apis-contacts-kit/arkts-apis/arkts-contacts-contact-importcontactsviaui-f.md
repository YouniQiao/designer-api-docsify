# importContactsViaUI

## Modules to Import

```TypeScript
import { contact } from 'kits/@kit.ContactsKit';
```

## importContactsViaUI

```TypeScript
function importContactsViaUI(context: Context, contacts: Array<Contact>): Promise<Array<number>>
```

Imports multiple contacts through UI interaction.A maximum of 100 contacts can be imported at a time. Importing contact portraits is not supported.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**System capability:** SystemCapability.Applications.Contacts

**Parameters:**

| [Name](arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [Context](../../apis-mind-spore-lite-kit/arkts-apis/arkts-mindsporelite-mindsporelite-context-i.md) | Yes |
| contacts | Array&lt;[Contact](arkts-contacts-contact-contact-c.md)&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Array & lt;number & gt; & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [16700001](../errorcode-contacts.md#16700001-system-internal-error) |
| [16700002](../errorcode-contacts.md#16700002-parameter-check-failed) |
| [16700004](../errorcode-contacts.md#16700004-number-of-contacts-exceeds-the-limit) |
| [16700103](../errorcode-contacts.md#16700103-operation-canceled) |
