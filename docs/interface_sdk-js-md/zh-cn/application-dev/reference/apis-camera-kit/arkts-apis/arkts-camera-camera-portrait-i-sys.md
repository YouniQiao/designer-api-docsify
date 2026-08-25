# Portrait（系统接口）

Portrait: inherits from [PortraitQuery](arkts-camera-camera-portraitquery-i-sys.md). Provides the APIs for portrait photo settings.

**继承/实现关系：** Portrait extends [PortraitQuery](arkts-camera-camera-portraitquery-i-sys.md)

**起始版本：** 11

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { camera } from 'kits/@kit.CameraKit';
```

## getPortraitEffect

```TypeScript
getPortraitEffect(): PortraitEffect
```

Obtains the portrait effect in use.

**起始版本：** 10

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| [PortraitEffect](arkts-camera-camera-portraiteffect-e-sys.md) |

**错误码：**

| 错误码ID |
| --- |
| [7400103](../errorcode-camera.md#7400103-会话未配置) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## setPortraitEffect

```TypeScript
setPortraitEffect(effect: PortraitEffect): void
```

Sets a portrait effect. Before the setting, use [getSupportedPortraitEffects](arkts-camera-camera-portraitquery-i-sys.md#getsupportedportraiteffects) to obtain the supported portrait effects and check whether the target portrait effect is supported.

**起始版本：** 10

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| effect | [PortraitEffect](arkts-camera-camera-portraiteffect-e-sys.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [7400103](../errorcode-camera.md#7400103-会话未配置) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
