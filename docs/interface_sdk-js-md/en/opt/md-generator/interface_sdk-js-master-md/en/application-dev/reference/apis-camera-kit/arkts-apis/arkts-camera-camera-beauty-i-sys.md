# Beauty (System API)

Beauty extends [BeautyQuery](arkts-camera-camera-beautyquery-i-sys.md#BeautyQuery)Provides APIs to obtain and set the beauty effect.

**Inheritance/Implementation:** Beauty extends [BeautyQuery](arkts-camera-camera-beautyquery-i-sys.md#BeautyQuery)

**Since:** 11

<!--Device-camera-interface Beauty extends BeautyQuery--><!--Device-camera-interface Beauty extends BeautyQuery-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { camera } from '@kit.CameraKit';
```

## getBeauty

```TypeScript
getBeauty(type: BeautyType): number
```

Obtains the level of the beauty type in use.

**Since:** 11

<!--Device-Beauty-getBeauty(type: BeautyType): int--><!--Device-Beauty-getBeauty(type: BeautyType): int-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | [BeautyType](arkts-camera-camera-beautytype-e-sys.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [7400103](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-camera-kit/errorcode-camera.md#7400103-session-not-configured) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
function getBeauty(portraitPhotoSession: camera.PortraitPhotoSession): number {
  const invalidValue: number = -1;
  let beautyTypes = portraitPhotoSession.getSupportedBeautyTypes();
  if (beautyTypes === undefined || beautyTypes.length <= 0) {
    return invalidValue;
  }
  let beautyLevels: Array<number> = portraitPhotoSession.getSupportedBeautyRange(beautyTypes[0]);
  if (beautyLevels === undefined || beautyLevels.length <= 0) {
    return invalidValue;
  }
  portraitPhotoSession.setBeauty(beautyTypes[0], beautyLevels[0]);
  let beautyLevel: number = portraitPhotoSession.getBeauty(beautyTypes[0]);
  return beautyLevel;
}
```

## setBeauty

```TypeScript
setBeauty(type: BeautyType, value: number): void
```

Sets a beauty type and its level. Beauty mode is turned off only when all the  
[beauty types](arkts-camera-camera-beautytype-e-sys.md#BeautyType) obtained through  
[getSupportedBeautyTypes](arkts-camera-camera-beautyquery-i-sys.md#getSupportedBeautyTypes) are disabled.

**Since:** 11

<!--Device-Beauty-setBeauty(type: BeautyType, value: int): void--><!--Device-Beauty-setBeauty(type: BeautyType, value: int): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | [BeautyType](arkts-camera-camera-beautytype-e-sys.md) | Yes |
| value | number | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [7400103](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-camera-kit/errorcode-camera.md#7400103-session-not-configured) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
function setBeauty(portraitPhotoSession: camera.PortraitPhotoSession): void {
  let beautyTypes: Array<camera.BeautyType> = portraitPhotoSession.getSupportedBeautyTypes();
  if (beautyTypes === undefined || beautyTypes.length <= 0) {
    return;
  }
  let beautyLevels: Array<number> = portraitPhotoSession.getSupportedBeautyRange(beautyTypes[0]);
  if (beautyLevels === undefined || beautyLevels.length <= 0) {
    return;
  }
  portraitPhotoSession.setBeauty(beautyTypes[0], beautyLevels[0]);
}
```

## setPortraitThemeType

```TypeScript
setPortraitThemeType(type: PortraitThemeType): void
```

Sets a portrait theme type for a camera device.

**Since:** 14

<!--Device-Beauty-setPortraitThemeType(type: PortraitThemeType): void--><!--Device-Beauty-setPortraitThemeType(type: PortraitThemeType): void-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | [PortraitThemeType](arkts-camera-camera-portraitthemetype-e-sys.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [7400101](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-camera-kit/errorcode-camera.md#7400101-invalid-parameter) |
| [7400103](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-camera-kit/errorcode-camera.md#7400103-session-not-configured) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
