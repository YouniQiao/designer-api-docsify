# addContacts

## Modules to Import

```TypeScript
import { contact } from 'kits/@kit.ContactsKit';
```

## addContacts

```TypeScript
function addContacts(context: Context, contacts: Array<Contact>): Promise<Array<number>>
```

Adds contacts in batches. This API uses a promise to return the result.

**Since:** 23

**Required permissions:** ohos.permission.WRITE_CONTACTS

**Atomic service API:** This API can be used in atomic services since API version 23.

**System capability:** SystemCapability.Applications.ContactsData

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
| [201](../../errorcode-universal.md#201-permission-denied) |
| [16700001](../errorcode-contacts.md#16700001-system-internal-error) |
| [16700002](../errorcode-contacts.md#16700002-parameter-check-failed) |
