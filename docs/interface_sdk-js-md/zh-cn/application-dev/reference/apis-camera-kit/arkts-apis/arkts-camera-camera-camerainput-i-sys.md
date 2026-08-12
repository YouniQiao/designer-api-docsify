# CameraInput

相机设备输入对象。

会话中[Session](arkts-camera-camera-session-i.md#Session)使用的相机信息。

**起始版本：** 10

**ArkTS模式：** ArkTS-Dyn起始版本为10；ArkTS-Sta起始版本为23。

<!--Device-camera-interface CameraInput--><!--Device-camera-interface CameraInput-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

## closeDelayed

ArkTS-Dyn:
```TypeScript
closeDelayed(time: number): Promise<void>
```

ArkTS-Sta:
```TypeScript
closeDelayed(time: int): Promise<void>
```

Delay close camera.

**起始版本：** 18

**ArkTS模式：** ArkTS-Dyn起始版本为18；ArkTS-Sta起始版本为23。

<!--Device-CameraInput-closeDelayed(time: int): Promise<void>--><!--Device-CameraInput-closeDelayed(time: int): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| time | ArkTS-Dyn: number  <br>ArkTS-Sta：int | 是 | delay time for turning off camera, in units of second. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise used to return the result. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [7400101](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-camera-kit/errorcode-camera.md#7400101-无效入参) | Parameter missing or parameter type incorrect. |
| [7400201](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-camera-kit/errorcode-camera.md#7400201-相机服务异常) | Camera service fatal error. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) | Not System Application. |

## controlAuxiliary

```TypeScript
controlAuxiliary(auxiliaryType: AuxiliaryType, auxiliaryStatus: AuxiliaryStatus): Promise<void>
```

Control auxiliary.

**起始版本：** 18

**ArkTS模式：** ArkTS-Dyn起始版本为18；ArkTS-Sta起始版本为23。

<!--Device-CameraInput-controlAuxiliary(auxiliaryType: AuxiliaryType, auxiliaryStatus: AuxiliaryStatus): Promise<void>--><!--Device-CameraInput-controlAuxiliary(auxiliaryType: AuxiliaryType, auxiliaryStatus: AuxiliaryStatus): Promise<void>-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| auxiliaryType | [AuxiliaryType](arkts-camera-camera-auxiliarytype-e-sys.md) | 是 | Auxiliary type. |
| auxiliaryStatus | [AuxiliaryStatus](arkts-camera-camera-auxiliarystatus-e-sys.md) | 是 | Auxiliary status. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | Promise used to return the result. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [7400102](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-camera-kit/errorcode-camera.md#7400102-非法操作) | Operation not allowed. |
| [7400201](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-camera-kit/errorcode-camera.md#7400201-相机服务异常) | Camera service fatal error. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) | Not System Application. |

## usedAsPosition

```TypeScript
usedAsPosition(position: CameraPosition): void
```

Sets the camera to be used as a camera at the specified position.

**起始版本：** 19

**ArkTS模式：** ArkTS-Dyn起始版本为19；ArkTS-Sta起始版本为23。

<!--Device-CameraInput-usedAsPosition(position: CameraPosition): void--><!--Device-CameraInput-usedAsPosition(position: CameraPosition): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| position | [CameraPosition](arkts-camera-camera-cameraposition-e.md) | 是 | The positon used for the camera. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [7400101](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-camera-kit/errorcode-camera.md#7400101-无效入参) | Parameter missing or parameter type incorrect. |
| [7400201](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/apis-camera-kit/errorcode-camera.md#7400201-相机服务异常) | Camera service fatal error. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) | Not System Application. |

