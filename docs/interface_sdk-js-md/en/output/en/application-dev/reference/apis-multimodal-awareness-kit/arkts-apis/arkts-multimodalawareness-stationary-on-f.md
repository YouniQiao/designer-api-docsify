# on

## on

```TypeScript
function on(activity: ActivityType, event: ActivityEvent, reportLatencyNs: number, callback: Callback<ActivityResponse>): void
```

Subscribes to the device status.

**Since:** 9

**ArkTS mode:** ArkTS-Dyn only, since version 9.

<!--Device-stationary-function on(activity: ActivityType, event: ActivityEvent, reportLatencyNs: number, callback: Callback<ActivityResponse>): void--><!--Device-stationary-function on(activity: ActivityType, event: ActivityEvent, reportLatencyNs: number, callback: Callback<ActivityResponse>): void-End-->

**System capability:** SystemCapability.Msdp.DeviceStatus.Stationary

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| activity | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Device status type. |
| event | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Event type. |
| reportLatencyNs | number | Yes | Report delay, in ns. The value ranges from **1000000000** to **3000000000**. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;ActivityResponse&gt; | Yes | Callback used to receive reported data. |

**Example**

```TypeScript
let reportLatencyNs = 1000000000;
stationary.on('still', stationary.ActivityEvent.ENTER, reportLatencyNs, (data) => {
    console.info('data=' + JSON.stringify(data));
})
```

