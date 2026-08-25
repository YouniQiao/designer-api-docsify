# Beauty（系统接口）

Beauty extends [BeautyQuery](arkts-camera-camera-beautyquery-i-sys.md) Provides APIs to obtain and set the beauty effect.

**继承/实现关系：** Beauty extends [BeautyQuery](arkts-camera-camera-beautyquery-i-sys.md)

**起始版本：** 11

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { camera } from 'kits/@kit.CameraKit';
```

## getBeauty

```TypeScript
getBeauty(type: BeautyType): number
```

Obtains the level of the beauty type in use.

**起始版本：** 11

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
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [7400103](../errorcode-camera.md#7400103-会话未配置) |

## setBeauty

```TypeScript
setBeauty(type: BeautyType, value: number): void
```

Sets a beauty type and its level. Beauty mode is turned off only when all the [beauty types](arkts-camera-camera-beautytype-e-sys.md) obtained through [getSupportedBeautyTypes](arkts-camera-camera-beautyquery-i-sys.md#getsupportedbeautytypes) are disabled.

**起始版本：** 11

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
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [7400103](../errorcode-camera.md#7400103-会话未配置) |

## setPortraitThemeType

```TypeScript
setPortraitThemeType(type: PortraitThemeType): void
```

Sets a portrait theme type for a camera device.

**起始版本：** 14

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | [PortraitThemeType](arkts-camera-camera-portraitthemetype-e-sys.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [7400101](../errorcode-camera.md#7400101-无效入参) |
| [7400103](../errorcode-camera.md#7400103-会话未配置) |
