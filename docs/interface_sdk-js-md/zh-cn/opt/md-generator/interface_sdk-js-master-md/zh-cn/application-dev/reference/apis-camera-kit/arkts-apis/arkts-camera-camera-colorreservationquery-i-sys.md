# ColorReservationQuery（系统接口）

Provides APIs for querying the color retention type supported by the device.

**起始版本：** 15

<!--Device-camera-interface ColorReservationQuery--><!--Device-camera-interface ColorReservationQuery-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

## getSupportedColorReservationTypes

```TypeScript
getSupportedColorReservationTypes(): Array<ColorReservationType>
```

Obtains the supported color reservation types.

**起始版本：** 15

<!--Device-ColorReservationQuery-getSupportedColorReservationTypes(): Array<ColorReservationType>--><!--Device-ColorReservationQuery-getSupportedColorReservationTypes(): Array<ColorReservationType>-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Array&lt;[ColorReservationType](arkts-camera-camera-colorreservationtype-e-sys.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [7400103](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-camera-kit/errorcode-camera.md#7400103-会话未配置) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |

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
