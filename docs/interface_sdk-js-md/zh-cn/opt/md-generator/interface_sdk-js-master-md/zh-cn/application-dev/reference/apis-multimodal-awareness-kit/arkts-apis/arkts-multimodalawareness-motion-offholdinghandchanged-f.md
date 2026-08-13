# offHoldingHandChanged

## offHoldingHandChanged

```TypeScript
function offHoldingHandChanged(callback?: Callback<HoldingHandStatus>): void
```

取消订阅握持手状态变化事件。

**起始版本：** 23

**废弃版本：** -1

**需要权限：** ohos.permission.DETECT_GESTURE

<!--Device-motion-function offHoldingHandChanged(callback?: Callback<HoldingHandStatus>): void--><!--Device-motion-function offHoldingHandChanged(callback?: Callback<HoldingHandStatus>): void-End-->

**系统能力：** SystemCapability.MultimodalAwareness.Motion

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[HoldingHandStatus](arkts-multimodalawareness-motion-holdinghandstatus-e.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [31500001](../../apis-multimodalawareness-kit/errorcode-motion.md#31500001-服务异常) |
| [31500003](../../apis-multimodalawareness-kit/errorcode-motion.md#31500003-取消订阅失败) |
| [201](../../errorcode-universal.md#201-权限校验失败) |
