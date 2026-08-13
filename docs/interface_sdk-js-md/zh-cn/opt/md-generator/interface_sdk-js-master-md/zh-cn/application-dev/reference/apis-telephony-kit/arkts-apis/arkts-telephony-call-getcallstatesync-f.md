# getCallStateSync

## getCallStateSync

```TypeScript
function getCallStateSync(): CallState
```

获取当前通话状态。

**起始版本：** 10

<!--Device-call-function getCallStateSync(): CallState--><!--Device-call-function getCallStateSync(): CallState-End-->

**系统能力：** SystemCapability.Telephony.CallManager

**返回值：**

| 类型 |
| --- |
| [CallState](arkts-telephony-call-callstate-e.md) |

## 示例

```TypeScript
let callState: call.CallState = call.getCallStateSync();
console.info(`the call state is:` + callState);
```
