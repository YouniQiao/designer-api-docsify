# queryContactSyncInfo

## Modules to Import

```TypeScript
import { contact } from '@kit.ContactsKit';
```

## queryContactSyncInfo

```TypeScript
function queryContactSyncInfo(context: Context): Promise<Array<ContactSyncInfo>>
```

Queries information about ongoing contact synchronization for the calling application.

If the returned contact synchronization information is empty, the invoking party does not synchronize contacts or the contact synchronization is complete.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Required permissions:** ohos.permission.READ_CONTACTS

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-contact-function queryContactSyncInfo(context: Context): Promise<Array<ContactSyncInfo>>--><!--Device-contact-function queryContactSyncInfo(context: Context): Promise<Array<ContactSyncInfo>>-End-->

**System capability:** SystemCapability.Applications.ContactsData

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | Context | Yes | Indicates the context of the application or capability. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;[ContactSyncInfo](arkts-contacts-contact-contactsyncinfo-i.md)&gt;&gt; | Returns the array of contacts synchronization information for the calling application. Returns null if no contacts are being synchronized. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/errorcode-universal.md#201-permission-denied) | Permission denied. |
| [16700001](../../../../../../../../gitee_tmp/docs/stamaster/en/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#16700001-system-internal-error) | General error. |

