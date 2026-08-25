# PhotoViewPicker

Provides APIs for selecting and saving images or videos. You are advised to use [PhotoViewPicker of PhotoAccessHelper](../../apis-media-library-kit/arkts-apis/arkts-file-photoaccesshelper.md) to select a file. Before using the APIs of **PhotoViewPicker**, you need to create a **PhotoViewPicker** instance.

**Since:** 9

**Deprecated since:** 12

**Substitutes:** [PhotoViewPicker](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-photoviewpicker-c.md)

**System capability:** SystemCapability.FileManagement.UserFileService

## Modules to Import

```TypeScript
import { picker } from 'kits/@kit.CoreFileKit';
```

## constructor

```TypeScript
constructor()
```

A constructor used to create a PhotoViewPicker instance. This constructor is not recommended due to the potential risk of operation failure.

**Since:** 12

**Deprecated since:** 18

**Substitutes:** [PhotoViewPicker](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-photoviewpicker-c.md)

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.FileManagement.UserFileService

## constructor

```TypeScript
constructor(context: Context)
```

A constructor used to create a PhotoViewPicker instance. This constructor is recommended. For details about how to obtain the context, see [getHostContext](../../apis-arkui/arkts-apis/arkts-arkui-arkui-uicontext-uicontext-c.md#gethostcontext).

**Since:** 12

**Deprecated since:** 18

**Substitutes:** [PhotoViewPicker](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-photoviewpicker-c.md)

**System capability:** SystemCapability.FileManagement.UserFileService

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | Yes |

## save

```TypeScript
save(option?: PhotoSaveOptions): Promise<Array<string>>
```

Starts a **photoPicker** page for the user to save one or more images or videos. This API uses a promise to return the result. You can pass in **PhotoSaveOptions** to specify the URIs of the images or videos to save.

**Since:** 9

**Deprecated since:** 12

**Substitutes:** SaveButton

**System capability:** SystemCapability.FileManagement.UserFileService

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| option | [PhotoSaveOptions](arkts-corefile-picker-photosaveoptions-c.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;Array & lt;string & gt; & gt; |

## save

```TypeScript
save(option: PhotoSaveOptions, callback: AsyncCallback<Array<string>>): void
```

Starts a **photoPicker** page for the user to save one or more images or videos. This API uses an asynchronous callback to return the result. You can pass in **PhotoSaveOptions** to specify the URIs of the images or videos to save.

**Since:** 9

**Deprecated since:** 12

**Substitutes:** SaveButton

**System capability:** SystemCapability.FileManagement.UserFileService

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| option | [PhotoSaveOptions](arkts-corefile-picker-photosaveoptions-c.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;string&gt;&gt; | Yes |

## save

```TypeScript
save(callback: AsyncCallback<Array<string>>): void
```

Starts a **photoPicker** page for the user to save one or more images or videos. This API uses an asynchronous callback to return the URIs of the images or videos to save.

**Since:** 9

**Deprecated since:** 12

**Substitutes:** SaveButton

**System capability:** SystemCapability.FileManagement.UserFileService

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;string&gt;&gt; | Yes |

## select

```TypeScript
select(option?: PhotoSelectOptions): Promise<PhotoSelectResult>
```

Starts a **photoPicker** page for the user to select one or more images or videos. This API uses a promise to return the result. You can pass in **PhotoSelectOptions** to specify the type and maximum number of the files to select.

**Since:** 9

**Deprecated since:** 12

**Substitutes:** [select](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-photoviewpicker-c.md#select)(option?: PhotoSelectOptions)

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.FileManagement.UserFileService

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| option | [PhotoSelectOptions](arkts-corefile-picker-photoselectoptions-c.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;PhotoSelectResult & gt; |

## select

```TypeScript
select(option: PhotoSelectOptions, callback: AsyncCallback<PhotoSelectResult>): void
```

Starts a **photoPicker** page for the user to select one or more images or videos. This API uses an asynchronous callback to return the result. You can pass in **PhotoSelectOptions** to specify the type and maximum number of the files to select.

**Since:** 9

**Deprecated since:** 12

**Substitutes:** [select](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-photoviewpicker-c.md#select)(option: PhotoSelectOptions, callback: AsyncCallback&lt;PhotoSelectResult&gt;)

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.FileManagement.UserFileService

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| option | [PhotoSelectOptions](arkts-corefile-picker-photoselectoptions-c.md) | Yes |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;PhotoSelectResult&gt; | Yes |

## select

```TypeScript
select(callback: AsyncCallback<PhotoSelectResult>): void
```

Starts a **photoPicker** page for the user to select one or more images or videos. This API uses an asynchronous callback to return the result.

**Since:** 9

**Deprecated since:** 12

**Substitutes:** [select](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-photoviewpicker-c.md#select)(callback: AsyncCallback&lt;PhotoSelectResult&gt;)

**Atomic service API:** This API can be used in atomic services since API version 11.

**System capability:** SystemCapability.FileManagement.UserFileService

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;PhotoSelectResult&gt; | Yes |
