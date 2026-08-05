# RequestOptions

Represents request options.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-photoAccessHelper-interface RequestOptions--><!--Device-photoAccessHelper-interface RequestOptions-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## compatibleMode

```TypeScript
compatibleMode?: CompatibleMode
```

HDR video transcoding policy, which can be **FAST\_ORIGINAL\_FORMAT\_MODE** (maintaining the original HDR format) or **COMPATIBLE\_FORMAT\_MODE** (converting HDR content to SDR format). The default value is **FAST\_ORIGINAL\_FORMAT\_MODE**.

**Type:** CompatibleMode

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 23.

<!--Device-RequestOptions-compatibleMode?: CompatibleMode--><!--Device-RequestOptions-compatibleMode?: CompatibleMode-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## deliveryMode

```TypeScript
deliveryMode: DeliveryMode
```

Delivery mode of the requested asset. The value can be **FAST\_MODE**, **HIGH\_QUALITY\_MODE**, or **BALANCE\_MODE**.

**Type:** DeliveryMode

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-RequestOptions-deliveryMode: DeliveryMode--><!--Device-RequestOptions-deliveryMode: DeliveryMode-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

## mediaAssetProgressHandler

```TypeScript
mediaAssetProgressHandler?: MediaAssetProgressHandler
```

Callback used to return the HDR-to-SDR conversion progress.

**Type:** MediaAssetProgressHandler

**Since:** 15

**ArkTS mode:** ArkTS-Dyn since version 15; ArkTS-Sta since version 23.

<!--Device-RequestOptions-mediaAssetProgressHandler?: MediaAssetProgressHandler--><!--Device-RequestOptions-mediaAssetProgressHandler?: MediaAssetProgressHandler-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

