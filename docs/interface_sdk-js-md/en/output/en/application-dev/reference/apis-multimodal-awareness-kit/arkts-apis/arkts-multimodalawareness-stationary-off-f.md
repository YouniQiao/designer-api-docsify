# off

## off

```TypeScript
function off(activity: ActivityType, event: ActivityEvent, callback?: Callback<ActivityResponse>): void
```

Unsubscribes from the device status.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

<!--Device-stationary-function off(activity: ActivityType, event: ActivityEvent, callback?: Callback<ActivityResponse>): void--><!--Device-stationary-function off(activity: ActivityType, event: ActivityEvent, callback?: Callback<ActivityResponse>): void-End-->

**System capability:** SystemCapability.Msdp.DeviceStatus.Stationary

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| activity | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Device status type. |
| event | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Event type. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;ActivityResponse&gt; | No | Callback used to receive reported data. If no value or **undefined** is passed, all callbacks associated with the specified event in the process will be unregistered. |

**Example**

```TypeScript
stationary.off('still', stationary.ActivityEvent.ENTER);
```

