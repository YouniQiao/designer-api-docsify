# MediaAssetDataHandler

MediaAssetDataHandler is a media asset handler used to customize the media asset processing logic in **onDataPrepared**.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-photoAccessHelper-interface MediaAssetDataHandler<T>--><!--Device-photoAccessHelper-interface MediaAssetDataHandler<T>-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## onDataPrepared

```TypeScript
onDataPrepared(data: T, map?: Map<string, string>): void
```

Called when the requested media asset is ready. If an error occurs, **data** returned by the callback is **undefined**. Each media asset request corresponds to a callback. T supports the following data types: ArrayBuffer, [ImageSource]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_, [MovingPhoto]\_\_\_JSDOC\_LINK\_DESC\_USD\_1\_\_\_, and boolean. ArrayBuffer indicates the image or video asset data, [ImageSource]\_\_\_JSDOC\_LINK\_DESC\_USD\_2\_\_\_ indicates the image source, [MovingPhoto]\_\_\_JSDOC\_LINK\_DESC\_USD\_3\_\_\_ indicates a moving photo object, and boolean indicates whether the image or video is successfully written to the application sandbox directory. Information returned by **map**: | Map Key | Description| |----------|-------| | 'quality' | Image quality. The value **high** means high quality, and **low** means poor quality.|

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

<!--Device-MediaAssetDataHandler-onDataPrepared(data: T, map?: Map<string, string>): void--><!--Device-MediaAssetDataHandler-onDataPrepared(data: T, map?: Map<string, string>): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | T | Yes | Data of the image asset that is ready. It is of the generic type and supports the following data types: ArrayBuffer, [ImageSource]\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_,[MovingPhoto]\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_JSDOC\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_1\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_, and boolean. |
| map | Map&lt;string, string&gt; | No | Additional information about the image asset, such as the image quality.Currently, only **quality** is supported.\_\_\_HTML\_TAG\_USD\_0\_\_\_**Since:** 12 |

## onDataPrepared

```TypeScript
onDataPrepared(data: T | undefined, map?: Map<string, string>): void
```

Indicates required media asset data is prepared

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-MediaAssetDataHandler-onDataPrepared(data: T | undefined, map?: Map<string, string>): void--><!--Device-MediaAssetDataHandler-onDataPrepared(data: T | undefined, map?: Map<string, string>): void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| data | T \| undefined | Yes | the returned data of media asset if data of media asset is invalid, return undefined. |
| map | Map&lt;string, string&gt; | No | additional information for the data |

