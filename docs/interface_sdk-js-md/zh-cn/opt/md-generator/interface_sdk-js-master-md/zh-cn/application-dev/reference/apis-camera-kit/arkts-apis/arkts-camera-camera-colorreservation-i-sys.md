# ColorReservation（系统接口）

ColorReservation extends [ColorReservationQuery](arkts-camera-camera-colorreservationquery-i-sys.md)Provides API for obtaining and setting a color reservation type.

**继承/实现关系：** ColorReservation extends [ColorReservationQuery](arkts-camera-camera-colorreservationquery-i-sys.md)

**起始版本：** 15

<!--Device-camera-interface ColorReservation extends ColorReservationQuery--><!--Device-camera-interface ColorReservation extends ColorReservationQuery-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

## getColorReservation

```TypeScript
getColorReservation(): ColorReservationType
```

Obtains the color reservation type in use.

**起始版本：** 15

<!--Device-ColorReservation-getColorReservation(): ColorReservationType--><!--Device-ColorReservation-getColorReservation(): ColorReservationType-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| [ColorReservationType](arkts-camera-camera-colorreservationtype-e-sys.md) |

**错误码：**

| 错误码ID |
| --- |
| [7400103](../errorcode-camera.md#7400103-会话未配置) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function getColorReservation(session: camera.VideoSessionForSys): camera.ColorReservationType | undefined {
  let colorReservation: camera.ColorReservationType | undefined = undefined;
  try {
    colorReservation = session.getColorReservation();
  } catch (error) {
    // 失败返回错误码error.code并处理。
    let err = error as BusinessError;
    console.error(`The setColorReservation call failed. error code: ${err.code}`);
  }
  return colorReservation;
}
```

## setColorReservation

```TypeScript
setColorReservation(type: ColorReservationType): void
```

Sets a color reservation type. Before the setting, call  
[getSupportedColorReservationTypes](arkts-camera-camera-colorreservationquery-i-sys.md#getsupportedcolorreservationtypes) to obtain the supported color reservation types.

**起始版本：** 15

<!--Device-ColorReservation-setColorReservation(type: ColorReservationType): void--><!--Device-ColorReservation-setColorReservation(type: ColorReservationType): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | [ColorReservationType](arkts-camera-camera-colorreservationtype-e-sys.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../apis-contacts-kit/errorcode-contacts.md#401-系统内部错误) |
| [7400102](../errorcode-camera.md#7400102-非法操作) |
| [7400103](../errorcode-camera.md#7400103-会话未配置) |
| [7400201](../errorcode-camera.md#7400201-相机服务异常) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function setColorReservation(session: camera.VideoSessionForSys, type: camera.ColorReservationType): void {
  try {
    session.setColorReservation(type);
  } catch (error) {
    // 失败返回错误码error.code并处理。
    let err = error as BusinessError;
    console.error(`The setColorReservation call failed. error code: ${err.code}`);
  }
}
```
