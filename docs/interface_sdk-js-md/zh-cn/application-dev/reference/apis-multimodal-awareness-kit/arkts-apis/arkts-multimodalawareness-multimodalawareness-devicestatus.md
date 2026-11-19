# @ohos.multimodalAwareness.deviceStatus(设备状态感知)

**deviceStatus**本模块提供对设备状态的感知能力，通过传感器实时感知设备物理状态，可帮助开发者根据设备物理状态调整应用行为。

**起始版本：** 18

<!--Device-unnamed-declare namespace deviceStatus--><!--Device-unnamed-declare namespace deviceStatus-End-->

**系统能力：** SystemCapability.MultimodalAwareness.DeviceStatus

## 导入模块

```TypeScript
import { deviceStatus } from '@kit.MultimodalAwarenessKit';
```

## 汇总

### 函数

| 名称 | 说明 |
| --- | --- |
| [off('steadyStandingDetect')](arkts-multimodalawareness-devicestatus-off-f.md#offsteadystandingdetect) | 取消订阅设备静止姿态感知（支架态）事件，用于应用在退出页面或不再需要监听支架态变化的场景。调用后释放相关资源。 |
| [offDropDetect](arkts-multimodalawareness-devicestatus-offdropdetect-f.md#offdropdetect-1) | 取消订阅设备跌落检测事件。用于应用在退出页面或不再需要监听跌落事件的场景。调用后释放相关资源。若未调用onDropDetect()就调用offDropDetect()，该方法会抛出异常。 |
| [on('steadyStandingDetect')](arkts-multimodalawareness-devicestatus-on-f.md#onsteadystandingdetect) | 订阅设备静止姿态感知（支架态）事件。建议在不需要时调用off()取消订阅，释放资源。 |
| [onDropDetect](arkts-multimodalawareness-devicestatus-ondropdetect-f.md#ondropdetect-1) | 订阅设备跌落检测事件。当应用需要检测设备是否发生跌落时使用。调用onDropDetect订阅后，系统开始监听加速度传感器数据。当检测到符合跌落特征的加速度变化时，触发STATUS_DROPPED回调。同一回调实例不可重复订阅，需先调用offDropDetect取消后再订阅。建议在不需要监听时调用offDropDetect()取消订阅，释放资源。 |

<!--Del-->
### 函数（系统接口）

| 名称 | 说明 |
| --- | --- |
| [getDeviceRotationRadian](arkts-multimodalawareness-devicestatus-getdevicerotationradian-f-sys.md#getdevicerotationradian-1) | 获取设备的姿态数据。 |
<!--DelEnd-->

<!--Del-->
### 接口（系统接口）

| 名称 | 说明 |
| --- | --- |
| [DeviceRotationRadian](arkts-multimodalawareness-devicestatus-devicerotationradian-i-sys.md) | 设备旋转弧度接口。 |
<!--DelEnd-->

### 枚举

| 名称 | 说明 |
| --- | --- |
| [DropDetectionStatus](arkts-multimodalawareness-devicestatus-dropdetectionstatus-e.md) | 定义设备的跌落检测状态。 |
| [SteadyStandingStatus](arkts-multimodalawareness-devicestatus-steadystandingstatus-e.md) | 设备静止姿态感知状态（支架态）。 |
