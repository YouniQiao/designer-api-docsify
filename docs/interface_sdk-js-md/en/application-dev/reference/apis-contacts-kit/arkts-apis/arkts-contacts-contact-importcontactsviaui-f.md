# importContactsViaUI

## Modules to Import

```TypeScript
import { contact } from 'kits/@kit.ContactsKit';
```

## importContactsViaUI

```TypeScript
function importContactsViaUI(context: Context, contacts: Array<Contact>): Promise<Array<int>>
```

通过UI交互批量导入多个联系人。

 每次最多可导入100个联系人。

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-contact-function importContactsViaUI(context: Context, contacts: Array<Contact>): Promise<Array<int>>--><!--Device-contact-function importContactsViaUI(context: Context, contacts: Array<Contact>): Promise<Array<int>>-End-->

**System capability:** SystemCapability.Applications.Contacts

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | [Context](../../apis-arkui/arkts-components/arkts-arkui-context-t.md) | Yes | 应用上下文Context。 |
| contacts | Array&lt;Contact&gt; | Yes | 表示待导入数据库的联系人信息数组。 |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;Array&lt;int&gt;&gt; | 返回联系人创建结果的数组。返回的联系人id有效（可通过[getId]{ |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 801 | The specified SystemCapability name was not found. |
| 16700103 | User cancel. |
| 16700004 | The number of contacts exceeds the limit. |
| 16700002 | Invalid parameter value. |
| 16700001 | General error. |

## Examples

In the examples in this document, this.context is used to obtain the UIAbilityContext, where this represents a UIAbility instance inherited from UIAbility. If you need to use the capabilities provided by UIAbilityContext in the UI, see [Obtaining the Context of UIAbility](../../application-models/uiability-usage.md#obtaining-the-context-of-uiability).

```TypeScript
import { contact } from '@kit.ContactsKit';
import { common } from '@kit.AbilityKit';

// Obtain the context in the component.
const context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let contactList: contact.Contact[] = [];
let contactInfo: contact.Contact = {
  name: {
    fullName: 'xxx'
  },
  phoneNumbers: [{
    phoneNumber: '138xxxxxx'
  }]
}
contactList.push(contactInfo);
let promise = contact.importContactsViaUI(context, contactList);
promise.then((data) => {
  console.info(`Succeeded in importing Contact via UI: data -> ${JSON.stringify(data)}`);
});
```

