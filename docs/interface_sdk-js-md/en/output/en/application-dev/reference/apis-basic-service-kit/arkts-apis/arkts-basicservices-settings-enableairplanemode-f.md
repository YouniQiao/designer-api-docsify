# enableAirplaneMode

## enableAirplaneMode

```TypeScript
function enableAirplaneMode(enable: boolean, callback: AsyncCallback<void>): void
```

Enables or disables airplane mode.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Deprecated since:** 26.0.0

<!--Device-settings-function enableAirplaneMode(enable: boolean, callback: AsyncCallback<void>): void--><!--Device-settings-function enableAirplaneMode(enable: boolean, callback: AsyncCallback<void>): void-End-->

**System capability:** SystemCapability.Applications.Settings.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enable | boolean | Yes | Specifies whether to enable airplane mode. The value {@code true} means to enable airplane mode, and {@code false} means to disable airplane mode. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;void&gt; | Yes | The callback of enableAirplaneMode result. |

**Example**

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

**ArkTS mode:** ArkTS-Dyn since version 7; ArkTS-Sta since version 23.

**Deprecated since:** 26.0.0

<!--Device-settings-function enableAirplaneMode(enable: boolean): Promise<void>--><!--Device-settings-function enableAirplaneMode(enable: boolean): Promise<void>-End-->

**System capability:** SystemCapability.Applications.Settings.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| enable | boolean | Yes | Specifies whether to enable airplane mode. The value {@code true} means to enable airplane mode, and {@code false} means to disable airplane mode. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;void&gt; | - Return Promise. |

**Example**

```TypeScript
let isEnabled :boolean = true;
settings.enableAirplaneMode(isEnabled).then(() => {
  console.info('Succeeded in enabling AirplaneMode.');
}).catch((err:Error) => {
  console.error(`Failed to enable AirplaneMode. Cause: ${err}`);
})
```

