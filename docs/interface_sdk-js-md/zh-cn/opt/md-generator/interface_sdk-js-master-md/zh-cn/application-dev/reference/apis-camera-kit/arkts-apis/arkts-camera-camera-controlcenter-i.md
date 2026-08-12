# ControlCenter

ControlCenter继承自[ControlCenterQuery](arkts-camera-camera-controlcenterquery-i.md#ControlCenterQuery)。

控制中心类，用于使能相机控制器。

**继承/实现关系：** ControlCenter extends [ControlCenterQuery](arkts-camera-camera-controlcenterquery-i.md#ControlCenterQuery)

**起始版本：** 20

<!--Device-camera-interface ControlCenter extends ControlCenterQuery--><!--Device-camera-interface ControlCenter extends ControlCenterQuery-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

## enableControlCenter

```TypeScript
enableControlCenter(enabled: boolean): void
```

使能相机控制器。

**起始版本：** 20

**原子化服务API：** 从API版本20开始，该接口支持在原子化服务API中使用。

<!--Device-ControlCenter-enableControlCenter(enabled: boolean): void--><!--Device-ControlCenter-enableControlCenter(enabled: boolean): void-End-->

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| enabled | boolean | 是 |

**错误码：**

| 错误码ID |
| --- |
| [7400103](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-camera-kit/errorcode-camera.md#7400103-会话未配置) |
