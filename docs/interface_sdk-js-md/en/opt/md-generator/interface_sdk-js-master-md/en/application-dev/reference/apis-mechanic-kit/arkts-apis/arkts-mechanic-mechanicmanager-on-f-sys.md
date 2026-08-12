# on (System API)

## Modules to Import

```TypeScript
import { mechanicManager } from '@kit.MechanicKit';
```

## on('rotationAxesStatusChange')

```TypeScript
function on(type: 'rotationAxesStatusChange', callback: Callback<RotationAxesStateChangeInfo>): void
```

Register a listener for axis state changes.The status of the rotation axis changes dynamically, which needs to be monitored.

**Since:** 20

<!--Device-mechanicManager-function on(type: 'rotationAxesStatusChange', callback: Callback<RotationAxesStateChangeInfo>): void--><!--Device-mechanicManager-function on(type: 'rotationAxesStatusChange', callback: Callback<RotationAxesStateChangeInfo>): void-End-->

**System capability:** SystemCapability.Mechanic.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| type | 'rotationAxesStatusChange' | Yes |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[RotationAxesStateChangeInfo](arkts-mechanic-mechanicmanager-rotationaxesstatechangeinfo-i-sys.md)&gt; | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [33300001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-mechanic-kit/errorcode-mechanic.md#33300001-system-error) |

## Examples

```TypeScript
console.info('Register Axis Status listener');
mechanicManager.on("rotationAxesStatusChange", (result: mechanicManager.RotationAxesStateChangeInfo) => {
  console.info(`'result:' ${result}`);
});
console.info('Successful registration');
```
