# onRttModifyInd（系统接口）

## onRttModifyInd

```TypeScript
function onRttModifyInd(callback: Callback<RttEventInfo>): void
```

订阅rtt通话变化

**起始版本：** 22

**需要权限：** ohos.permission.SET_TELEPHONY_STATE

<!--Device-call-function onRttModifyInd(callback: Callback<RttEventInfo>): void--><!--Device-call-function onRttModifyInd(callback: Callback<RttEventInfo>): void-End-->

**系统能力：** SystemCapability.Telephony.CallManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[RttEventInfo](arkts-telephony-call-rtteventinfo-i-sys.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| 8400001 |
| 8400002 |
| 8400003 |
| 8400999 |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |
