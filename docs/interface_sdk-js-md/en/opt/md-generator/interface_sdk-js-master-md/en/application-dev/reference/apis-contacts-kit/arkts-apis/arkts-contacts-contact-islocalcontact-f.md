# isLocalContact

## Modules to Import

```TypeScript
import { contact } from 'kits/@kit.ContactsKit';
```

## isLocalContact

```TypeScript
function isLocalContact(id: number, callback: AsyncCallback<boolean>): void
```

Checks whether the ID of this contact is in the local address book. This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 10

**Substitutes:** [contact.isLocalContact](arkts-contacts-contact-islocalcontact-f.md#islocalcontact)(context:

**Required permissions:** ohos.permission.READ_CONTACTS

<!--Device-contact-function isLocalContact(id: number, callback: AsyncCallback<boolean>): void--><!--Device-contact-function isLocalContact(id: number, callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.Applications.ContactsData

**Parameters:**

| [Name](arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| id | number | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { contact } from '@kit.ContactsKit';

// Check whether the contact with ID 1 is in the local phone book.
contact.isLocalContact(1, (err: BusinessError, data) => {
  if (err) {
    console.error(`Failed to isLocalContact. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in isLocalContact. data->${JSON.stringify(data)}`);
});
```


## isLocalContact

```TypeScript
function isLocalContact(context: Context, id: number, callback: AsyncCallback<boolean>): void
```

Checks whether the ID of this contact is in the local address book. This API uses an asynchronous callback to return the result.

**Since:** 10

**Required permissions:** ohos.permission.READ_CONTACTS

<!--Device-contact-function isLocalContact(context: Context, id: number, callback: AsyncCallback<boolean>): void--><!--Device-contact-function isLocalContact(context: Context, id: number, callback: AsyncCallback<boolean>): void-End-->

**System capability:** SystemCapability.Applications.ContactsData

**Parameters:**

| [Name](arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [Context](../../apis-arkui/arkts-components/arkts-arkui-context-t.md) | Yes |
| id | number | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;boolean&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../errorcode-universal.md#201-permission-denied) |

## Examples

In the examples in this document, this.context is used to obtain the UIAbilityContext, where this represents a UIAbility instance that inherits from UIAbility. To use the capabilities provided by UIAbilityContext in the UI, see [Obtaining the Context of UIAbility](../../application-models/uiability-usage.md#obtaining-the-context-of-uiability).

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { contact } from '@kit.ContactsKit';
import { common } from '@kit.AbilityKit';

// Obtain the context in the component.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
contact.isLocalContact(context, 1, (err: BusinessError, data) => {
  if (err) {
    console.error(`Failed to isLocalContact. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in isLocalContact. data->${JSON.stringify(data)}`);
});
```


## isLocalContact

```TypeScript
function isLocalContact(id: number): Promise<boolean>
```

Checks whether the ID of this contact is in the local address book. This API uses a promise to return the result.

**Since:** 7

**Deprecated since:** 10

**Substitutes:** [contact.isLocalContact](arkts-contacts-contact-islocalcontact-f.md#islocalcontact)(context:

**Required permissions:** ohos.permission.READ_CONTACTS

<!--Device-contact-function isLocalContact(id: number): Promise<boolean>--><!--Device-contact-function isLocalContact(id: number): Promise<boolean>-End-->

**System capability:** SystemCapability.Applications.ContactsData

**Parameters:**

| [Name](arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| id | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;boolean&gt; |

## Examples

```TypeScript
import { contact } from '@kit.ContactsKit';

// Check whether the contact with ID 1 is in the local phone book.
let promise = contact.isLocalContact(1);
promise.then((data) => {
  console.info(`Succeeded in isLocalContact. data->${JSON.stringify(data)}`);
});
```


## isLocalContact

```TypeScript
function isLocalContact(context: Context, id: number): Promise<boolean>
```

Checks whether the ID of this contact is in the local address book. This API uses a promise to return the result.

**Since:** 10

**Required permissions:** ohos.permission.READ_CONTACTS

<!--Device-contact-function isLocalContact(context: Context, id: number): Promise<boolean>--><!--Device-contact-function isLocalContact(context: Context, id: number): Promise<boolean>-End-->

**System capability:** SystemCapability.Applications.ContactsData

**Parameters:**

| [Name](arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [Context](../../apis-arkui/arkts-components/arkts-arkui-context-t.md) | Yes |
| id | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;boolean&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [201](../../errorcode-universal.md#201-permission-denied) |

## Examples

In the examples in this document, this.context is used to obtain the UIAbilityContext, where this represents a UIAbility instance inherited from UIAbility. If you need to use the capabilities provided by UIAbilityContext in the UI, see [Obtaining the Context of UIAbility](../../application-models/uiability-usage.md#obtaining-the-context-of-uiability).

```TypeScript
import { contact } from '@kit.ContactsKit';
  import { common } from '@kit.AbilityKit';

  // Obtain the context in the component.
  let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
  let promise = contact.isLocalContact(context, 1);
  promise.then((data) => {
    console.info(`Succeeded in isLocalContact. data->${JSON.stringify(data)}`);
  });
```
