# ColorEffect（系统接口）

ColorEffect extends [ColorEffectQuery](arkts-camera-camera-coloreffectquery-i-sys.md) Provides the APIs to obtain and set the lens color effect.

**继承/实现关系：** ColorEffect extends [ColorEffectQuery](arkts-camera-camera-coloreffectquery-i-sys.md)

**起始版本：** 11

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { camera } from 'kits/@kit.CameraKit';
```

## getColorEffect

```TypeScript
getColorEffect(): ColorEffectType
```

Obtains the color effect in use.

**起始版本：** 11

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| [ColorEffectType](arkts-camera-camera-coloreffecttype-e-sys.md) |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [7400103](../errorcode-camera.md#7400103-会话未配置) |

## setColorEffect

```TypeScript
setColorEffect(type: ColorEffectType): void
```

Sets a color effect. Before the setting, call [getSupportedColorEffects](arkts-camera-camera-coloreffectquery-i-sys.md#getsupportedcoloreffects) to obtain the supported color effects.

**起始版本：** 11

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | [ColorEffectType](arkts-camera-camera-coloreffecttype-e-sys.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [7400103](../errorcode-camera.md#7400103-会话未配置) |
