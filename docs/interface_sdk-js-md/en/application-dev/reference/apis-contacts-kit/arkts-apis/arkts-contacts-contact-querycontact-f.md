# queryContact

## Modules to Import

```TypeScript
import { contact } from 'kits/@kit.ContactsKit';
```

## queryContact

```TypeScript
function queryContact(key: string, callback: AsyncCallback<Contact>): void
```

Queries a contact based on the specified key. This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 10

**Substitutes:** [queryContact](#querycontact)(context: Context, key: string, callback: AsyncCallback&lt;Contact&gt;)

**Required permissions:** ohos.permission.READ_CONTACTS

**System capability:** SystemCapability.Applications.ContactsData

**Parameters:**

| [Name](arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | string | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[Contact](arkts-contacts-contact-contact-c.md)&gt; | Yes |


## queryContact

```TypeScript
function queryContact(context: Context, key: string, callback: AsyncCallback<Contact>): void
```

Queries a contact based on the specified key. This API uses an asynchronous callback to return the result.

**Since:** 10

**Required permissions:** ohos.permission.READ_CONTACTS

**System capability:** SystemCapability.Applications.ContactsData

**Parameters:**

| [Name](arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [Context](../../apis-mind-spore-lite-kit/arkts-apis/arkts-mindsporelite-mindsporelite-context-i.md) | Yes |
| key | string | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[Contact](arkts-contacts-contact-contact-c.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../errorcode-contacts.md#401-failed-to-open-the-contact-portrait-file) |


## queryContact

```TypeScript
function queryContact(key: string, holder: Holder, callback: AsyncCallback<Contact>): void
```

Queries a contact based on the specified key and holder. This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 10

**Substitutes:** [queryContact](#querycontact)(context: Context, key: string, holder: Holder, callback: AsyncCallback&lt;Contact&gt;)

**Required permissions:** ohos.permission.READ_CONTACTS

**System capability:** SystemCapability.Applications.ContactsData

**Parameters:**

| [Name](arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | string | Yes |
| holder | [Holder](arkts-contacts-contact-holder-c.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[Contact](arkts-contacts-contact-contact-c.md)&gt; | Yes |


## queryContact

```TypeScript
function queryContact(context: Context, key: string, holder: Holder, callback: AsyncCallback<Contact>): void
```

Queries a contact based on the specified key and holder. This API uses an asynchronous callback to return the result.

**Since:** 10

**Required permissions:** ohos.permission.READ_CONTACTS

**System capability:** SystemCapability.Applications.ContactsData

**Parameters:**

| [Name](arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [Context](../../apis-mind-spore-lite-kit/arkts-apis/arkts-mindsporelite-mindsporelite-context-i.md) | Yes |
| key | string | Yes |
| holder | [Holder](arkts-contacts-contact-holder-c.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[Contact](arkts-contacts-contact-contact-c.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../errorcode-contacts.md#401-failed-to-open-the-contact-portrait-file) |


## queryContact

```TypeScript
function queryContact(key: string, attrs: ContactAttributes, callback: AsyncCallback<Contact>): void
```

Queries a contact based on the specified key and attributes. This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 10

**Substitutes:** [queryContact](#querycontact)(context: Context, key: string, attrs: ContactAttributes, callback: AsyncCallback&lt;Contact&gt;)

**Required permissions:** ohos.permission.READ_CONTACTS

**System capability:** SystemCapability.Applications.ContactsData

**Parameters:**

| [Name](arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | string | Yes |
| attrs | [ContactAttributes](arkts-contacts-contact-contactattributes-c.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[Contact](arkts-contacts-contact-contact-c.md)&gt; | Yes |


## queryContact

```TypeScript
function queryContact(context: Context, key: string, attrs: ContactAttributes, callback: AsyncCallback<Contact>): void
```

Queries a contact based on the specified key and attributes. This API uses an asynchronous callback to return the result.

**Since:** 10

**Required permissions:** ohos.permission.READ_CONTACTS

**System capability:** SystemCapability.Applications.ContactsData

**Parameters:**

| [Name](arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [Context](../../apis-mind-spore-lite-kit/arkts-apis/arkts-mindsporelite-mindsporelite-context-i.md) | Yes |
| key | string | Yes |
| attrs | [ContactAttributes](arkts-contacts-contact-contactattributes-c.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[Contact](arkts-contacts-contact-contact-c.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../errorcode-contacts.md#401-failed-to-open-the-contact-portrait-file) |


## queryContact

```TypeScript
function queryContact(key: string, holder: Holder, attrs: ContactAttributes, callback: AsyncCallback<Contact>): void
```

Queries a contact based on the specified key, holder, and attributes. This API uses an asynchronous callback to return the result.

**Since:** 7

**Deprecated since:** 10

**Substitutes:** [queryContact](#querycontact)(context: Context, key: string, holder: Holder, attrs: ContactAttributes, callback: AsyncCallback&lt;Contact&gt;)

**Required permissions:** ohos.permission.READ_CONTACTS

**System capability:** SystemCapability.Applications.ContactsData

**Parameters:**

| [Name](arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | string | Yes |
| holder | [Holder](arkts-contacts-contact-holder-c.md) | Yes |
| attrs | [ContactAttributes](arkts-contacts-contact-contactattributes-c.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[Contact](arkts-contacts-contact-contact-c.md)&gt; | Yes |


## queryContact

```TypeScript
function queryContact(context: Context, key: string, holder: Holder, attrs: ContactAttributes, callback: AsyncCallback<Contact>): void
```

Queries a contact based on the specified key, holder, and attributes. This API uses an asynchronous callback to return the result.

**Since:** 10

**Required permissions:** ohos.permission.READ_CONTACTS

**System capability:** SystemCapability.Applications.ContactsData

**Parameters:**

| [Name](arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [Context](../../apis-mind-spore-lite-kit/arkts-apis/arkts-mindsporelite-mindsporelite-context-i.md) | Yes |
| key | string | Yes |
| holder | [Holder](arkts-contacts-contact-holder-c.md) | Yes |
| attrs | [ContactAttributes](arkts-contacts-contact-contactattributes-c.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[Contact](arkts-contacts-contact-contact-c.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../errorcode-contacts.md#401-failed-to-open-the-contact-portrait-file) |


## queryContact

```TypeScript
function queryContact(key: string, holder?: Holder, attrs?: ContactAttributes): Promise<Contact>
```

Queries a contact based on the specified key, holder, and attributes. This API uses a promise to return the result.

**Since:** 7

**Deprecated since:** 10

**Substitutes:** [queryContact](#querycontact)(context: Context, key: string, holder?: Holder, attrs?: ContactAttributes)

**Required permissions:** ohos.permission.READ_CONTACTS

**System capability:** SystemCapability.Applications.ContactsData

**Parameters:**

| [Name](arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| key | string | Yes |
| holder | [Holder](arkts-contacts-contact-holder-c.md) | No |
| attrs | [ContactAttributes](arkts-contacts-contact-contactattributes-c.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[Contact](arkts-contacts-contact-contact-c.md)&gt; |


## queryContact

```TypeScript
function queryContact(context: Context, key: string, holder?: Holder, attrs?: ContactAttributes): Promise<Contact>
```

Queries a contact based on the specified key, holder, and attributes. This API uses a promise to return the result.

**Since:** 10

**Required permissions:** ohos.permission.READ_CONTACTS

**System capability:** SystemCapability.Applications.ContactsData

**Parameters:**

| [Name](arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [Context](../../apis-mind-spore-lite-kit/arkts-apis/arkts-mindsporelite-mindsporelite-context-i.md) | Yes |
| key | string | Yes |
| holder | [Holder](arkts-contacts-contact-holder-c.md) | No |
| attrs | [ContactAttributes](arkts-contacts-contact-contactattributes-c.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[Contact](arkts-contacts-contact-contact-c.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../errorcode-contacts.md#401-failed-to-open-the-contact-portrait-file) |
