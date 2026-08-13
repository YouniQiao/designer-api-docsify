# preloadCallUI（系统接口）

## preloadCallUI

```TypeScript
function preloadCallUI(): Promise<boolean>
```

预加载通话应用

**起始版本：** 24

**需要权限：** ohos.permission.SET_TELEPHONY_STATE

<!--Device-call-function preloadCallUI(): Promise<boolean>--><!--Device-call-function preloadCallUI(): Promise<boolean>-End-->

**系统能力：** SystemCapability.Telephony.CallManager

**系统接口：** 此接口为系统接口。

**返回值：**

| 类型 |
| --- |
| Promise & lt;boolean & gt; |

**错误码：**

| 错误码ID |
| --- |
| 8400001 |
| 8400002 |
| 8400003 |
| 8400999 |
| [201](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) |
| [202](../../../../../../../../gitee_tmp/docs/master/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) |
