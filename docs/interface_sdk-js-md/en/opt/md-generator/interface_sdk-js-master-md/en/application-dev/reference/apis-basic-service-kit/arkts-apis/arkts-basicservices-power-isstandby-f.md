# isStandby

## Modules to Import

```TypeScript
```

## isStandby

```TypeScript
function isStandby(): boolean
```

Checks whether the device is in standby mode.

**Since:** 23

<!--Device-power-function isStandby(): boolean--><!--Device-power-function isStandby(): boolean-End-->

**System capability:** SystemCapability.PowerManager.PowerManager.Core

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [4900101](../../apis-basic-services-kit/errorcode-power.md#4900101-service-connection-failure) |

**Examples**

```TypeScript
try {
    let isStandby = power.isStandby();
    console.info('device is in standby: ' + isStandby);
} catch(err) {
    console.error('check isStandby failed, err: ' + err);
}
```
