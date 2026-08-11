# enableAirplaneMode

## Modules to Import

```TypeScript
import { settings } from 'kits/@kit.BasicServicesKit';
```

## enableAirplaneMode

```TypeScript
function enableAirplaneMode(enable: boolean, callback: AsyncCallback<void>): void
```

Enables or disables airplane mode.

**Since:** 7

**Deprecated since:** 26.0.0

<!--Device-settings-function enableAirplaneMode(enable: boolean, callback: AsyncCallback<void>): void--><!--Device-settings-function enableAirplaneMode(enable: boolean, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Applications.Settings.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enable | boolean | Yes |
| callback | [AsyncCallback](arkts-basicservices-base-asynccallback-i.md)&lt;void&gt; | Yes |

## Examples

```TypeScript
let isEnabled :boolean = true;
settings.enableAirplaneMode(isEnabled, (err:Error) => {
    if (err) {
        console.error('Failed to enable AirplaneMode.');
        return;
    }
    console.info('Return true if enable.');
})
```


## enableAirplaneMode

```TypeScript
function enableAirplaneMode(enable: boolean): Promise<void>
```

Enables or disables airplane mode.

**Since:** 7

**Deprecated since:** 26.0.0

<!--Device-settings-function enableAirplaneMode(enable: boolean): Promise<void>--><!--Device-settings-function enableAirplaneMode(enable: boolean): Promise<void>-End-->

**System capability:** SystemCapability.Applications.Settings.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| enable | boolean | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;void&gt; |

## Examples

```TypeScript
let isEnabled :boolean = true;
settings.enableAirplaneMode(isEnabled).then(() => {
  console.info('Succeeded in enabling AirplaneMode.');
}).catch((err:Error) => {
  console.error(`Failed to enable AirplaneMode. Cause: ${err}`);
})
```
