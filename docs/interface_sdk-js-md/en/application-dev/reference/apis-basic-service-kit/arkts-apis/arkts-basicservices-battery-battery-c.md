# Battery

The module allows you to query the charging status and remaining power of a device.

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 6

<!--Device-unnamed-export default class Battery--><!--Device-unnamed-export default class Battery-End-->

**System capability:** SystemCapability.PowerManager.BatteryManager.Lite

## getStatus

```TypeScript
static getStatus(options?: GetStatusOptions): void
```

Obtains the current charging state and battery level.

**Since:** 3

**ArkTS mode:** ArkTS-Dyn only, since version 3.

**Deprecated since:** 6

<!--Device-Battery-static getStatus(options?: GetStatusOptions): void--><!--Device-Battery-static getStatus(options?: GetStatusOptions): void-End-->

**System capability:** SystemCapability.PowerManager.BatteryManager.Lite

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| options | \_\_\_MD\_LINK\_USD\_0\_\_\_ | No | Object that contains the API calling result. This parameter is optional and is left blank by default. |

**Example**

```TypeScript
Battery.getStatus({
    success: (data: BatteryResponse) => {
        console.info('success get battery level:' + data.level);
    },
    fail: (data: string, code: number) => {
        console.error('fail to get battery level code:' + code + ', data: ' + data);
    }
});
```

