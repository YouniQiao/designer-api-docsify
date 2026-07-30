# ApertureQuery

Provides the aperture query capability.

**起始版本：** 24

<!--Device-camera-interface ApertureQuery--><!--Device-camera-interface ApertureQuery-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

## 导入模块

```TypeScript
import { camera } from '@kit.CameraKit';
```

## getSupportedVirtualApertures

```TypeScript
getSupportedVirtualApertures(): Array<number>
```

Obtains the supported virtual apertures.

**起始版本：** 11

<!--Device-ApertureQuery-getSupportedVirtualApertures(): Array<double>--><!--Device-ApertureQuery-getSupportedVirtualApertures(): Array<double>-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array&lt;number&gt; | Array of virtual apertures supported. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) | Not System Application. |
| [7400103](../errorcode-camera.md#7400103-会话未配置) | Session not config, only throw in session usage. |

**示例：**

```TypeScript
function getSupportedVirtualApertures(session: camera.PortraitPhotoSession): Array<number> {
  let virtualApertures: Array<number> = session.getSupportedVirtualApertures();
  return virtualApertures;
}

```

