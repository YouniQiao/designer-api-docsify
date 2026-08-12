# ColorReservationQuery（系统接口）

Provides APIs for querying the color retention type supported by the device.

**起始版本：** 15

**ArkTS模式：** ArkTS-Dyn起始版本为15；ArkTS-Sta起始版本为23。

<!--Device-camera-interface ColorReservationQuery--><!--Device-camera-interface ColorReservationQuery-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

## getSupportedColorReservationTypes

```TypeScript
getSupportedColorReservationTypes(): Array<ColorReservationType>
```

Obtains the supported color reservation types.

**起始版本：** 15

**ArkTS模式：** ArkTS-Dyn起始版本为15；ArkTS-Sta起始版本为23。

<!--Device-ColorReservationQuery-getSupportedColorReservationTypes(): Array<ColorReservationType>--><!--Device-ColorReservationQuery-getSupportedColorReservationTypes(): Array<ColorReservationType>-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array&lt;[ColorReservationType](arkts-camera-camera-colorreservationtype-e-sys.md)&gt; | Array of color reservation types supported. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [7400103](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-camera-kit/errorcode-camera.md#7400103-会话未配置) | Session not config, only throw in session usage. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) | Not System Application. |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function getSupportedColorReservationTypes(session: camera.VideoSessionForSys): Array<camera.ColorReservationType> {
  let colorReservationTypes: Array<camera.ColorReservationType> = [];
  try {
    colorReservationTypes = session.getSupportedColorReservationTypes();
  } catch (error) {
    // 失败返回错误码error.code并处理。
    let err = error as BusinessError;
    console.error(`The getSupportedColorReservationTypes call failed. error code: ${err.code}`);
  }
  return colorReservationTypes;
}
```

