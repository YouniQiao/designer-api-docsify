# getCameraTrackingLayout

## getCameraTrackingLayout

```TypeScript
function getCameraTrackingLayout(): CameraTrackingLayout
```

获取当前摄像头跟踪布局

**起始版本：** 20

<!--Device-mechanicManager-function getCameraTrackingLayout(): CameraTrackingLayout--><!--Device-mechanicManager-function getCameraTrackingLayout(): CameraTrackingLayout-End-->

**系统能力：** SystemCapability.Mechanic.Core

**返回值：**

| 类型 |
| --- |
| [CameraTrackingLayout](arkts-mechanic-mechanicmanager-cameratrackinglayout-e.md) |

**错误码：**

| 错误码ID |
| --- |
| [33300001](../errorcode-mechanic.md#33300001-系统错误) |
| [33300002](../errorcode-mechanic.md#33300002-设备未连接) |

## 示例

```TypeScript
console.info('Query layout');
// 调用getCameraTrackingLayout方法获取当前摄像头跟踪布局
let layout = mechanicManager.getCameraTrackingLayout();
console.info(`'Succeeded in querying layout, current layout:' ${layout}`);
```
