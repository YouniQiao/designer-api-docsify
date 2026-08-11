# on

## on('steadyStandingDetect')

```TypeScript
function on(type: 'steadyStandingDetect', callback: Callback<SteadyStandingStatus>): void
```

订阅设备静止姿态感知（支架态）事件。建议在不需要时调用off()取消订阅，释放资源。

**起始版本：** 18

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为18。

<!--Device-deviceStatus-function on(type: 'steadyStandingDetect', callback: Callback<SteadyStandingStatus>): void--><!--Device-deviceStatus-function on(type: 'steadyStandingDetect', callback: Callback<SteadyStandingStatus>): void-End-->

**系统能力：** SystemCapability.MultimodalAwareness.DeviceStatus

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | 'steadyStandingDetect' | 是 | 事件类型。type为“steadyStandingDetect”，表示设备静止姿态（支架态）感知。 |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;SteadyStandingStatus&gt; | 是 | 回调函数，用于接收设备静止姿态（支架态）状态信息。 |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) | Capability not supported. Function can not work correctly due to limited &lt;br&gt; device capabilities. |
| [32500002](../../apis-multimodalawareness-kit/errorcode-deviceStatus.md#32500002-订阅失败) | Subscription failed. |
| [32500001](../../apis-multimodalawareness-kit/errorcode-deviceStatus.md#32500001-服务异常) | Service exception. |

## 示例

```TypeScript
try {
   deviceStatus.on('steadyStandingDetect', (data:deviceStatus.SteadyStandingStatus) => {
      console.info('succeed to get status, now status = ' + data);
   });
} catch (err) {
   console.error('on failed, err = ' + err);
}
```

