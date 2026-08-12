# BeautyQuery（系统接口）

Provides APIs to obtain and set the beauty effect.

**起始版本：** 12

<!--Device-camera-interface BeautyQuery--><!--Device-camera-interface BeautyQuery-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

## getSupportedBeautyRange

```TypeScript
getSupportedBeautyRange(type: BeautyType): Array<number>
```

Obtains the levels that can be set a beauty type. The beauty levels vary according to the device type. The following table is only an example.  
| Input Parameter | Example Return Value | Return Value Description |
| ----------------| ---- | ---------|
| AUTO | [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] |Beauty levels supported when **type** is set to **AUTO**. The value **0** * means that beauty mode is disabled, and other positive values mean the corresponding automatic beauty levels. |
| [SKIN_SMOOTH](arkts-camera-camera-beautytype-e-sys.md) | [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] | Beauty levels supported when **type** is set to **SKIN_SMOOTH**. The value * **0** means that the skin smoothing feature is disabled, and other positive values mean the corresponding skin smoothing levels. |
| [FACE_SLENDER](arkts-camera-camera-beautytype-e-sys.md) | [0, 1, 2, 3, 4, 5] | Beauty levels supported when **type** is set to **FACE_SLENDER**. The value **0** means that * the face slimming feature is disabled, and other positive values mean the corresponding face slimming levels. |
| [SKIN_TONE](arkts-camera-camera-beautytype-e-sys.md) | [-1, 16242611] |

**起始版本：** 11

<!--Device-BeautyQuery-getSupportedBeautyRange(type: BeautyType): Array<int>--><!--Device-BeautyQuery-getSupportedBeautyRange(type: BeautyType): Array<int>-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | [BeautyType](arkts-camera-camera-beautytype-e-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| Array & lt;number & gt; |

**错误码：**

| 错误码ID |
| --- |
| [7400103](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-camera-kit/errorcode-camera.md#7400103-会话未配置) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
function getSupportedBeautyRange(portraitPhotoSession: camera.PortraitPhotoSession): Array<number> {
  let beautyTypes: Array<camera.BeautyType> = portraitPhotoSession.getSupportedBeautyTypes();
  if (beautyTypes === undefined || beautyTypes.length <= 0) {
    return [];
  }
  let beautyLevels: Array<number> = portraitPhotoSession.getSupportedBeautyRange(beautyTypes[0]);
  return beautyLevels;
}
```

## getSupportedBeautyTypes

```TypeScript
getSupportedBeautyTypes(): Array<BeautyType>
```

Obtains the supported beauty types.

**起始版本：** 11

<!--Device-BeautyQuery-getSupportedBeautyTypes(): Array<BeautyType>--><!--Device-BeautyQuery-getSupportedBeautyTypes(): Array<BeautyType>-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Array&lt;[BeautyType](arkts-camera-camera-beautytype-e-sys.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [7400103](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-camera-kit/errorcode-camera.md#7400103-会话未配置) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
function getSupportedBeautyTypes(portraitPhotoSession: camera.PortraitPhotoSession): Array<camera.BeautyType> {
  let beautyTypes: Array<camera.BeautyType> = portraitPhotoSession.getSupportedBeautyTypes();
  return beautyTypes;
}
```

## getSupportedPortraitThemeTypes

```TypeScript
getSupportedPortraitThemeTypes(): Array<PortraitThemeType>
```

Gets supported portrait theme type.

**起始版本：** 14

<!--Device-BeautyQuery-getSupportedPortraitThemeTypes(): Array<PortraitThemeType>--><!--Device-BeautyQuery-getSupportedPortraitThemeTypes(): Array<PortraitThemeType>-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Array&lt;[PortraitThemeType](arkts-camera-camera-portraitthemetype-e-sys.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [7400103](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-camera-kit/errorcode-camera.md#7400103-会话未配置) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |

## isPortraitThemeSupported

```TypeScript
isPortraitThemeSupported(): boolean
```

Checks whether portrait theme is supported.

**起始版本：** 14

<!--Device-BeautyQuery-isPortraitThemeSupported(): boolean--><!--Device-BeautyQuery-isPortraitThemeSupported(): boolean-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| boolean |

**错误码：**

| 错误码ID |
| --- |
| [7400103](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-camera-kit/errorcode-camera.md#7400103-会话未配置) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |
