# off

## 导入模块

```TypeScript
import { deviceStatus } from 'kits/@kit.MultimodalAwarenessKit';
```

## off('steadyStandingDetect')

```TypeScript
function off(type: 'steadyStandingDetect', callback?: Callback<SteadyStandingStatus>): void
```

Unsubscribes from steady standing state events.

**起始版本：** 18

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为18。

<!--Device-deviceStatus-function off(type: 'steadyStandingDetect', callback?: Callback<SteadyStandingStatus>): void--><!--Device-deviceStatus-function off(type: 'steadyStandingDetect', callback?: Callback<SteadyStandingStatus>): void-End-->

**系统能力：** SystemCapability.MultimodalAwareness.DeviceStatus

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'steadyStandingDetect' | 是 | Event type. This field has a fixed value of **steadyStandingDetect**. |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;SteadyStandingStatus&gt; | 否 | Callback used to return the steady standing state of the device. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. Function can not work correctly due to limited &lt;br&gt; device capabilities. |
| 32500003 | Unsubscription failed. |
| 32500001 | Service exception. |

## 示例

示例一：取消订阅该客户端订阅设备静止姿态感知（支架态）事件的所有回调。

```TypeScript
try {
   deviceStatus.off('steadyStandingDetect');
} catch (err) {
   console.error(`off failed, err = ${err}`);
}
```

示例二：取消订阅该客户端订阅设备静止姿态感知（支架态）事件的特定回调。

```TypeScript
// 定义callback变量
let callback : Callback<deviceStatus.SteadyStandingStatus> = (data : deviceStatus.SteadyStandingStatus) => {
   console.info('succeeded to get status, now status = ' + JSON.stringify(data));
};
// 以callback为回调函数，订阅设备静止姿态感知（支架态）事件
try {
   deviceStatus.on('steadyStandingDetect', callback);
} catch (err) {
   console.error(`on failed. Code: ${err.code}, message: ${err.message}`);
}
// 取消该客户端订阅设备静止姿态感知（支架态）事件的特定回调函数
try {
   deviceStatus.off('steadyStandingDetect', callback);
} catch (err) {
   console.error(`off failed. Code: ${err.code}, message: ${err.message}`);
}
```

