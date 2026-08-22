# queryKey

## Modules to Import

```TypeScript
import { contact } from '@kit.ContactsKit';
```

## queryKey

```TypeScript
function queryKey(id: number, callback: AsyncCallback<string>): void
```

Queries the key of a contact based on the specified contact ID. This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 10

**Substitutes:** [queryKey](#querykey)(context: Context, id: number, callback: AsyncCallback&lt;string&gt;)

**Required permissions:** ohos.permission.READ_CONTACTS

<!--Device-contact-function queryKey(id: number, callback: AsyncCallback<string>): void--><!--Device-contact-function queryKey(id: number, callback: AsyncCallback<string>): void-End-->

**System capability:** SystemCapability.Applications.ContactsData

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| id | number | Yes | Contact ID. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes | Indicates the callback for getting the result of the call. If the operation is successful, the key of the queried contact is returned. If the operation fails, an error code is returned. |

**Examples**

In the sample code provided in this topic, this.context is used to obtain UIAbilityContext, where this indicates a UIAbility instance inherited from UIAbility. To use UIAbilityContext APIs on pages, see [Obtaining the Context of UIAbility](../../../application-models/uiability-usage.md#obtaining-the-context-of-uiability).

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context within the component.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
contact.queryKey(context, 1, (err: BusinessError, data) => {
  if (err) {
    console.error(`Failed to query Key. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in querying Key. data->${JSON.stringify(data)}`);
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

contact.queryKey(1, (err: BusinessError, data) => {
  if (err) {
    console.error(`Failed to query Key. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in querying Key. data->${JSON.stringify(data)}`);
});
```

In the sample code provided in this topic, this.context is used to obtain UIAbilityContext, where this indicates a UIAbility instance inherited from UIAbility. To use UIAbilityContext APIs on pages, see [Obtaining the Context of UIAbility](../../../application-models/uiability-usage.md#obtaining-the-context-of-uiability).

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context within the component.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
contact.queryKey(context, 1, {
  holderId: 1,
  bundleName: "",
  displayName: ""
}, (err: BusinessError, data) => {
  if (err) {
    console.error(`Failed to query Key. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in querying Key. data->${JSON.stringify(data)}`);
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

contact.queryKey(1, {
  holderId: 1,
  bundleName: "",
  displayName: ""
}, (err: BusinessError, data) => {
  if (err) {
    console.error(`Failed to query Key. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in querying Key. data->${JSON.stringify(data)}`);
});
```

In the sample code provided in this topic, this.context is used to obtain UIAbilityContext, where this indicates a UIAbility instance inherited from UIAbility. To use UIAbilityContext APIs on pages, see [Obtaining the Context of UIAbility](../../../application-models/uiability-usage.md#obtaining-the-context-of-uiability).

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the context within the component.
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let promise = contact.queryKey(context, 1, {
  holderId: 1,
  bundleName: "",
  displayName: ""
});
promise.then((data) => {
  console.info(`Succeeded in querying Key. data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to query Key. Code: ${err.code}, message: ${err.message}`);
});
```

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

let promise = contact.queryKey(1, {
  holderId: 1,
  bundleName: "",
  displayName: ""
});
promise.then((data) => {
  console.info(`Succeeded in querying Key. data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to query Key. Code: ${err.code}, message: ${err.message}`);
});
```


## queryKey

```TypeScript
function queryKey(context: Context, id: number, callback: AsyncCallback<string>): void
```

Queries the key of a contact based on the specified contact ID. This API uses an asynchronous callback to return the result.

**Since:** 10

**Required permissions:** ohos.permission.READ_CONTACTS

<!--Device-contact-function queryKey(context: Context, id: number, callback: AsyncCallback<string>): void--><!--Device-contact-function queryKey(context: Context, id: number, callback: AsyncCallback<string>): void-End-->

**System capability:** SystemCapability.Applications.ContactsData

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | Context | Yes | Indicates the context of application or capability. |
| id | number | Yes | Contact ID. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes | Indicates the callback for getting the result of the call. If the operation is successful, the key of the queried contact is returned. If the operation fails, an error code is returned. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [401](../errorcode-contacts.md#401-failed-to-open-the-contact-portrait-file) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |

**Examples**

See [queryKey](#querykey)


## queryKey

```TypeScript
function queryKey(id: number, holder: Holder, callback: AsyncCallback<string>): void
```

Queries the key of a contact based on the specified contact ID and holder. This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 10

**Substitutes:** [queryKey](#querykey)(context: Context, id: number, holder: Holder, callback: AsyncCallback&lt;string&gt;)

**Required permissions:** ohos.permission.READ_CONTACTS

<!--Device-contact-function queryKey(id: number, holder: Holder, callback: AsyncCallback<string>): void--><!--Device-contact-function queryKey(id: number, holder: Holder, callback: AsyncCallback<string>): void-End-->

**System capability:** SystemCapability.Applications.ContactsData

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| id | number | Yes | Contact ID. |
| holder | [Holder](arkts-contacts-contact-holder-c.md) | Yes | Application that creates the contacts.If the passed parameter is empty, the system contact application is used by default. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes | Indicates the callback for getting the result of the call. If the operation is successful, the key of the queried contact is returned. If the operation fails, an error code is returned. |

**Examples**

See [queryKey](#querykey)


## queryKey

```TypeScript
function queryKey(context: Context, id: number, holder: Holder, callback: AsyncCallback<string>): void
```

Queries the key of a contact based on the specified contact ID and holder. This API uses an asynchronous callback to return the result.

**Since:** 10

**Required permissions:** ohos.permission.READ_CONTACTS

<!--Device-contact-function queryKey(context: Context, id: number, holder: Holder, callback: AsyncCallback<string>): void--><!--Device-contact-function queryKey(context: Context, id: number, holder: Holder, callback: AsyncCallback<string>): void-End-->

**System capability:** SystemCapability.Applications.ContactsData

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | Context | Yes | Indicates the context of application or capability. |
| id | number | Yes | Contact ID. |
| holder | [Holder](arkts-contacts-contact-holder-c.md) | Yes | Application that creates the contacts.If the passed parameter is empty, the system contact application is used by default. |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;string&gt; | Yes | Indicates the callback for getting the result of the call. If the operation is successful, the key of the queried contact is returned. If the operation fails, an error code is returned. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [401](../errorcode-contacts.md#401-failed-to-open-the-contact-portrait-file) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |

**Examples**

See [queryKey](#querykey)


## queryKey

```TypeScript
function queryKey(id: number, holder?: Holder): Promise<string>
```

Queries the key of a contact based on the specified contact ID and holder. This API uses a promise to return the result.

**Since:** 7

**Deprecated since:** 10

**Substitutes:** [queryKey](#querykey)(context: Context, id: number, holder?: Holder)

**Required permissions:** ohos.permission.READ_CONTACTS

<!--Device-contact-function queryKey(id: number, holder?: Holder): Promise<string>--><!--Device-contact-function queryKey(id: number, holder?: Holder): Promise<string>-End-->

**System capability:** SystemCapability.Applications.ContactsData

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| id | number | Yes | Contact ID. |
| holder | [Holder](arkts-contacts-contact-holder-c.md) | No | Application information for a contact. If this parameter is not specified, the system contact application is used by default. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;string&gt; | Promise used to return the result, which is the key of the queried contact. |

**Examples**

See [queryKey](#querykey)


## queryKey

```TypeScript
function queryKey(context: Context, id: number, holder?: Holder): Promise<string>
```

Queries the key of a contact based on the specified contact ID and holder. This API uses a promise to return the result.

**Since:** 10

**Required permissions:** ohos.permission.READ_CONTACTS

<!--Device-contact-function queryKey(context: Context, id: number, holder?: Holder): Promise<string>--><!--Device-contact-function queryKey(context: Context, id: number, holder?: Holder): Promise<string>-End-->

**System capability:** SystemCapability.Applications.ContactsData

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| context | Context | Yes | Indicates the context of application or capability. |
| id | number | Yes | Contact ID. |
| holder | [Holder](arkts-contacts-contact-holder-c.md) | No | Application information for a contact. If this parameter is not specified, the system contact application is used by default. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;string&gt; | Promise used to return the result, which is the key of the queried contact. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [401](../errorcode-contacts.md#401-failed-to-open-the-contact-portrait-file) | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Parameter verification failed. |

**Examples**

See [queryKey](#querykey)

