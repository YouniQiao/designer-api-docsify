# DocumentViewPicker

Provides APIs for selecting and saving documents in different formats. Before using the APIs of **DocumentViewPicker**, you need to create a **DocumentViewPicker** instance.

**Since:** 9

**System capability:** SystemCapability.FileManagement.UserFileService

## Modules to Import

```TypeScript
import { picker } from 'kits/@kit.CoreFileKit';
```

## constructor

```TypeScript
constructor()
```

A constructor used to create a **DocumentViewPicker** instance. This constructor is not recommended due to the potential risk of operation failure.

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.FileManagement.UserFileService

## constructor

```TypeScript
constructor(context: Context)
```

A constructor used to create a **DocumentViewPicker** instance. This constructor is recommended. For details about how to obtain the context, see [getHostContext](../../../reference/apis-arkui/arkts-apis-uicontext-uicontext.md#gethostcontext).

**Since:** 12

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.FileManagement.UserFileService

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | Yes |

## constructor

```TypeScript
constructor(context: Context, window: window.Window)
```

A constructor used to create a **DocumentViewPicker** object in a window created by an application. In other scenarios, you are advised to use **constructor(context: Context)** to create a **DocumentViewPicker** object.

> **NOTE：**&gt;
> This method is supported on 2-in-1 devices and tablets since API version 19.

**Since:** 13

**System capability:** SystemCapability.FileManagement.UserFileService

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | Yes |
| [window](../../apis-arkui/arkts-apis/arkts-arkui-window-n.md) | window.Window | Yes |

## getSelectedIndex

```TypeScript
getSelectedIndex(): number
```

Obtains the index of the file suffix type of the file saved. This method takes effect only when used with [save()](#save). This method can be used only after [DocumentSaveOptions.fileSuffixChoices](arkts-corefile-picker-documentsaveoptions-c.md) is configured. The index (number) returned by this method indicates the location of the file suffix specified in [DocumentSaveOptions.fileSuffixChoices](arkts-corefile-picker-documentsaveoptions-c.md). If no file suffix is specified, **getSelectedIndex()** returns **-1**.

**Since:** 14

**Atomic service API:** This API can be used in atomic services since API version 14.

**System capability:** SystemCapability.FileManagement.UserFileService.FolderSelection

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

## save

```TypeScript
save(option?: DocumentSaveOptions): Promise<Array<string>>
```

Starts a **documentPicker** page for the user to save one or more documents. This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.FileManagement.UserFileService

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| option | [DocumentSaveOptions](arkts-corefile-picker-documentsaveoptions-c.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Array & lt;string & gt; & gt; |

## save

```TypeScript
save(option: DocumentSaveOptions, callback: AsyncCallback<Array<string>>): void
```

Starts a **documentPicker** page for the user to save one or more documents. This API uses an asynchronous callback to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.FileManagement.UserFileService

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| option | [DocumentSaveOptions](arkts-corefile-picker-documentsaveoptions-c.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;string&gt;&gt; | Yes |

## save

```TypeScript
save(callback: AsyncCallback<Array<string>>): void
```

Starts a **documentPicker** page for the user to save one or more documents. This API uses an asynchronous callback to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.FileManagement.UserFileService

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;string&gt;&gt; | Yes |

## select

```TypeScript
select(option?: DocumentSelectOptions): Promise<Array<string>>
```

Starts a **documentPicker** page for the user to select one or more documents. This API uses a promise to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.FileManagement.UserFileService

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| option | [DocumentSelectOptions](arkts-corefile-picker-documentselectoptions-c.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Array & lt;string & gt; & gt; |

## select

```TypeScript
select(option: DocumentSelectOptions, callback: AsyncCallback<Array<string>>): void
```

Starts a **documentPicker** page for the user to select one or more documents. This API uses an asynchronous callback to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.FileManagement.UserFileService

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| option | [DocumentSelectOptions](arkts-corefile-picker-documentselectoptions-c.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;string&gt;&gt; | Yes |

## select

```TypeScript
select(callback: AsyncCallback<Array<string>>): void
```

Starts a **documentPicker** page for the user to select one or more documents. This API uses an asynchronous callback to return the result.

**Since:** 9

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.FileManagement.UserFileService

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;string&gt;&gt; | Yes |
