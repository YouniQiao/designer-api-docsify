# setPowerKeyFilteringStrategy (System API)

## Modules to Import

```TypeScript
import { power } from '@kit.BasicServicesKit';
```

## setPowerKeyFilteringStrategy

```TypeScript
function setPowerKeyFilteringStrategy(strategy: PowerKeyFilteringStrategy): void
```

Sets the power key filtering strategy. After the power service subscribes to the power key event, this API is used to configure the processing mode of this event. For details about the power key filtering strategy, see [power.PowerKeyFilteringStrategy](arkts-basicservices-power-powerkeyfilteringstrategy-e.md#PowerKeyFilteringStrategy).

**Since:** 23

**Deprecated since:** -1

**Required permissions:** ohos.permission.POWER_MANAGER

<!--Device-power-function setPowerKeyFilteringStrategy(strategy: PowerKeyFilteringStrategy): void--><!--Device-power-function setPowerKeyFilteringStrategy(strategy: PowerKeyFilteringStrategy): void-End-->

**System capability:** SystemCapability.PowerManager.PowerManager.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| strategy | [PowerKeyFilteringStrategy](arkts-basicservices-power-powerkeyfilteringstrategy-e.md) | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [4900101](../../apis-basic-services-kit/errorcode-power.md#4900101-service-connection-failure) |

## Examples

```TypeScript
try {
    power.setPowerKeyFilteringStrategy(power.PowerKeyFilteringStrategy.LONG_PRESS_FILTERING_ONCE);
} catch(err) {
    console.error('setPowerKeyFilteringStrategy failed, err: ' + err);
}
```
