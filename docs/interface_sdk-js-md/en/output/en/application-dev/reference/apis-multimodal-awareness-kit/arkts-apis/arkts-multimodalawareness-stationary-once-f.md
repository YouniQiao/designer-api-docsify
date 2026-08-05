# once

## once

```TypeScript
function once(activity: ActivityType, callback: Callback<ActivityResponse>): void
```

Obtains the device status.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

<!--Device-stationary-function once(activity: ActivityType, callback: Callback<ActivityResponse>): void--><!--Device-stationary-function once(activity: ActivityType, callback: Callback<ActivityResponse>): void-End-->

**System capability:** SystemCapability.Msdp.DeviceStatus.Stationary

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| activity | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Device status type. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;ActivityResponse&gt; | Yes | Callback used to receive reported data. |

**Example**

```TypeScript
stationary.once('still', (data) => {
    console.info('data=' + JSON.stringify(data));
})
```

