# getURI

## getURI

```TypeScript
function getURI(name: string, callback: AsyncCallback<object>): void
```

Constructs a URI for a specific name-value pair for monitoring data of the ability that uses the Data template.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

<!--Device-settings-function getURI(name: string, callback: AsyncCallback<object>): void--><!--Device-settings-function getURI(name: string, callback: AsyncCallback<object>): void-End-->

**System capability:** SystemCapability.Applications.Settings.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | Indicates the name of the setting to set. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;object&gt; | Yes | The callback of getURI result. |

**Example**

```TypeScript
settings.getURI(settings.display.SCREEN_BRIGHTNESS_STATUS, (uri:string) => {
    console.info(`callback:uri -> ${JSON.stringify(uri)}`)
})
```


## getURI

```TypeScript
function getURI(name: string): Promise<object>
```

Constructs a URI for a specific name-value pair for monitoring data of the ability that uses the Data template.

**Since:** 7

**ArkTS mode:** ArkTS-Dyn only, since version 7.

**Deprecated since:** 9

<!--Device-settings-function getURI(name: string): Promise<object>--><!--Device-settings-function getURI(name: string): Promise<object>-End-->

**System capability:** SystemCapability.Applications.Settings.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| name | string | Yes | Indicates the name of the setting to set. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;object&gt; | Returns the corresponding URI; returns { |

**Example**

```TypeScript
settings.getURI(settings.display.SCREEN_BRIGHTNESS_STATUS).then((uri:string) => {
    console.info(`promise:uri -> ${JSON.stringify(uri)}`)
})
```

