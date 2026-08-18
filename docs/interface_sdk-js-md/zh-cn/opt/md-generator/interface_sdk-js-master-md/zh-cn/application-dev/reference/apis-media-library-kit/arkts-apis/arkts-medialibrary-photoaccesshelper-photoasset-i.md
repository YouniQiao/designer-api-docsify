# PhotoAsset

提供封装文件属性的方法。

**起始版本：** 23

<!--Device-photoAccessHelper-interface PhotoAsset--><!--Device-photoAccessHelper-interface PhotoAsset-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## 导入模块

```TypeScript
```

## clone

```TypeScript
clone(title: string): Promise<PhotoAsset>
```

克隆资产，可设置文件名，但不支持修改文件类型。使用promise异步回调。

**起始版本：** 23

**需要权限：** ohos.permission.WRITE_IMAGEVIDEO

<!--Device-PhotoAsset-clone(title: string): Promise<PhotoAsset>--><!--Device-PhotoAsset-clone(title: string): Promise<PhotoAsset>-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| title | string | 是 | 克隆后资产的标题。参数规格为： <br>- 不应包含扩展名。 <br>- 文件名字符串长度的取值范围为[1, 255]（资产文件名为标题+扩展名）。 <br>- 不允许出现的非法英文字符，包括：. \ / : ? " ' ` &lt; &gt; \|

**返回值：**

| 类型 |
| --- |
| Promise & lt;PhotoAsset & gt; |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| 14000011 |

## close

```TypeScript
close(fd: number, callback: AsyncCallback<void>): void
```

关闭当前文件。使用callback异步回调。

**起始版本：** 10

**废弃版本：** 11

**替代接口：** close

<!--Device-PhotoAsset-close(fd: number, callback: AsyncCallback<void>): void--><!--Device-PhotoAsset-close(fd: number, callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| fd | number | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 14000011 |

## close

```TypeScript
close(fd: number): Promise<void>
```

关闭当前文件。使用Promise异步回调。

**起始版本：** 10

**废弃版本：** 11

**替代接口：** close

<!--Device-PhotoAsset-close(fd: number): Promise<void>--><!--Device-PhotoAsset-close(fd: number): Promise<void>-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| fd | number | 是 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 14000011 |

## commitModify

```TypeScript
commitModify(callback: AsyncCallback<void>): void
```

修改文件的元数据。使用callback异步回调。

**起始版本：** 23

**需要权限：** ohos.permission.WRITE_IMAGEVIDEO

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-PhotoAsset-commitModify(callback: AsyncCallback<void>): void--><!--Device-PhotoAsset-commitModify(callback: AsyncCallback<void>): void-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 14000001 |
| 13900012 |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| 14000011 |

## commitModify

```TypeScript
commitModify(): Promise<void>
```

修改文件的元数据。使用Promise异步回调。

**起始版本：** 23

**需要权限：** ohos.permission.WRITE_IMAGEVIDEO

**原子化服务API：** 从API版本11开始，该接口支持在原子化服务API中使用。

<!--Device-PhotoAsset-commitModify(): Promise<void>--><!--Device-PhotoAsset-commitModify(): Promise<void>-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**返回值：**

| 类型 |
| --- |
| Promise & lt;void & gt; |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 14000001 |
| 13900012 |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| 14000011 |

## get

```TypeScript
get(member: string): MemberType
```

获取PhotoAsset成员参数的值。

**起始版本：** 23

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-PhotoAsset-get(member: string): MemberType--><!--Device-PhotoAsset-get(member: string): MemberType-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| member | string | 是 |

**返回值：**

| 类型 |
| --- |
| [MemberType](arkts-medialibrary-photoaccesshelper-membertype-t.md) |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| 14000014 |

## getReadOnlyFd

```TypeScript
getReadOnlyFd(callback: AsyncCallback<number>): void
```

以只读方式打开当前文件。使用callback异步回调。 使用完毕后调用close释放文件描述符。

**起始版本：** 10

**废弃版本：** 11

**替代接口：** open

**需要权限：** ohos.permission.READ_IMAGEVIDEO

<!--Device-PhotoAsset-getReadOnlyFd(callback: AsyncCallback<number>): void--><!--Device-PhotoAsset-getReadOnlyFd(callback: AsyncCallback<number>): void-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;number&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| 14000011 |

## getReadOnlyFd

```TypeScript
getReadOnlyFd(): Promise<number>
```

以只读方式打开当前文件。使用promise异步回调。 返回的文件描述符在使用完毕后需要调用close进行释放。

**起始版本：** 10

**废弃版本：** 11

**替代接口：** open

**需要权限：** ohos.permission.READ_IMAGEVIDEO

<!--Device-PhotoAsset-getReadOnlyFd(): Promise<number>--><!--Device-PhotoAsset-getReadOnlyFd(): Promise<number>-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**返回值：**

| 类型 |
| --- |
| Promise & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
| 14000011 |

## getThumbnail

```TypeScript
getThumbnail(callback: AsyncCallback<image.PixelMap>): void
```

获取文件的缩略图。使用callback异步回调。

**起始版本：** 23

**需要权限：** ohos.permission.READ_IMAGEVIDEO

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-PhotoAsset-getThumbnail(callback: AsyncCallback<image.PixelMap>): void--><!--Device-PhotoAsset-getThumbnail(callback: AsyncCallback<image.PixelMap>): void-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;image.PixelMap&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 13900012 |
| 14000011 |

## getThumbnail

```TypeScript
getThumbnail(size: image.Size, callback: AsyncCallback<image.PixelMap>): void
```

获取文件的缩略图，传入缩略图尺寸。使用callback异步回调。

**起始版本：** 23

**需要权限：** ohos.permission.READ_IMAGEVIDEO

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-PhotoAsset-getThumbnail(size: image.Size, callback: AsyncCallback<image.PixelMap>): void--><!--Device-PhotoAsset-getThumbnail(size: image.Size, callback: AsyncCallback<image.PixelMap>): void-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| size | image.Size | 是 |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;image.PixelMap&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 13900012 |
| 14000011 |

## getThumbnail

```TypeScript
getThumbnail(size?: image.Size): Promise<image.PixelMap>
```

获取文件的缩略图，传入缩略图尺寸。使用Promise异步回调。

**起始版本：** 23

**需要权限：** ohos.permission.READ_IMAGEVIDEO

**原子化服务API：** 从API版本22开始，该接口支持在原子化服务API中使用。

<!--Device-PhotoAsset-getThumbnail(size?: image.Size): Promise<image.PixelMap>--><!--Device-PhotoAsset-getThumbnail(size?: image.Size): Promise<image.PixelMap>-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| size | image.Size | 否 |

**返回值：**

| 类型 |
| --- |
| Promise & lt;image.PixelMap & gt; |

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 13900012 |
| 14000011 |

## set

```TypeScript
set(member: string, value: string): void
```

设置PhotoAsset成员参数。

**起始版本：** 23

<!--Device-PhotoAsset-set(member: string, value: string): void--><!--Device-PhotoAsset-set(member: string, value: string): void-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| member | string | 是 |
| value | string | 是 | 设置成员参数名称，只能修改 [PhotoKeys](arkts-medialibrary-photoaccesshelper-photokeys-e.md#photokeys).TITLE的值。title的参数规格为： <br>- 不应包含扩展名。 <br>- 文件名字符串长度的取值范围为[1, 255]（资产文件名为标题+扩展名）。 <br>- 不允许出现的非法英文字符，包括：. \ / : ? " ' ` &lt; &gt; \|

**错误码：**

| 错误码ID |
| --- |
| 13900020 |
| [401](../../errorcode-universal.md#401-参数检查失败) |
| 14000014 |

## displayName

```TypeScript
readonly displayName: string
```

显示文件名，包含后缀名。字符串长度的取值范围为[1, 255]。

**类型：** string

**起始版本：** 23

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-PhotoAsset-readonly displayName: string--><!--Device-PhotoAsset-readonly displayName: string-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## photoType

```TypeScript
readonly photoType: PhotoType
```

媒体文件类型。

**类型：** PhotoType

**起始版本：** 23

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-PhotoAsset-readonly photoType: PhotoType--><!--Device-PhotoAsset-readonly photoType: PhotoType-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## uri

```TypeScript
readonly uri: string
```

媒体文件资源URI（如：**file://media/Photo/1/IMG_datetime_0001/displayName.jpg**）， 详情参见用户文件URI介绍中的 [媒体文件URI](../../../file-management/user-file-uri-intro.md#media-file-uri).

**类型：** string

**起始版本：** 23

**原子化服务API：** 从API版本12开始，该接口支持在原子化服务API中使用。

<!--Device-PhotoAsset-readonly uri: string--><!--Device-PhotoAsset-readonly uri: string-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core
