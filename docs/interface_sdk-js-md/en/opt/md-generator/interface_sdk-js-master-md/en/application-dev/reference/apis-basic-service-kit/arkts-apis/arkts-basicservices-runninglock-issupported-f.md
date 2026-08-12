# isSupported

## Modules to Import

```TypeScript
import { runningLock } from '@kit.BasicServicesKit';
```

## isSupported

```TypeScript
function isSupported(type: RunningLockType): boolean
```

Checks whether a specified type of [RunningLock](arkts-basicservices-runninglock-runninglock-c.md#RunningLock) is supported.

**Since:** 9

<!--Device-runningLock-function isSupported(type: RunningLockType): boolean--><!--Device-runningLock-function isSupported(type: RunningLockType): boolean-End-->

**System capability:** SystemCapability.PowerManager.PowerManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | [RunningLockType](arkts-basicservices-runninglock-runninglocktype-e.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| boolean |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |

## Examples

```TypeScript
try {
    let isSupported = runningLock.isSupported(runningLock.RunningLockType.PROXIMITY_SCREEN_CONTROL);
    console.info('BACKGROUND type supported: ' + isSupported);
} catch(err) {
    console.error('check supported failed, err: ' + err);
}
```
