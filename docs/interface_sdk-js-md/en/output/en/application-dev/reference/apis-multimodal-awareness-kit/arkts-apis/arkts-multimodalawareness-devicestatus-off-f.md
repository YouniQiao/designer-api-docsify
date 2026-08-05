# off

## off('steadyStandingDetect')

```TypeScript
function off(type: 'steadyStandingDetect', callback?: Callback<SteadyStandingStatus>): void
```

Unsubscribes from steady standing state events.

**Since:** 18

**ArkTS mode:** ArkTS-Dyn only, since version 18.

<!--Device-deviceStatus-function off(type: 'steadyStandingDetect', callback?: Callback<SteadyStandingStatus>): void--><!--Device-deviceStatus-function off(type: 'steadyStandingDetect', callback?: Callback<SteadyStandingStatus>): void-End-->

**System capability:** SystemCapability.MultimodalAwareness.DeviceStatus

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| type | 'steadyStandingDetect' | Yes | Event type. This field has a fixed value of **steadyStandingDetect**. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;SteadyStandingStatus&gt; | No | Callback used to return the steady standing state of the device. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. Function can not work correctly due to limited\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_HTML\_\_\_ESCAPED\_UNDERSCORE\_\_\_TAG\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ device capabilities. |
| [32500001](../../apis-multimodalawareness-kit/errorcode-deviceStatus.md#32500001-abnormal-service) | Service exception. |
| [32500003](../../apis-multimodalawareness-kit/errorcode-deviceStatus.md#32500003-unsubscription-failed) | Unsubscription failed. |

**Example**

Example 1: Unsubscribe from all callbacks of steady standing state change events.

```TypeScript
try {
   deviceStatus.off('steadyStandingDetect');
} catch (err) {
   console.error('off failed, err = ' + err);
}
```

Example 2: Unsubscribe from a specific callback of steady standing state change events.

```TypeScript
// Define the callback variable.
let callback : Callback<deviceStatus.SteadyStandingStatus> = (data : deviceStatus. SteadyStandingStatus) => {
   console.info('succeed to get status, now status = ' + data);
};
// Subscribe to a specific callback of steady standing state change events.
try {
   deviceStatus.on('steadyStandingDetect', callback);
} catch (err) {
   console.error('on failed, err = ' + err);
}
// Unsubscribe from the specific callback of steady standing state change events.
try {
   deviceStatus.off('steadyStandingDetect', callback);
} catch (err) {
   console.error('off failed, err = ' + err);
}
```

