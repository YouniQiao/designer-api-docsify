# BeautyQuery (System API)

Provides APIs to obtain and set the beauty effect.

**Since:** 12

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-camera-interface BeautyQuery--><!--Device-camera-interface BeautyQuery-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

## getSupportedBeautyRange

ArkTS-Dyn:
```TypeScript
getSupportedBeautyRange(type: BeautyType): Array<number>
```

ArkTS-Sta:
```TypeScript
getSupportedBeautyRange(type: BeautyType): Array<int>
```

Obtains the levels that can be set a beauty type. The beauty levels vary according to the device type. The following table is only an example.  
| Input Parameter | Example Return Value | Return Value Description |  
| ----------------| ---- | ---------|  
| AUTO | [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] |Beauty levels supported when **type** is set to **AUTO**. The value **0** * means that beauty mode is disabled, and other positive values mean the corresponding automatic beauty levels. |  
| SKIN\_SMOOTH | [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] | Beauty levels supported when **type** is set to **SKIN\_SMOOTH**. The value * **0** means that the skin smoothing feature is disabled, and other positive values mean the corresponding skin smoothing levels. |  
| FACE\_SLENDER | [0, 1, 2, 3, 4, 5] | Beauty levels supported when **type** is set to **FACE\_SLENDER**. The value **0** means that * the face slimming feature is disabled, and other positive values mean the corresponding face slimming levels. |  
| SKIN\_TONE | [-1, 16242611] | Beauty levels supported when **type** is set to **SKIN\_TONE**. The value **-1** means that the skin tone perfection feature is disabled. Other non-negative values mean the skin tone perfection levels represented by RGB,\_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_ for example, 16242611, which is 0xF7D7B3 in hexadecimal format, where F7, D7, and B3 represent the values of the R channel, G channel, and B channel, respectively. |

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-BeautyQuery-getSupportedBeautyRange(type: BeautyType): Array<int>--><!--Device-BeautyQuery-getSupportedBeautyRange(type: BeautyType): Array<int>-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Beauty type. |

**Return value:**

| Type | Description |
| --- | --- |
| ArkTS-Dyn: Array&lt;number&gt;  \_\_\_HTML\_TAG\_USD\_0\_\_\_ArkTS-Sta：Array&lt;int&gt; | Array of levels supported. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System Application. |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) | Session not config, only throw in session usage. |

**Example**

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

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

<!--Device-BeautyQuery-getSupportedBeautyTypes(): Array<BeautyType>--><!--Device-BeautyQuery-getSupportedBeautyTypes(): Array<BeautyType>-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;BeautyType&gt; | Array of beauty types supported. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System Application. |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) | Session not config, only throw in session usage. |

**Example**

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

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

<!--Device-BeautyQuery-getSupportedPortraitThemeTypes(): Array<PortraitThemeType>--><!--Device-BeautyQuery-getSupportedPortraitThemeTypes(): Array<PortraitThemeType>-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| Array&lt;PortraitThemeType&gt; | Lists of portrait theme types |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System Application. |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) | Session not config, only throw in session usage. |

## isPortraitThemeSupported

```TypeScript
isPortraitThemeSupported(): boolean
```

Checks whether portrait theme is supported.

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 14; ArkTS-Sta since version 23.

<!--Device-BeautyQuery-isPortraitThemeSupported(): boolean--><!--Device-BeautyQuery-isPortraitThemeSupported(): boolean-End-->

**System capability:** SystemCapability.Multimedia.Camera.Core

**System API:** This is a system API.

**Return value:**

| Type | Description |
| --- | --- |
| boolean | Is portrait theme supported. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System Application. |
| [7400103](../errorcode-camera.md#7400103-session-not-configured) | Session not config, only throw in session usage. |

