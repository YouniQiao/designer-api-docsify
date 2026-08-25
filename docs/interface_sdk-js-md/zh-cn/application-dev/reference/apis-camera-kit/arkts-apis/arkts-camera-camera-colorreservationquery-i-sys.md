# ColorReservationQuery（系统接口）

Provides APIs for querying the color retention type supported by the device.

**起始版本：** 15

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

## 导入模块

```TypeScript
import { camera } from 'kits/@kit.CameraKit';
```

## getSupportedColorReservationTypes

```TypeScript
getSupportedColorReservationTypes(): Array<ColorReservationType>
```

Obtains the supported color reservation types.

**起始版本：** 15

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Array&lt;[ColorReservationType](arkts-camera-camera-colorreservationtype-e-sys.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [7400103](../errorcode-camera.md#7400103-会话未配置) |
