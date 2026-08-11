# PortraitQuery（系统接口）

Queries portrait parameters.

**起始版本：** 12

<!--Device-camera-interface PortraitQuery--><!--Device-camera-interface PortraitQuery-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

## getSupportedPortraitEffects

```TypeScript
getSupportedPortraitEffects(): Array<PortraitEffect>
```

Obtains the supported portrait effects.

**起始版本：** 10

<!--Device-PortraitQuery-getSupportedPortraitEffects(): Array<PortraitEffect>--><!--Device-PortraitQuery-getSupportedPortraitEffects(): Array<PortraitEffect>-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Array&lt;PortraitEffect&gt; |

**错误码：**

| 错误码ID |
| --- |
| [7400103](../errorcode-camera.md#7400103-会话未配置) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |

## 示例

```TypeScript
function getSupportedPortraitEffects(portraitPhotoSession: camera.PortraitPhotoSession): Array<camera.PortraitEffect> {
  let portraitEffects: Array<camera.PortraitEffect> = portraitPhotoSession.getSupportedPortraitEffects();
  return portraitEffects;
}
```
