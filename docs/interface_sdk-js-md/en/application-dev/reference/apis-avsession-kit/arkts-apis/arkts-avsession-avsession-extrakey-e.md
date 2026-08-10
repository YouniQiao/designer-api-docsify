# ExtraKey

表示定义在不同场景中使用的额外键的枚举。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-avSession-enum ExtraKey--><!--Device-avSession-enum ExtraKey-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

## REQUIRE_ABILITY_LIST

```TypeScript
REQUIRE_ABILITY_LIST = 'requireAbilityList'
```

作为[setExtras](arkts-avsession-avsession-avsession-i.md#setextras))}接口传入的键，用于向系统设置应用所需的能力列表。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ExtraKey-REQUIRE_ABILITY_LIST = 'requireAbilityList'--><!--Device-ExtraKey-REQUIRE_ABILITY_LIST = 'requireAbilityList'-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Core

## SUPPORT_URL_CASTING

```TypeScript
SUPPORT_URL_CASTING = 'url-cast'
```

作为[setExtras](arkts-avsession-avsession-avsession-i.md#setextras))}接口，给REQUIRE_ABILITY_LIST键传入能力列表的值，用于通知系统当前应用支持URL投播功能。

[setExtras](arkts-avsession-avsession-avsession-i.md#setextras))}接口传入入参`{[avSession.ExtraKey.REQUIRE_ABILITY_LIST]: [avSession.ExtraKey.SUPPORT_URL_CASTING]}`表示当前应用支持投播功能。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ExtraKey-SUPPORT_URL_CASTING = 'url-cast'--><!--Device-ExtraKey-SUPPORT_URL_CASTING = 'url-cast'-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

## DLNA_CURRENT_URI_METADATA

```TypeScript
DLNA_CURRENT_URI_METADATA = 'CurrentURIMetadata'
```

[AVMediaDescription](arkts-avsession-avsession-avmediadescription-i.md)中extras属性可传入的键，值传入string类型。

用于DLNA投播场景下，在发送给对端的报文中，为CurrentURIMetaData标签添加内容。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ExtraKey-DLNA_CURRENT_URI_METADATA = 'CurrentURIMetadata'--><!--Device-ExtraKey-DLNA_CURRENT_URI_METADATA = 'CurrentURIMetadata'-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

## DLNA_DIDL_LITE

```TypeScript
DLNA_DIDL_LITE = 'DIDL-Lite'
```

[AVMediaDescription](arkts-avsession-avsession-avmediadescription-i.md)中extras属性可传入的键，值传入string类型。

用于DLNA投播场景下，在发送给对端的报文中，为DIDL-Lite标签添加内容。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-ExtraKey-DLNA_DIDL_LITE = 'DIDL-Lite'--><!--Device-ExtraKey-DLNA_DIDL_LITE = 'DIDL-Lite'-End-->

**System capability:** SystemCapability.Multimedia.AVSession.AVCast

