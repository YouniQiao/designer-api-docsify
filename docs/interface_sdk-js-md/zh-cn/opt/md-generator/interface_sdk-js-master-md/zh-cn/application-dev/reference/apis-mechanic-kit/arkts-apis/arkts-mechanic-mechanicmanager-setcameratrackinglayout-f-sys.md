# setCameraTrackingLayout（系统接口）

## setCameraTrackingLayout

```TypeScript
function setCameraTrackingLayout(trackingLayout: CameraTrackingLayout): void
```

设置相机跟踪布局

**起始版本：** 20

<!--Device-mechanicManager-function setCameraTrackingLayout(trackingLayout: CameraTrackingLayout): void--><!--Device-mechanicManager-function setCameraTrackingLayout(trackingLayout: CameraTrackingLayout): void-End-->

**系统能力：** SystemCapability.Mechanic.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| trackingLayout | [CameraTrackingLayout](arkts-mechanic-mechanicmanager-cameratrackinglayout-e.md) | 是 |

**错误码：**

| 错误码ID |
| --- |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
| [33300001](../errorcode-mechanic.md#33300001-系统错误) |
| [33300002](../errorcode-mechanic.md#33300002-设备未连接) |
| [33300003](../errorcode-mechanic.md#33300003-功能不支持) |

## 示例

```TypeScript
console.info('Set layout');
mechanicManager.setCameraTrackingLayout(mechanicManager.CameraTrackingLayout.LEFT);
console.info('Set layout successful');
```
