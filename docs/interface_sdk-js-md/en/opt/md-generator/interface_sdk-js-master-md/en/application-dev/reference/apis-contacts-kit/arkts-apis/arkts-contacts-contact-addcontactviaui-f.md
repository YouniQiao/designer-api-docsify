# addContactViaUI

## Modules to Import

```TypeScript
import { contact } from 'kits/@kit.ContactsKit';
```

## addContactViaUI

```TypeScript
function addContactViaUI(context: Context, contact: Contact): Promise<number>
```

Calls the API for adding a contact to open the UI. This API uses a promise to return the result.

**Since:** 15

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-contact-function addContactViaUI(context: Context, contact: Contact): Promise<number>--><!--Device-contact-function addContactViaUI(context: Context, contact: Contact): Promise<number>-End-->

**System capability:** SystemCapability.Applications.Contacts

**Parameters:**

| [Name](arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [Context](../../apis-arkui/arkts-components/arkts-arkui-context-t.md) | Yes |
| contact | [Contact](arkts-contacts-contact-contact-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;number&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [16700102](../errorcode-contacts.md#16700102-database-data-addition-deletion-or-modification-failed) |
| [16700103](../errorcode-contacts.md#16700103-operation-canceled) |
| [16700001](../errorcode-contacts.md#16700001-system-internal-error) |

## Examples

In the examples in this document, the UIAbilityContext is obtained through this.context, where this represents the UIAbility instance that inherits from UIAbility. If you need to use the capabilities provided by UIAbilityContext in the UI, see [Obtaining the Context of UIAbility](../../application-models/uiability-usage.md#obtaining-the-context-of-uiability).

```TypeScript
import { common } from '@kit.AbilityKit';
import { contact } from '@kit.ContactsKit';

// Obtain the context in the component.
let contactInfo: contact.Contact = {
  name: {
    fullName: 'xxx'
  },
  phoneNumbers: [{
    phoneNumber: '138xxxxxx'
  }]
}
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let promise = contact.addContactViaUI(context, contactInfo);
promise.then((data) => {
    console.info(`Succeeded in add Contact via UI.data->${JSON.stringify(data)}`);
  });
```
