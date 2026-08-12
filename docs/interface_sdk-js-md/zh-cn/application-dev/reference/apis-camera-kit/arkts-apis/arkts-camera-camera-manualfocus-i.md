# ManualFocus

ManualFocus object.

**继承/实现关系：** ManualFocus extends [ManualFocusQuery](arkts-camera-camera-manualfocusquery-i.md#ManualFocusQuery)

**起始版本：** 24

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

<!--Device-camera-interface ManualFocus extends ManualFocusQuery--><!--Device-camera-interface ManualFocus extends ManualFocusQuery-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

## getFocusDistance

ArkTS-Dyn:
```TypeScript
getFocusDistance(): number
```

ArkTS-Sta:
```TypeScript
getFocusDistance(): double
```

Gets current focus distance, ranging from 0.0 to 1.0, with 0.0 being shortest distance at which the lens can focus and 1.0 the furthest. The default value is 1.0.

**起始版本：** 24

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本24开始，该接口支持在原子化服务API中使用。

<!--Device-ManualFocus-getFocusDistance(): double--><!--Device-ManualFocus-getFocusDistance(): double-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| ArkTS-Dyn: number  <br>ArkTS-Sta：double | The current focus distance. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [7400102](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-camera-kit/errorcode-camera.md#7400102-非法操作) | Operation not allowed, the inputDevice or the session is abnormal.<br>**适用版本：** 24+ |
| [7400103](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-camera-kit/errorcode-camera.md#7400103-会话未配置) | Session not config. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) | Not System Application.<br>**适用版本：** 12 - 23 |

## setFocusDistance

ArkTS-Dyn:
```TypeScript
setFocusDistance(distance: number): void
```

ArkTS-Sta:
```TypeScript
setFocusDistance(distance: double): void
```

Sets focus distance. Possible distance values range from 0.0 to 1.0, with 0.0 being shortest distance at which the lens can focus and 1.0 the furthest. The default value is 1.0.

**起始版本：** 24

**ArkTS模式：** ArkTS-Dyn起始版本为12；ArkTS-Sta起始版本为23。

**原子化服务API：** 从API版本24开始，该接口支持在原子化服务API中使用。

<!--Device-ManualFocus-setFocusDistance(distance: double): void--><!--Device-ManualFocus-setFocusDistance(distance: double): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| distance | ArkTS-Dyn: number  <br>ArkTS-Sta：double | 是 | Focus distance. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [7400101](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-camera-kit/errorcode-camera.md#7400101-无效入参) | Parameter missing or parameter type incorrect.<br>**适用版本：** 12 - 23 |
| [7400102](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-camera-kit/errorcode-camera.md#7400102-非法操作) | Operation not allowed, the inputDevice or the session is abnormal.<br>**适用版本：** 24+ |
| [7400103](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-camera-kit/errorcode-camera.md#7400103-会话未配置) | Session not config. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) | Not System Application.<br>**适用版本：** 12 - 23 |

