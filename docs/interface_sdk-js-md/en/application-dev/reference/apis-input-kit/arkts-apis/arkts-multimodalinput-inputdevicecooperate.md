# @ohos.multimodalInput.inputDeviceCooperate(Screen Hopping)

键鼠穿越功能模块，提供两台或多台设备组网协同后键鼠共享能力，实现键鼠输入设备的跨设备协同操作。

> **说明：**
> 
> - 本模块接口从API Version 10开始不再维护，从API version 23开始废弃，推荐使用新接口[@ohos.cooperate](../../apis-distributed-service-kit/arkts-apis/arkts-cooperate.md/arkts-cooperate.md) (键鼠穿越)。
> 
> - 本模块接口均为系统接口。

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

**Deprecated since:** 23

**Substitutes:** ohos.cooperate/cooperate

<!--Device-unnamed-declare namespace inputDeviceCooperate--><!--Device-unnamed-declare namespace inputDeviceCooperate-End-->

**System capability:** SystemCapability.MultimodalInput.Input.Cooperator

## Modules to Import

```TypeScript
import { inputDeviceCooperate } from 'kits/@kit.InputKit';
```

## Summary

<!--Del-->
### Functions（系统接口）

| Name | Description |
| --- | --- |
| [enable](arkts-input-inputdevicecooperate-enable-f-sys.md#enable) | 开启、关闭键鼠穿越，使用callback异步回调。 |
| [enable](arkts-input-inputdevicecooperate-enable-f-sys.md#enable-1) | 开启、关闭键鼠穿越，使用Promise异步回调。 |
| [getState](arkts-input-inputdevicecooperate-getstate-f-sys.md#getstate) | 获取键鼠穿越开关的状态，使用callback异步回调。 |
| [getState](arkts-input-inputdevicecooperate-getstate-f-sys.md#getstate-1) | 获取键鼠穿越开关的状态，使用Promise异步回调。 |
| [off](arkts-input-inputdevicecooperate-off-f-sys.md#off) | 关闭监听键鼠穿越状态，使用callback异步回调。 |
| [on](arkts-input-inputdevicecooperate-on-f-sys.md#on) | 注册监听键鼠穿越状态，使用callback异步回调。 |
| [start](arkts-input-inputdevicecooperate-start-f-sys.md#start) | 启动键鼠穿越，使用callback异步回调。 |
| [start](arkts-input-inputdevicecooperate-start-f-sys.md#start-1) | 启动键鼠穿越，使用Promise异步回调。 |
| [stop](arkts-input-inputdevicecooperate-stop-f-sys.md#stop) | 停止键鼠穿越，使用callback异步回调。 |
| [stop](arkts-input-inputdevicecooperate-stop-f-sys.md#stop-1) | 停止键鼠穿越，使用Promise异步回调。 |
<!--DelEnd-->

<!--Del-->
### Enums（系统接口）

| Name | Description |
| --- | --- |
| [EventMsg](arkts-input-inputdevicecooperate-eventmsg-e-sys.md) | 键鼠穿越事件。 |
<!--DelEnd-->

