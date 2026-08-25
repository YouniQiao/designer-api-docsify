# queryContactsCount

## Modules to Import

```TypeScript
import { contact } from 'kits/@kit.ContactsKit';
```

## queryContactsCount

```TypeScript
function queryContactsCount(context: Context): Promise<number>
```

Queries the number of all contacts. This API uses a promise to return the result.

**Since:** 22

**Required permissions:** ohos.permission.READ_CONTACTS

**Atomic service API:** This API can be used in atomic services since API version 22.

**System capability:** SystemCapability.Applications.ContactsData

**Parameters:**

| [Name](arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [Context](../../apis-mind-spore-lite-kit/arkts-apis/arkts-mindsporelite-mindsporelite-context-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;number & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [16700001](../errorcode-contacts.md#16700001-system-internal-error) |
