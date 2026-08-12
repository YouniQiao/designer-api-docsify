# offConnectionStateChanged

## offConnectionStateChanged

```TypeScript
function offConnectionStateChanged(callback?: Callback<ConnectionResult>): void
```

取消订阅连接状态变更事件。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-dataTransfer-function offConnectionStateChanged(callback?: Callback<ConnectionResult>): void--><!--Device-dataTransfer-function offConnectionStateChanged(callback?: Callback<ConnectionResult>): void-End-->

**系统能力：** SystemCapability.Communication.NearLink.Base

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[ConnectionResult](arkts-connectivity-datatransfer-connectionresult-i.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [801](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#801-该设备不支持此api) |
| [36100099](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/apis-connectivity-kit/errorcode-nearlink-service.md#36100099-操作失败) |
