# offAcbStateChange

## offAcbStateChange

```TypeScript
function offAcbStateChange(callback?: Callback<AcbStateParam>): void
```

取消订阅星闪 ACB连接状态更改事件。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-remoteDevice-function offAcbStateChange(callback?: Callback<AcbStateParam>): void--><!--Device-remoteDevice-function offAcbStateChange(callback?: Callback<AcbStateParam>): void-End-->

**系统能力：** SystemCapability.Communication.NearLink.Base

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;AcbStateParam&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../errorcode-universal.md#801-该设备不支持此api) |
| [36100099](../errorcode-nearlink-service.md#36100099-操作失败) |
