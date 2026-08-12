# on

## on('steadyStandingDetect')

```TypeScript
function on(type: 'steadyStandingDetect', callback: Callback<SteadyStandingStatus>): void
```

订阅设备静止姿态感知（支架态）事件。建议在不需要时调用off()取消订阅，释放资源。

**起始版本：** 18

<!--Device-deviceStatus-function on(type: 'steadyStandingDetect', callback: Callback<SteadyStandingStatus>): void--><!--Device-deviceStatus-function on(type: 'steadyStandingDetect', callback: Callback<SteadyStandingStatus>): void-End-->

**系统能力：** SystemCapability.MultimodalAwareness.DeviceStatus

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'steadyStandingDetect' | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[SteadyStandingStatus](arkts-multimodalawareness-devicestatus-steadystandingstatus-e.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#801-该设备不支持此api) |
| [32500002](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-multimodalawareness-kit/errorcode-deviceStatus.md#32500002-订阅失败) |
| [32500001](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-multimodalawareness-kit/errorcode-deviceStatus.md#32500001-服务异常) |

## 示例

```TypeScript
try {
   deviceStatus.on('steadyStandingDetect', (data:deviceStatus.SteadyStandingStatus) => {
      console.info(`succeeded to get status, now status = ${JSON.stringify(data)}`);
   });
} catch (err) {
   console.error(`on failed. Code: ${err.code}, message: ${err.message}`);
}
```
