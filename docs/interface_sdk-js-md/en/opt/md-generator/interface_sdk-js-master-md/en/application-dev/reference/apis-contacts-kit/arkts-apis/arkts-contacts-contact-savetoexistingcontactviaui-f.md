# saveToExistingContactViaUI

## Modules to Import

```TypeScript
import { contact } from '@kit.ContactsKit';
```

## saveToExistingContactViaUI

```TypeScript
function saveToExistingContactViaUI(context: Context, contact: Contact): Promise<number>
```

Saves the information to an existing contact through UI interaction.. This API uses a promise to return the result.

**Since:** 15

**Atomic service API:** This API can be used in atomic services since API version 15.

<!--Device-contact-function saveToExistingContactViaUI(context: Context, contact: Contact): Promise<number>--><!--Device-contact-function saveToExistingContactViaUI(context: Context, contact: Contact): Promise<number>-End-->

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
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [16700102](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#16700102-database-data-addition-deletion-or-modification-failed) |
| [16700103](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#16700103-operation-canceled) |
| [16700101](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#16700101-database-query-failed) |
| [16700001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#16700001-system-internal-error) |

## Examples

In the examples in this document, this.context is used to obtain the UIAbilityContext, where this represents a UIAbility instance inherited from UIAbility. To use the capabilities provided by UIAbilityContext in the UI, see [Obtaining the Context of UIAbility](../../application-models/uiability-usage.md#obtaining-the-context-of-uiability).

```TypeScript
import { common } from '@kit.AbilityKit';
import { contact } from '@kit.ContactsKit';

// Obtain the context in the component.
let contactInfo: contact.Contact = {
  id: 1,
  name: {
    fullName: 'xxx'
  },
  phoneNumbers: [{
    phoneNumber: '138xxxxxx'
  }]
}
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let promise = contact.saveToExistingContactViaUI(context, contactInfo);
promise.then((data) => {
    console.info(`Succeeded in save to existing Contact via UI.data->${JSON.stringify(data)}`);
  });
```
