# Album

Provides APIs to manage albums.

**Inheritance/Implementation:** Album extends [AbsAlbum](arkts-medialibrary-photoaccesshelper-absalbum-i.md#absalbum)

**Since:** 23

<!--Device-photoAccessHelper-interface Album--><!--Device-photoAccessHelper-interface Album-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## Modules to Import

```TypeScript
```

## addAssets

```TypeScript
addAssets(assets: Array<PhotoAsset>, callback: AsyncCallback<void>): void
```

Adds image and video assets to a user album. Before the operation, ensure that the image and video assets to add and the album exist. This API uses an asynchronous callback to return the result.

**Since:** 10

**Deprecated since:** 11

**Substitutes:** [addAssets](arkts-medialibrary-photoaccesshelper-mediaalbumchangerequest-c.md#addassets)

**Required permissions:** ohos.permission.WRITE_IMAGEVIDEO

<!--Device-Album-addAssets(assets: Array<PhotoAsset>, callback: AsyncCallback<void>): void--><!--Device-Album-addAssets(assets: Array<PhotoAsset>, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| assets | Array & lt;PhotoAsset & gt; | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| 14000011 |

## addAssets

```TypeScript
addAssets(assets: Array<PhotoAsset>): Promise<void>
```

Adds image and video assets to a user album. Before the operation, ensure that the image and video assets to add and the album exist. This API uses a promise to return the result.

**Since:** 10

**Deprecated since:** 11

**Substitutes:** [addAssets](arkts-medialibrary-photoaccesshelper-mediaalbumchangerequest-c.md#addassets)

**Required permissions:** ohos.permission.WRITE_IMAGEVIDEO

<!--Device-Album-addAssets(assets: Array<PhotoAsset>): Promise<void>--><!--Device-Album-addAssets(assets: Array<PhotoAsset>): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| assets | Array & lt;PhotoAsset & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| 14000011 |

## commitModify

```TypeScript
commitModify(callback: AsyncCallback<void>): void
```

Commits the modification on the album attributes to the database. This API uses an asynchronous callback to return the result.

**Since:** 23

**Required permissions:** ohos.permission.WRITE_IMAGEVIDEO

<!--Device-Album-commitModify(callback: AsyncCallback<void>): void--><!--Device-Album-commitModify(callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| 14000011 |

## commitModify

```TypeScript
commitModify(): Promise<void>
```

Commits the modification on the album attributes to the database. This API uses a promise to return the result.

**Since:** 23

**Required permissions:** ohos.permission.WRITE_IMAGEVIDEO

<!--Device-Album-commitModify(): Promise<void>--><!--Device-Album-commitModify(): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| 14000011 |

## removeAssets

```TypeScript
removeAssets(assets: Array<PhotoAsset>, callback: AsyncCallback<void>): void
```

Removes image and video assets from a user album. The album and file resources must exist. This API uses an asynchronous callback to return the result.

**Since:** 10

**Deprecated since:** 11

**Substitutes:** [removeAssets](arkts-medialibrary-photoaccesshelper-mediaalbumchangerequest-c.md#removeassets)

**Required permissions:** ohos.permission.WRITE_IMAGEVIDEO

<!--Device-Album-removeAssets(assets: Array<PhotoAsset>, callback: AsyncCallback<void>): void--><!--Device-Album-removeAssets(assets: Array<PhotoAsset>, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| assets | Array & lt;PhotoAsset & gt; | Yes |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| 14000011 |

## removeAssets

```TypeScript
removeAssets(assets: Array<PhotoAsset>): Promise<void>
```

Removes image and video assets from a user album. The album and file resources must exist. This API uses a promise to return the result.

**Since:** 10

**Deprecated since:** 11

**Substitutes:** [removeAssets](arkts-medialibrary-photoaccesshelper-mediaalbumchangerequest-c.md#removeassets)

**Required permissions:** ohos.permission.WRITE_IMAGEVIDEO

<!--Device-Album-removeAssets(assets: Array<PhotoAsset>): Promise<void>--><!--Device-Album-removeAssets(assets: Array<PhotoAsset>): Promise<void>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| assets | Array & lt;PhotoAsset & gt; | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| 13900020 |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| 14000011 |

## imageCount

```TypeScript
readonly imageCount?: number
```

Number of images in the album.

**Type:** number

**Since:** 23

<!--Device-Album-readonly imageCount?: int--><!--Device-Album-readonly imageCount?: int-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## videoCount

```TypeScript
readonly videoCount?: number
```

Number of videos in the album.

**Type:** number

**Since:** 23

<!--Device-Album-readonly videoCount?: int--><!--Device-Album-readonly videoCount?: int-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core
