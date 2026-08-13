# Focus

Focus继承自[FocusQuery](arkts-camera-camera-focusquery-i.md#FocusQuery)。 对焦类，对设备对焦操作。

**继承/实现关系：** Focus extends [FocusQuery](arkts-camera-camera-focusquery-i.md#FocusQuery)

**起始版本：** 23

**废弃版本：** -1

<!--Device-camera-interface Focus--><!--Device-camera-interface Focus-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

## getFocalLength

```TypeScript
getFocalLength(): number
```

查询当前的焦距值。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-Focus-getFocalLength(): double--><!--Device-Focus-getFocalLength(): double-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 |
| --- |
| number |

**错误码：**

| 错误码ID |
| --- |
| [7400103](../errorcode-camera.md#7400103-会话未配置) |

## getFocusMode

```TypeScript
getFocusMode(): FocusMode
```

获取当前的对焦模式。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-Focus-getFocusMode(): FocusMode--><!--Device-Focus-getFocusMode(): FocusMode-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 |
| --- |
| [FocusMode](arkts-camera-camera-focusmode-e.md) |

**错误码：**

| 错误码ID |
| --- |
| [7400103](../errorcode-camera.md#7400103-会话未配置) |

## getFocusPoint

```TypeScript
getFocusPoint(): Point
```

查询当前的焦点。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-Focus-getFocusPoint(): Point--><!--Device-Focus-getFocusPoint(): Point-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 |
| --- |
| [Point](../../apis-test-kit/arkts-apis/arkts-test-uitest-point-i.md) |

**错误码：**

| 错误码ID |
| --- |
| [7400103](../errorcode-camera.md#7400103-会话未配置) |

## lockFocusTracking

```TypeScript
lockFocusTracking(focusPoint: Point): void
```

锁定焦点跟踪，使对焦持续追踪指定的物体。通过focusPoint参数指定追踪目标。

**起始版本：** 26.0.0

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-Focus-lockFocusTracking(focusPoint: Point): void--><!--Device-Focus-lockFocusTracking(focusPoint: Point): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| focusPoint | [Point](../../apis-test-kit/arkts-apis/arkts-test-uitest-point-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [7400103](../errorcode-camera.md#7400103-会话未配置) |
| [7400201](../errorcode-camera.md#7400201-相机服务异常) |

## setFocusMode

```TypeScript
setFocusMode(afMode: FocusMode): void
```

设置对焦模式。 进行设置之前，需要先检查设备是否支持指定的焦距模式，可使用方法[isFocusModeSupported](arkts-camera-camera-focusquery-i.md#isFocusModeSupported)。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-Focus-setFocusMode(afMode: FocusMode): void--><!--Device-Focus-setFocusMode(afMode: FocusMode): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| afMode | [FocusMode](arkts-camera-camera-focusmode-e.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [7400103](../errorcode-camera.md#7400103-会话未配置) |

## setFocusPoint

```TypeScript
setFocusPoint(point: Point): void
```

设置焦点，焦点应在0-1坐标系内，该坐标系左上角为{0，0}，右下角为{1，1}。 此坐标系是以设备充电口在右侧时的横向设备方向为基准的，例如应用的预览界面布局以设备充电口在下侧时的竖向方向为基准，布局宽高为{w，h}，且触碰点为{x，y}，则转换后的坐标点为{y/h，1-x/w}。

**起始版本：** 23

**废弃版本：** -1

**原子化服务API：** 从API版本19开始，该接口支持在原子化服务API中使用。

<!--Device-Focus-setFocusPoint(point: Point): void--><!--Device-Focus-setFocusPoint(point: Point): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| point | [Point](../../apis-test-kit/arkts-apis/arkts-test-uitest-point-i.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [7400103](../errorcode-camera.md#7400103-会话未配置) |

## unlockFocusTracking

```TypeScript
unlockFocusTracking(): void
```

解锁焦点跟踪。

**起始版本：** 26.0.0

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

**原子化服务API：** 从API版本26.0.0开始，该接口支持在原子化服务API中使用。

<!--Device-Focus-unlockFocusTracking(): void--><!--Device-Focus-unlockFocusTracking(): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**错误码：**

| 错误码ID |
| --- |
| [7400103](../errorcode-camera.md#7400103-会话未配置) |
| [7400201](../errorcode-camera.md#7400201-相机服务异常) |
