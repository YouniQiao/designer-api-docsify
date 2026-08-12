# MacroQuery

提供查询设备是否支持相机微距拍摄的方法。

**起始版本：** 19

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

<!--Device-camera-interface MacroQuery--><!--Device-camera-interface MacroQuery-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

## isMacroSupported

```TypeScript
isMacroSupported(): boolean
```

检测当前状态下是否支持微距能力，需要在CaptureSession调用  
[commitConfig](arkts-camera-camera-session-i.md#commitConfig)之后进行调用。

**起始版本：** 19

**ArkTS模式：** ArkTS-Dyn起始版本为11；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-MacroQuery-isMacroSupported(): boolean--><!--Device-MacroQuery-isMacroSupported(): boolean-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回是否支持微距能力。true表示支持，false表示不支持。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) | Not System Application.<br>**适用版本：** 11 - 18 |

