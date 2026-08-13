# updateContact

## Modules to Import

```TypeScript
import { contact } from '@kit.ContactsKit';
```

## updateContact

```TypeScript
function updateContact(contact: Contact, callback: AsyncCallback<void>): void
```

Updates a contact. This API uses an asynchronous callback to return the result.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 10

**Substitutes:** [updateContact](#updateContact)(context: Context, contact: Contact, callback: AsyncCallback&lt;void&gt;)

**Required permissions:** ohos.permission.WRITE_CONTACTS

<!--Device-contact-function updateContact(contact: Contact, callback: AsyncCallback<void>): void--><!--Device-contact-function updateContact(contact: Contact, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Applications.ContactsData

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| contact | [Contact](arkts-contacts-contact-contact-c.md) | Yes | Indicates the contact information. The ID is mandatory and can be obtained through [selectContacts](arkts-contacts-contact-selectcontacts-f.md#selectContacts). |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Indicates the callback for getting the result of the call. If the operation is successful, the ID of the updated contact is returned. If the operation fails, an error code is returned. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// Select a contact via selectContacts.
contact.selectContacts().then((data) => {
  // Obtain the context within the component.
  let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
  contact.updateContact(context, {
    id: data[0].id, // Select the contact ID.
    name: {
      fullName: 'xxx'
    },
    phoneNumbers: [{
      phoneNumber: '138xxxxxxxx'
    }]
  }, (err: BusinessError) => {
    if (err) {
      console.error(`Failed to update Contact. Code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info('Succeeded in updating Contact.');
  });
}).catch((err: BusinessError) => {
  console.error(`Failed to select Contacts. Code: ${err.code}, message: ${err.message}`);
});
```


## updateContact

```TypeScript
function updateContact(context: Context, contact: Contact, callback: AsyncCallback<void>): void
```

Updates a contact. This API uses an asynchronous callback to return the result.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** -1

**Required permissions:** ohos.permission.WRITE_CONTACTS

<!--Device-contact-function updateContact(context: Context, contact: Contact, callback: AsyncCallback<void>): void--><!--Device-contact-function updateContact(context: Context, contact: Contact, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Applications.ContactsData

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | Context | Yes | Indicates the context of application or capability. |
| contact | [Contact](arkts-contacts-contact-contact-c.md) | Yes | Indicates the contact information. The ID is mandatory and can be obtained through [selectContacts](arkts-contacts-contact-selectcontacts-f.md#selectContacts). |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Indicates the callback for getting the result of the call. If the operation is successful, the ID of the updated contact is returned. If the operation fails, an error code is returned. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../errorcode-contacts.md#401-failed-to-open-the-contact-portrait-file) | 1.Parameter error. Possible causes: Mandatory parameters are left unspecified. 2.Failed to open contact portrait file. 3.Internal error. Invalid contact id. Failed to generate contact profile. 4.Internal error. Failed to save contact portrait. 5.Internal error. Invalid contact rawId. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |

## Examples

In the sample code provided in this topic, this.context is used to obtain UIAbilityContext, where this indicates a UIAbility instance inherited from UIAbility. To use UIAbilityContext APIs on pages, see [Obtaining the Context of UIAbility](../../../application-models/uiability-usage.md#obtaining-the-context-of-uiability).

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Select a contact via selectContacts.
contact.selectContacts().then((data) => {
  // Obtain the context within the component.
  let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
  contact.updateContact(context, {
    id: data[0].id, // Select the contact ID.
    name: {
      fullName: 'xxx'
    },
    phoneNumbers: [{
      phoneNumber: '138xxxxxxxx'
    }]
  }, (err: BusinessError) => {
    if (err) {
      console.error(`Failed to update Contact. Code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info('Succeeded in updating Contact.');
  });
}).catch((err: BusinessError) => {
  console.error(`Failed to select Contacts. Code: ${err.code}, message: ${err.message}`);
});
```


## updateContact

```TypeScript
function updateContact(contact: Contact, attrs: ContactAttributes, callback: AsyncCallback<void>): void
```

Updates a contact. (The contact attribute list can be imported.) This API uses an asynchronous callback to return the result.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 10

**Substitutes:** [updateContact](#updateContact)(context: Context, contact: Contact, attrs: ContactAttributes, callback: AsyncCallback&lt;void&gt;)

**Required permissions:** ohos.permission.WRITE_CONTACTS

<!--Device-contact-function updateContact(contact: Contact, attrs: ContactAttributes, callback: AsyncCallback<void>): void--><!--Device-contact-function updateContact(contact: Contact, attrs: ContactAttributes, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Applications.ContactsData

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| contact | [Contact](arkts-contacts-contact-contact-c.md) | Yes | Indicates the contact information. The ID is mandatory and can be obtained through [selectContacts](arkts-contacts-contact-selectcontacts-f.md#selectContacts). |
| attrs | [ContactAttributes](arkts-contacts-contact-contactattributes-c.md) | Yes | Contact attribute list. If this parameter is left empty, all attribute fields of the contact are updated, including the name, phone number, and email address. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Indicates the callback for getting the result of the call. If the operation is successful, the ID of the updated contact is returned. If the operation fails, an error code is returned. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// Select a contact via selectContacts.
contact.selectContacts().then((data) => {
  contact.updateContact({
    id: data[0].id, // Select the contact ID.
    name: {
      fullName: 'xxx'
    },
    phoneNumbers: [{
      phoneNumber: '138xxxxxxxx'
    }]
  }, {
    attributes: [contact.Attribute.ATTR_NAME, contact.Attribute.ATTR_PHONE]
  }, (err: BusinessError) => {
    if (err) {
      console.error(`Failed to update Contact. Code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info('Succeeded in updating Contact.');
  });
}).catch((err: BusinessError) => {
  console.error(`Failed to select Contacts. Code: ${err.code}, message: ${err.message}`);
});
```


## updateContact

```TypeScript
function updateContact(context: Context, contact: Contact, attrs: ContactAttributes, callback: AsyncCallback<void>): void
```

Updates a contact. (The contact attribute list can be imported.) This API uses an asynchronous callback to return the result.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** -1

**Required permissions:** ohos.permission.WRITE_CONTACTS

<!--Device-contact-function updateContact(context: Context, contact: Contact, attrs: ContactAttributes, callback: AsyncCallback<void>): void--><!--Device-contact-function updateContact(context: Context, contact: Contact, attrs: ContactAttributes, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Applications.ContactsData

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | Context | Yes | Indicates the context of application or capability. |
| contact | [Contact](arkts-contacts-contact-contact-c.md) | Yes | Indicates the contact information. The ID is mandatory and can be obtained through [selectContacts](arkts-contacts-contact-selectcontacts-f.md#selectContacts). |
| attrs | [ContactAttributes](arkts-contacts-contact-contactattributes-c.md) | Yes | Contact attribute list. If this parameter is left empty, all attribute fields of the contact are updated, including the name, phone number, and email address. |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes | Indicates the callback for getting the result of the call. If the operation is successful, the ID of the updated contact is returned. If the operation fails, an error code is returned. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../errorcode-contacts.md#401-failed-to-open-the-contact-portrait-file) | 1.Parameter error. Possible causes:Mandatory parameters are left unspecified. 2.Failed to open contact portrait file. 3.Internal error. Invalid contact id. Failed to generate contact profile. 4.Internal error. Failed to save contact portrait. 5.Internal error. Invalid contact rawId. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |

## Examples

In the sample code provided in this topic, this.context is used to obtain UIAbilityContext, where this indicates a UIAbility instance inherited from UIAbility. To use UIAbilityContext APIs on pages, see [Obtaining the Context of UIAbility](../../../application-models/uiability-usage.md#obtaining-the-context-of-uiability).

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Select a contact via selectContacts.
contact.selectContacts().then((data) => {
  // Obtain the context within the component.
  let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
  contact.updateContact(context, {
    id: data[0].id, // Select the contact ID.
    name: {
      fullName: 'xxx'
    },
    phoneNumbers: [{
      phoneNumber: '138xxxxxxxx'
    }]
  }, {
    attributes: [contact.Attribute.ATTR_NAME, contact.Attribute.ATTR_PHONE]
  }, (err: BusinessError) => {
    if (err) {
      console.error(`Failed to update Contact. Code: ${err.code}, message: ${err.message}`);
      return;
    }
    console.info('Succeeded in updating Contact.');
  });
}).catch((err: BusinessError) => {
  console.error(`Failed to select Contacts. Code: ${err.code}, message: ${err.message}`);
});
```


## updateContact

```TypeScript
function updateContact(contact: Contact, attrs?: ContactAttributes): Promise<void>
```

Updates a contact. (The contact attribute list can be imported.) This API uses a promise to return the result.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 10

**Substitutes:** [updateContact](#updateContact)(context: Context, contact: Contact, attrs?: ContactAttributes)

**Required permissions:** ohos.permission.WRITE_CONTACTS

<!--Device-contact-function updateContact(contact: Contact, attrs?: ContactAttributes): Promise<void>--><!--Device-contact-function updateContact(contact: Contact, attrs?: ContactAttributes): Promise<void>-End-->

**System capability:** SystemCapability.Applications.ContactsData

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| contact | [Contact](arkts-contacts-contact-contact-c.md) | Yes | Indicates the contact information. The ID is mandatory and can be obtained through [selectContacts](arkts-contacts-contact-selectcontacts-f.md#selectContacts). |
| attrs | [ContactAttributes](arkts-contacts-contact-contactattributes-c.md) | No | Contact attribute list. If this parameter is left empty, all attribute fields of the contact are updated, including the name, phone number, and email address. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

## Examples

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

// Select a contact via selectContacts.
contact.selectContacts().then((data) => {
  let promise = contact.updateContact({
    id: data[0].id, // Select the contact ID.
    name: {
      fullName: 'xxx'
    },
    phoneNumbers: [{
      phoneNumber: '138xxxxxxxx'
    }]
  }, {
    attributes: [contact.Attribute.ATTR_NAME, contact.Attribute.ATTR_PHONE]
  });
  promise.then(() => {
    console.info('Succeeded in updating Contact.');
  }).catch((err: BusinessError) => {
    console.error(`Failed to update Contact. Code: ${err.code}, message: ${err.message}`);
  });
}).catch((err: BusinessError) => {
  console.error(`Failed to select Contacts. Code: ${err.code}, message: ${err.message}`);
});
```


## updateContact

```TypeScript
function updateContact(context: Context, contact: Contact, attrs?: ContactAttributes): Promise<void>
```

Updates a contact. (The contact attribute list can be imported.) This API uses a promise to return the result.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** -1

**Required permissions:** ohos.permission.WRITE_CONTACTS

<!--Device-contact-function updateContact(context: Context, contact: Contact, attrs?: ContactAttributes): Promise<void>--><!--Device-contact-function updateContact(context: Context, contact: Contact, attrs?: ContactAttributes): Promise<void>-End-->

**System capability:** SystemCapability.Applications.ContactsData

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | Context | Yes | Indicates the context of application or capability. |
| contact | [Contact](arkts-contacts-contact-contact-c.md) | Yes | Indicates the contact information. The ID is mandatory and can be obtained through [selectContacts](arkts-contacts-contact-selectcontacts-f.md#selectContacts). |
| attrs | [ContactAttributes](arkts-contacts-contact-contactattributes-c.md) | No | Contact attribute list. If this parameter is left empty, all attribute fields of the contact are updated, including the name, phone number, and email address. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | Promise that returns no value. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../errorcode-contacts.md#401-failed-to-open-the-contact-portrait-file) | 1.Parameter error. Possible causes: Mandatory parameters are left unspecified. 2.Failed to open contact portrait file. 3.Internal error. Invalid contact id. Failed to generate contact profile. 4.Internal error. Failed to save contact portrait. 5.Internal error. Invalid contact rawId. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |

## Examples

In the sample code provided in this topic, this.context is used to obtain UIAbilityContext, where this indicates a UIAbility instance inherited from UIAbility. To use UIAbilityContext APIs on pages, see [Obtaining the Context of UIAbility](../../../application-models/uiability-usage.md#obtaining-the-context-of-uiability).

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
  import { common } from '@kit.AbilityKit';

  // Select a contact via selectContacts.
  contact.selectContacts().then((data) => {
    // Obtain the context within the component.
    let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
    let promise = contact.updateContact(context, {
      id: data[0].id, // Select the contact ID.
      name: {
        fullName: 'xxx'
      },
      phoneNumbers: [{
        phoneNumber: '138xxxxxxxx'
      }]
    }, {
      attributes: [contact.Attribute.ATTR_NAME, contact.Attribute.ATTR_PHONE]
    });
    promise.then(() => {
      console.info('Succeeded in updating Contact.');
    }).catch((err: BusinessError) => {
      console.error(`Failed to update Contact. Code: ${err.code}, message: ${err.message}`);
    });
  }).catch((err: BusinessError) => {
    console.error(`Failed to select Contacts. Code: ${err.code}, message: ${err.message}`);
  });
```

