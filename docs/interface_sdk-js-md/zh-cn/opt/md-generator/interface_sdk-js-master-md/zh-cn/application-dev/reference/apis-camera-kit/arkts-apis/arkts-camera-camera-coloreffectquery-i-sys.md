# ColorEffectQuery（系统接口）

Provides the API to obtain the color effects supported.

**起始版本：** 12

<!--Device-camera-interface ColorEffectQuery--><!--Device-camera-interface ColorEffectQuery-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

## getSupportedColorEffects

```TypeScript
getSupportedColorEffects(): Array<ColorEffectType>
```

Obtains the supported color effects.

**起始版本：** 11

<!--Device-ColorEffectQuery-getSupportedColorEffects(): Array<ColorEffectType>--><!--Device-ColorEffectQuery-getSupportedColorEffects(): Array<ColorEffectType>-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Array&lt;[ColorEffectType](arkts-camera-camera-coloreffecttype-e-sys.md)&gt; |

**错误码：**

| 错误码ID |
| --- |
| [7400103](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-camera-kit/errorcode-camera.md#7400103-会话未配置) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
function getSupportedColorEffects(session: camera.PhotoSessionForSys): Array<camera.ColorEffectType> {
  let colorEffects: Array<camera.ColorEffectType> = session.getSupportedColorEffects();
  return colorEffects;
}
```
