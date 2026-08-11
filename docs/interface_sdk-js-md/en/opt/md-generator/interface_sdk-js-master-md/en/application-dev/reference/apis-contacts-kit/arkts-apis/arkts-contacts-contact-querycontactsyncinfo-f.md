# queryContactSyncInfo

## Modules to Import

```TypeScript
import { contact } from 'kits/@kit.ContactsKit';
```

## queryContactSyncInfo

```TypeScript
function queryContactSyncInfo(context: Context): Promise<Array<ContactSyncInfo>>
```

Queries information about ongoing contact synchronization for the calling application.

If the returned contact synchronization information is empty, the invoking party does not synchronize contacts or the contact synchronization is complete.

**Since:** 26.0.0

**Required permissions:** ohos.permission.READ_CONTACTS

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-contact-function queryContactSyncInfo(context: Context): Promise<Array<ContactSyncInfo>>--><!--Device-contact-function queryContactSyncInfo(context: Context): Promise<Array<ContactSyncInfo>>-End-->

**System capability:** SystemCapability.Applications.ContactsData

**Parameters:**

| [Name](arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [Context](../../apis-arkui/arkts-components/arkts-arkui-context-t.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;ContactSyncInfo&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [16700001](../errorcode-contacts.md#16700001-system-internal-error) |

## Examples

In the examples of this document, UIAbilityContext is obtained through this.context, where this represents a UIAbility instance inherited from UIAbility. If you need to use the capabilities provided by UIAbilityContext in the UI, see [Obtaining the Context of UIAbility](../../application-models/uiability-usage.md#obtaining-the-context-of-uiability).

```TypeScript
import { contact } from '@kit.ContactsKit';
import { common } from '@kit.AbilityKit';

// Obtain the context within the component.
const context = this.getUIContext().getHostContext() as common.UIAbilityContext;
const syncInfoList: contact.ContactSyncInfo[] = await contact.queryContactSyncInfo(context) as contact.ContactSyncInfo[];
console.info('queryContactSyncInfo syncInfoList '  + JSON.stringify(syncInfoList));
```
