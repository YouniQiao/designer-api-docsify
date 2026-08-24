# queryMyCard

## Modules to Import

```TypeScript
import { contact } from '@kit.ContactsKit';
```

## queryMyCard

```TypeScript
function queryMyCard(callback: AsyncCallback<Contact>): void
```

Queries my card. This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 10

**Substitutes:** [queryMyCard](#querymycard)(context: Context, callback: AsyncCallback&lt;Contact&gt;)

**Required permissions:** ohos.permission.READ_CONTACTS

<!--Device-contact-function queryMyCard(callback: AsyncCallback<Contact>): void--><!--Device-contact-function queryMyCard(callback: AsyncCallback<Contact>): void-End-->

**System capability:** SystemCapability.Applications.ContactsData

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[Contact](arkts-contacts-contact-contact-c.md)&gt; | Yes | Indicates the callback for getting the result of the call. If the operation is successful, information about my card is returned. If the operation fails, an error code is returned. |

**Examples**

In the sample code provided in this topic, this.context is used to obtain UIAbilityContext, where this indicates a UIAbility instance inherited from UIAbility. To use UIAbilityContext APIs on pages, see [Obtaining the Context of UIAbility](../../../application-models/uiability-usage.md#obtaining-the-context-of-uiability).

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
  import { common } from '@kit.AbilityKit';

  // Obtain the context within the component.
  let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
  contact.queryMyCard(context, (err: BusinessError, data) => {
    if (err) {
      console.error(`Failed to query My Card. Code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info(`Succeeded in querying My Card. data->${JSON.stringify(data)}`);
  });
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

contact.queryMyCard((err: BusinessError, data) => {
  if (err) {
    console.error(`Failed to query My Card. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in querying My Card. data->${JSON.stringify(data)}`);
});
```

In the sample code provided in this topic, this.context is used to obtain UIAbilityContext, where this indicates a UIAbility instance inherited from UIAbility. To use UIAbilityContext APIs on pages, see [Obtaining the Context of UIAbility](../../../application-models/uiability-usage.md#obtaining-the-context-of-uiability).

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
  import { common } from '@kit.AbilityKit';

  // Obtain the context within the component.
  let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
  contact.queryMyCard(context, {
    attributes: [contact.Attribute.ATTR_NAME, contact.Attribute.ATTR_PHONE]
  }, (err: BusinessError, data) => {
    if (err) {
      console.error(`Failed to query My Card. Code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info(`Succeeded in querying My Card. data->${JSON.stringify(data)}`);
  });
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

contact.queryMyCard({
  attributes: [contact.Attribute.ATTR_NAME, contact.Attribute.ATTR_PHONE]
}, (err: BusinessError, data) => {
  if (err) {
    console.error(`Failed to query My Card. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in querying My Card. data->${JSON.stringify(data)}`);
});
```

In the sample code provided in this topic, this.context is used to obtain UIAbilityContext, where this indicates a UIAbility instance inherited from UIAbility. To use UIAbilityContext APIs on pages, see [Obtaining the Context of UIAbility](../../../application-models/uiability-usage.md#obtaining-the-context-of-uiability).

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
  import { common } from '@kit.AbilityKit';

  // Obtain the context within the component.
  let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
  let promise = contact.queryMyCard(context, {
    attributes: [contact.Attribute.ATTR_NAME, contact.Attribute.ATTR_PHONE]
  });
  promise.then((data) => {
    console.info(`Succeeded in querying My Card. data->${JSON.stringify(data)}`);
  }).catch((err: BusinessError) => {
    console.error(`Failed to query My Card. Code: ${err.code}, message: ${err.message}`);
  });
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let promise = contact.queryMyCard({
  attributes: [contact.Attribute.ATTR_NAME, contact.Attribute.ATTR_PHONE]
});
promise.then((data) => {
  console.info(`Succeeded in querying My Card. data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to query My Card. Code: ${err.code}, message: ${err.message}`);
});
```


## queryMyCard

```TypeScript
function queryMyCard(context: Context, callback: AsyncCallback<Contact>): void
```

Queries my card. This API uses an asynchronous callback to return the result.

**Since:** 10

**Required permissions:** ohos.permission.READ_CONTACTS

<!--Device-contact-function queryMyCard(context: Context, callback: AsyncCallback<Contact>): void--><!--Device-contact-function queryMyCard(context: Context, callback: AsyncCallback<Contact>): void-End-->

**System capability:** SystemCapability.Applications.ContactsData

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | Context | Yes | Indicates the context of application or capability. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[Contact](arkts-contacts-contact-contact-c.md)&gt; | Yes | Indicates the callback for getting the result of the call. If the operation is successful, information about my card is returned. If the operation fails, an error code is returned. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [401](../errorcode-contacts.md#401-failed-to-open-the-contact-portrait-file) | Parameter error. Possible causes: Mandatory parameters are left unspecified. |

**Examples**

See [queryMyCard](#querymycard)


## queryMyCard

```TypeScript
function queryMyCard(attrs: ContactAttributes, callback: AsyncCallback<Contact>): void
```

Queries my card. (The contact attribute list can be imported.) This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 10

**Substitutes:** [queryMyCard](#querymycard)(context: Context, attrs: ContactAttributes, callback: AsyncCallback&lt;Contact&gt;)

**Required permissions:** ohos.permission.READ_CONTACTS

<!--Device-contact-function queryMyCard(attrs: ContactAttributes, callback: AsyncCallback<Contact>): void--><!--Device-contact-function queryMyCard(attrs: ContactAttributes, callback: AsyncCallback<Contact>): void-End-->

**System capability:** SystemCapability.Applications.ContactsData

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| attrs | [ContactAttributes](arkts-contacts-contact-contactattributes-c.md) | Yes | List of contact attributes. If this parameter is empty, all attribute fields (including the name, phone number, and email address) of the contact are queried. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[Contact](arkts-contacts-contact-contact-c.md)&gt; | Yes | Indicates the callback for getting the result of the call. If the operation is successful, information about my card is returned. If the operation fails, an error code is returned. |

**Examples**

See [queryMyCard](#querymycard)


## queryMyCard

```TypeScript
function queryMyCard(context: Context, attrs: ContactAttributes, callback: AsyncCallback<Contact>): void
```

Queries my card. (The contact attribute list can be imported.) This API uses an asynchronous callback to return the result.

**Since:** 10

**Required permissions:** ohos.permission.READ_CONTACTS

<!--Device-contact-function queryMyCard(context: Context, attrs: ContactAttributes, callback: AsyncCallback<Contact>): void--><!--Device-contact-function queryMyCard(context: Context, attrs: ContactAttributes, callback: AsyncCallback<Contact>): void-End-->

**System capability:** SystemCapability.Applications.ContactsData

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | Context | Yes | Indicates the context of application or capability. |
| attrs | [ContactAttributes](arkts-contacts-contact-contactattributes-c.md) | Yes | List of contact attributes. If this parameter is empty, all attribute fields (including the name, phone number, and email address) of the contact are queried. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[Contact](arkts-contacts-contact-contact-c.md)&gt; | Yes | Indicates the callback for getting the result of the call. If the operation is successful, information about my card is returned. If the operation fails, an error code is returned. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [401](../errorcode-contacts.md#401-failed-to-open-the-contact-portrait-file) | Parameter error. Possible causes: Mandatory parameters are left unspecified. |

**Examples**

See [queryMyCard](#querymycard)


## queryMyCard

```TypeScript
function queryMyCard(attrs?: ContactAttributes): Promise<Contact>
```

Queries my card. (The contact attribute list can be imported.) This API uses a promise to return the result.

**Since:** 7

**Deprecated since:** 10

**Substitutes:** [queryMyCard](#querymycard)(context: Context, attrs?: ContactAttributes)

**Required permissions:** ohos.permission.READ_CONTACTS

<!--Device-contact-function queryMyCard(attrs?: ContactAttributes): Promise<Contact>--><!--Device-contact-function queryMyCard(attrs?: ContactAttributes): Promise<Contact>-End-->

**System capability:** SystemCapability.Applications.ContactsData

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| attrs | [ContactAttributes](arkts-contacts-contact-contactattributes-c.md) | No | List of contact attributes. If this parameter is empty, all attribute fields (including the name, phone number, and email address) of the contact are queried. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[Contact](arkts-contacts-contact-contact-c.md)&gt; | Promise used to return the result, which is a contact in my card. |

**Examples**

See [queryMyCard](#querymycard)


## queryMyCard

```TypeScript
function queryMyCard(context: Context, attrs?: ContactAttributes): Promise<Contact>
```

Queries my card. (The contact attribute list can be imported.) This API uses a promise to return the result.

**Since:** 10

**Required permissions:** ohos.permission.READ_CONTACTS

<!--Device-contact-function queryMyCard(context: Context, attrs?: ContactAttributes): Promise<Contact>--><!--Device-contact-function queryMyCard(context: Context, attrs?: ContactAttributes): Promise<Contact>-End-->

**System capability:** SystemCapability.Applications.ContactsData

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | Context | Yes | Indicates the context of application or capability. |
| attrs | [ContactAttributes](arkts-contacts-contact-contactattributes-c.md) | No | List of contact attributes. If this parameter is empty, all attribute fields (including the name, phone number, and email address) of the contact are queried. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[Contact](arkts-contacts-contact-contact-c.md)&gt; | Promise used to return the result, which is a contact in my card. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [401](../errorcode-contacts.md#401-failed-to-open-the-contact-portrait-file) | Parameter error. Possible causes: Mandatory parameters are left unspecified. |

**Examples**

See [queryMyCard](#querymycard)

