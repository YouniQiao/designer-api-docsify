# PhotoViewPicker

图库选择器对象，用来支撑选择图片/视频和保存图片/视频等用户场景。选择文件推荐使用 [PhotoAccessHelper的PhotoViewPicker](../../apis-media-library-kit/arkts-apis/arkts-file-photoaccesshelper.md)。 在使用前，需要先创建PhotoViewPicker实例。

**起始版本：** 9

**废弃版本：** 12

**替代接口：** [PhotoViewPicker](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-photoviewpicker-c.md)

**系统能力：** SystemCapability.FileManagement.UserFileService

## 导入模块

```TypeScript
import { picker } from 'kits/@kit.CoreFileKit';
```

## constructor

```TypeScript
constructor()
```

**起始版本：** 12

**废弃版本：** 18

**替代接口：** [PhotoViewPicker](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-photoviewpicker-c.md)

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.FileManagement.UserFileService

## constructor

```TypeScript
constructor(context: Context)
```

**起始版本：** 12

**废弃版本：** 18

**替代接口：** [PhotoViewPicker](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-photoviewpicker-c.md)

**系统能力：** SystemCapability.FileManagement.UserFileService

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| context | [Context](../../apis-ability-kit/arkts-apis/arkts-ability-context-c.md) | 是 |

## save

```TypeScript
save(option?: PhotoSaveOptions): Promise<Array<string>>
```

通过保存模式拉起photoPicker界面，用户可以保存一个或多个图片/视频。接口采用Promise异步返回形式， 传入可选参数PhotoSaveOptions对象，返回保存文件的uri数组。

**起始版本：** 9

**废弃版本：** 12

**替代接口：** SaveButton

**系统能力：** SystemCapability.FileManagement.UserFileService

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| option | [PhotoSaveOptions](arkts-corefile-picker-photosaveoptions-c.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;Array & lt;string & gt; & gt; |

## save

```TypeScript
save(option: PhotoSaveOptions, callback: AsyncCallback<Array<string>>): void
```

通过保存模式拉起photoPicker界面，用户可以保存一个或多个图片/视频。接口采用callback异步返回形式， 传入参数PhotoSaveOptions对象，返回保存文件的uri数组。

**起始版本：** 9

**废弃版本：** 12

**替代接口：** SaveButton

**系统能力：** SystemCapability.FileManagement.UserFileService

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| option | [PhotoSaveOptions](arkts-corefile-picker-photosaveoptions-c.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;string&gt;&gt; | 是 |

## save

```TypeScript
save(callback: AsyncCallback<Array<string>>): void
```

通过保存模式拉起photoPicker界面，用户可以保存一个或多个图片/视频。接口采用callback异步返回形式，返回保存文件的uri数组。

**起始版本：** 9

**废弃版本：** 12

**替代接口：** SaveButton

**系统能力：** SystemCapability.FileManagement.UserFileService

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;string&gt;&gt; | 是 |

## select

```TypeScript
select(option?: PhotoSelectOptions): Promise<PhotoSelectResult>
```

通过选择模式拉起photoPicker界面，用户可以选择一个或多个图片/视频。接口采用Promise异步返回形式， 传入可选参数PhotoSelectOptions对象，返回PhotoSelectResult对象。

**起始版本：** 9

**废弃版本：** 12

**替代接口：** [select](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-photoviewpicker-c.md#select)(option?: PhotoSelectOptions)

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.FileManagement.UserFileService

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| option | [PhotoSelectOptions](arkts-corefile-picker-photoselectoptions-c.md) | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;PhotoSelectResult & gt; |

## select

```TypeScript
select(option: PhotoSelectOptions, callback: AsyncCallback<PhotoSelectResult>): void
```

通过选择模式拉起photoPicker界面，用户可以选择一个或多个图片/视频。接口采用callback异步返回形式， 传入参数PhotoSelectOptions对象，返回PhotoSelectResult对象。

**起始版本：** 9

**废弃版本：** 12

**替代接口：** [select](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-photoviewpicker-c.md#select)(option: PhotoSelectOptions, callback: AsyncCallback&lt;PhotoSelectResult&gt;)

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.FileManagement.UserFileService

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| option | [PhotoSelectOptions](arkts-corefile-picker-photoselectoptions-c.md) | 是 |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;PhotoSelectResult&gt; | 是 |

## select

```TypeScript
select(callback: AsyncCallback<PhotoSelectResult>): void
```

通过选择模式拉起photoPicker界面，用户可以选择一个或多个图片/视频。接口采用callback异步返回形式， 返回PhotoSelectResult对象。

**起始版本：** 9

**废弃版本：** 12

**替代接口：** [select](../../apis-media-library-kit/arkts-apis/arkts-medialibrary-photoaccesshelper-photoviewpicker-c.md#select)(callback: AsyncCallback&lt;PhotoSelectResult&gt;)

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

**系统能力：** SystemCapability.FileManagement.UserFileService

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;PhotoSelectResult&gt; | 是 |
