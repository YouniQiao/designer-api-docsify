# App

Defines static functions of App class

**Since:** 3

**System capability:** SystemCapability.ArkUI.ArkUI.Lite

## Modules to Import

```TypeScript
import { App, AppResponse, RequestFullWindowOptions, ScreenOnVisibleOptions } from 'kits/@kit.ArkUI';
```

## getInfo

```TypeScript
static getInfo(): AppResponse
```

Obtains the declared information in the **config.json** file of an application. In the stage model, this API returns **null**.This API is deprecated since API version 9. You are advised to use [bundleManager.getBundleInfoForSelf](../../apis-ability-kit/arkts-apis/arkts-ability-bundlemanager-getbundleinfoforself-f.md) instead.

**Since:** 3

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Lite

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [AppResponse](arkts-arkui-system-app-appresponse-i.md) |

## requestFullWindow

```TypeScript
static requestFullWindow(options?: RequestFullWindowOptions): void
```

Requests the application to run in full window. In some scenarios, such as semi-modal FA, the FA runs in non-full window. In this case, you can call this API. This API is invalid for an application already in full-window mode.

**Since:** 3

**Deprecated since:** 8

**Substitutes:** startAbility

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [RequestFullWindowOptions](arkts-arkui-system-app-requestfullwindowoptions-i.md) | No |

## screenOnVisible

```TypeScript
static screenOnVisible(options?: ScreenOnVisibleOptions): void
```

Defines whether to keep the application visible when the screen is woken up.This API is deprecated since API version 8.

**Since:** 3

**Deprecated since:** 8

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [ScreenOnVisibleOptions](arkts-arkui-system-app-screenonvisibleoptions-i.md) | No |

## setImageCacheCount

```TypeScript
static setImageCacheCount(value: number): void
```

Set image cache capacity of decoded image count. if not set, the application will not cache any decoded image.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | number | Yes |

## setImageFileCacheSize

```TypeScript
static setImageFileCacheSize(value: number): void
```

Set image file cache size in bytes on disk before decode. if not set, the application will cache 100MB image files on disk.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | number | Yes |

## setImageRawDataCacheSize

```TypeScript
static setImageRawDataCacheSize(value: number): void
```

Set image cache capacity of raw image data size in bytes before decode. if not set, the application will not cache any raw image data.

**Since:** 7

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| value | number | Yes |

## terminate

```TypeScript
static terminate(): void
```

Terminates the current ability. In the stage model, this API has no effect.This API is deprecated since API version 7. You are advised to use [@ohos.ability.featureAbility](../../apis-ability-kit/arkts-apis/arkts-ability-featureability.md) instead.

**Since:** 3

**Atomic service API:** This API can be used in atomic services since API version 12.

**System capability:** SystemCapability.ArkUI.ArkUI.Lite
