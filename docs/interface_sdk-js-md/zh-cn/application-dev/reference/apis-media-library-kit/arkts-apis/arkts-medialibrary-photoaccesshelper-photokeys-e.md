# PhotoKeys

Defines the key information about an image or video file.

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

<!--Device-photoAccessHelper-enum PhotoKeys--><!--Device-photoAccessHelper-enum PhotoKeys-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## URI

```TypeScript
URI = 'uri'
```

URI of the file.

**Note：**:

Only the   
[DataSharePredicates.equalTo](../../apis-arkdata/arkts-apis/arkts-arkdata-datasharepredicates-datasharepredicates-c.md/arkts-arkdata-datasharepredicates-datasharepredicates-c.md#equalto)predicate can be used for this field during photo query.

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-PhotoKeys-URI = 'uri'--><!--Device-PhotoKeys-URI = 'uri'-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## PHOTO_TYPE

```TypeScript
PHOTO_TYPE = 'media_type'
```

Type of the file.

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-PhotoKeys-PHOTO_TYPE = 'media_type'--><!--Device-PhotoKeys-PHOTO_TYPE = 'media_type'-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## DISPLAY_NAME

```TypeScript
DISPLAY_NAME = 'display_name'
```

File name displayed. The file name must meet the following requirements:

- A valid file name must include a base name and a supported image or video extension.  
- The file name length ranges from 1 to 255.  
- The base name must not contain any invalid characters, which are:.. \ / : * ? " ' ` &lt; &gt; | { } [ ]

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-PhotoKeys-DISPLAY_NAME = 'display_name'--><!--Device-PhotoKeys-DISPLAY_NAME = 'display_name'-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## SIZE

```TypeScript
SIZE = 'size'
```

File size, in bytes. The size of a moving photo includes the total size of the image and video.

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-PhotoKeys-SIZE = 'size'--><!--Device-PhotoKeys-SIZE = 'size'-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## DATE_ADDED

```TypeScript
DATE_ADDED = 'date_added'
```

Unix timestamp when the file was created, in seconds.

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-PhotoKeys-DATE_ADDED = 'date_added'--><!--Device-PhotoKeys-DATE_ADDED = 'date_added'-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## DATE_MODIFIED

```TypeScript
DATE_MODIFIED = 'date_modified'
```

Unix timestamp when the file content (not the file name) was last modified, in seconds. This value is updated when the file content is modified, but not when the file name is modified.

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-PhotoKeys-DATE_MODIFIED = 'date_modified'--><!--Device-PhotoKeys-DATE_MODIFIED = 'date_modified'-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## DURATION

```TypeScript
DURATION = 'duration'
```

Duration, in ms.

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-PhotoKeys-DURATION = 'duration'--><!--Device-PhotoKeys-DURATION = 'duration'-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## WIDTH

```TypeScript
WIDTH = 'width'
```

Image width, in pixels.

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-PhotoKeys-WIDTH = 'width'--><!--Device-PhotoKeys-WIDTH = 'width'-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## HEIGHT

```TypeScript
HEIGHT = 'height'
```

Image height, in pixels.

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-PhotoKeys-HEIGHT = 'height'--><!--Device-PhotoKeys-HEIGHT = 'height'-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## DATE_TAKEN

```TypeScript
DATE_TAKEN = 'date_taken'
```

Unix timestamp when the photo was taken, in seconds.

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-PhotoKeys-DATE_TAKEN = 'date_taken'--><!--Device-PhotoKeys-DATE_TAKEN = 'date_taken'-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## ORIENTATION

```TypeScript
ORIENTATION = 'orientation'
```

Orientation of the file, in degrees.

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-PhotoKeys-ORIENTATION = 'orientation'--><!--Device-PhotoKeys-ORIENTATION = 'orientation'-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## FAVORITE

```TypeScript
FAVORITE = 'is_favorite'
```

Whether the file is marked as favorites.

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-PhotoKeys-FAVORITE = 'is_favorite'--><!--Device-PhotoKeys-FAVORITE = 'is_favorite'-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## TITLE

```TypeScript
TITLE = 'title'
```

Title of the file.

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-PhotoKeys-TITLE = 'title'--><!--Device-PhotoKeys-TITLE = 'title'-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## POSITION

```TypeScript
POSITION = 'position'
```

File location type.

**起始版本：** 16

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-PhotoKeys-POSITION = 'position'--><!--Device-PhotoKeys-POSITION = 'position'-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## DATE_ADDED_MS

```TypeScript
DATE_ADDED_MS = 'date_added_ms'
```

Unix timestamp when the file was created, in milliseconds.

**Note：**:

The photos queried cannot be sorted based on this field.

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-PhotoKeys-DATE_ADDED_MS = 'date_added_ms'--><!--Device-PhotoKeys-DATE_ADDED_MS = 'date_added_ms'-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## DATE_MODIFIED_MS

```TypeScript
DATE_MODIFIED_MS = 'date_modified_ms'
```

Unix timestamp when the file was modified, in milliseconds. This value is updated when the file content is modified, but not when the file name is modified.

**Note：**:

The photos queried cannot be sorted based on this field.

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-PhotoKeys-DATE_MODIFIED_MS = 'date_modified_ms'--><!--Device-PhotoKeys-DATE_MODIFIED_MS = 'date_modified_ms'-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## PHOTO_SUBTYPE

```TypeScript
PHOTO_SUBTYPE = 'subtype'
```

Subtype of the media file.

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-PhotoKeys-PHOTO_SUBTYPE = 'subtype'--><!--Device-PhotoKeys-PHOTO_SUBTYPE = 'subtype'-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## DYNAMIC_RANGE_TYPE

```TypeScript
DYNAMIC_RANGE_TYPE = 'dynamic_range_type'
```

Dynamic range type of the media asset.

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-PhotoKeys-DYNAMIC_RANGE_TYPE = 'dynamic_range_type'--><!--Device-PhotoKeys-DYNAMIC_RANGE_TYPE = 'dynamic_range_type'-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## COVER_POSITION

```TypeScript
COVER_POSITION = 'cover_position'
```

Position of the moving photo cover, which is the video timestamp (in μs) corresponding to the cover frame.

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-PhotoKeys-COVER_POSITION = 'cover_position'--><!--Device-PhotoKeys-COVER_POSITION = 'cover_position'-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## BURST_KEY

```TypeScript
BURST_KEY = 'burst_key'
```

Unique ID of a group of burst photos.

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-PhotoKeys-BURST_KEY = 'burst_key'--><!--Device-PhotoKeys-BURST_KEY = 'burst_key'-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## LCD_SIZE

```TypeScript
LCD_SIZE = 'lcd_size'
```

Width and height of an LCD image, in the format of a **width:height** string.

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-PhotoKeys-LCD_SIZE = 'lcd_size'--><!--Device-PhotoKeys-LCD_SIZE = 'lcd_size'-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## THM_SIZE

```TypeScript
THM_SIZE = 'thm_size'
```

Width and height of a thumbnail image, in the format of a **width:height** string.

**起始版本：** 12

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-PhotoKeys-THM_SIZE = 'thm_size'--><!--Device-PhotoKeys-THM_SIZE = 'thm_size'-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## DETAIL_TIME

```TypeScript
DETAIL_TIME = 'detail_time'
```

Detailed time. The value is a string of time when the image or video was taken in the time zone and does not change with the time zone.

**起始版本：** 13

**ArkTS模式：** ArkTS-Dyn起始版本为13；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-PhotoKeys-DETAIL_TIME = 'detail_time'--><!--Device-PhotoKeys-DETAIL_TIME = 'detail_time'-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## DATE_TAKEN_MS

```TypeScript
DATE_TAKEN_MS = 'date_taken_ms'
```

Unix timestamp when the image was captured, in milliseconds.

**起始版本：** 13

**ArkTS模式：** ArkTS-Dyn起始版本为13；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-PhotoKeys-DATE_TAKEN_MS = 'date_taken_ms'--><!--Device-PhotoKeys-DATE_TAKEN_MS = 'date_taken_ms'-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## OWNER_ALBUM_ID

```TypeScript
OWNER_ALBUM_ID = 'owner_album_id'
```

ID of the album to which the photo belongs.

**起始版本：** 22

**ArkTS模式：** ArkTS-Dyn起始版本为18；ArkTS-Sta起始版本为23。

<!--Device-PhotoKeys-OWNER_ALBUM_ID = 'owner_album_id'--><!--Device-PhotoKeys-OWNER_ALBUM_ID = 'owner_album_id'-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## MEDIA_SUFFIX

```TypeScript
MEDIA_SUFFIX = 'media_suffix'
```

File name extension.

**起始版本：** 18

**ArkTS模式：** ArkTS-Dyn起始版本为18；ArkTS-Sta起始版本为23。

<!--Device-PhotoKeys-MEDIA_SUFFIX = 'media_suffix'--><!--Device-PhotoKeys-MEDIA_SUFFIX = 'media_suffix'-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## ASPECT_RATIO

```TypeScript
ASPECT_RATIO = 'aspect_ratio'
```

Aspect ratio of the image or video.

**起始版本：** 22

**ArkTS模式：** ArkTS-Dyn起始版本为22；ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PhotoKeys-ASPECT_RATIO = 'aspect_ratio'--><!--Device-PhotoKeys-ASPECT_RATIO = 'aspect_ratio'-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## CHANGE_TIME

```TypeScript
CHANGE_TIME = 'change_time'
```

Time when the photo is changed.

**起始版本：** 23

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为23。

<!--Device-PhotoKeys-CHANGE_TIME = 'change_time'--><!--Device-PhotoKeys-CHANGE_TIME = 'change_time'-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

## LOCAL_ASSET_SIZE

```TypeScript
LOCAL_ASSET_SIZE = 'local_asset_size'
```

Size of local asset, which well matched the content read by the application.

**起始版本：** 26.0.0

**ArkTS模式：** 同时支持ArkTS-Dyn、ArkTS-Sta，起始版本为26.0.0。

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-PhotoKeys-LOCAL_ASSET_SIZE = 'local_asset_size'--><!--Device-PhotoKeys-LOCAL_ASSET_SIZE = 'local_asset_size'-End-->

**系统能力：** SystemCapability.FileManagement.PhotoAccessHelper.Core

