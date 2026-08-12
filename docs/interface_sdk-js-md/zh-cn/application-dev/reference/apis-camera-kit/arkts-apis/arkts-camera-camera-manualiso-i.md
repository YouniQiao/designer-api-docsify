# ManualIso

ManualIso object.

**继承/实现关系：** ManualIso extends [ManualIsoQuery](arkts-camera-camera-manualisoquery-i.md#ManualIsoQuery)

**起始版本：** 24

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

<!--Device-camera-interface ManualIso extends ManualIsoQuery--><!--Device-camera-interface ManualIso extends ManualIsoQuery-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

## getIso

ArkTS-Dyn:
```TypeScript
getIso(): number
```

ArkTS-Sta:
```TypeScript
getIso(): int
```

Gets current ISO.

**起始版本：** 24

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本24开始，该接口支持在原子化服务API中使用。

<!--Device-ManualIso-getIso(): int--><!--Device-ManualIso-getIso(): int-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：int | The current ISO. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [7400102](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-camera-kit/errorcode-camera.md#7400102-非法操作) | Operation not allowed, the inputDevice or the session is abnormal.<br>**适用版本：** 24+ |
| [7400103](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-camera-kit/errorcode-camera.md#7400103-会话未配置) | Session not config. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) | Not System Application.<br>**适用版本：** 12 - 23 |

## setIso

ArkTS-Dyn:
```TypeScript
setIso(iso: number): void
```

ArkTS-Sta:
```TypeScript
setIso(iso: int): void
```

Sets ISO sensitivity value, within the range of getSupportedIsoRange. This control can not be effective if ExposureMode is set to EXPOSURE_MODE_LOCKED.

**起始版本：** 24

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本24开始，该接口支持在原子化服务API中使用。

<!--Device-ManualIso-setIso(iso: int): void--><!--Device-ManualIso-setIso(iso: int): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| iso | ArkTS-Dyn: number  <br>ArkTS-Sta：int | 是 | ISO |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [7400101](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-camera-kit/errorcode-camera.md#7400101-无效入参) | Parameter missing or parameter type incorrect.<br>**适用版本：** 12 - 23 |
| [7400102](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-camera-kit/errorcode-camera.md#7400102-非法操作) | Operation not allowed, the inputDevice or the session is abnormal.<br>**适用版本：** 24+ |
| [7400103](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-camera-kit/errorcode-camera.md#7400103-会话未配置) | Session not config. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) | Not System Application.<br>**适用版本：** 12 - 23 |

