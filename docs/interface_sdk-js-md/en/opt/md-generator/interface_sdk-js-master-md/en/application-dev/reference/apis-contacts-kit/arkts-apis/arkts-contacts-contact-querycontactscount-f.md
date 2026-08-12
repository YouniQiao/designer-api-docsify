# queryContactsCount

## Modules to Import

```TypeScript
import { contact } from '@kit.ContactsKit';
```

## queryContactsCount

```TypeScript
function queryContactsCount(context: Context): Promise<number>
```

Queries the number of all contacts. This API uses a promise to return the result.

**Since:** 22

**Required permissions:** ohos.permission.READ_CONTACTS

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-contact-function queryContactsCount(context: Context): Promise<int>--><!--Device-contact-function queryContactsCount(context: Context): Promise<int>-End-->

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
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [16700001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-contacts-kit/errorcode-contacts.md#16700001-system-internal-error) |

## Examples

In the examples of this document, the UIAbilityContext is obtained through this.context, where this represents a UIAbility instance inherited from UIAbility. If you need to use the capabilities provided by UIAbilityContext in the UI, see [Obtaining the Context of UIAbility](../../application-models/uiability-usage.md#obtaining-the-context-of-uiability).

```TypeScript
import { common } from '@kit.AbilityKit';
import { contact } from '@kit.ContactsKit';

// Obtain the context in the component.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let promise = contact.queryContactsCount(context);
promise.then((data) => {
  console.info(`Succeeded in querying ContactsCount. data->${JSON.stringify(data)}`);
});
```
