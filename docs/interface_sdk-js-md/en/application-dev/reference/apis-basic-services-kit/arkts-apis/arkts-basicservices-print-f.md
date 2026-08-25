# print

## Modules to Import

```TypeScript
import { print } from 'kits/@kit.BasicServicesKit';
```

## print

```TypeScript
function print(files: Array<string>, callback: AsyncCallback<PrintTask>): void
```

Prints files. This API uses an asynchronous callback to return the result. To start the system print preview page, call the [print](#print) API and pass in context.

**Since:** 10

**Deprecated since:** 26.0.0

**Substitutes:** [print](#print)

**Required permissions:** ohos.permission.PRINT

**System capability:** SystemCapability.Print.PrintFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| files | Array & lt;string & gt; | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;[PrintTask](arkts-basicservices-print-printtask-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |


## print

```TypeScript
function print(files: Array<string>): Promise<PrintTask>
```

Prints files. This API uses a promise to return the result. To start the system print preview page, call the [print](#print) API and pass in context.

**Since:** 10

**Deprecated since:** 26.0.0

**Substitutes:** [print](#print)

**Required permissions:** ohos.permission.PRINT

**System capability:** SystemCapability.Print.PrintFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| files | Array & lt;string & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[PrintTask](arkts-basicservices-print-printtask-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |


## print

```TypeScript
function print(files: Array<string>, context: Context, callback: AsyncCallback<PrintTask>): void
```

Prints files. This API uses an asynchronous callback to return the result.

**Since:** 11

**Required permissions:** ohos.permission.PRINT

**System capability:** SystemCapability.Print.PrintFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| files | Array & lt;string & gt; | Yes |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;[PrintTask](arkts-basicservices-print-printtask-i.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |


## print

```TypeScript
function print(files: Array<string>, context: Context): Promise<PrintTask>
```

Prints files. This API uses a promise to return the result.

**Since:** 11

**Required permissions:** ohos.permission.PRINT

**System capability:** SystemCapability.Print.PrintFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| files | Array & lt;string & gt; | Yes |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[PrintTask](arkts-basicservices-print-printtask-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |


## print

```TypeScript
function print(jobName: string, printAdapter: PrintDocumentAdapter, printAttributes: PrintAttributes,
    context: Context): Promise<PrintTask>
```

Prints a file. This API uses a promise to return the result.

**Since:** 11

**Required permissions:** ohos.permission.PRINT

**System capability:** SystemCapability.Print.PrintFramework

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| [jobName](arkts-basicservices-print-printjobdata-i.md) | string | Yes |
| printAdapter | [PrintDocumentAdapter](arkts-basicservices-print-printdocumentadapter-i.md) | Yes |
| printAttributes | [PrintAttributes](arkts-basicservices-print-printattributes-i.md) | Yes |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[PrintTask](arkts-basicservices-print-printtask-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
