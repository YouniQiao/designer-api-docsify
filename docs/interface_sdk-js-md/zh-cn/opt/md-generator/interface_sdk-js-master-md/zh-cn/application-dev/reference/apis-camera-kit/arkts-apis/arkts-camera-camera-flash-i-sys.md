# Flash

Flash继承自[FlashQuery](arkts-camera-camera-flashquery-i.md#FlashQuery)。

闪光灯类，对设备闪光灯操作。

**继承/实现关系：** Flash extends [FlashQuery](arkts-camera-camera-flashquery-i.md#FlashQuery)

**起始版本：** 11

<!--Device-camera-interface Flash extends FlashQuery--><!--Device-camera-interface Flash extends FlashQuery-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

## enableLcdFlash

```TypeScript
enableLcdFlash(enabled: boolean): void
```

Enables or disables the LCD flash.

Before the setting, call [isLcdFlashSupported](arkts-camera-camera-flashquery-i-sys.md#isLcdFlashSupported) to check whether the device supports the LCD flash.

**起始版本：** 13

<!--Device-Flash-enableLcdFlash(enabled: boolean): void--><!--Device-Flash-enableLcdFlash(enabled: boolean): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enabled | boolean | 是 |

**错误码：**

| 错误码ID |
| --- |
| [7400103](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-camera-kit/errorcode-camera.md#7400103-会话未配置) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';

function enableLcdFlash(session: camera.PhotoSessionForSys | camera.VideoSessionForSys | camera.NightPhotoSession): void {
  try {
    session.enableLcdFlash(true);
  } catch (error) {
    // 失败返回错误码error.code并处理。
    let err = error as BusinessError;
    console.error(`The setFlashMode call failed. error code: ${err.code}`);
  }
}
```
