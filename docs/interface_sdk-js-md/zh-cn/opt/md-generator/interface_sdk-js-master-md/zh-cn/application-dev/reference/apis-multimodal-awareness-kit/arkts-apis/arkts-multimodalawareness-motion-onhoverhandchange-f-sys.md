# onHoverHandChange（系统接口）

## onHoverHandChange

```TypeScript
function onHoverHandChange(detectionArea: HoverHandDetectionArea, callback: Callback<HoverHandAction>): void
```

订阅悬停手势事件，并立即开始5秒检测。

**起始版本：** 26.0.0

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-motion-function onHoverHandChange(detectionArea: HoverHandDetectionArea, callback: Callback<HoverHandAction>): void--><!--Device-motion-function onHoverHandChange(detectionArea: HoverHandDetectionArea, callback: Callback<HoverHandAction>): void-End-->

**系统能力：** SystemCapability.MultimodalAwareness.Motion

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| detectionArea | [HoverHandDetectionArea](arkts-multimodalawareness-motion-hoverhanddetectionarea-i-sys.md) | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[HoverHandAction](arkts-multimodalawareness-motion-hoverhandaction-e-sys.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [31500001](../../apis-multimodalawareness-kit/errorcode-motion.md#31500001-服务异常) |
| [31500002](../../apis-multimodalawareness-kit/errorcode-motion.md#31500002-订阅失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |


## onHoverHandChange

```TypeScript
function onHoverHandChange(
    detectionArea: HoverHandDetectionArea, duration: number, callback: Callback<HoverHandAction>): void
```

订阅悬停手势事件，并立即开始检测。

**起始版本：** 26.0.0

**废弃版本：** -1

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-motion-function onHoverHandChange(    detectionArea: HoverHandDetectionArea, duration: int, callback: Callback<HoverHandAction>): void--><!--Device-motion-function onHoverHandChange(    detectionArea: HoverHandDetectionArea, duration: int, callback: Callback<HoverHandAction>): void-End-->

**系统能力：** SystemCapability.MultimodalAwareness.Motion

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| detectionArea | [HoverHandDetectionArea](arkts-multimodalawareness-motion-hoverhanddetectionarea-i-sys.md) | 是 |
| duration | number | 是 |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[HoverHandAction](arkts-multimodalawareness-motion-hoverhandaction-e-sys.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [31500001](../../apis-multimodalawareness-kit/errorcode-motion.md#31500001-服务异常) |
| [31500002](../../apis-multimodalawareness-kit/errorcode-motion.md#31500002-订阅失败) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
