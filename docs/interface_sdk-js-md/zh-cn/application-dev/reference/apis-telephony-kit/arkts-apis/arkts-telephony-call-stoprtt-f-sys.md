# stopRtt（系统接口）

## stopRtt

```TypeScript
function stopRtt(callId: int, type: ImsRttMode): Promise<void>
```

停止rtt

**起始版本：** 22

**ArkTS模式：** ArkTS-Dyn起始版本为22；ArkTS-Sta起始版本为23。

**需要权限：** ohos.permission.PLACE_CALL

<!--Device-call-function stopRtt(callId: int, type: ImsRttMode): Promise<void>--><!--Device-call-function stopRtt(callId: int, type: ImsRttMode): Promise<void>-End-->

**系统能力：** SystemCapability.Telephony.CallManager

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callId | ArkTS-Dyn: number  <br>ArkTS-Sta：int | 是 | Indicates the identifier of the call. |
| type | [ImsRttMode](arkts-telephony-call-imsrttmode-e-sys.md) | 是 | Indicates the type of operation. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;void&gt; | The promise returned by the stopRtt. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 8400001 | Invalid parameter value. |
| 8400002 | Operation failed. Cannot connect to service. |
| 8400003 | System internal error. |
| 8400999 | Unknown error code. |
| [201](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/errorcode-universal.md#201-权限校验失败) | Permission denied. |
| [202](../../../../../../../../gitee_tmp/docs/stamaster/zh-cn/application-dev/reference/errorcode-universal.md#202-系统api权限校验失败) | Non-system applications use system APIs. |

