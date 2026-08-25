# syncContacts

## Modules to Import

```TypeScript
import { contact } from '@kit.ContactsKit';
```

## syncContacts

```TypeScript
function syncContacts(context: Context, mode: ContactSyncMode, progress: ContactSyncProgress, contacts: Array<Contact>): Promise<Array<number>>
```

Synchronizes multiple contacts to the contacts database in batches.A maximum of 400 contacts can be synchronized at a time. The caller must be running in the foreground.

**Since:** 26.0.0

**ArkTS mode:** Supports only ArkTS-Dyn, since version 26.0.0.

**Required permissions:** ohos.permission.WRITE_CONTACTS

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

**System capability:** SystemCapability.Applications.ContactsData

**Parameters:**

| [Name](arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [Context](../../apis-mind-spore-lite-kit/arkts-apis/arkts-mindsporelite-mindsporelite-context-i.md) | Yes |
| mode | [ContactSyncMode](arkts-contacts-contact-contactsyncmode-e.md) | Yes |
| progress | [ContactSyncProgress](arkts-contacts-contact-contactsyncprogress-i.md) | Yes |
| contacts | Array&lt;[Contact](arkts-contacts-contact-contact-c.md)&gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Array & lt;int & gt; & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [16700001](../errorcode-contacts.md#16700001-system-internal-error) |
| [16700002](../errorcode-contacts.md#16700002-parameter-check-failed) |
| [16700003](../errorcode-contacts.md#16700003-background-service-calling-prohibited) |
| [16700004](../errorcode-contacts.md#16700004-number-of-contacts-exceeds-the-limit) |
| [16700103](../errorcode-contacts.md#16700103-operation-canceled) |
