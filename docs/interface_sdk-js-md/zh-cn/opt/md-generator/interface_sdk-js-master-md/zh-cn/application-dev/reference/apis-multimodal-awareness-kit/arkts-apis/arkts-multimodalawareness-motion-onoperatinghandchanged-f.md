# onOperatingHandChanged

## onOperatingHandChanged

```TypeScript
function onOperatingHandChanged(callback: Callback<OperatingHandStatus>): void
```

订阅触控操作手变化事件。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.ACTIVITY_MOTION or ohos.permission.DETECT_GESTURE

<!--Device-motion-function onOperatingHandChanged(callback: Callback<OperatingHandStatus>): void--><!--Device-motion-function onOperatingHandChanged(callback: Callback<OperatingHandStatus>): void-End-->

**系统能力：** SystemCapability.MultimodalAwareness.Motion

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[OperatingHandStatus](arkts-multimodalawareness-motion-operatinghandstatus-e.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [31500001](../../apis-multimodalawareness-kit/errorcode-motion.md#31500001-服务异常) |
| [31500002](../../apis-multimodalawareness-kit/errorcode-motion.md#31500002-订阅失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
