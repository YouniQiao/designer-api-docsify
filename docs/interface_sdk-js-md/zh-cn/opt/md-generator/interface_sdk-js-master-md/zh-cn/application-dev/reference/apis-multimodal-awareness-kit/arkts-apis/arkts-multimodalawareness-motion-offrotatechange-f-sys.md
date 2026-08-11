# offRotateChange（系统接口）

## offRotateChange

```TypeScript
function offRotateChange(callback?: Callback<RotateEvent>): void
```

取消订阅旋转传感器事件。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-motion-function offRotateChange(callback?: Callback<RotateEvent>): void--><!--Device-motion-function offRotateChange(callback?: Callback<RotateEvent>): void-End-->

**系统能力：** SystemCapability.MultimodalAwareness.Motion

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-arkui/arkts-components/arkts-arkui-callback-i.md)&lt;RotateEvent&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [31500001](../../apis-multimodalawareness-kit/errorcode-motion.md#31500001-服务异常) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
