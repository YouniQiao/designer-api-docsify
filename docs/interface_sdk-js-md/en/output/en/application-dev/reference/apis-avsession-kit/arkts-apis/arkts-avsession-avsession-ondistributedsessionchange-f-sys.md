# onDistributedSessionChange (System API)

## onDistributedSessionChange

```TypeScript
function onDistributedSessionChange(distributedSessionType: DistributedSessionType, callback: Callback<Array<AVSessionController>>): void
```

Register distributed session changed callback

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-avSession-function onDistributedSessionChange(distributedSessionType: DistributedSessionType, callback: Callback<Array<AVSessionController>>): void--><!--Device-avSession-function onDistributedSessionChange(distributedSessionType: DistributedSessionType, callback: Callback<Array<AVSessionController>>): void-End-->

**System capability:** SystemCapability.Multimedia.AVSession.Manager

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| distributedSessionType | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Indicates the distributed session type |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;Array&lt;AVSessionController&gt;&gt; | Yes | The callback will return remote changed AVSessionController. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not System App. |
| [6600101](../errorcode-avsession.md#6600101-session-service-exception) | Session service exception. |

