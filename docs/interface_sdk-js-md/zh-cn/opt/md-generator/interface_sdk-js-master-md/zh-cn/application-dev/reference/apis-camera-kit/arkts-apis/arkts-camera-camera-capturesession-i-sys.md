# CaptureSession

拍照会话类，保存一次相机运行所需要的所有资源[CameraInput](arkts-camera-camera-camerainput-i.md#CameraInput)、[CameraOutput](arkts-camera-camera-cameraoutput-i.md#CameraOutput)，并向相机设备申请完成相机功能(录像，拍照)。

> **说明：**
> 
> 从 API version 10开始支持，从API version 11开始废弃。

**起始版本：** 10

**废弃版本：** 11

**替代接口：** [VideoSession](arkts-camera-camera-videosession-i.md#VideoSession)

<!--Device-camera-interface CaptureSession--><!--Device-camera-interface CaptureSession-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

## getBeauty

```TypeScript
getBeauty(type: BeautyType): number
```

Obtains the level of the beauty type in use.

**起始版本：** 10

**废弃版本：** 11

**替代接口：** [getBeauty](arkts-camera-camera-beauty-i-sys.md#getBeauty)

<!--Device-CaptureSession-getBeauty(type: BeautyType): number--><!--Device-CaptureSession-getBeauty(type: BeautyType): number-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | [BeautyType](arkts-camera-camera-beautytype-e-sys.md) | 是 |

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [7400103](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-camera-kit/errorcode-camera.md#7400103-会话未配置) |

## 示例

```TypeScript
function getBeauty(captureSession: camera.CaptureSession): number {
  const invalidValue: number = -1;
  let beautyTypes: Array<camera.BeautyType> = captureSession.getSupportedBeautyTypes();
  if (beautyTypes === undefined || beautyTypes.length <= 0) {
    return invalidValue;
  }
  let beautyLevels: Array<number> = captureSession.getSupportedBeautyRange(beautyTypes[0]);
  if (beautyLevels === undefined || beautyLevels.length <= 0) {
    return invalidValue;
  }
  captureSession.setBeauty(beautyTypes[0], beautyLevels[0]);
  let beautyLevel: number = captureSession.getBeauty(beautyTypes[0]);
  return beautyLevel;
}
```

## getSupportedBeautyRange

```TypeScript
getSupportedBeautyRange(type: BeautyType): Array<number>
```

Obtains the levels that can be set a beauty type. The beauty levels vary according to the device type. The following table is only an example.  
| Input Parameter | Example Return Value | Return Value Description |
| ----------------| ---- | ---------|
| AUTO | [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] |Beauty levels supported when **type** is set to **AUTO**. The value **0** means that beauty mode is disabled, and other positive values mean the corresponding automatic beauty levels. |
| [SKIN_SMOOTH](arkts-camera-camera-beautytype-e-sys.md) | [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] | Beauty levels supported when **type** is set to **SKIN_SMOOTH**. The value **0** means that the skin smoothing feature is disabled, and other positive values mean the corresponding skin smoothing levels. |
| [FACE_SLENDER](arkts-camera-camera-beautytype-e-sys.md) | [0, 1, 2, 3, 4, 5] | Beauty levels supported when **type** is set to **FACE_SLENDER**. The value **0** means that the face slimming feature is disabled, and other positive values mean the corresponding face slimming levels. |
| [SKIN_TONE](arkts-camera-camera-beautytype-e-sys.md) | [-1, 16242611] |

**起始版本：** 10

**废弃版本：** 11

**替代接口：** [getSupportedBeautyRange](arkts-camera-camera-beautyquery-i-sys.md#getSupportedBeautyRange)

<!--Device-CaptureSession-getSupportedBeautyRange(type: BeautyType): Array<number>--><!--Device-CaptureSession-getSupportedBeautyRange(type: BeautyType): Array<number>-End-->

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

## 示例

```TypeScript
function getSupportedBeautyRange(captureSession: camera.CaptureSession): Array<number> {
  let beautyTypes: Array<camera.BeautyType> = captureSession.getSupportedBeautyTypes();
  if (beautyTypes === undefined || beautyTypes.length <= 0) {
    return [];
  }
  let beautyLevels: Array<number> = captureSession.getSupportedBeautyRange(beautyTypes[0]);
  return beautyLevels;
}
```

## getSupportedBeautyTypes

```TypeScript
getSupportedBeautyTypes(): Array<BeautyType>
```

Obtains the supported beauty types.

**起始版本：** 10

**废弃版本：** 11

**替代接口：** [getSupportedBeautyTypes](arkts-camera-camera-beautyquery-i-sys.md#getSupportedBeautyTypes)

<!--Device-CaptureSession-getSupportedBeautyTypes(): Array<BeautyType>--><!--Device-CaptureSession-getSupportedBeautyTypes(): Array<BeautyType>-End-->

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

## 示例

```TypeScript
function getSupportedBeautyTypes(captureSession: camera.CaptureSession): Array<camera.BeautyType> {
  let beautyTypes: Array<camera.BeautyType> = captureSession.getSupportedBeautyTypes();
  return beautyTypes;
}
```

## setBeauty

```TypeScript
setBeauty(type: BeautyType, value: number): void
```

Sets a beauty type and its level. Beauty mode is turned off only when all the  
[beauty types](arkts-camera-camera-beautytype-e-sys.md#BeautyType) obtained through  
[getSupportedBeautyTypes](#getSupportedBeautyTypes) are disabled.

**起始版本：** 10

**废弃版本：** 11

**替代接口：** [setBeauty](arkts-camera-camera-beauty-i-sys.md#setBeauty)

<!--Device-CaptureSession-setBeauty(type: BeautyType, value: number): void--><!--Device-CaptureSession-setBeauty(type: BeautyType, value: number): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | [BeautyType](arkts-camera-camera-beautytype-e-sys.md) | 是 |
| value | number | 是 |

**错误码：**

| 错误码ID |
| --- |
| [7400103](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-camera-kit/errorcode-camera.md#7400103-会话未配置) |

## 示例

```TypeScript
function setBeauty(captureSession: camera.CaptureSession): void {
  let beautyTypes: Array<camera.BeautyType> = captureSession.getSupportedBeautyTypes();
  if (beautyTypes === undefined || beautyTypes.length <= 0) {
    return;
  }
  let beautyLevels: Array<number> = captureSession.getSupportedBeautyRange(beautyTypes[0]);
  if (beautyLevels === undefined || beautyLevels.length <= 0) {
    return;
  }
  captureSession.setBeauty(beautyTypes[0], beautyLevels[0]);
}
```
