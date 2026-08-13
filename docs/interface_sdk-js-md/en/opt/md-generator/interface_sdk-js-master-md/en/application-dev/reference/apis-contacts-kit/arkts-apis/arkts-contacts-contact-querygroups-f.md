# queryGroups

## Modules to Import

```TypeScript
import { contact } from '@kit.ContactsKit';
```

## queryGroups

```TypeScript
function queryGroups(callback: AsyncCallback<Array<Group>>): void
```

Queries all groups of a contact. This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 10

**Substitutes:** [queryGroups](#queryGroups)(context: Context, callback: AsyncCallback&lt;Array&lt;Group&gt;&gt;)

**Required permissions:** ohos.permission.READ_CONTACTS

<!--Device-contact-function queryGroups(callback: AsyncCallback<Array<Group>>): void--><!--Device-contact-function queryGroups(callback: AsyncCallback<Array<Group>>): void-End-->

**System capability:** SystemCapability.Applications.ContactsData

**Parameters:**

| [Name](arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[Group](arkts-contacts-contact-group-c.md)&gt;&gt; | Yes |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { contact } from '@kit.ContactsKit';

contact.queryGroups((err: BusinessError, data) => {
  if (err) {
    console.error(`Failed to query Groups. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in querying Groups.. data->${JSON.stringify(data)}`);
});
```


## queryGroups

```TypeScript
function queryGroups(context: Context, callback: AsyncCallback<Array<Group>>): void
```

Queries all groups of a contact. This API uses an asynchronous callback to return the result.

**Since:** 10

**Deprecated since:** -1

**Required permissions:** ohos.permission.READ_CONTACTS

<!--Device-contact-function queryGroups(context: Context, callback: AsyncCallback<Array<Group>>): void--><!--Device-contact-function queryGroups(context: Context, callback: AsyncCallback<Array<Group>>): void-End-->

**System capability:** SystemCapability.Applications.ContactsData

**Parameters:**

| [Name](arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [Context](../../apis-mind-spore-lite-kit/arkts-apis/arkts-mindsporelite-mindsporelite-context-i.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[Group](arkts-contacts-contact-group-c.md)&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../errorcode-contacts.md#401-failed-to-open-the-contact-portrait-file) |
| [201](../../errorcode-universal.md#201-permission-denied) |

## Examples

In the examples in this document, this.context is used to obtain the UIAbilityContext, where this represents a UIAbility instance that inherits from UIAbility. To use the capabilities provided by UIAbilityContext in the UI, see [Obtaining the Context of UIAbility](../../../application-models/uiability-usage.md#obtaining-the-context-of-uiability).

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { contact } from '@kit.ContactsKit';
import { common } from '@kit.AbilityKit';

// Obtain the context in the component.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
contact.queryGroups(context, (err: BusinessError, data) => {
  if (err) {
    console.error(`Failed to query Groups. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in querying Groups. data->${JSON.stringify(data)}`);
});
```


## queryGroups

```TypeScript
function queryGroups(holder: Holder, callback: AsyncCallback<Array<Group>>): void
```

Queries all groups of a contact based on the specified holder. This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 10

**Substitutes:** [queryGroups](#queryGroups)(context: Context, holder: Holder, callback: AsyncCallback&lt;Array&lt;Group&gt;&gt;)

**Required permissions:** ohos.permission.READ_CONTACTS

<!--Device-contact-function queryGroups(holder: Holder, callback: AsyncCallback<Array<Group>>): void--><!--Device-contact-function queryGroups(holder: Holder, callback: AsyncCallback<Array<Group>>): void-End-->

**System capability:** SystemCapability.Applications.ContactsData

**Parameters:**

| [Name](arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| holder | [Holder](arkts-contacts-contact-holder-c.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[Group](arkts-contacts-contact-group-c.md)&gt;&gt; | Yes |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { contact } from '@kit.ContactsKit';

contact.queryGroups({
  holderId: 1,
  bundleName: '',
  displayName: ''
}, (err: BusinessError, data) => {
  if (err) {
    console.error(`Failed to query Groups. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in querying Groups. data->${JSON.stringify(data)}`);
});
```


## queryGroups

```TypeScript
function queryGroups(context: Context, holder: Holder, callback: AsyncCallback<Array<Group>>): void
```

Queries all groups of a contact based on the specified holder. This API uses an asynchronous callback to return the result.

**Since:** 10

**Deprecated since:** -1

**Required permissions:** ohos.permission.READ_CONTACTS

<!--Device-contact-function queryGroups(context: Context, holder: Holder, callback: AsyncCallback<Array<Group>>): void--><!--Device-contact-function queryGroups(context: Context, holder: Holder, callback: AsyncCallback<Array<Group>>): void-End-->

**System capability:** SystemCapability.Applications.ContactsData

**Parameters:**

| [Name](arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [Context](../../apis-mind-spore-lite-kit/arkts-apis/arkts-mindsporelite-mindsporelite-context-i.md) | Yes |
| holder | [Holder](arkts-contacts-contact-holder-c.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[Group](arkts-contacts-contact-group-c.md)&gt;&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../errorcode-contacts.md#401-failed-to-open-the-contact-portrait-file) |
| [201](../../errorcode-universal.md#201-permission-denied) |

## Examples

In the examples of this document, UIAbilityContext is obtained through this.context, where this represents a UIAbility instance inherited from UIAbility. To use the capabilities provided by UIAbilityContext in the UI, see [Obtaining the Context of UIAbility](../../../application-models/uiability-usage.md#obtaining-the-context-of-uiability).

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { contact } from '@kit.ContactsKit';
import { common } from '@kit.AbilityKit';

// Obtain the context in the component.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
contact.queryGroups(context, {
  holderId: 1,
  bundleName: '',
  displayName: ''
}, (err: BusinessError, data) => {
  if (err) {
    console.error(`Failed to query Groups. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in querying Groups. data->${JSON.stringify(data)}`);
});
```


## queryGroups

```TypeScript
function queryGroups(holder?: Holder): Promise<Array<Group>>
```

Queries all groups of a contact based on the specified holder. This API uses a promise to return the result.

**Since:** 7

**Deprecated since:** 10

**Substitutes:** [queryGroups](#queryGroups)(context: Context, holder?: Holder)

**Required permissions:** ohos.permission.READ_CONTACTS

<!--Device-contact-function queryGroups(holder?: Holder): Promise<Array<Group>>--><!--Device-contact-function queryGroups(holder?: Holder): Promise<Array<Group>>-End-->

**System capability:** SystemCapability.Applications.ContactsData

**Parameters:**

| [Name](arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| holder | [Holder](arkts-contacts-contact-holder-c.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[Group](arkts-contacts-contact-group-c.md)&gt;&gt; |

## Examples

```TypeScript
import { contact } from '@kit.ContactsKit';

let promise = contact.queryGroups({
  holderId: 1,
  bundleName: '',
  displayName: ''
});
promise.then((data) => {
  console.info(`Succeeded in querying Groups. data->${JSON.stringify(data)}`);
});
```


## queryGroups

```TypeScript
function queryGroups(context: Context, holder?: Holder): Promise<Array<Group>>
```

Queries all groups of a contact based on the specified holder. This API uses a promise to return the result.

**Since:** 10

**Deprecated since:** -1

**Required permissions:** ohos.permission.READ_CONTACTS

<!--Device-contact-function queryGroups(context: Context, holder?: Holder): Promise<Array<Group>>--><!--Device-contact-function queryGroups(context: Context, holder?: Holder): Promise<Array<Group>>-End-->

**System capability:** SystemCapability.Applications.ContactsData

**Parameters:**

| [Name](arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [Context](../../apis-mind-spore-lite-kit/arkts-apis/arkts-mindsporelite-mindsporelite-context-i.md) | Yes |
| holder | [Holder](arkts-contacts-contact-holder-c.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[Group](arkts-contacts-contact-group-c.md)&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [401](../errorcode-contacts.md#401-failed-to-open-the-contact-portrait-file) |
| [201](../../errorcode-universal.md#201-permission-denied) |

## Examples

In the examples in this document, this.context is used to obtain UIAbilityContext, where this refers to a UIAbility instance inherited from UIAbility. If you need to use the capabilities provided by UIAbilityContext in the UI, see [Obtaining the Context of UIAbility](../../../application-models/uiability-usage.md#obtaining-the-context-of-uiability).

```TypeScript
import { common } from '@kit.AbilityKit';
import { contact } from '@kit.ContactsKit';

// Obtain the context in the component.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let promise = contact.queryGroups(context, {
  holderId: 1,
  bundleName: '',
  displayName: ''
});
promise.then((data) => {
  console.info(`Succeeded in querying Groups. data->${JSON.stringify(data)}`);
});
```
