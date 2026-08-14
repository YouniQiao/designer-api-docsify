# queryContactsCount

## Modules to Import

```TypeScript
import { contact } from 'contact';
```

## queryContactsCount

```TypeScript
function queryContactsCount(context: Context): Promise<int>
```

Queries the number of all contacts. This API uses a promise to return the result.

**Since:** 22

**ArkTS mode:** ArkTS-Dyn only, since version 22.

**Deprecated since:** -1

**Required permissions:** ohos.permission.READ_CONTACTS

**Atomic service API:** This API can be used in atomic services since API version 22.

<!--Device-contact-function queryContactsCount(context: Context): Promise<int>--><!--Device-contact-function queryContactsCount(context: Context): Promise<int>-End-->

**System capability:** SystemCapability.Applications.ContactsData

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | Context | Yes | Indicates the context of application or capability. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;int&gt; | Promise used to return the result, which is the number of queried contacts. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [16700001](../errorcode-contacts.md#16700001-system-internal-error) | General error. |

## Examples

```TypeScript
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Obtain the context within the component.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let promise = contact.queryContactsCount(context);
promise.then((data) => {
  console.info(`Succeeded in querying ContactsCount. data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to query ContactsCount. Code: ${err.code}, message: ${err.message}`);
});
```

