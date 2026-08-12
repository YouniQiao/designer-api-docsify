# Beauty（系统接口）

Beauty extends [BeautyQuery](arkts-camera-camera-beautyquery-i-sys.md#BeautyQuery)Provides APIs to obtain and set the beauty effect.

**继承/实现关系：** Beauty extends [BeautyQuery](arkts-camera-camera-beautyquery-i-sys.md#BeautyQuery)

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

<!--Device-camera-interface Beauty extends BeautyQuery--><!--Device-camera-interface Beauty extends BeautyQuery-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

## getBeauty

ArkTS-Dyn:
```TypeScript
getBeauty(type: BeautyType): number
```

ArkTS-Sta:
```TypeScript
getBeauty(type: BeautyType): int
```

Obtains the level of the beauty type in use.

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

<!--Device-Beauty-getBeauty(type: BeautyType): int--><!--Device-Beauty-getBeauty(type: BeautyType): int-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [BeautyType](arkts-camera-camera-beautytype-e-sys.md) | 是 | Beauty type. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：int | the beauty effect in use. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [7400103](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-camera-kit/errorcode-camera.md#7400103-会话未配置) | Session not config. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) | Not System Application. |

## 示例

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

ArkTS-Dyn:
```TypeScript
setBeauty(type: BeautyType, value: number): void
```

ArkTS-Sta:
```TypeScript
setBeauty(type: BeautyType, value: int): void
```

Sets a beauty type and its level. Beauty mode is turned off only when all the  
[beauty types](arkts-camera-camera-beautytype-e-sys.md#BeautyType) obtained through  
[getSupportedBeautyTypes](arkts-camera-camera-beautyquery-i-sys.md#getSupportedBeautyTypes) are disabled.

**起始版本：** 11

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

<!--Device-Beauty-setBeauty(type: BeautyType, value: int): void--><!--Device-Beauty-setBeauty(type: BeautyType, value: int): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [BeautyType](arkts-camera-camera-beautytype-e-sys.md) | 是 | Beauty type. |
| value | ArkTS-Dyn: number  <br>ArkTS-Sta：int | 是 | Beauty level, which is obtained through [getSupportedBeautyRange](arkts-camera-camera-beautyquery-i-sys.md#getSupportedBeautyRange). |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [7400103](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-camera-kit/errorcode-camera.md#7400103-会话未配置) | Session not config. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) | Not System Application. |

## 示例

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

**起始版本：** 14

**ArkTS模式：** ArkTS-Dyn起始版本为14；ArkTS-Sta起始版本为23。

<!--Device-Beauty-setPortraitThemeType(type: PortraitThemeType): void--><!--Device-Beauty-setPortraitThemeType(type: PortraitThemeType): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [PortraitThemeType](arkts-camera-camera-portraitthemetype-e-sys.md) | 是 | The type of portrait theme. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [7400101](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-camera-kit/errorcode-camera.md#7400101-无效入参) | Parameter missing or parameter type incorrect. |
| [7400103](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-camera-kit/errorcode-camera.md#7400103-会话未配置) | Session not config, only throw in session usage. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) | Not System Application. |

