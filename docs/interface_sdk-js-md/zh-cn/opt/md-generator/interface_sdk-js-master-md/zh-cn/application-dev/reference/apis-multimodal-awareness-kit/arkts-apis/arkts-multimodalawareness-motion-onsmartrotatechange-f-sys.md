# onSmartRotateChange（系统接口）

## 导入模块

```TypeScript
```

## onSmartRotateChange

```TypeScript
function onSmartRotateChange(callback: Callback<SmartRotateEvent>): void
```

订阅智能旋转传感器事件。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-motion-function onSmartRotateChange(callback: Callback<SmartRotateEvent>): void--><!--Device-motion-function onSmartRotateChange(callback: Callback<SmartRotateEvent>): void-End-->

**系统能力：** SystemCapability.MultimodalAwareness.Motion

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[SmartRotateEvent](arkts-multimodalawareness-motion-smartrotateevent-i-sys.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [31500001](../../apis-multimodalawareness-kit/errorcode-motion.md#31500001-服务异常) |
| [202](../../errorcode-universal.md#202-系统api权限校验失败) |
